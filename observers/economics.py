from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

import numpy as np
import pandas as pd

from apgym.observers.base import Observer


@dataclass
class EconomicsObserver(Observer):
    def __post_init__(self) -> None:
        self.feature_names = ("cumulative_n_kg_ha", "remaining_budget_usd_ha")
        self.low = np.array([0.0, -5000.0], dtype=np.float32)
        self.high = np.array([600.0, 10000.0], dtype=np.float32)

    def observe(
        self, reports: Mapping[str, pd.DataFrame], state: Mapping[str, float]
    ) -> np.ndarray:
        del reports
        return np.array(
            [
                state.get("cumulative_n_kg_ha", 0.0),
                state.get("remaining_budget_usd_ha", 0.0),
            ],
            dtype=np.float32,
        )
