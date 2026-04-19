"""Management event schema for APGym scenarios."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date


@dataclass(frozen=True)
class NitrogenApplication:
    date: date
    amount_kg_ha: float
    source: str = "Urea"
    method: str = "Surface"


@dataclass(frozen=True)
class SeasonManagementPlan:
    planting_date: date
    harvest_date: date
    crop: str
    cultivar: str | None = None
    nitrogen_events: tuple[NitrogenApplication, ...] = field(default_factory=tuple)
    irrigation_mm: float = 0.0

    def validate(self) -> None:
        if self.harvest_date <= self.planting_date:
            raise ValueError("Harvest date must be after planting date")
        for event in self.nitrogen_events:
            if event.amount_kg_ha < 0:
                raise ValueError("Nitrogen application amount must be non-negative")
