"""Fit metrics for simulator and policy validation."""

from __future__ import annotations

import numpy as np
import warnings

_RANK_WARNING = getattr(np, "RankWarning", getattr(np.exceptions, "RankWarning", Warning))


def rmse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.sqrt(np.mean((y_pred - y_true) ** 2)))


def mae(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.mean(np.abs(y_pred - y_true)))


def mean_bias(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.mean(y_pred - y_true))


def r2(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    if ss_tot == 0:
        return float("nan")
    return float(1 - ss_res / ss_tot)


def nse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    numerator = np.sum((y_true - y_pred) ** 2)
    denominator = np.sum((y_true - np.mean(y_true)) ** 2)
    if denominator == 0:
        return float("nan")
    return float(1 - numerator / denominator)


def slope_intercept(y_true: np.ndarray, y_pred: np.ndarray) -> tuple[float, float]:
    if len(y_true) < 2 or np.unique(y_true).size < 2:
        return float("nan"), float("nan")
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", _RANK_WARNING)
        slope, intercept = np.polyfit(y_true, y_pred, deg=1)
    return float(slope), float(intercept)


def compute_fit_metrics(y_true: np.ndarray, y_pred: np.ndarray) -> dict[str, float]:
    if y_true.shape != y_pred.shape:
        raise ValueError("y_true and y_pred must have identical shape")
    slope, intercept = slope_intercept(y_true, y_pred)
    return {
        "rmse": rmse(y_true, y_pred),
        "mae": mae(y_true, y_pred),
        "mean_bias": mean_bias(y_true, y_pred),
        "r2": r2(y_true, y_pred),
        "nse": nse(y_true, y_pred),
        "slope": slope,
        "intercept": intercept,
    }
