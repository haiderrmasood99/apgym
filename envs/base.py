"""Common environment scaffolding for APSIM-backed tasks."""

from __future__ import annotations

from abc import ABC
from pathlib import Path
from typing import Any

import numpy as np

from apgym._compat import IS_GYMNASIUM, gym
from apgym.simulator import ApsimRunner


class ApsimBaseEnv(gym.Env, ABC):
    metadata = {"render_modes": []}

    def __init__(self, runner: ApsimRunner, template_path: str | Path):
        super().__init__()
        self.runner = runner
        self.template_path = Path(template_path).expanduser().resolve()
        self.last_info: dict[str, Any] = {}
        self.last_observation: np.ndarray | None = None
        self.last_reward: float = 0.0
        self.terminated = False
        self.truncated = False

    def _pack_reset(self, obs: np.ndarray, info: dict[str, Any]):
        if IS_GYMNASIUM:
            return obs, info
        return obs

    def _pack_step(
        self,
        obs: np.ndarray,
        reward: float,
        terminated: bool,
        truncated: bool,
        info: dict[str, Any],
    ):
        if IS_GYMNASIUM:
            return obs, reward, terminated, truncated, info
        return obs, reward, terminated or truncated, info
