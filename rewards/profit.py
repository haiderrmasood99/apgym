"""Reward shaping based on grower economics."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ProfitRewarder:
    grain_price_usd_per_ton: float
    nitrogen_cost_usd_per_kg: float
    fixed_cost_usd_per_ha: float = 0.0

    def step_reward(self, applied_n_kg_ha: float) -> float:
        return -applied_n_kg_ha * self.nitrogen_cost_usd_per_kg

    def terminal_reward(self, yield_t_ha: float) -> float:
        return yield_t_ha * self.grain_price_usd_per_ton - self.fixed_cost_usd_per_ha
