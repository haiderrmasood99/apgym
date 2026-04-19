"""NASA POWER daily weather fetch helpers."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
from typing import Iterable

import pandas as pd
import requests

from apgym.data.ingestion.utils import load_tabular

NASA_POWER_DAILY_URL = "https://power.larc.nasa.gov/api/temporal/daily/point"


def _yyyymmdd(d: date) -> str:
    return d.strftime("%Y%m%d")


def fetch_nasa_power_daily(
    *,
    site_id: str,
    latitude: float,
    longitude: float,
    start_date: date,
    end_date: date,
    timeout_sec: int = 60,
) -> pd.DataFrame:
    params = {
        "parameters": "T2M_MIN,T2M_MAX,PRECTOTCORR,ALLSKY_SFC_SW_DWN,WS2M,RH2M",
        "community": "AG",
        "format": "JSON",
        "latitude": latitude,
        "longitude": longitude,
        "start": _yyyymmdd(start_date),
        "end": _yyyymmdd(end_date),
    }
    response = requests.get(NASA_POWER_DAILY_URL, params=params, timeout=timeout_sec)
    response.raise_for_status()
    payload = response.json()
    params_payload = payload["properties"]["parameter"]

    tmin = params_payload["T2M_MIN"]
    tmax = params_payload["T2M_MAX"]
    rain = params_payload["PRECTOTCORR"]
    rad = params_payload["ALLSKY_SFC_SW_DWN"]
    wind = params_payload.get("WS2M", {})
    rh = params_payload.get("RH2M", {})

    dates = sorted(tmin.keys())
    date_values = pd.to_datetime(dates, format="%Y%m%d").strftime("%Y-%m-%d")
    frame = pd.DataFrame(
        {
            "site_id": site_id,
            "date": pd.Series(date_values, dtype="string"),
            "tmin_c": [tmin[d] for d in dates],
            "tmax_c": [tmax[d] for d in dates],
            "rain_mm": [rain[d] for d in dates],
            "rad_mj_m2": [rad[d] for d in dates],
            "wind_m_s": [wind.get(d) for d in dates],
            "vp_kpa": [rh.get(d) for d in dates],  # placeholder: RH2M mapped until VP source added
        }
    )
    # NASA POWER can return fill values like -999.
    numeric_cols = ("tmin_c", "tmax_c", "rain_mm", "rad_mj_m2", "wind_m_s", "vp_kpa")
    for col in numeric_cols:
        frame[col] = pd.to_numeric(frame[col], errors="coerce")
        frame.loc[frame[col] < -900, col] = pd.NA
    return frame.dropna(subset=["tmin_c", "tmax_c", "rain_mm", "rad_mj_m2"]).reset_index(drop=True)


def fetch_weather_for_sites(
    sites: pd.DataFrame,
    *,
    start_date: date,
    end_date: date,
    site_id_col: str = "site_id",
    lat_col: str = "latitude",
    lon_col: str = "longitude",
) -> pd.DataFrame:
    rows: list[pd.DataFrame] = []
    for _, row in sites.iterrows():
        site_weather = fetch_nasa_power_daily(
            site_id=str(row[site_id_col]),
            latitude=float(row[lat_col]),
            longitude=float(row[lon_col]),
            start_date=start_date,
            end_date=end_date,
        )
        rows.append(site_weather)
    if not rows:
        return pd.DataFrame(
            columns=["site_id", "date", "tmin_c", "tmax_c", "rain_mm", "rad_mj_m2", "wind_m_s", "vp_kpa"]
        )
    return pd.concat(rows, ignore_index=True)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch NASA POWER daily weather for APGym sites.")
    parser.add_argument("--sites", required=True, help="CSV/Parquet with site_id, latitude, longitude")
    parser.add_argument("--start", required=True, help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end", required=True, help="End date (YYYY-MM-DD)")
    parser.add_argument("--output", required=True, help="Output weather file path (.parquet/.csv)")
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    sites = load_tabular(args.sites)
    start = pd.to_datetime(args.start).date()
    end = pd.to_datetime(args.end).date()
    weather = fetch_weather_for_sites(sites, start_date=start, end_date=end)

    output = Path(args.output).expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.suffix.lower() == ".parquet":
        weather.to_parquet(output, index=False)
    else:
        weather.to_csv(output, index=False)
    print(f"Wrote weather table: {output}")


if __name__ == "__main__":
    main()
