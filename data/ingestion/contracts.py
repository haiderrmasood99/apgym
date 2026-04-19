"""Contract and schema validation helpers for normalized APGym tables."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Final

import pandas as pd

SCHEMA_DIR: Final[Path] = Path(__file__).resolve().parents[1] / "schemas"

SCHEMA_NAMES: Final[tuple[str, ...]] = (
    "site_identity",
    "weather_daily",
    "soil_profile",
    "management_events",
    "observed_outputs",
    "simulation_outputs",
)

SCHEMA_FILE_MAP: Final[dict[str, str]] = {
    "site_identity": "site_identity.schema.json",
    "weather_daily": "weather_daily.schema.json",
    "soil_profile": "soil_profile.schema.json",
    "management_events": "management_events.schema.json",
    "observed_outputs": "observed_outputs.schema.json",
    "simulation_outputs": "simulation_outputs.schema.json",
}


def _schema_path(schema_name: str) -> Path:
    if schema_name not in SCHEMA_FILE_MAP:
        raise KeyError(
            f"Unknown schema {schema_name!r}. Expected one of: {sorted(SCHEMA_FILE_MAP)}"
        )
    return SCHEMA_DIR / SCHEMA_FILE_MAP[schema_name]


def load_schema(schema_name: str) -> dict:
    path = _schema_path(schema_name)
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def get_required_columns(schema_name: str) -> list[str]:
    schema = load_schema(schema_name)
    required = schema.get("required", [])
    return list(required)


def validate_required_columns(frame: pd.DataFrame, schema_name: str) -> None:
    required = get_required_columns(schema_name)
    missing = sorted(set(required) - set(frame.columns))
    if missing:
        raise ValueError(f"{schema_name} missing required columns: {missing}")


def _validate_weather_ranges(frame: pd.DataFrame) -> None:
    if frame.empty:
        return
    if (frame["rain_mm"] < 0).any():
        raise ValueError("weather_daily contains negative rain_mm values")
    if (frame["rad_mj_m2"] < 0).any():
        raise ValueError("weather_daily contains negative rad_mj_m2 values")
    bad_temp = frame["tmin_c"] > frame["tmax_c"]
    if bad_temp.any():
        raise ValueError("weather_daily contains rows where tmin_c > tmax_c")


def _validate_soil_ranges(frame: pd.DataFrame) -> None:
    if frame.empty:
        return
    for col in ("ll15", "dul", "sat"):
        if ((frame[col] < 0) | (frame[col] > 1)).any():
            raise ValueError(f"soil_profile column {col!r} must lie within [0, 1]")
    if (frame["ll15"] > frame["dul"]).any() or (frame["dul"] > frame["sat"]).any():
        raise ValueError("soil_profile must satisfy ll15 <= dul <= sat")


def validate_dataframe_contract(frame: pd.DataFrame, schema_name: str) -> None:
    validate_required_columns(frame, schema_name)

    if schema_name == "weather_daily":
        _validate_weather_ranges(frame)
    elif schema_name == "soil_profile":
        _validate_soil_ranges(frame)
