"""Nitrogen action mapping for the first APGym benchmark."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Sequence

from apgym._compat import spaces


@dataclass(frozen=True)
class NitrogenAction:
    date: date
    amount_kg_ha: float


class DiscreteNitrogenActionMapper:
    def __init__(self, dose_levels_kg_ha: Sequence[float]):
        if not dose_levels_kg_ha:
            raise ValueError("At least one nitrogen dose level is required")
        if any(level < 0 for level in dose_levels_kg_ha):
            raise ValueError("Dose levels must be non-negative")
        self.dose_levels_kg_ha = tuple(float(x) for x in dose_levels_kg_ha)
        self.action_space = spaces.Discrete(len(self.dose_levels_kg_ha))

    def map(self, action: int, action_date: date) -> NitrogenAction:
        if not self.action_space.contains(action):
            raise ValueError(f"Invalid action index {action}")
        return NitrogenAction(
            date=action_date,
            amount_kg_ha=self.dose_levels_kg_ha[action],
        )
