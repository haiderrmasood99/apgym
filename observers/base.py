"""Observation component interfaces."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Mapping, Sequence

import numpy as np
import pandas as pd


class Observer(ABC):
    feature_names: Sequence[str]
    low: np.ndarray
    high: np.ndarray

    @abstractmethod
    def observe(
        self,
        reports: Mapping[str, pd.DataFrame],
        state: Mapping[str, float],
    ) -> np.ndarray:
        raise NotImplementedError
