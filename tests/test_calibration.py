from __future__ import annotations

import json
from pathlib import Path
import tempfile
from unittest import TestCase

import pandas as pd

from apgym.validation.calibration import (
    CalibrationThresholds,
    evaluate_calibration,
    run_calibration_from_files,
)


class TestCalibration(TestCase):
    def test_evaluate_calibration_pass_fail(self) -> None:
        predicted = pd.DataFrame(
            {
                "site_id": ["A", "A", "B", "B"],
                "season_year": [2020, 2021, 2020, 2021],
                "yield_t_ha": [10.0, 10.2, 8.0, 8.5],
            }
        )
        observed = pd.DataFrame(
            {
                "site_id": ["A", "A", "B", "B"],
                "season_year": [2020, 2021, 2020, 2021],
                "yield_t_ha": [10.1, 10.1, 7.9, 8.4],
            }
        )
        strict = CalibrationThresholds(rmse_max=0.05)
        result_strict = evaluate_calibration(
            predicted,
            observed,
            thresholds=strict,
            group_cols=("site_id",),
        )
        self.assertFalse(result_strict["passes_thresholds"])

        loose = CalibrationThresholds(rmse_max=0.5, mae_max=0.5, mean_bias_abs_max=0.5)
        result_loose = evaluate_calibration(
            predicted,
            observed,
            thresholds=loose,
            group_cols=("site_id",),
        )
        self.assertTrue(result_loose["passes_thresholds"])
        self.assertIn("by_group", result_loose)
        self.assertGreater(len(result_loose["by_group"]), 0)

    def test_run_calibration_from_files_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            predicted_path = root / "pred.csv"
            observed_path = root / "obs.csv"
            out_dir = root / "out"

            pd.DataFrame(
                {
                    "site_id": ["A", "B"],
                    "season_year": [2020, 2020],
                    "yield_t_ha": [10.0, 8.0],
                }
            ).to_csv(predicted_path, index=False)
            pd.DataFrame(
                {
                    "site_id": ["A", "B"],
                    "season_year": [2020, 2020],
                    "yield_t_ha": [9.8, 8.1],
                }
            ).to_csv(observed_path, index=False)

            result = run_calibration_from_files(
                predicted_path=predicted_path,
                observed_path=observed_path,
                output_dir=out_dir,
                thresholds=CalibrationThresholds(rmse_max=1.0),
                report_prefix="calib_test",
            )
            self.assertIn("outputs", result)
            outputs = result["outputs"]
            self.assertTrue(Path(outputs["json"]).exists())
            self.assertTrue(Path(outputs["markdown"]).exists())
            self.assertTrue(Path(outputs["aligned_csv"]).exists())

            with Path(outputs["json"]).open("r", encoding="utf-8") as handle:
                payload = json.load(handle)
            self.assertIn("global_metrics", payload)
