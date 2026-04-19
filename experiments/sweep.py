"""Hyperparameter/algorithm sweep helpers for APGym RL experiments."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable

import pandas as pd

from apgym.experiments.rl import RlExperimentConfig, run_split_rl_experiment


@dataclass(frozen=True)
class RlSweepConfig:
    """Grid configuration for split-aware RL sweeps."""

    algorithms: tuple[str, ...] = ("ppo", "a2c")
    total_timesteps: tuple[int, ...] = (1_000, 5_000)
    seeds: tuple[int, ...] = (0, 1, 2)
    max_train_envs: int = 4
    deterministic_eval: bool = True
    holdout_frac: float = 0.2
    test_years: tuple[int, ...] | None = None


def _iter_experiment_configs(sweep: RlSweepConfig) -> list[RlExperimentConfig]:
    configs: list[RlExperimentConfig] = []
    for algorithm in sweep.algorithms:
        for timesteps in sweep.total_timesteps:
            for seed in sweep.seeds:
                configs.append(
                    RlExperimentConfig(
                        algorithm=algorithm,
                        total_timesteps=int(timesteps),
                        seed=int(seed),
                        deterministic_eval=sweep.deterministic_eval,
                        max_train_envs=sweep.max_train_envs,
                        test_years=sweep.test_years,
                        holdout_frac=sweep.holdout_frac,
                    )
                )
    return configs


def _split_metric(eval_all: pd.DataFrame, split: str) -> tuple[float | None, float | None]:
    frame = eval_all.loc[eval_all["split"] == split]
    if frame.empty:
        return None, None
    series = pd.to_numeric(frame["total_reward"], errors="coerce")
    if series.dropna().empty:
        return None, None
    return float(series.mean()), float(series.std(ddof=0))


def run_rl_sweep(
    episodes: pd.DataFrame,
    env_builder: Callable[[dict[str, Any], str], Any],
    *,
    sweep: RlSweepConfig | None = None,
) -> pd.DataFrame:
    """Run an RL grid sweep and return one result row per configuration."""

    if sweep is None:
        sweep = RlSweepConfig()

    rows: list[dict[str, Any]] = []
    for config in _iter_experiment_configs(sweep):
        result = run_split_rl_experiment(
            episodes=episodes,
            env_builder=env_builder,
            config=config,
        )
        eval_all = result["evaluations"]["all"]
        train_mean, train_std = _split_metric(eval_all, "train")
        test_year_mean, test_year_std = _split_metric(eval_all, "test_year")
        holdout_mean, holdout_std = _split_metric(eval_all, "holdout_site")

        rows.append(
            {
                "algorithm": config.algorithm,
                "total_timesteps": config.total_timesteps,
                "seed": config.seed,
                "max_train_envs": config.max_train_envs,
                "holdout_frac": config.holdout_frac,
                "train_reward_mean": train_mean,
                "train_reward_std": train_std,
                "test_year_reward_mean": test_year_mean,
                "test_year_reward_std": test_year_std,
                "holdout_site_reward_mean": holdout_mean,
                "holdout_site_reward_std": holdout_std,
                "n_eval_rows": int(len(eval_all)),
            }
        )
    return pd.DataFrame(rows)


def select_best_sweep_run(
    results: pd.DataFrame,
    *,
    metric_col: str = "test_year_reward_mean",
    higher_is_better: bool = True,
) -> dict[str, Any]:
    """Return the best config row from a sweep table."""

    if results.empty:
        raise ValueError("Sweep results are empty")
    if metric_col not in results.columns:
        raise KeyError(f"Metric column not found: {metric_col}")

    scores = pd.to_numeric(results[metric_col], errors="coerce")
    valid = results.loc[scores.notna()].copy()
    if valid.empty:
        raise ValueError(f"No valid numeric values in metric column: {metric_col}")

    if higher_is_better:
        best_idx = pd.to_numeric(valid[metric_col], errors="coerce").idxmax()
    else:
        best_idx = pd.to_numeric(valid[metric_col], errors="coerce").idxmin()
    return valid.loc[best_idx].to_dict()

