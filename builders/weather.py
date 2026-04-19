"""Weather ingestion helpers for APGym."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable

import pandas as pd


@dataclass(frozen=True)
class DailyWeather:
    date: date
    tmin_c: float
    tmax_c: float
    rain_mm: float
    rad_mj_m2: float
    wind_m_s: float | None = None
    vp_kpa: float | None = None


def weather_to_frame(records: Iterable[DailyWeather]) -> pd.DataFrame:
    rows = [
        {
            "Date": r.date.isoformat(),
            "Tmin": float(r.tmin_c),
            "Tmax": float(r.tmax_c),
            "Rain": float(r.rain_mm),
            "Radn": float(r.rad_mj_m2),
            "Wind": None if r.wind_m_s is None else float(r.wind_m_s),
            "VP": None if r.vp_kpa is None else float(r.vp_kpa),
        }
        for r in records
    ]
    frame = pd.DataFrame(rows)
    required = ("Date", "Tmin", "Tmax", "Rain", "Radn")
    if frame.empty:
        raise ValueError("Weather frame is empty")
    missing = [c for c in required if c not in frame.columns]
    if missing:
        raise ValueError(f"Weather data missing required columns: {missing}")
    if (frame["Tmin"] > frame["Tmax"]).any():
        raise ValueError("Weather records contain Tmin > Tmax")
    return frame


def write_weather_csv(path: str | Path, records: Iterable[DailyWeather]) -> Path:
    target = Path(path).expanduser().resolve()
    target.parent.mkdir(parents=True, exist_ok=True)
    frame = weather_to_frame(records)
    frame.to_csv(target, index=False)
    return target
