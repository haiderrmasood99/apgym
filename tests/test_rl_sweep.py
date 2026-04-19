from __future__ import annotations

from datetime import date
from unittest import TestCase

import pandas as pd

from apgym.envs import MaizeNConfig, MaizeNEnv
from apgym.experiments import RlSweepConfig, run_rl_sweep, select_best_sweep_run


def _env_builder(row: dict, split: str) -> MaizeNEnv:
    del split
    year = int(row["season_year"])
    cfg = MaizeNConfig(
        dry_run=True,
        season_start=date(year, 1, 1),
        season_end=date(year, 3, 31),
        planting_date=date(year, 1, 15),
        decision_interval_days=14,
    )
    return MaizeNEnv(cfg)


class TestRlSweep(TestCase):
    def test_rl_sweep_runs(self) -> None:
        episodes = pd.DataFrame(
            {
                "site_id": ["A", "A", "B", "B"],
                "season_year": [2018, 2019, 2018, 2019],
            }
        )
        sweep = RlSweepConfig(
            algorithms=("ppo",),
            total_timesteps=(64,),
            seeds=(0, 1),
            test_years=(2019,),
            holdout_frac=0.25,
            max_train_envs=2,
        )
        results = run_rl_sweep(episodes, _env_builder, sweep=sweep)
        self.assertEqual(len(results), 2)
        self.assertIn("test_year_reward_mean", results.columns)

        best = select_best_sweep_run(results)
        self.assertIn("algorithm", best)
        self.assertEqual(best["algorithm"], "ppo")

