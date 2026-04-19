from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class IrrigationAction:
    date: date
    amount_mm: float
