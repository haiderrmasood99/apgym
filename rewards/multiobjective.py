"""Composed objective with explicit environmental penalties."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MultiObjectiveRewarder:
    base_rewarder: object
    leaching_penalty_usd_per_kg: float = 0.0
    water_penalty_usd_per_mm: float = 0.0

    def step_reward(self, applied_n_kg_ha: float) -> float:
        return float(self.base_rewarder.step_reward(applied_n_kg_ha))

    def terminal_reward(
        self,
        yield_t_ha: float,
        leaching_kg_ha: float = 0.0,
        irrigation_mm: float = 0.0,
    ) -> float:
        reward = float(self.base_rewarder.terminal_reward(yield_t_ha))
        reward -= self.leaching_penalty_usd_per_kg * leaching_kg_ha
        reward -= self.water_penalty_usd_per_mm * irrigation_mm
        return reward
