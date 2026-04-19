"""Normalized APGym data bundle container."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from apgym.data.ingestion.contracts import validate_dataframe_contract


@dataclass
class DataBundle:
    site_identity: pd.DataFrame | None = None
    weather_daily: pd.DataFrame | None = None
    soil_profile: pd.DataFrame | None = None
    management_events: pd.DataFrame | None = None
    observed_outputs: pd.DataFrame | None = None

    def validate(self) -> None:
        table_map: dict[str, pd.DataFrame | None] = {
            "site_identity": self.site_identity,
            "weather_daily": self.weather_daily,
            "soil_profile": self.soil_profile,
            "management_events": self.management_events,
            "observed_outputs": self.observed_outputs,
        }
        for schema_name, frame in table_map.items():
            if frame is None:
                continue
            validate_dataframe_contract(frame, schema_name=schema_name)

    def summary(self) -> dict[str, int]:
        return {
            "site_identity_rows": 0 if self.site_identity is None else int(len(self.site_identity)),
            "weather_daily_rows": 0 if self.weather_daily is None else int(len(self.weather_daily)),
            "soil_profile_rows": 0 if self.soil_profile is None else int(len(self.soil_profile)),
            "management_events_rows": 0
            if self.management_events is None
            else int(len(self.management_events)),
            "observed_outputs_rows": 0
            if self.observed_outputs is None
            else int(len(self.observed_outputs)),
        }

    def save(self, root_dir: str | Path, fmt: str = "parquet") -> dict[str, Path]:
        self.validate()
        root = Path(root_dir).expanduser().resolve()
        root.mkdir(parents=True, exist_ok=True)
        extension = "parquet" if fmt == "parquet" else "csv"
        outputs: dict[str, Path] = {}

        for name, frame in [
            ("site_identity", self.site_identity),
            ("weather_daily", self.weather_daily),
            ("soil_profile", self.soil_profile),
            ("management_events", self.management_events),
            ("observed_outputs", self.observed_outputs),
        ]:
            if frame is None:
                continue
            out_path = root / f"{name}.{extension}"
            if extension == "parquet":
                frame.to_parquet(out_path, index=False)
            else:
                frame.to_csv(out_path, index=False)
            outputs[name] = out_path
        return outputs
