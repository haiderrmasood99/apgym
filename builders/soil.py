"""Soil profile data structures and validation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import pandas as pd


@dataclass(frozen=True)
class SoilLayer:
    thickness_mm: float
    bulk_density: float
    ll15: float
    dul: float
    sat: float
    ph: float
    oc_pct: float
    no3_kg_ha: float | None = None
    nh4_kg_ha: float | None = None
    sand_pct: float | None = None
    silt_pct: float | None = None
    clay_pct: float | None = None


@dataclass(frozen=True)
class SoilProfile:
    site_id: str
    layers: tuple[SoilLayer, ...]

    def validate(self) -> None:
        if not self.layers:
            raise ValueError("Soil profile must include at least one layer")
        for idx, layer in enumerate(self.layers):
            if layer.thickness_mm <= 0:
                raise ValueError(f"Layer {idx} has non-positive thickness")
            if not (0 <= layer.ll15 <= layer.dul <= layer.sat <= 1.0):
                raise ValueError(
                    f"Layer {idx} must satisfy 0 <= LL15 <= DUL <= SAT <= 1"
                )
            if layer.bulk_density <= 0:
                raise ValueError(f"Layer {idx} has non-positive bulk density")

    def to_frame(self) -> pd.DataFrame:
        self.validate()
        return pd.DataFrame(
            [
                {
                    "Thickness_mm": layer.thickness_mm,
                    "BulkDensity": layer.bulk_density,
                    "LL15": layer.ll15,
                    "DUL": layer.dul,
                    "SAT": layer.sat,
                    "pH": layer.ph,
                    "OC_pct": layer.oc_pct,
                    "NO3_kg_ha": layer.no3_kg_ha,
                    "NH4_kg_ha": layer.nh4_kg_ha,
                    "Sand_pct": layer.sand_pct,
                    "Silt_pct": layer.silt_pct,
                    "Clay_pct": layer.clay_pct,
                }
                for layer in self.layers
            ]
        )


def build_soil_profile(site_id: str, layers: Iterable[SoilLayer]) -> SoilProfile:
    profile = SoilProfile(site_id=site_id, layers=tuple(layers))
    profile.validate()
    return profile
