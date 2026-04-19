from __future__ import annotations

from datetime import date
from pathlib import Path
import tempfile
from unittest import TestCase

import pandas as pd

from apgym.envs import MaizeNConfig, MaizeNEnv
from apgym.experiments import (
    CalibrationGateConfig,
    RlExperimentConfig,
    run_benchmark_training_workflow,
)
from apgym.validation import CalibrationThresholds


def _build_env(row: dict, split: str) -> MaizeNEnv:
    del split
    year = int(row["season_year"])
    cfg = MaizeNConfig(
        dry_run=True,
        season_start=date(year, 1, 1),
        season_end=date(year, 4, 1),
        planting_date=date(year, 1, 15),
        decision_interval_days=14,
    )
    return MaizeNEnv(cfg)


class TestExperimentWorkflow(TestCase):
    def test_calibration_gate_blocks_training(self) -> None:
        episodes = pd.DataFrame(
            {
                "site_id": ["A", "A", "B", "B"],
                "season_year": [2018, 2019, 2018, 2019],
            }
        )
        predicted = pd.DataFrame(
            {
                "site_id": ["A", "A", "B", "B"],
                "season_year": [2018, 2019, 2018, 2019],
                "yield_t_ha": [1.0, 1.2, 0.8, 1.1],
            }
        )
        observed = pd.DataFrame(
            {
                "site_id": ["A", "A", "B", "B"],
                "season_year": [2018, 2019, 2018, 2019],
                "yield_t_ha": [10.0, 9.8, 8.9, 9.1],
            }
        )

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            predicted_path = root / "predicted.csv"
            observed_path = root / "observed.csv"
            predicted.to_csv(predicted_path, index=False)
            observed.to_csv(observed_path, index=False)

            gate = CalibrationGateConfig(
                predicted_path=predicted_path,
                observed_path=observed_path,
                output_dir=root / "calibration",
                thresholds=CalibrationThresholds(rmse_max=0.5),
                require_pass=True,
            )
            rl_cfg = RlExperimentConfig(
                algorithm="ppo",
                total_timesteps=64,
                max_train_envs=2,
                test_years=(2019,),
                holdout_frac=0.25,
                seed=0,
            )

            with self.assertRaises(RuntimeError):
                run_benchmark_training_workflow(
                    episodes=episodes,
                    env_builder=_build_env,
                    rl_config=rl_cfg,
                    calibration_gate=gate,
                    output_dir=root / "out",
                    run_name="blocked",
                )

            self.assertTrue((root / "calibration" / "calibration.md").exists())

    def test_workflow_runs_and_writes_artifacts(self) -> None:
        episodes = pd.DataFrame(
            {
                "site_id": ["A", "A", "B", "B"],
                "season_year": [2018, 2019, 2018, 2019],
            }
        )
        predicted = pd.DataFrame(
            {
                "site_id": ["A", "A", "B", "B"],
                "season_year": [2018, 2019, 2018, 2019],
                "yield_t_ha": [10.0, 9.9, 8.1, 8.5],
            }
        )
        observed = predicted.copy()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            predicted_path = root / "predicted.csv"
            observed_path = root / "observed.csv"
            predicted.to_csv(predicted_path, index=False)
            observed.to_csv(observed_path, index=False)

            gate = CalibrationGateConfig(
                predicted_path=predicted_path,
                observed_path=observed_path,
                output_dir=root / "calibration",
                thresholds=CalibrationThresholds(rmse_max=0.01, r2_min=0.99),
                require_pass=True,
            )
            rl_cfg = RlExperimentConfig(
                algorithm="ppo",
                total_timesteps=64,
                max_train_envs=2,
                test_years=(2019,),
                holdout_frac=0.25,
                seed=0,
            )

            result = run_benchmark_training_workflow(
                episodes=episodes,
                env_builder=_build_env,
                rl_config=rl_cfg,
                calibration_gate=gate,
                output_dir=root / "out",
                run_name="accepted",
            )

            self.assertTrue(result["calibration"]["passes_thresholds"])
            self.assertIn("summary_csv", result["artifacts"])
            self.assertTrue(Path(result["artifacts"]["summary_csv"]).exists())
            self.assertFalse(result["evaluations"]["all"].empty)

