from __future__ import annotations

from datetime import date

import pandas as pd

from apgym.envs import MaizeNConfig, MaizeNEnv
from apgym.experiments import RlExperimentConfig, run_split_rl_experiment


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
    config = RlExperimentConfig(
        algorithm="ppo",
        total_timesteps=512,
        seed=0,
        holdout_frac=0.33,
        test_years=(2019,),
        max_train_envs=2,
    )
    result = run_split_rl_experiment(episodes, build_env, config=config)
    print("Summary:")
    print(result["summary"].to_string())
    print("\nEvaluation sample:")
    print(result["evaluations"]["all"].head().to_string())


if __name__ == "__main__":
    main()
