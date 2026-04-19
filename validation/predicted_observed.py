"""Utilities to align APSIM predictions with observed measurements."""

from __future__ import annotations

from collections.abc import Sequence

import pandas as pd


def align_predicted_observed(
    predicted: pd.DataFrame,
    observed: pd.DataFrame,
    keys: Sequence[str],
    predicted_col: str,
    observed_col: str,
) -> pd.DataFrame:
    required_pred = set(keys) | {predicted_col}
    required_obs = set(keys) | {observed_col}

    missing_pred = sorted(required_pred - set(predicted.columns))
    missing_obs = sorted(required_obs - set(observed.columns))
    if missing_pred:
        raise ValueError(f"Predicted frame missing columns: {missing_pred}")
    if missing_obs:
        raise ValueError(f"Observed frame missing columns: {missing_obs}")

    merged = predicted.merge(observed, on=list(keys), how="inner", suffixes=("_pred", "_obs"))
    pred_name = predicted_col if predicted_col in merged.columns else f"{predicted_col}_pred"
    obs_name = observed_col if observed_col in merged.columns else f"{observed_col}_obs"
    return merged.rename(columns={pred_name: "predicted", obs_name: "observed"})
