from __future__ import annotations

from datetime import date
import json
from pathlib import Path
import tempfile
from unittest import TestCase
from unittest.mock import patch

import pandas as pd

from apgym.data.ingestion.bundle import DataBundle
from apgym.data.ingestion.contracts import validate_dataframe_contract
from apgym.data.ingestion.g2f import (
    ingest_g2f_observed_outputs,
    ingest_g2f_site_identity,
    ingest_g2f_weather,
)
from apgym.data.ingestion.nasa_power import fetch_nasa_power_daily
from apgym.data.ingestion.pipeline import assemble_bundle_with_manifest
from apgym.data.ingestion.ssurgo import ingest_ssurgo_chorizon


class TestDataIngestion(TestCase):
    def test_g2f_normalization_contracts(self) -> None:
        site_raw = pd.DataFrame(
            {
                "location": ["A", "B"],
                "lat": [40.0, 41.0],
                "lon": [-88.0, -89.0],
                "year": [2020, 2020],
                "state": ["IL", "IL"],
                "hybrid": ["H1", "H2"],
            }
        )
        obs_raw = pd.DataFrame(
            {
                "location": ["A", "B"],
                "year": [2020, 2020],
                "yield_bu_ac": [200.0, 180.0],
            }
        )
        weather_raw = pd.DataFrame(
            {
                "location": ["A", "A"],
                "date": ["2020-06-01", "2020-06-02"],
                "tmin": [18.0, 17.0],
                "tmax": [29.0, 30.0],
                "rain": [0.0, 2.1],
                "radn": [20.5, 21.1],
            }
        )

        site = ingest_g2f_site_identity(site_raw)
        observed = ingest_g2f_observed_outputs(obs_raw)
        weather = ingest_g2f_weather(weather_raw)

        validate_dataframe_contract(site, "site_identity")
        validate_dataframe_contract(observed, "observed_outputs")
        validate_dataframe_contract(weather, "weather_daily")

        self.assertGreater(observed["yield_t_ha"].iloc[0], 0.0)

    def test_ssurgo_normalization_contract(self) -> None:
        raw = pd.DataFrame(
            {
                "mukey": ["100", "100"],
                "hzdept_r": [0, 15],
                "hzdepb_r": [15, 45],
                "dbthirdbar_r": [1.25, 1.35],
                "wfifteenbar_r": [12, 18],
                "wthirdbar_r": [24, 30],
                "wsatiated_r": [42, 45],
                "ph1to1h2o_r": [6.8, 6.5],
                "om_r": [2.5, 1.8],
                "sandtotal_r": [30, 28],
                "silttotal_r": [40, 38],
                "claytotal_r": [30, 34],
            }
        )
        soil = ingest_ssurgo_chorizon(raw)
        validate_dataframe_contract(soil, "soil_profile")
        self.assertTrue((soil["ll15"] <= soil["dul"]).all())
        self.assertTrue((soil["dul"] <= soil["sat"]).all())

    def test_data_bundle_validation(self) -> None:
        site = pd.DataFrame(
            {
                "site_id": ["A"],
                "latitude": [40.0],
                "longitude": [-88.0],
                "elevation_m": [250.0],
                "region": ["IL"],
                "crop": ["maize"],
                "season_year": [2020],
            }
        )
        observed = pd.DataFrame({"site_id": ["A"], "season_year": [2020], "yield_t_ha": [10.0]})
        bundle = DataBundle(site_identity=site, observed_outputs=observed)
        bundle.validate()

    def test_pipeline_writes_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            site_path = root / "site.csv"
            observed_path = root / "observed.csv"
            out_dir = root / "out"

            pd.DataFrame(
                {
                    "location": ["A"],
                    "lat": [40.0],
                    "lon": [-88.0],
                    "year": [2020],
                    "state": ["IL"],
                }
            ).to_csv(site_path, index=False)
            pd.DataFrame(
                {
                    "location": ["A"],
                    "year": [2020],
                    "yield_bu_ac": [200.0],
                }
            ).to_csv(observed_path, index=False)

            bundle, manifest_path = assemble_bundle_with_manifest(
                output_dir=out_dir,
                site_path=site_path,
                observed_path=observed_path,
                output_format="csv",
            )
            self.assertTrue(manifest_path.exists())
            with manifest_path.open("r", encoding="utf-8") as handle:
                manifest = json.load(handle)
            self.assertIn("inputs", manifest)
            self.assertIn("outputs", manifest)
            self.assertGreater(len(manifest["outputs"]), 0)
            self.assertGreater(bundle.summary()["site_identity_rows"], 0)

    @patch("apgym.data.ingestion.public_sources.requests.get")
    def test_pipeline_accepts_url_inputs(self, mock_get) -> None:
        class _Resp:
            def __init__(self, body: bytes):
                self._body = body

            def raise_for_status(self) -> None:
                return None

            def iter_content(self, chunk_size: int = 1024):
                del chunk_size
                yield self._body

        site_csv = b"location,lat,lon,year,state\nA,40,-88,2020,IL\n"
        obs_csv = b"location,year,yield_bu_ac\nA,2020,200\n"

        def _get(url: str, *args, **kwargs):
            del args, kwargs
            if "site" in url:
                return _Resp(site_csv)
            if "observed" in url:
                return _Resp(obs_csv)
            raise AssertionError(f"Unexpected URL: {url}")

        mock_get.side_effect = _get

        with tempfile.TemporaryDirectory() as tmp:
            out_dir = Path(tmp) / "out"
            bundle, manifest_path = assemble_bundle_with_manifest(
                output_dir=out_dir,
                site_url="https://example.com/site.csv",
                observed_url="https://example.com/observed.csv",
                output_format="csv",
            )
            self.assertTrue(manifest_path.exists())
            self.assertGreater(bundle.summary()["site_identity_rows"], 0)

    @patch("apgym.data.ingestion.nasa_power.requests.get")
    def test_nasa_power_fetch(self, mock_get) -> None:
        class _Resp:
            def raise_for_status(self) -> None:
                return None

            def json(self) -> dict:
                return {
                    "properties": {
                        "parameter": {
                            "T2M_MIN": {"20200101": 10.0, "20200102": 11.0},
                            "T2M_MAX": {"20200101": 20.0, "20200102": 21.0},
                            "PRECTOTCORR": {"20200101": 1.2, "20200102": 0.0},
                            "ALLSKY_SFC_SW_DWN": {"20200101": 15.0, "20200102": 16.0},
                            "WS2M": {"20200101": 3.0, "20200102": 3.2},
                            "RH2M": {"20200101": 55.0, "20200102": 50.0},
                        }
                    }
                }

        mock_get.return_value = _Resp()

        weather = fetch_nasa_power_daily(
            site_id="A",
            latitude=40.0,
            longitude=-88.0,
            start_date=date(2020, 1, 1),
            end_date=date(2020, 1, 2),
        )
        validate_dataframe_contract(weather, "weather_daily")
        self.assertEqual(len(weather), 2)
