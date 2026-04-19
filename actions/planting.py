from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class PlantingAction:
    date: date
    cultivar: str
    density_plants_m2: float | None = None
