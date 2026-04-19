"""Helpers to compare policy outcomes on common metrics."""

from __future__ import annotations

import pandas as pd


def compare_policies(
    results: pd.DataFrame,
    policy_col: str = "policy",
    metric_cols: tuple[str, ...] = ("profit_usd_ha", "yield_t_ha", "leaching_kg_ha"),
) -> pd.DataFrame:
    required = {policy_col, *metric_cols}
    missing = sorted(required - set(results.columns))
    if missing:
        raise ValueError(f"Policy results missing columns: {missing}")
    return (
        results.groupby(policy_col)[list(metric_cols)]
        .agg(["mean", "std", "min", "max"])
        .sort_values((metric_cols[0], "mean"), ascending=False)
    )
