"""Nitrogen usage constraints and diagnostic costs."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class NitrogenConstraintTracker:
    max_total_n_kg_ha: float
    max_events: int

    def costs(self, total_n_kg_ha: float, event_count: int) -> dict[str, float]:
        return {
            "cost_total_n_excess": max(0.0, total_n_kg_ha - self.max_total_n_kg_ha),
            "cost_event_excess": float(max(0, event_count - self.max_events)),
        }
