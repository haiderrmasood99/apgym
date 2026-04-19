from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

import numpy as np
import pandas as pd

from apgym.observers.base import Observer


@dataclass
class SoilObserver(Observer):
    def __post_init__(self) -> None:
        self.feature_names = ("soil_water_top_mm", "soil_mineral_n_kg_ha")
        self.low = np.array([0.0, 0.0], dtype=np.float32)
        self.high = np.array([500.0, 500.0], dtype=np.float32)

    def observe(
        self, reports: Mapping[str, pd.DataFrame], state: Mapping[str, float]
    ) -> np.ndarray:
        del reports
        return np.array(
            [
                state.get("soil_water_top_mm", 0.0),
                state.get("soil_mineral_n_kg_ha", 0.0),
            ],
            dtype=np.float32,
        )
