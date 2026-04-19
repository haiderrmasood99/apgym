from __future__ import annotations

from dataclasses import dataclass


@dataclass
class WaterConstraint:
    max_irrigation_mm: float

    def costs(self, irrigation_mm: float) -> dict[str, float]:
        return {"cost_water_excess": max(0.0, irrigation_mm - self.max_irrigation_mm)}
