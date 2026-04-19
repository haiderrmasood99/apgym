from __future__ import annotations

from datetime import date
from unittest import TestCase

import pandas as pd

from apgym.envs import MaizeNConfig, MaizeNEnv
from apgym.validation import (
    SplitResult,
    evaluate_policy_set,
    fixed_schedule_policy,
    make_generalization_splits,
    no_action_policy,
)


class TestValidationHarness(TestCase):
    def test_split_generation(self) -> None:
        frame = pd.DataFrame(
            {
                "site_id": ["A", "A", "B", "B", "C", "C"],
                "season_year": [2018, 2019, 2018, 2019, 2018, 2019],
                "yield_t_ha": [8, 9, 7, 8, 6, 7],
            }
        )
        splits = make_generalization_splits(
            frame, test_years=[2019], holdout_frac=0.33, seed=1
        )
        self.assertIsInstance(splits, SplitResult)
        self.assertTrue((splits.test_year["season_year"] == 2019).all())
        self.assertGreater(len(splits.train), 0)

    def test_baseline_evaluation(self) -> None:
        def env_factory(_: int) -> MaizeNEnv:
            cfg = MaizeNConfig(
                dry_run=True,
                season_start=date(1990, 1, 1),
                season_end=date(1990, 4, 1),
                planting_date=date(1990, 1, 15),
                decision_interval_days=14,
            )
            return MaizeNEnv(cfg)

        policies = {
            "no_action": no_action_policy,
            "fixed_split": fixed_schedule_policy({1: 2, 2: 2}),
        }
        results = evaluate_policy_set(env_factory, policies, n_episodes=2, max_steps=6)
        self.assertIn("policy", results.columns)
        self.assertIn("total_reward", results.columns)
        self.assertEqual(set(results["policy"]), {"no_action", "fixed_split"})
