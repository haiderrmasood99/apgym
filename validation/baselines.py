"""Baseline policy evaluation harness for APGym environments."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

import pandas as pd


PolicyFn = Callable[[Any, dict[str, Any], int, Any], int]


def no_action_policy(obs: Any, info: dict[str, Any], step_idx: int, env: Any) -> int:
    del obs, info, step_idx, env
    return 0


def fixed_schedule_policy(schedule: dict[int, int]) -> PolicyFn:
    def _policy(obs: Any, info: dict[str, Any], step_idx: int, env: Any) -> int:
        del obs, info, env
        return int(schedule.get(step_idx, 0))

    return _policy


def capped_n_policy(target_total_n_kg_ha: float, action_if_under_cap: int) -> PolicyFn:
    def _policy(obs: Any, info: dict[str, Any], step_idx: int, env: Any) -> int:
        del obs, step_idx, env
        if float(info.get("total_n_applied_kg_ha", 0.0)) < target_total_n_kg_ha:
            return int(action_if_under_cap)
        return 0

    return _policy


@dataclass(frozen=True)
class EpisodeResult:
    total_reward: float
    steps: int
    final_info: dict[str, Any]


def _step_done(step_out: tuple) -> tuple[Any, float, bool, dict[str, Any]]:
    if len(step_out) == 5:
        obs, reward, terminated, truncated, info = step_out
        done = bool(terminated or truncated)
    else:
        obs, reward, done, info = step_out
        done = bool(done)
    return obs, float(reward), done, dict(info)


def rollout_episode(env: Any, policy: PolicyFn, max_steps: int | None = None) -> EpisodeResult:
    reset_out = env.reset()
    if isinstance(reset_out, tuple) and len(reset_out) == 2:
        obs, info = reset_out
    else:
        obs, info = reset_out, {}

    total_reward = 0.0
    step_idx = 0
    while True:
        action = policy(obs, info, step_idx, env)
        obs, reward, done, info = _step_done(env.step(action))
        total_reward += reward
        step_idx += 1
        if done:
            break
        if max_steps is not None and step_idx >= max_steps:
            break

    return EpisodeResult(total_reward=total_reward, steps=step_idx, final_info=info)


def evaluate_policy(
    env_factory: Callable[[int], Any],
    policy: PolicyFn,
    *,
    n_episodes: int = 5,
    max_steps: int | None = None,
) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for episode_idx in range(n_episodes):
        env = env_factory(episode_idx)
        result = rollout_episode(env, policy, max_steps=max_steps)
        row = {
            "episode": episode_idx,
            "total_reward": result.total_reward,
            "steps": result.steps,
        }
        row.update(result.final_info)
        rows.append(row)
    return pd.DataFrame(rows)


def evaluate_policy_set(
    env_factory: Callable[[int], Any],
    policies: dict[str, PolicyFn],
    *,
    n_episodes: int = 5,
    max_steps: int | None = None,
) -> pd.DataFrame:
    all_results: list[pd.DataFrame] = []
    for name, policy in policies.items():
        result = evaluate_policy(
            env_factory=env_factory,
            policy=policy,
            n_episodes=n_episodes,
            max_steps=max_steps,
        )
        result["policy"] = name
        all_results.append(result)
    if not all_results:
        return pd.DataFrame()
    return pd.concat(all_results, ignore_index=True)
