"""Calibration-gated benchmark workflow helpers."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any, Callable

import pandas as pd

from apgym.data.ingestion.utils import load_tabular
from apgym.experiments.rl import RlExperimentConfig, run_split_rl_experiment
from apgym.validation.calibration import CalibrationThresholds, run_calibration_from_files


@dataclass(frozen=True)
class CalibrationGateConfig:
    """Configuration for threshold-gated predicted-vs-observed checks."""

    predicted_path: str | Path
    observed_path: str | Path
    output_dir: str | Path
    keys: tuple[str, ...] = ("site_id", "season_year")
    predicted_col: str = "yield_t_ha"
    observed_col: str = "yield_t_ha"
    group_cols: tuple[str, ...] = ("site_id",)
    report_prefix: str = "calibration"
    thresholds: CalibrationThresholds = field(default_factory=CalibrationThresholds)
    require_pass: bool = True


def load_episode_table(path: str | Path) -> pd.DataFrame:
    """Load benchmark episode table and enforce required identifiers."""

    frame = load_tabular(path)
    required = {"site_id", "season_year"}
    missing = sorted(required - set(frame.columns))
    if missing:
        raise ValueError(
            f"Episode table missing required columns: {missing}. "
            "Expected at least site_id and season_year."
        )
    frame = frame.copy()
    frame["site_id"] = frame["site_id"].astype("string")
    frame["season_year"] = pd.to_numeric(frame["season_year"], errors="coerce").astype("Int64")
    frame = frame.dropna(subset=["site_id", "season_year"])
    frame["season_year"] = frame["season_year"].astype(int)
    return frame.reset_index(drop=True)


def run_calibration_gate(config: CalibrationGateConfig) -> dict[str, Any]:
    """Run calibration report and return structured result."""

    return run_calibration_from_files(
        predicted_path=config.predicted_path,
        observed_path=config.observed_path,
        output_dir=config.output_dir,
        keys=config.keys,
        predicted_col=config.predicted_col,
        observed_col=config.observed_col,
        group_cols=config.group_cols,
        thresholds=config.thresholds,
        report_prefix=config.report_prefix,
    )


def _flatten_summary(summary: pd.DataFrame) -> pd.DataFrame:
    if isinstance(summary.columns, pd.MultiIndex):
        flattened = summary.copy()
        flattened.columns = [
            "_".join([str(level) for level in col if str(level)])
            for col in flattened.columns.to_flat_index()
        ]
        return flattened.reset_index()
    return summary.reset_index()


def _write_table(frame: pd.DataFrame, path: Path) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(path, index=False)
    return str(path)


def _jsonable(value: Any) -> Any:
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    if isinstance(value, tuple):
        return [_jsonable(v) for v in value]
    if isinstance(value, list):
        return [_jsonable(v) for v in value]
    if isinstance(value, dict):
        return {str(k): _jsonable(v) for k, v in value.items()}
    return str(value)


def write_workflow_artifacts(
    *,
    output_dir: str | Path,
    experiment_result: dict[str, Any],
    rl_config: RlExperimentConfig,
    calibration_result: dict[str, Any] | None = None,
    calibration_config: CalibrationGateConfig | None = None,
    run_name: str = "benchmark",
) -> dict[str, str]:
    """Persist workflow outputs and return artifact path map."""

    root = Path(output_dir).expanduser().resolve()
    run_dir = root / run_name
    run_dir.mkdir(parents=True, exist_ok=True)

    evaluations: dict[str, pd.DataFrame] = experiment_result["evaluations"]
    summary_frame = _flatten_summary(experiment_result["summary"])

    artifacts = {
        "summary_csv": _write_table(summary_frame, run_dir / "rl_summary.csv"),
        "eval_train_csv": _write_table(evaluations["train"], run_dir / "eval_train.csv"),
        "eval_test_year_csv": _write_table(
            evaluations["test_year"], run_dir / "eval_test_year.csv"
        ),
        "eval_holdout_site_csv": _write_table(
            evaluations["holdout_site"], run_dir / "eval_holdout_site.csv"
        ),
        "eval_all_csv": _write_table(evaluations["all"], run_dir / "eval_all.csv"),
    }

    metadata = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "rl_config": _jsonable(asdict(rl_config)),
        "n_eval_rows": int(len(evaluations["all"])),
    }
    if calibration_config is not None:
        metadata["calibration_config"] = _jsonable(asdict(calibration_config))
    if calibration_result is not None:
        metadata["calibration_passes_thresholds"] = bool(
            calibration_result["passes_thresholds"]
        )
        metadata["calibration_outputs"] = _jsonable(calibration_result.get("outputs", {}))

    metadata_path = run_dir / "run_metadata.json"
    with metadata_path.open("w", encoding="utf-8") as handle:
        json.dump(metadata, handle, indent=2)
        handle.write("\n")
    artifacts["run_metadata_json"] = str(metadata_path)
    return artifacts


def run_benchmark_training_workflow(
    episodes: pd.DataFrame,
    env_builder: Callable[[dict[str, Any], str], Any],
    *,
    rl_config: RlExperimentConfig | None = None,
    calibration_gate: CalibrationGateConfig | None = None,
    output_dir: str | Path | None = None,
    run_name: str = "benchmark",
) -> dict[str, Any]:
    """Run calibration gate (optional) then split-aware RL training/evaluation."""

    if rl_config is None:
        rl_config = RlExperimentConfig()

    calibration_result: dict[str, Any] | None = None
    if calibration_gate is not None:
        calibration_result = run_calibration_gate(calibration_gate)
        if calibration_gate.require_pass and not calibration_result["passes_thresholds"]:
            outputs = calibration_result.get("outputs", {})
            raise RuntimeError(
                "Calibration gate failed; refusing RL training. "
                f"Review calibration outputs: {outputs}"
            )

    experiment_result = run_split_rl_experiment(
        episodes=episodes,
        env_builder=env_builder,
        config=rl_config,
    )

    artifacts: dict[str, str] = {}
    if output_dir is not None:
        artifacts = write_workflow_artifacts(
            output_dir=output_dir,
            experiment_result=experiment_result,
            rl_config=rl_config,
            calibration_result=calibration_result,
            calibration_config=calibration_gate,
            run_name=run_name,
        )

    experiment_result["calibration"] = calibration_result
    experiment_result["artifacts"] = artifacts
    return experiment_result

