from __future__ import annotations

from datetime import date

from apgym.envs import MaizeNConfig, MaizeNEnv
from apgym.validation import (
    capped_n_policy,
    compare_policies,
    evaluate_policy_set,
    fixed_schedule_policy,
    no_action_policy,
)


def env_factory(_: int) -> MaizeNEnv:
    config = MaizeNConfig(
        dry_run=True,
        season_start=date(1990, 1, 1),
        season_end=date(1990, 9, 30),
        planting_date=date(1990, 2, 1),
        decision_interval_days=14,
    )
    return MaizeNEnv(config)


def main() -> None:
    policies = {
        "no_action": no_action_policy,
        "fixed_split": fixed_schedule_policy({3: 2, 6: 2, 9: 2}),
        "capped_n": capped_n_policy(target_total_n_kg_ha=120.0, action_if_under_cap=2),
    }
    results = evaluate_policy_set(env_factory, policies, n_episodes=4)
    print(results.head().to_string())
    summary = compare_policies(
        results,
        metric_cols=("total_reward", "yield_t_ha", "leaching_kg_ha"),
    )
    print("\nPolicy summary:")
    print(summary.to_string())


if __name__ == "__main__":
    main()
