from __future__ import annotations

from datetime import date

import pandas as pd

from apgym.envs import MaizeNConfig, MaizeNEnv
from apgym.experiments import RlSweepConfig, run_rl_sweep, select_best_sweep_run


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
    sweep = RlSweepConfig(
        algorithms=("ppo", "a2c"),
        total_timesteps=(256, 512),
        seeds=(0,),
        test_years=(2019,),
        holdout_frac=0.33,
        max_train_envs=2,
    )
    results = run_rl_sweep(episodes, build_env, sweep=sweep)
    print("Sweep results:")
    print(results.to_string(index=False))
    best = select_best_sweep_run(results, metric_col="test_year_reward_mean")
    print("\nBest config:")
    for key in ("algorithm", "total_timesteps", "seed", "test_year_reward_mean"):
        print(f"- {key}: {best.get(key)}")


if __name__ == "__main__":
    main()

