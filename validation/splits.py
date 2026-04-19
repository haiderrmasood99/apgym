"""Train/test/holdout split helpers for APGym experiments."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class SplitResult:
    train: pd.DataFrame
    test_year: pd.DataFrame
    holdout_site: pd.DataFrame


def split_by_year(
    frame: pd.DataFrame,
    *,
    year_col: str = "season_year",
    test_years: Sequence[int] | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    if year_col not in frame.columns:
        raise KeyError(f"Missing year column: {year_col}")
    years = sorted(pd.Series(frame[year_col]).dropna().astype(int).unique().tolist())
    if not years:
        return frame.copy(), frame.iloc[0:0].copy()
    if test_years is None:
        test_years = [years[-1]]
    test_years_set = set(int(y) for y in test_years)
    is_test = frame[year_col].astype(int).isin(test_years_set)
    return frame.loc[~is_test].copy(), frame.loc[is_test].copy()


def split_holdout_sites(
    frame: pd.DataFrame,
    *,
    site_col: str = "site_id",
    holdout_frac: float = 0.2,
    seed: int = 0,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    if site_col not in frame.columns:
        raise KeyError(f"Missing site column: {site_col}")
    if not (0 < holdout_frac < 1):
        raise ValueError("holdout_frac must be in (0, 1)")
    sites = sorted(pd.Series(frame[site_col]).dropna().astype(str).unique().tolist())
    if len(sites) <= 1:
        return frame.copy(), frame.iloc[0:0].copy()
    rng = np.random.default_rng(seed)
    n_holdout = max(1, int(round(len(sites) * holdout_frac)))
    holdout_sites = set(rng.choice(sites, size=n_holdout, replace=False).tolist())
    is_holdout = frame[site_col].astype(str).isin(holdout_sites)
    return frame.loc[~is_holdout].copy(), frame.loc[is_holdout].copy()


def make_generalization_splits(
    frame: pd.DataFrame,
    *,
    site_col: str = "site_id",
    year_col: str = "season_year",
    test_years: Sequence[int] | None = None,
    holdout_frac: float = 0.2,
    seed: int = 0,
) -> SplitResult:
    in_sample, test_year = split_by_year(frame, year_col=year_col, test_years=test_years)
    train, holdout_site = split_holdout_sites(
        in_sample, site_col=site_col, holdout_frac=holdout_frac, seed=seed
    )
    return SplitResult(train=train, test_year=test_year, holdout_site=holdout_site)
