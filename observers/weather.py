from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

import numpy as np
import pandas as pd

from apgym.observers.base import Observer


@dataclass
class WeatherObserver(Observer):
    def __post_init__(self) -> None:
        self.feature_names = ("recent_rain_mm", "recent_tmean_c", "cumulative_rain_mm")
        self.low = np.array([0.0, -20.0, 0.0], dtype=np.float32)
        self.high = np.array([300.0, 60.0, 5000.0], dtype=np.float32)

    def observe(
        self, reports: Mapping[str, pd.DataFrame], state: Mapping[str, float]
    ) -> np.ndarray:
        del reports
        return np.array(
            [
                state.get("recent_rain_mm", 0.0),
                state.get("recent_tmean_c", 0.0),
                state.get("cumulative_rain_mm", 0.0),
            ],
            dtype=np.float32,
        )
