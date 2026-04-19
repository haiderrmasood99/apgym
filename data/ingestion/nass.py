"""Schema-aware NASS Quick Stats normalizers."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
from typing import Any

import pandas as pd

from apgym.data.ingestion.utils import load_tabular

MAIZE_BU_AC_TO_T_HA = 0.06277
_NON_NUMERIC_TOKENS = {"(d)", "(h)", "(l)", "(na)", "nan", "none", ""}


def _to_numeric_value(value: Any) -> float | None:
    if value is None:
        return None
    text = str(value).strip().lower()
    if text in _NON_NUMERIC_TOKENS:
        return None
    if text == "(z)":
        return 0.0
    cleaned = re.sub(r"[,\s]", "", text)
    try:
        return float(cleaned)
    except ValueError:
        return None


def _normalize_filter_value(frame: pd.DataFrame, column: str, expected: str) -> pd.Series:
    if column not in frame.columns:
        return pd.Series([True] * len(frame), index=frame.index)
    values = frame[column].astype("string").str.upper().str.strip()
    return values == expected.upper().strip()


def _zero_pad(value: Any, width: int) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    if text == "" or text.lower() == "nan":
        return None
    if not re.fullmatch(r"\d+", text):
        return None
    return text.zfill(width)


def _site_id_from_row(row: pd.Series) -> str | None:
    state_fips = _zero_pad(row.get("state_fips_code"), 2)
    county_fips = _zero_pad(row.get("county_code"), 3)
    if state_fips and county_fips:
        return f"US-{state_fips}{county_fips}"

    state_name = str(row.get("state_name", "")).strip().upper()
    county_name = str(row.get("county_name", "")).strip().upper()
    if state_name and county_name and state_name != "NAN" and county_name != "NAN":
        state_slug = re.sub(r"[^A-Z0-9]+", "_", state_name).strip("_")
        county_slug = re.sub(r"[^A-Z0-9]+", "_", county_name).strip("_")
        if state_slug and county_slug:
            return f"US-{state_slug}-{county_slug}"
    return None


def normalize_nass_quickstats_yield(
    frame: pd.DataFrame,
    *,
    commodity_desc: str = "CORN",
    statisticcat_desc: str = "YIELD",
    unit_desc: str = "BU / ACRE",
) -> pd.DataFrame:
    """Convert NASS Quick Stats rows to APGym observed output contract."""

    normalized = frame.copy()
    normalized.columns = [str(col).strip().lower() for col in normalized.columns]

    required = {"year", "value"}
    missing = sorted(required - set(normalized.columns))
    if missing:
        raise ValueError(
            f"NASS table missing required columns: {missing}. "
            "Expected at least year and Value."
        )

    commodity_mask = _normalize_filter_value(normalized, "commodity_desc", commodity_desc)
    statistic_mask = _normalize_filter_value(normalized, "statisticcat_desc", statisticcat_desc)
    unit_mask = _normalize_filter_value(normalized, "unit_desc", unit_desc)

    filtered = normalized.loc[commodity_mask & statistic_mask & unit_mask].copy()
    if filtered.empty:
        return pd.DataFrame(columns=["site_id", "season_year", "yield_t_ha"])

    filtered["season_year"] = pd.to_numeric(filtered["year"], errors="coerce").astype("Int64")
    filtered["yield_bu_ac"] = filtered["value"].map(_to_numeric_value)
    filtered["yield_t_ha"] = pd.to_numeric(filtered["yield_bu_ac"], errors="coerce") * MAIZE_BU_AC_TO_T_HA
    filtered["site_id"] = filtered.apply(_site_id_from_row, axis=1)

    keep_cols = [
        "site_id",
        "season_year",
        "yield_t_ha",
        "state_name",
        "county_name",
        "state_fips_code",
        "county_code",
        "commodity_desc",
        "statisticcat_desc",
        "unit_desc",
    ]
    for col in keep_cols:
        if col not in filtered.columns:
            filtered[col] = pd.NA

    out = filtered[keep_cols].dropna(subset=["site_id", "season_year", "yield_t_ha"])
    if out.empty:
        return pd.DataFrame(columns=["site_id", "season_year", "yield_t_ha"])

    out = out.rename(
        columns={
            "state_fips_code": "state_fips",
            "county_code": "county_fips",
        }
    )
    out["season_year"] = out["season_year"].astype(int)
    out["source"] = "nass_quickstats"
    return out.reset_index(drop=True)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Normalize NASS Quick Stats yield rows into APGym observed_outputs format."
    )
    parser.add_argument("--input", required=True, help="Input .csv/.parquet from NASS API")
    parser.add_argument("--output", required=True, help="Output .csv/.parquet path")
    parser.add_argument("--commodity", default="CORN", help="Filter commodity_desc")
    parser.add_argument("--statistic", default="YIELD", help="Filter statisticcat_desc")
    parser.add_argument("--unit", default="BU / ACRE", help="Filter unit_desc")
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    frame = load_tabular(args.input)
    out = normalize_nass_quickstats_yield(
        frame,
        commodity_desc=args.commodity,
        statisticcat_desc=args.statistic,
        unit_desc=args.unit,
    )
    target = Path(args.output).expanduser().resolve()
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.suffix.lower() == ".parquet":
        out.to_parquet(target, index=False)
    else:
        out.to_csv(target, index=False)
    print(f"Wrote normalized NASS outputs: {target}")


if __name__ == "__main__":
    main()
