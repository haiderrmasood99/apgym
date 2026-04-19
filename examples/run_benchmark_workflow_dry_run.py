from __future__ import annotations

from datetime import date
from pathlib import Path
import tempfile

import pandas as pd

from apgym.envs import MaizeNConfig, MaizeNEnv
from apgym.experiments import (
    CalibrationGateConfig,
    RlExperimentConfig,
    run_benchmark_training_workflow,
)
from apgym.validation import CalibrationThresholds


def build_env(row: dict, split: str) -> MaizeNEnv:
    del split
    year = int(row["season_year"])
    config = MaizeNConfig(
        dry_run=True,
        season_start=date(year, 1, 1),
        season_end=date(year, 9, 30),
        planting_date=date(year, 2, 1),
        decision_interval_days=14,
    )
    return MaizeNEnv(config)


def main() -> None:
    episodes = pd.DataFrame(
        {
            "site_id": ["A", "A", "B", "B", "C", "C"],
            "season_year": [2018, 2019, 2018, 2019, 2018, 2019],
        }
    )

    predicted = pd.DataFrame(
        {
            "site_id": ["A", "A", "B", "B", "C", "C"],
            "season_year": [2018, 2019, 2018, 2019, 2018, 2019],
            "yield_t_ha": [10.0, 9.7, 8.2, 8.5, 7.9, 8.1],
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
            thresholds=CalibrationThresholds(rmse_max=0.05, r2_min=0.95),
            require_pass=True,
        )
        config = RlExperimentConfig(
            algorithm="ppo",
            total_timesteps=512,
            seed=0,
            holdout_frac=0.33,
            test_years=(2019,),
            max_train_envs=2,
        )

        result = run_benchmark_training_workflow(
            episodes=episodes,
            env_builder=build_env,
            rl_config=config,
            calibration_gate=gate,
            output_dir=root / "workflow_out",
            run_name="dry_run_demo",
        )
        print("Calibration pass:", result["calibration"]["passes_thresholds"])
        print("Summary:")
        print(result["summary"].to_string())
        print("Artifacts:")
        for name, path in result["artifacts"].items():
            print(f"- {name}: {path}")


if __name__ == "__main__":
    main()

