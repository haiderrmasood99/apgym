"""Economic assumptions used by rewards and validation."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EconomicsScenario:
    grain_price_usd_per_ton: float
    nitrogen_cost_usd_per_kg: float
    irrigation_cost_usd_per_mm: float = 0.0
    fixed_operating_cost_usd_per_ha: float = 0.0

    def validate(self) -> None:
        if self.grain_price_usd_per_ton <= 0:
            raise ValueError("Grain price must be positive")
        if self.nitrogen_cost_usd_per_kg < 0:
            raise ValueError("Nitrogen cost cannot be negative")
        if self.irrigation_cost_usd_per_mm < 0:
            raise ValueError("Irrigation cost cannot be negative")
