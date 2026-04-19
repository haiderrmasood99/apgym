from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass
class TimingConstraint:
    latest_application_date: date

    def costs(self, action_date: date, applied_amount_kg_ha: float) -> dict[str, float]:
        late = action_date > self.latest_application_date and applied_amount_kg_ha > 0
        return {"cost_late_application": float(late)}
