"""First APGym benchmark: in-season maize nitrogen management."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta
from pathlib import Path
from typing import Any, Mapping

import numpy as np
import pandas as pd

from apgym._compat import spaces
from apgym.actions import DiscreteNitrogenActionMapper, NitrogenAction
from apgym.constraints import (
    EnvironmentalConstraint,
    NitrogenConstraintTracker,
    TimingConstraint,
)
from apgym.envs.base import ApsimBaseEnv
from apgym.observers import (
    CompoundObserver,
    CropObserver,
    EconomicsObserver,
    SoilObserver,
    WeatherObserver,
)
from apgym.rewards import MultiObjectiveRewarder, ProfitRewarder
from apgym.simulator import (
    ApsimManagerParameterPatch,
    ApsimModelPropertyPatch,
    ApsimPatch,
    ApsimRunRequest,
    ApsimRunner,
)


def _default_template_path() -> Path:
    templates_dir = Path(__file__).resolve().parents[1] / "templates"
    real = templates_dir / "maize_n_real.apsimx"
    if real.exists():
        return real
    return templates_dir / "maize_n_base.apsimx"


@dataclass
class MaizeNConfig:
    template_path: Path = field(default_factory=_default_template_path)
    season_start: date = date(1990, 1, 1)
    season_end: date = date(1991, 12, 31)
    planting_date: date = date(1990, 6, 15)
    decision_interval_days: int = 7
    dose_levels_kg_ha: tuple[float, ...] = (0.0, 20.0, 40.0, 60.0, 80.0)
    max_total_n_kg_ha: float = 260.0
    max_n_events: int = 8
    max_leaching_kg_ha: float = 30.0
    budget_usd_per_ha: float = 900.0
    grain_price_usd_per_ton: float = 190.0
    n_cost_usd_per_kg: float = 1.1
    fixed_cost_usd_per_ha: float = 0.0
    leaching_penalty_usd_per_kg: float = 0.0
    latest_n_application_date: date | None = None
    # Generic named patching for real APSIM templates.
    n_manager_name: str | None = "APGym TopDress N"
    n_manager_parameter: str = "ScheduleCsv"
    n_manager_value_mode: str = "schedule_csv"
    disable_sowing_fertiliser_manager: bool = True
    sowing_manager_name: str = "Fertilise at sowing"
    sowing_manager_parameter: str = "Amount"
    simulation_name: str | None = "Simulation"
    zone_name: str | None = "Field"
    weather_file: str | None = None
    weather_model_name: str = "Weather"
    clock_model_name: str = "Clock"
    use_clock_patch: bool = True
    # Optional legacy patch path for APGym-specific JSON schedules.
    nitrogen_schedule_patch_path: str | None = None
    fixed_patches: tuple[Any, ...] = ()
    report_tables: tuple[str, ...] = ("Report",)
    dry_run: bool = True
    models_exe: Path | None = None
    work_root: Path | None = None
    keep_runs: bool = True

    def __post_init__(self) -> None:
        if self.season_end <= self.season_start:
            raise ValueError("season_end must be after season_start")
        if self.planting_date < self.season_start or self.planting_date > self.season_end:
            raise ValueError("planting_date must be within the season window")
        if self.decision_interval_days <= 0:
            raise ValueError("decision_interval_days must be positive")
        if self.latest_n_application_date is None:
            self.latest_n_application_date = self.season_end - timedelta(days=45)
        if not (self.season_start <= self.latest_n_application_date <= self.season_end):
            raise ValueError("latest_n_application_date must lie within [season_start, season_end]")
        if self.n_manager_value_mode not in {"schedule_csv", "cumulative_total"}:
            raise ValueError("n_manager_value_mode must be 'schedule_csv' or 'cumulative_total'")


class MaizeNEnv(ApsimBaseEnv):
    """Weekly/biweekly top-dress N decision environment."""

    _STAGE_MAP = {
        "sowing": 1.0,
        "germin": 2.0,
        "emerg": 2.0,
        "veget": 3.0,
        "floral": 4.0,
        "flower": 4.0,
        "grain": 5.0,
        "fill": 5.0,
        "matur": 6.0,
        "harvest": 7.0,
        "end": 8.0,
    }

    def __init__(self, config: MaizeNConfig | None = None, runner: ApsimRunner | None = None):
        self.config = config or MaizeNConfig()
        self.action_mapper = DiscreteNitrogenActionMapper(self.config.dose_levels_kg_ha)
        self.observer = CompoundObserver(
            observers=[
                WeatherObserver(),
                SoilObserver(),
                CropObserver(),
                EconomicsObserver(),
            ]
        )

        if runner is None:
            runner = ApsimRunner(
                models_exe=self.config.models_exe,
                work_root=self.config.work_root,
                keep_runs=self.config.keep_runs,
                dry_run=self.config.dry_run,
            )

        super().__init__(runner=runner, template_path=self.config.template_path)

        self.action_space = self.action_mapper.action_space
        self.observation_space = spaces.Box(
            low=self.observer.low,
            high=self.observer.high,
            shape=self.observer.low.shape,
            dtype=np.float32,
        )

        self.rewarder = MultiObjectiveRewarder(
            base_rewarder=ProfitRewarder(
                grain_price_usd_per_ton=self.config.grain_price_usd_per_ton,
                nitrogen_cost_usd_per_kg=self.config.n_cost_usd_per_kg,
                fixed_cost_usd_per_ha=self.config.fixed_cost_usd_per_ha,
            ),
            leaching_penalty_usd_per_kg=self.config.leaching_penalty_usd_per_kg,
        )
        self.n_constraints = NitrogenConstraintTracker(
            max_total_n_kg_ha=self.config.max_total_n_kg_ha,
            max_events=self.config.max_n_events,
        )
        self.environment_constraint = EnvironmentalConstraint(
            max_leaching_kg_ha=self.config.max_leaching_kg_ha
        )
        self.timing_constraint = TimingConstraint(
            latest_application_date=self.config.latest_n_application_date
        )

        self.current_date = self.config.season_start
        self.applied_actions: list[NitrogenAction] = []
        self.cumulative_n_kg_ha = 0.0
        self.n_event_count = 0
        self.state: dict[str, float] = {}
        self.latest_reports: dict[str, pd.DataFrame] = {}
        self.season_metrics: dict[str, float] = {}

    @staticmethod
    def _find_column(frame: pd.DataFrame, candidates: tuple[str, ...]) -> str | None:
        if frame.empty:
            return None
        normalized = {c.lower(): c for c in frame.columns}
        for candidate in candidates:
            if candidate in frame.columns:
                return candidate
            lowered = candidate.lower()
            if lowered in normalized:
                return normalized[lowered]
        return None

    @staticmethod
    def _safe_value(
        frame: pd.DataFrame, candidates: tuple[str, ...], default: float = 0.0
    ) -> float:
        col = MaizeNEnv._find_column(frame, candidates)
        if col is None or frame.empty:
            return default
        return MaizeNEnv._to_float(frame.iloc[0][col], default=default)

    @staticmethod
    def _to_float(value: Any, default: float = 0.0) -> float:
        try:
            if pd.isna(value):
                return default
            return float(value)
        except (TypeError, ValueError):
            return default

    @classmethod
    def _coerce_stage_code(cls, value: Any) -> float:
        numeric = cls._to_float(value, default=float("nan"))
        if not np.isnan(numeric):
            return numeric
        text = str(value).strip().lower()
        for token, code in cls._STAGE_MAP.items():
            if token in text:
                return code
        return 0.0

    @staticmethod
    def _safe_metric_from_report(
        report: pd.DataFrame,
        candidates: tuple[str, ...],
        default: float = 0.0,
        agg: str = "max",
    ) -> float:
        col = MaizeNEnv._find_column(report, candidates)
        if col is None or report.empty:
            return default
        series = pd.to_numeric(report[col], errors="coerce").dropna()
        if series.empty:
            return default
        if agg == "last":
            return float(series.iloc[-1])
        return float(series.max())

    def _build_request(self) -> ApsimRunRequest:
        patches = list(self.config.fixed_patches)
        if self.config.use_clock_patch:
            patches.append(
                ApsimModelPropertyPatch(
                    model_name=self.config.clock_model_name,
                    property_name="Start",
                    value=f"{self.config.season_start.isoformat()}T00:00:00",
                    type_contains="Models.Clock",
                    simulation_name=self.config.simulation_name,
                )
            )
            patches.append(
                ApsimModelPropertyPatch(
                    model_name=self.config.clock_model_name,
                    property_name="End",
                    value=f"{self.config.season_end.isoformat()}T00:00:00",
                    type_contains="Models.Clock",
                    simulation_name=self.config.simulation_name,
                )
            )

        if self.config.weather_file:
            patches.append(
                ApsimModelPropertyPatch(
                    model_name=self.config.weather_model_name,
                    property_name="FileName",
                    value=self.config.weather_file,
                    type_contains="Models.Climate.Weather",
                    simulation_name=self.config.simulation_name,
                )
            )

        # For real APSIM templates, this is the default action hook.
        if (not self.runner.dry_run) and self.config.n_manager_name:
            if self.config.disable_sowing_fertiliser_manager:
                patches.append(
                    ApsimManagerParameterPatch(
                        manager_name=self.config.sowing_manager_name,
                        parameter_key=self.config.sowing_manager_parameter,
                        value=0.0,
                        simulation_name=self.config.simulation_name,
                        zone_name=self.config.zone_name,
                    )
                )
            if self.config.n_manager_value_mode == "schedule_csv":
                entries = [
                    f"{action.date.isoformat()}:{round(action.amount_kg_ha, 6)}"
                    for action in self.applied_actions
                    if action.amount_kg_ha > 0
                ]
                manager_value: Any = ";".join(entries)
            else:
                manager_value = round(self.cumulative_n_kg_ha, 6)
            patches.append(
                ApsimManagerParameterPatch(
                    manager_name=self.config.n_manager_name,
                    parameter_key=self.config.n_manager_parameter,
                    value=manager_value,
                    simulation_name=self.config.simulation_name,
                    zone_name=self.config.zone_name,
                )
            )

        # Optional APGym-specific template schedule path.
        if self.config.nitrogen_schedule_patch_path:
            schedule = [
                {"date": action.date.isoformat(), "amount_kg_ha": action.amount_kg_ha}
                for action in self.applied_actions
                if action.amount_kg_ha > 0
            ]
            patches.append(
                ApsimPatch(
                    json_path=self.config.nitrogen_schedule_patch_path,
                    value=schedule,
                )
            )

        metadata = {
            "total_n_applied": self.cumulative_n_kg_ha,
            "season_start": self.config.season_start.isoformat(),
            "season_days": (self.config.season_end - self.config.season_start).days,
        }
        return ApsimRunRequest(
            template_path=self.template_path,
            patches=patches,
            report_tables=list(self.config.report_tables),
            metadata=metadata,
        )

    def _run_and_collect(self) -> dict[str, Any]:
        result = self.runner.run(self._build_request())
        if not result.ok:
            raise RuntimeError(
                "APSIM run failed with return code "
                f"{result.returncode}.\nSTDERR:\n{result.stderr}\nSTDOUT:\n{result.stdout}"
            )
        reports = result.reports
        self.latest_reports = reports
        self._update_state_from_reports(reports)
        return {"run_id": result.run_id, "run_dir": str(result.run_dir), "dry_run": result.is_dry_run}

    def _update_state_from_reports(self, reports: Mapping[str, pd.DataFrame]) -> None:
        report = reports.get("Report", pd.DataFrame())
        summary = reports.get("SeasonSummary", pd.DataFrame())

        if not report.empty:
            if self._find_column(report, ("Date", "Today")) is not None:
                report = report.copy()
                report_date_col = self._find_column(report, ("Date", "Today"))
                report["_DateTS"] = pd.to_datetime(report[report_date_col], errors="coerce")
                cutoff = pd.Timestamp(self.current_date)
                window = report.loc[report["_DateTS"] <= cutoff]
                if window.empty:
                    window = report.iloc[[0]]
            else:
                window = report
            current = window.tail(1)
            recent = window.tail(7)
        else:
            current = pd.DataFrame([{}])
            recent = current

        rain_col = self._find_column(current, ("Rain", "Rain_mm", "Precip", "Precipitation"))
        tmean_col = self._find_column(current, ("Tmean", "TempMean"))
        tmin_col = self._find_column(current, ("Tmin", "MinTemp"))
        tmax_col = self._find_column(current, ("Tmax", "MaxTemp"))
        soil_water_col = self._find_column(current, ("SoilWaterTop", "SWTop", "SoilWater"))
        soil_n_col = self._find_column(current, ("SoilN", "MineralN", "NO3"))
        nh4_col = self._find_column(current, ("NH4",))
        lai_col = self._find_column(current, ("LAI",))
        biomass_col = self._find_column(current, ("Biomass", "AGB"))
        stage_col = self._find_column(current, ("StageCode", "Stage"))

        recent_rain = float(recent[rain_col].fillna(0.0).sum()) if rain_col else 0.0
        cumulative_rain = float(
            report[rain_col].fillna(0.0).sum() if rain_col and not report.empty else 0.0
        )
        if tmean_col:
            recent_tmean = float(recent[tmean_col].fillna(0.0).mean())
        elif tmin_col and tmax_col:
            recent_tmean = float((recent[tmin_col].fillna(0.0) + recent[tmax_col].fillna(0.0)).mean() / 2.0)
        else:
            recent_tmean = 0.0

        soil_n = self._to_float(current.iloc[0][soil_n_col], default=0.0) if soil_n_col else 0.0
        if nh4_col:
            soil_n += self._to_float(current.iloc[0][nh4_col], default=0.0)

        stage_value = current.iloc[0][stage_col] if stage_col else 0.0

        self.state = {
            "recent_rain_mm": recent_rain,
            "recent_tmean_c": recent_tmean,
            "cumulative_rain_mm": cumulative_rain,
            "soil_water_top_mm": self._to_float(current.iloc[0][soil_water_col], default=0.0)
            if soil_water_col
            else 0.0,
            "soil_mineral_n_kg_ha": soil_n,
            "days_since_planting": float(
                max(0, (self.current_date - self.config.planting_date).days)
            ),
            "crop_stage_code": self._coerce_stage_code(stage_value),
            "lai": self._to_float(current.iloc[0][lai_col], default=0.0) if lai_col else 0.0,
            "biomass_kg_ha": self._to_float(current.iloc[0][biomass_col], default=0.0)
            if biomass_col
            else 0.0,
            "cumulative_n_kg_ha": self.cumulative_n_kg_ha,
            "remaining_budget_usd_ha": self.config.budget_usd_per_ha
            - self.cumulative_n_kg_ha * self.config.n_cost_usd_per_kg,
        }

        yield_from_summary = self._safe_value(
            summary, ("Yield_t_ha", "Yield", "GrainYield"), default=0.0
        )
        if yield_from_summary == 0.0:
            yield_from_summary = self._safe_metric_from_report(
                report,
                ("Yield_t_ha", "Yield", "GrainYield", "Maize.Grain.Total.Wt"),
                default=0.0,
                agg="max",
            )

        self.season_metrics = {
            "yield_t_ha": yield_from_summary,
            "leaching_kg_ha": self._safe_value(
                summary, ("Leaching_kg_ha", "NO3Leaching", "Leaching")
            ),
            "season_et_mm": self._safe_value(summary, ("SeasonET_mm", "ET", "SeasonET")),
        }

    def _build_observation(self) -> np.ndarray:
        obs = self.observer.observe(self.latest_reports, self.state)
        self.last_observation = obs
        return obs

    def reset(self, *, seed: int | None = None, options: dict[str, Any] | None = None):
        del options
        try:
            super().reset(seed=seed)
        except TypeError:
            super().reset()

        self.terminated = False
        self.truncated = False
        self.current_date = self.config.season_start
        self.applied_actions = []
        self.cumulative_n_kg_ha = 0.0
        self.n_event_count = 0

        run_info = self._run_and_collect()
        obs = self._build_observation()
        info = {
            "date": self.current_date.isoformat(),
            "total_n_applied_kg_ha": self.cumulative_n_kg_ha,
            "n_application_events": self.n_event_count,
            **self.season_metrics,
            **run_info,
        }
        self.last_info = info
        self.last_reward = 0.0
        return self._pack_reset(obs, info)

    def step(self, action: int):
        if self.terminated:
            raise RuntimeError("Episode already terminated. Call reset() before step().")
        if not self.action_space.contains(action):
            raise ValueError(f"Action {action} not in action space")

        action_obj = self.action_mapper.map(action, self.current_date)
        self.applied_actions.append(action_obj)
        self.cumulative_n_kg_ha += action_obj.amount_kg_ha
        if action_obj.amount_kg_ha > 0:
            self.n_event_count += 1

        reward = self.rewarder.step_reward(action_obj.amount_kg_ha)
        timing_cost = self.timing_constraint.costs(
            action_date=action_obj.date,
            applied_amount_kg_ha=action_obj.amount_kg_ha,
        )

        self.current_date += timedelta(days=self.config.decision_interval_days)
        self.terminated = self.current_date > self.config.season_end

        run_info = self._run_and_collect()

        if self.terminated:
            reward += self.rewarder.terminal_reward(
                yield_t_ha=self.season_metrics["yield_t_ha"],
                leaching_kg_ha=self.season_metrics["leaching_kg_ha"],
                irrigation_mm=0.0,
            )

        obs = self._build_observation()
        n_costs = self.n_constraints.costs(self.cumulative_n_kg_ha, self.n_event_count)
        env_costs = self.environment_constraint.costs(self.season_metrics["leaching_kg_ha"])
        budget_cost = {
            "cost_budget_excess": max(0.0, -self.state.get("remaining_budget_usd_ha", 0.0))
        }

        info = {
            "date": self.current_date.isoformat(),
            "applied_n_kg_ha": action_obj.amount_kg_ha,
            "total_n_applied_kg_ha": self.cumulative_n_kg_ha,
            "n_application_events": self.n_event_count,
            **self.season_metrics,
            **timing_cost,
            **n_costs,
            **env_costs,
            **budget_cost,
            **run_info,
        }

        self.last_info = info
        self.last_reward = float(reward)
        return self._pack_step(obs, float(reward), self.terminated, self.truncated, info)
