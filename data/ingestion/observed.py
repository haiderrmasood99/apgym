"""Generic observed-output normalization helpers."""

from __future__ import annotations

from typing import Any

import pandas as pd

from apgym.data.ingestion.utils import optional_float, require_column


def normalize_observed_outputs(
    frame: pd.DataFrame,
    mapping: dict[str, Any] | None = None,
) -> pd.DataFrame:
    mapping = mapping or {}
    site_candidates = mapping.get("site_id", ["site_id", "location", "field_id"])
    year_candidates = mapping.get("season_year", ["season_year", "year"])
    yield_candidates = mapping.get("yield_t_ha", ["yield_t_ha", "yield", "grain_yield"])

    site_col = require_column(frame, site_candidates, "site_id")
    year_col = require_column(frame, year_candidates, "season_year")
    yield_col = require_column(frame, yield_candidates, "yield_t_ha")

    out = pd.DataFrame(
        {
            "site_id": frame[site_col].astype("string"),
            "season_year": pd.to_numeric(frame[year_col], errors="coerce").astype("Int64"),
            "yield_t_ha": optional_float(frame[yield_col]),
        }
    ).dropna(subset=["site_id", "season_year", "yield_t_ha"])

    optional_map = {
        "biomass_t_ha": ["biomass_t_ha", "biomass"],
        "season_irrigation_mm": ["season_irrigation_mm", "irrigation_mm"],
        "season_et_mm": ["season_et_mm", "et_mm", "et"],
    }
    for target_col, candidates in optional_map.items():
        source = next((c for c in candidates if c in frame.columns), None)
        if source is not None:
            out[target_col] = optional_float(frame[source])

    out["season_year"] = out["season_year"].astype(int)
    return out.reset_index(drop=True)
