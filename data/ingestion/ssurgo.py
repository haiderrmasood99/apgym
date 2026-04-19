"""SSURGO horizon ingestion into APGym soil profile contract."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import pandas as pd

from apgym.data.ingestion.utils import coalesce_column, load_mapping_json, load_tabular, optional_float


def _candidates(mapping: dict[str, Any], key: str, defaults: list[str]) -> list[str]:
    value = mapping.get(key)
    if value is None:
        return defaults
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [str(v) for v in value]
    raise ValueError(f"Invalid mapping for {key!r}")


def _resolve(frame: pd.DataFrame, candidates: list[str], label: str, required: bool = True) -> str | None:
    col = coalesce_column(frame, candidates)
    if col is None and required:
        raise KeyError(f"Could not resolve {label}. Tried: {candidates}")
    return col


def ingest_ssurgo_chorizon(
    frame: pd.DataFrame,
    mapping: dict[str, Any] | None = None,
    default_site_id_prefix: str = "ssurgo",
) -> pd.DataFrame:
    """Convert SSURGO horizon table to APGym normalized soil layers.

    Expected raw columns usually include:
    - `mukey` or provided `site_id`
    - `hzdept_r`, `hzdepb_r` (cm)
    - `dbthirdbar_r` (g/cc)
    - `wfifteenbar_r`, `wthirdbar_r`, `wsatiated_r` (%)
    - `ph1to1h2o_r`
    - `om_r` (% organic matter)
    """

    mapping = mapping or {}
    site_col = _resolve(frame, _candidates(mapping, "site_id", ["site_id", "mukey", "cokey"]), "site_id")
    top_col = _resolve(frame, _candidates(mapping, "layer_top_cm", ["hzdept_r", "layer_top_cm"]), "layer_top_cm")
    bottom_col = _resolve(
        frame, _candidates(mapping, "layer_bottom_cm", ["hzdepb_r", "layer_bottom_cm"]), "layer_bottom_cm"
    )
    bd_col = _resolve(frame, _candidates(mapping, "bulk_density", ["dbthirdbar_r", "bulk_density"]), "bulk_density")
    ll15_col = _resolve(frame, _candidates(mapping, "ll15_pct", ["wfifteenbar_r", "ll15_pct"]), "ll15_pct")
    dul_col = _resolve(frame, _candidates(mapping, "dul_pct", ["wthirdbar_r", "dul_pct"]), "dul_pct")
    sat_col = _resolve(
        frame, _candidates(mapping, "sat_pct", ["wsatiated_r", "sat_pct"]), "sat_pct", required=False
    )
    ph_col = _resolve(frame, _candidates(mapping, "ph", ["ph1to1h2o_r", "ph"]), "ph")
    oc_col = _resolve(frame, _candidates(mapping, "oc_pct", ["oc", "oc_pct"]), "oc_pct", required=False)
    om_col = _resolve(frame, _candidates(mapping, "om_pct", ["om_r", "om_pct"]), "om_pct", required=False)
    no3_col = _resolve(frame, _candidates(mapping, "no3_kg_ha", ["no3_kg_ha", "no3"]), "no3_kg_ha", required=False)
    nh4_col = _resolve(frame, _candidates(mapping, "nh4_kg_ha", ["nh4_kg_ha", "nh4"]), "nh4_kg_ha", required=False)
    sand_col = _resolve(
        frame, _candidates(mapping, "sand_pct", ["sandtotal_r", "sand_pct"]), "sand_pct", required=False
    )
    silt_col = _resolve(
        frame, _candidates(mapping, "silt_pct", ["silttotal_r", "silt_pct"]), "silt_pct", required=False
    )
    clay_col = _resolve(
        frame, _candidates(mapping, "clay_pct", ["claytotal_r", "clay_pct"]), "clay_pct", required=False
    )

    site_series = frame[site_col].astype("string")
    if site_series.isna().all():
        site_series = pd.Series(
            [f"{default_site_id_prefix}_{i}" for i in range(len(frame))], dtype="string"
        )

    ll15 = optional_float(frame[ll15_col]) / 100.0
    dul = optional_float(frame[dul_col]) / 100.0
    sat = optional_float(frame[sat_col]) / 100.0 if sat_col else (dul + 0.05).clip(upper=0.9)

    if oc_col:
        oc_pct = optional_float(frame[oc_col])
    elif om_col:
        oc_pct = optional_float(frame[om_col]) / 1.724
    else:
        oc_pct = pd.Series([pd.NA] * len(frame))

    out = pd.DataFrame(
        {
            "site_id": site_series,
            "layer_top_mm": optional_float(frame[top_col]) * 10.0,
            "layer_bottom_mm": optional_float(frame[bottom_col]) * 10.0,
            "bulk_density": optional_float(frame[bd_col]),
            "ll15": ll15,
            "dul": dul,
            "sat": sat,
            "ph": optional_float(frame[ph_col]),
            "oc_pct": oc_pct,
            "no3_kg_ha": optional_float(frame[no3_col]) if no3_col else pd.Series([pd.NA] * len(frame)),
            "nh4_kg_ha": optional_float(frame[nh4_col]) if nh4_col else pd.Series([pd.NA] * len(frame)),
            "sand_pct": optional_float(frame[sand_col]) if sand_col else pd.Series([pd.NA] * len(frame)),
            "silt_pct": optional_float(frame[silt_col]) if silt_col else pd.Series([pd.NA] * len(frame)),
            "clay_pct": optional_float(frame[clay_col]) if clay_col else pd.Series([pd.NA] * len(frame)),
        }
    )
    out = out.dropna(
        subset=[
            "site_id",
            "layer_top_mm",
            "layer_bottom_mm",
            "bulk_density",
            "ll15",
            "dul",
            "sat",
            "ph",
            "oc_pct",
        ]
    )
    out = out.sort_values(by=["site_id", "layer_top_mm"]).reset_index(drop=True)
    return out


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Normalize SSURGO horizon table to APGym soil profile schema.")
    parser.add_argument("--input", required=True, help="Path to SSURGO horizon table")
    parser.add_argument("--output", required=True, help="Output file path (.parquet or .csv)")
    parser.add_argument("--mapping-json", default=None, help="Optional mapping JSON")
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    frame = load_tabular(args.input)
    mapping = load_mapping_json(args.mapping_json)
    normalized = ingest_ssurgo_chorizon(frame, mapping=mapping)
    output = Path(args.output).expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.suffix.lower() == ".parquet":
        normalized.to_parquet(output, index=False)
    else:
        normalized.to_csv(output, index=False)
    print(f"Wrote soil profile table: {output}")


if __name__ == "__main__":
    main()
