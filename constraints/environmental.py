from __future__ import annotations

from dataclasses import dataclass


@dataclass
class EnvironmentalConstraint:
    max_leaching_kg_ha: float

    def costs(self, leaching_kg_ha: float) -> dict[str, float]:
        return {
            "cost_leaching_excess": max(0.0, leaching_kg_ha - self.max_leaching_kg_ha)
        }
