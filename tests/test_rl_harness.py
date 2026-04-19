from __future__ import annotations

from datetime import date
from unittest import TestCase

import pandas as pd

from apgym.envs import MaizeNConfig, MaizeNEnv
from apgym.experiments import RlExperimentConfig, run_split_rl_experiment


class TestRlHarness(TestCase):
    def test_split_rl_experiment_runs(self) -> None:
        episodes = pd.DataFrame(
            {
                "site_id": ["A", "A", "B", "B"],
                "season_year": [2018, 2019, 2018, 2019],
            }
        )

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

        config = RlExperimentConfig(
            algorithm="ppo",
            total_timesteps=128,
            max_train_envs=2,
            test_years=(2019,),
            holdout_frac=0.25,
            seed=0,
        )
        out = run_split_rl_experiment(episodes, _env_builder, config=config)
        self.assertIn("summary", out)
        self.assertIn("evaluations", out)
        self.assertIn("all", out["evaluations"])
        self.assertGreaterEqual(len(out["evaluations"]["all"]), 1)
