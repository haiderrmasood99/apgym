from __future__ import annotations

from pathlib import Path
import tempfile

import pandas as pd

from apgym.validation import CalibrationThresholds, run_calibration_from_files


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        predicted_path = root / "predicted.csv"
        observed_path = root / "observed.csv"
        out_dir = root / "reports"

        predicted = pd.DataFrame(
            {
                "site_id": ["A", "A", "B", "B"],
                "season_year": [2020, 2021, 2020, 2021],
                "yield_t_ha": [10.2, 9.7, 8.1, 8.8],
            }
        )
        observed = pd.DataFrame(
            {
                "site_id": ["A", "A", "B", "B"],
                "season_year": [2020, 2021, 2020, 2021],
                "yield_t_ha": [10.0, 9.9, 8.0, 8.5],
            }
        )
        predicted.to_csv(predicted_path, index=False)
        observed.to_csv(observed_path, index=False)

        result = run_calibration_from_files(
            predicted_path=predicted_path,
            observed_path=observed_path,
            output_dir=out_dir,
            thresholds=CalibrationThresholds(
                rmse_max=0.5,
                mae_max=0.4,
                mean_bias_abs_max=0.3,
                r2_min=0.9,
                nse_min=0.8,
                slope_min=0.8,
                slope_max=1.2,
                intercept_abs_max=1.0,
            ),
            report_prefix="demo_calibration",
        )
        print("Calibration pass:", result["passes_thresholds"])
        for name, path in result["outputs"].items():
            print(f"- {name}: {path}")


if __name__ == "__main__":
    main()
