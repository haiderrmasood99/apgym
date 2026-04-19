from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

import numpy as np
import pandas as pd

from apgym.observers.base import Observer


@dataclass
class CropObserver(Observer):
    def __post_init__(self) -> None:
        self.feature_names = (
            "days_since_planting",
            "crop_stage_code",
            "lai",
            "biomass_kg_ha",
        )
        self.low = np.array([0.0, 0.0, 0.0, 0.0], dtype=np.float32)
        self.high = np.array([400.0, 20.0, 15.0, 50000.0], dtype=np.float32)

    def observe(
        self, reports: Mapping[str, pd.DataFrame], state: Mapping[str, float]
    ) -> np.ndarray:
        del reports
        return np.array(
            [
                state.get("days_since_planting", 0.0),
                state.get("crop_stage_code", 0.0),
                state.get("lai", 0.0),
                state.get("biomass_kg_ha", 0.0),
            ],
            dtype=np.float32,
        )
