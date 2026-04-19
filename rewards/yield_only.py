"""Reward utility for pure yield objectives."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class YieldRewarder:
    scale: float = 1.0

    def step_reward(self, applied_n_kg_ha: float) -> float:
        del applied_n_kg_ha
        return 0.0

    def terminal_reward(self, yield_t_ha: float) -> float:
        return self.scale * yield_t_ha
