"""Stable-Baselines3 training harness integrated with APGym split utilities."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable

import pandas as pd

from apgym.validation.splits import SplitResult, make_generalization_splits


@dataclass(frozen=True)
class RlExperimentConfig:
    algorithm: str = "ppo"
    total_timesteps: int = 5_000
    seed: int = 0
    deterministic_eval: bool = True
    max_train_envs: int = 4
    test_years: tuple[int, ...] | None = None
    holdout_frac: float = 0.2


def _parse_reset(reset_out: Any) -> tuple[Any, dict[str, Any]]:
    if isinstance(reset_out, tuple) and len(reset_out) == 2:
        return reset_out[0], dict(reset_out[1])
    return reset_out, {}


def _parse_step(step_out: Any) -> tuple[Any, float, bool, dict[str, Any]]:
    if isinstance(step_out, tuple) and len(step_out) == 5:
        obs, reward, terminated, truncated, info = step_out
        done = bool(terminated or truncated)
        return obs, float(reward), done, dict(info)
    if isinstance(step_out, tuple) and len(step_out) == 4:
        obs, reward, done, info = step_out
        return obs, float(reward), bool(done), dict(info)
    raise TypeError("Unexpected env.step output shape")


def _build_sb3_model(algorithm: str, env: Any, seed: int):
    try:
        from stable_baselines3 import A2C, PPO
    except ImportError as exc:  # pragma: no cover
        raise RuntimeError(
            "stable-baselines3 is required for RL training. Install it with: pip install stable-baselines3"
        ) from exc

    algo = algorithm.lower()
    if algo == "ppo":
        return PPO("MlpPolicy", env, verbose=0, seed=seed)
    if algo == "a2c":
        return A2C("MlpPolicy", env, verbose=0, seed=seed)
    raise ValueError(f"Unsupported algorithm: {algorithm!r} (use 'ppo' or 'a2c')")


def evaluate_model_on_rows(
    model: Any,
    rows: pd.DataFrame,
    env_builder: Callable[[dict[str, Any], str], Any],
    *,
    split_name: str,
    deterministic: bool = True,
) -> pd.DataFrame:
    if rows.empty:
        return pd.DataFrame(
            columns=[
                "split",
                "episode",
                "total_reward",
                "steps",
                "site_id",
                "season_year",
            ]
        )

    results: list[dict[str, Any]] = []
    for episode_idx, (_, row) in enumerate(rows.iterrows()):
        row_dict = row.to_dict()
        env = env_builder(row_dict, split_name)
        obs, info = _parse_reset(env.reset())

        total_reward = 0.0
        steps = 0
        done = False
        while not done:
            action, _state = model.predict(obs, deterministic=deterministic)
            obs, reward, done, info = _parse_step(env.step(action))
            total_reward += reward
            steps += 1
            if steps > 2000:
                break

        result = {
            "split": split_name,
            "episode": episode_idx,
            "total_reward": total_reward,
            "steps": steps,
        }
        for key in ("site_id", "season_year"):
            if key in row_dict:
                result[key] = row_dict[key]
        result.update(info)
        results.append(result)
    return pd.DataFrame(results)


def _train_model(
    train_rows: pd.DataFrame,
    env_builder: Callable[[dict[str, Any], str], Any],
    config: RlExperimentConfig,
):
    try:
        from stable_baselines3.common.vec_env import DummyVecEnv
    except ImportError as exc:  # pragma: no cover
        raise RuntimeError(
            "stable-baselines3 is required for RL training. Install it with: pip install stable-baselines3"
        ) from exc

    selected = train_rows.head(max(1, config.max_train_envs))
    env_fns = []
    for _, row in selected.iterrows():
        row_dict = row.to_dict()
        env_fns.append(lambda row_dict=row_dict: env_builder(row_dict, "train"))

    vec_env = DummyVecEnv(env_fns)
    model = _build_sb3_model(config.algorithm, vec_env, config.seed)
    model.learn(total_timesteps=int(config.total_timesteps))
    return model


def run_split_rl_experiment(
    episodes: pd.DataFrame,
    env_builder: Callable[[dict[str, Any], str], Any],
    *,
    config: RlExperimentConfig | None = None,
) -> dict[str, Any]:
    if config is None:
        config = RlExperimentConfig()
    if episodes.empty:
        raise ValueError("episodes table is empty")

    split_result: SplitResult = make_generalization_splits(
        episodes,
        test_years=config.test_years,
        holdout_frac=config.holdout_frac,
        seed=config.seed,
    )
    train_rows = split_result.train if not split_result.train.empty else episodes
    model = _train_model(train_rows, env_builder, config=config)

    train_eval = evaluate_model_on_rows(
        model, train_rows, env_builder, split_name="train", deterministic=config.deterministic_eval
    )
    test_eval = evaluate_model_on_rows(
        model,
        split_result.test_year,
        env_builder,
        split_name="test_year",
        deterministic=config.deterministic_eval,
    )
    holdout_eval = evaluate_model_on_rows(
        model,
        split_result.holdout_site,
        env_builder,
        split_name="holdout_site",
        deterministic=config.deterministic_eval,
    )

    all_eval = pd.concat([train_eval, test_eval, holdout_eval], ignore_index=True)
    summary = (
        all_eval.groupby("split")[["total_reward"]]
        .agg(["mean", "std", "min", "max"])
        .sort_index()
    )
    return {
        "model": model,
        "splits": split_result,
        "evaluations": {
            "train": train_eval,
            "test_year": test_eval,
            "holdout_site": holdout_eval,
            "all": all_eval,
        },
        "summary": summary,
    }
