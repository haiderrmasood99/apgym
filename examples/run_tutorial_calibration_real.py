from __future__ import annotations

import argparse
from pathlib import Path

from apgym.validation import TutorialCalibrationConfig, run_tutorial_calibration


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run APSIM tutorial predicted-vs-observed calibration and write artifacts."
    )
    parser.add_argument(
        "--output-dir",
        default="docs/calibration_runs/tutorial_predicted_observed",
        help="Directory for calibration outputs.",
    )
    parser.add_argument(
        "--work-dir",
        default=".apgym_runtime/tutorial_calibration",
        help="Working directory for staged APSIM run files.",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    config = TutorialCalibrationConfig(
        output_dir=Path(args.output_dir).expanduser().resolve(),
        work_dir=Path(args.work_dir).expanduser().resolve(),
    )
    result = run_tutorial_calibration(config)
    print("Calibration complete")
    print(f"Passes thresholds: {result['passes_thresholds']}")
    for name, path in result["outputs"].items():
        print(f"- {name}: {path}")


if __name__ == "__main__":
    main()

