from __future__ import annotations

from unittest import TestCase

import pandas as pd

from apgym.data.ingestion.nass import normalize_nass_quickstats_yield


class TestNassExtractor(TestCase):
    def test_normalize_nass_quickstats_yield(self) -> None:
        raw = pd.DataFrame(
            {
                "commodity_desc": ["CORN", "CORN", "SOYBEANS"],
                "statisticcat_desc": ["YIELD", "YIELD", "YIELD"],
                "unit_desc": ["BU / ACRE", "BU / ACRE", "BU / ACRE"],
                "year": ["2020", "2020", "2020"],
                "Value": ["200.5", "(D)", "55.0"],
                "state_fips_code": ["17", "17", "17"],
                "county_code": ["019", "019", "019"],
                "state_name": ["Illinois", "Illinois", "Illinois"],
                "county_name": ["Champaign", "Champaign", "Champaign"],
            }
        )
        out = normalize_nass_quickstats_yield(raw)
        self.assertEqual(len(out), 1)
        self.assertEqual(out.loc[0, "site_id"], "US-17019")
        self.assertEqual(int(out.loc[0, "season_year"]), 2020)
        self.assertAlmostEqual(float(out.loc[0, "yield_t_ha"]), 200.5 * 0.06277, places=6)

    def test_name_fallback_site_id(self) -> None:
        raw = pd.DataFrame(
            {
                "commodity_desc": ["CORN"],
                "statisticcat_desc": ["YIELD"],
                "unit_desc": ["BU / ACRE"],
                "year": ["2021"],
                "Value": ["150"],
                "state_name": ["Iowa"],
                "county_name": ["Story"],
            }
        )
        out = normalize_nass_quickstats_yield(raw)
        self.assertEqual(out.loc[0, "site_id"], "US-IOWA-STORY")

