"""Reproducible calibration runs against APSIM-provided observed datasets."""

from __future__ import annotations

from dataclasses import dataclass, field
import json
from pathlib import Path
import shutil
import sqlite3
import subprocess
from typing import Any

import pandas as pd

from apgym.simulator.apsim_locator import find_models_exe
from apgym.validation.calibration import (
    CalibrationThresholds,
    run_calibration_from_files,
)


@dataclass(frozen=True)
class TutorialCalibrationConfig:
    """Configuration for the APSIM tutorial predicted-vs-observed benchmark run."""

    output_dir: Path
    work_dir: Path
    report_prefix: str = "tutorial_lai"
    thresholds: CalibrationThresholds = field(
        default_factory=lambda: CalibrationThresholds(
            rmse_max=1.0,
            mae_max=0.6,
            mean_bias_abs_max=0.6,
            r2_min=0.7,
            nse_min=0.7,
            slope_min=0.8,
            slope_max=1.3,
            intercept_abs_max=0.2,
        )
    )


def _prepare_tutorial_workspace(*, models_exe: Path, work_dir: Path) -> dict[str, Path]:
    apsim_root = models_exe.parent.parent
    source_apsimx = apsim_root / "Examples" / "Tutorials" / "PredictedObserved.apsimx"
    source_observed = apsim_root / "Examples" / "Tutorials" / "Observed.xlsx"

    if not source_apsimx.exists():
        raise FileNotFoundError(f"Tutorial APSIM file not found: {source_apsimx}")
    if not source_observed.exists():
        raise FileNotFoundError(f"Tutorial observed workbook not found: {source_observed}")

    work_dir.mkdir(parents=True, exist_ok=True)
    staged_apsimx = work_dir / "PredictedObserved.apsimx"
    staged_observed = work_dir / "Observed.xlsx"
    shutil.copy2(source_apsimx, staged_apsimx)
    shutil.copy2(source_observed, staged_observed)
    return {
        "source_apsimx": source_apsimx,
        "source_observed": source_observed,
        "staged_apsimx": staged_apsimx,
        "staged_observed": staged_observed,
    }


def _run_apsim(models_exe: Path, apsimx_path: Path, *, cwd: Path) -> None:
    process = subprocess.run(
        [str(models_exe), str(apsimx_path)],
        cwd=cwd,
        capture_output=True,
        text=True,
        timeout=300,
    )
    if process.returncode != 0:
        raise RuntimeError(
            "APSIM tutorial benchmark run failed.\n"
            f"STDOUT:\n{process.stdout}\n\nSTDERR:\n{process.stderr}"
        )


def _extract_predicted_observed(db_path: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    if not db_path.exists():
        raise FileNotFoundError(f"DataStore not produced: {db_path}")

    con = sqlite3.connect(db_path)
    try:
        frame = pd.read_sql_query('SELECT * FROM "PredictedObserved"', con)
    finally:
        con.close()

    required = {"SimulationID", "Clock.Today", "Observed.Barley.Leaf.LAI", "Predicted.Barley.Leaf.LAI"}
    missing = sorted(required - set(frame.columns))
    if missing:
        raise ValueError(f"PredictedObserved table missing expected columns: {missing}")

    frame["date"] = pd.to_datetime(frame["Clock.Today"], errors="coerce")
    frame = frame.dropna(subset=["date"]).copy()
    frame["date"] = frame["date"].dt.strftime("%Y-%m-%d")
    frame["site_id"] = frame["SimulationID"].astype(str)
    frame["season_year"] = pd.to_datetime(frame["date"]).dt.year.astype(int)

    predicted = frame[
        ["site_id", "season_year", "date", "Predicted.Barley.Leaf.LAI"]
    ].rename(columns={"Predicted.Barley.Leaf.LAI": "lai"})
    observed = frame[
        ["site_id", "season_year", "date", "Observed.Barley.Leaf.LAI"]
    ].rename(columns={"Observed.Barley.Leaf.LAI": "lai"})
    return predicted.reset_index(drop=True), observed.reset_index(drop=True)


def run_tutorial_calibration(config: TutorialCalibrationConfig) -> dict[str, Any]:
    """Run APSIM tutorial benchmark and export calibration artifacts."""

    models_exe = find_models_exe()
    output_dir = config.output_dir.expanduser().resolve()
    work_dir = config.work_dir.expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    workspace = _prepare_tutorial_workspace(models_exe=models_exe, work_dir=work_dir)
    staged_apsimx = workspace["staged_apsimx"]

    _run_apsim(models_exe=models_exe, apsimx_path=staged_apsimx, cwd=work_dir)
    db_path = staged_apsimx.with_suffix(".db")

    predicted, observed = _extract_predicted_observed(db_path)
    predicted_path = output_dir / "predicted_lai.csv"
    observed_path = output_dir / "observed_lai.csv"
    predicted.to_csv(predicted_path, index=False)
    observed.to_csv(observed_path, index=False)

    result = run_calibration_from_files(
        predicted_path=predicted_path,
        observed_path=observed_path,
        output_dir=output_dir,
        keys=("site_id", "season_year", "date"),
        predicted_col="lai",
        observed_col="lai",
        group_cols=("site_id",),
        thresholds=config.thresholds,
        report_prefix=config.report_prefix,
    )

    metadata = {
        "models_exe": str(models_exe),
        "tutorial_apsimx_source": str(workspace["source_apsimx"]),
        "tutorial_observed_source": str(workspace["source_observed"]),
        "staged_apsimx": str(staged_apsimx),
        "datastore": str(db_path),
        "predicted_path": str(predicted_path),
        "observed_path": str(observed_path),
        "thresholds": config.thresholds.__dict__,
        "passes_thresholds": bool(result["passes_thresholds"]),
    }
    metadata_path = output_dir / "run_metadata.json"
    with metadata_path.open("w", encoding="utf-8") as handle:
        json.dump(metadata, handle, indent=2)
        handle.write("\n")
    result["outputs"]["run_metadata_json"] = str(metadata_path)
    return result

