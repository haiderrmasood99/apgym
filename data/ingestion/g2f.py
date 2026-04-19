"""G2F harmonization helpers into APGym normalized tables."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import pandas as pd

from apgym.data.ingestion.bundle import DataBundle
from apgym.data.ingestion.utils import (
    coalesce_column,
    load_mapping_json,
    load_tabular,
    optional_float,
    parse_date_column,
    require_column,
)

MAIZE_BU_AC_TO_T_HA = 0.06277


def _candidates(mapping: dict[str, Any], key: str, defaults: list[str]) -> list[str]:
    custom = mapping.get(key)
    if custom is None:
        return defaults
    if isinstance(custom, str):
        return [custom]
    if isinstance(custom, list):
        return [str(x) for x in custom]
    raise ValueError(f"Invalid mapping value for key {key!r}")


def ingest_g2f_site_identity(
    frame: pd.DataFrame,
    mapping: dict[str, Any] | None = None,
    default_crop: str = "maize",
) -> pd.DataFrame:
    mapping = mapping or {}
    site_col = require_column(
        frame,
        _candidates(mapping, "site_id", ["site_id", "location", "env", "environment", "field_id"]),
        "site_id",
    )
    lat_col = require_column(frame, _candidates(mapping, "latitude", ["latitude", "lat"]), "latitude")
    lon_col = require_column(
        frame, _candidates(mapping, "longitude", ["longitude", "lon", "long"]), "longitude"
    )
    year_col = require_column(
        frame, _candidates(mapping, "season_year", ["year", "season_year", "yr"]), "season_year"
    )
    elevation_col = coalesce_column(
        frame, _candidates(mapping, "elevation_m", ["elevation_m", "elevation", "elev"])
    )
    region_col = coalesce_column(frame, _candidates(mapping, "region", ["region", "state", "location"]))
    cultivar_col = coalesce_column(
        frame, _candidates(mapping, "cultivar", ["cultivar", "hybrid", "genotype"])
    )
    crop_col = coalesce_column(frame, _candidates(mapping, "crop", ["crop"]))

    out = pd.DataFrame(
        {
            "site_id": frame[site_col].astype("string"),
            "latitude": optional_float(frame[lat_col]),
            "longitude": optional_float(frame[lon_col]),
            "elevation_m": optional_float(frame[elevation_col]) if elevation_col else 0.0,
            "region": frame[region_col].astype("string") if region_col else "unknown",
            "crop": frame[crop_col].astype("string") if crop_col else default_crop,
            "cultivar": frame[cultivar_col].astype("string") if cultivar_col else pd.Series([pd.NA] * len(frame)),
            "season_year": pd.to_numeric(frame[year_col], errors="coerce").astype("Int64"),
        }
    )
    out = out.dropna(subset=["site_id", "latitude", "longitude", "season_year"])
    out["season_year"] = out["season_year"].astype(int)
    return out.drop_duplicates(subset=["site_id", "season_year"]).reset_index(drop=True)


def ingest_g2f_observed_outputs(
    frame: pd.DataFrame,
    mapping: dict[str, Any] | None = None,
    yield_unit: str | None = None,
) -> pd.DataFrame:
    mapping = mapping or {}
    site_col = require_column(
        frame,
        _candidates(mapping, "site_id", ["site_id", "location", "env", "environment", "field_id"]),
        "site_id",
    )
    year_col = require_column(
        frame, _candidates(mapping, "season_year", ["year", "season_year", "yr"]), "season_year"
    )
    yield_col = require_column(
        frame,
        _candidates(
            mapping,
            "yield",
            ["yield_t_ha", "yield", "grain_yield", "grainyield", "yield_bu_ac", "yield_kg_ha"],
        ),
        "yield",
    )

    yield_series = optional_float(frame[yield_col])
    resolved_unit = yield_unit
    if resolved_unit is None:
        lower_name = yield_col.lower()
        if "bu" in lower_name:
            resolved_unit = "bu_ac"
        elif "kg_ha" in lower_name:
            resolved_unit = "kg_ha"
        else:
            resolved_unit = "t_ha"

    if resolved_unit == "bu_ac":
        yield_t_ha = yield_series * MAIZE_BU_AC_TO_T_HA
    elif resolved_unit == "kg_ha":
        yield_t_ha = yield_series / 1000.0
    else:
        yield_t_ha = yield_series

    out = pd.DataFrame(
        {
            "site_id": frame[site_col].astype("string"),
            "season_year": pd.to_numeric(frame[year_col], errors="coerce").astype("Int64"),
            "yield_t_ha": yield_t_ha,
        }
    ).dropna(subset=["site_id", "season_year", "yield_t_ha"])
    out["season_year"] = out["season_year"].astype(int)
    return out.reset_index(drop=True)


def ingest_g2f_weather(frame: pd.DataFrame, mapping: dict[str, Any] | None = None) -> pd.DataFrame:
    mapping = mapping or {}
    site_col = require_column(
        frame,
        _candidates(mapping, "site_id", ["site_id", "location", "env", "environment", "field_id"]),
        "site_id",
    )
    date_col = require_column(frame, _candidates(mapping, "date", ["date", "day", "time"]), "date")
    tmin_col = require_column(frame, _candidates(mapping, "tmin_c", ["tmin_c", "tmin", "mintemp"]), "tmin")
    tmax_col = require_column(frame, _candidates(mapping, "tmax_c", ["tmax_c", "tmax", "maxtemp"]), "tmax")
    rain_col = require_column(frame, _candidates(mapping, "rain_mm", ["rain_mm", "rain", "precip"]), "rain")
    rad_col = require_column(
        frame, _candidates(mapping, "rad_mj_m2", ["rad_mj_m2", "radn", "solar_rad"]), "rad_mj_m2"
    )
    wind_col = coalesce_column(frame, _candidates(mapping, "wind_m_s", ["wind_m_s", "wind"]))
    vp_col = coalesce_column(frame, _candidates(mapping, "vp_kpa", ["vp_kpa", "vapor_pressure"]))

    out = pd.DataFrame(
        {
            "site_id": frame[site_col].astype("string"),
            "date": parse_date_column(frame[date_col]),
            "tmin_c": optional_float(frame[tmin_col]),
            "tmax_c": optional_float(frame[tmax_col]),
            "rain_mm": optional_float(frame[rain_col]),
            "rad_mj_m2": optional_float(frame[rad_col]),
            "wind_m_s": optional_float(frame[wind_col]) if wind_col else pd.Series([pd.NA] * len(frame)),
            "vp_kpa": optional_float(frame[vp_col]) if vp_col else pd.Series([pd.NA] * len(frame)),
        }
    )
    return out.dropna(subset=["site_id", "date", "tmin_c", "tmax_c", "rain_mm", "rad_mj_m2"]).reset_index(
        drop=True
    )


def ingest_g2f_management_events(
    frame: pd.DataFrame,
    mapping: dict[str, Any] | None = None,
) -> pd.DataFrame:
    mapping = mapping or {}
    site_col = require_column(
        frame,
        _candidates(mapping, "site_id", ["site_id", "location", "env", "environment", "field_id"]),
        "site_id",
    )
    date_col = require_column(
        frame,
        _candidates(mapping, "date", ["date", "application_date", "event_date", "fert_date"]),
        "date",
    )
    amount_col = coalesce_column(
        frame,
        _candidates(mapping, "amount_kg_ha", ["amount_kg_ha", "n_kg_ha", "n_rate", "nitrogen_kg_ha"]),
    )
    event_type_col = coalesce_column(
        frame, _candidates(mapping, "event_type", ["event_type", "operation", "event"])
    )
    source_col = coalesce_column(frame, _candidates(mapping, "source", ["source", "fertilizer_type"]))
    method_col = coalesce_column(frame, _candidates(mapping, "method", ["method", "application_method"]))

    event_type = (
        frame[event_type_col].astype("string")
        if event_type_col
        else pd.Series(["fertilizer"] * len(frame), dtype="string")
    )

    out = pd.DataFrame(
        {
            "site_id": frame[site_col].astype("string"),
            "date": parse_date_column(frame[date_col]),
            "event_type": event_type.str.lower(),
            "amount_kg_ha": optional_float(frame[amount_col]) if amount_col else 0.0,
            "source": frame[source_col].astype("string")
            if source_col
            else pd.Series([pd.NA] * len(frame), dtype="string"),
            "method": frame[method_col].astype("string")
            if method_col
            else pd.Series([pd.NA] * len(frame), dtype="string"),
        }
    )
    out["event_type"] = out["event_type"].fillna("fertilizer")
    return out.dropna(subset=["site_id", "date", "event_type"]).reset_index(drop=True)


def build_g2f_bundle(
    *,
    site_path: str | Path,
    observed_path: str | Path,
    weather_path: str | Path | None = None,
    management_path: str | Path | None = None,
    mapping_json: str | Path | None = None,
) -> DataBundle:
    mapping = load_mapping_json(mapping_json)
    site_frame = load_tabular(site_path)
    obs_frame = load_tabular(observed_path)

    bundle = DataBundle(
        site_identity=ingest_g2f_site_identity(site_frame, mapping=mapping.get("site_identity")),
        observed_outputs=ingest_g2f_observed_outputs(
            obs_frame, mapping=mapping.get("observed_outputs")
        ),
    )
    if weather_path is not None:
        weather_frame = load_tabular(weather_path)
        bundle.weather_daily = ingest_g2f_weather(weather_frame, mapping=mapping.get("weather_daily"))
    if management_path is not None:
        management_frame = load_tabular(management_path)
        bundle.management_events = ingest_g2f_management_events(
            management_frame, mapping=mapping.get("management_events")
        )
    bundle.validate()
    return bundle


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Normalize G2F tables into APGym contract tables.")
    parser.add_argument("--site", required=True, help="Site/metadata table path")
    parser.add_argument("--observed", required=True, help="Observed outcomes table path")
    parser.add_argument("--weather", default=None, help="Optional weather table path")
    parser.add_argument("--management", default=None, help="Optional management table path")
    parser.add_argument("--mapping-json", default=None, help="Optional column mapping JSON file")
    parser.add_argument("--output-dir", required=True, help="Directory to write normalized outputs")
    parser.add_argument("--format", default="parquet", choices=("parquet", "csv"))
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    bundle = build_g2f_bundle(
        site_path=args.site,
        observed_path=args.observed,
        weather_path=args.weather,
        management_path=args.management,
        mapping_json=args.mapping_json,
    )
    outputs = bundle.save(args.output_dir, fmt=args.format)
    print("Wrote normalized tables:")
    for name, path in outputs.items():
        print(f"- {name}: {path}")


if __name__ == "__main__":
    main()
