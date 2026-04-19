"""Compose several observers into a single vector."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence

import numpy as np
import pandas as pd

from apgym.observers.base import Observer


@dataclass
class CompoundObserver(Observer):
    observers: Sequence[Observer]

    def __post_init__(self) -> None:
        self.feature_names = [
            name for observer in self.observers for name in observer.feature_names
        ]
        self.low = np.concatenate([observer.low for observer in self.observers]).astype(
            np.float32
        )
        self.high = np.concatenate([observer.high for observer in self.observers]).astype(
            np.float32
        )

    def observe(
        self, reports: Mapping[str, pd.DataFrame], state: Mapping[str, float]
    ) -> np.ndarray:
        vectors = [observer.observe(reports, state) for observer in self.observers]
        return np.concatenate(vectors).astype(np.float32)
