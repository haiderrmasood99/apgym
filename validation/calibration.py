"""Calibration tooling for predicted-vs-observed validation gates."""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any, Sequence

import numpy as np
import pandas as pd

from apgym.data.ingestion.utils import load_tabular
from apgym.validation.metrics import compute_fit_metrics
from apgym.validation.predicted_observed import align_predicted_observed


@dataclass(frozen=True)
class CalibrationThresholds:
    rmse_max: float | None = None
    mae_max: float | None = None
    mean_bias_abs_max: float | None = None
    r2_min: float | None = None
    nse_min: float | None = None
    slope_min: float | None = None
    slope_max: float | None = None
    intercept_abs_max: float | None = None


def _is_nan(value: Any) -> bool:
    try:
        return bool(np.isnan(float(value)))
    except (TypeError, ValueError):
        return False


def _check_metric(
    metric_name: str,
    value: float,
    thresholds: CalibrationThresholds,
) -> bool | None:
    if _is_nan(value):
        return None

    if metric_name == "rmse" and thresholds.rmse_max is not None:
        return value <= thresholds.rmse_max
    if metric_name == "mae" and thresholds.mae_max is not None:
        return value <= thresholds.mae_max
    if metric_name == "mean_bias" and thresholds.mean_bias_abs_max is not None:
        return abs(value) <= thresholds.mean_bias_abs_max
    if metric_name == "r2" and thresholds.r2_min is not None:
        return value >= thresholds.r2_min
    if metric_name == "nse" and thresholds.nse_min is not None:
        return value >= thresholds.nse_min
    if metric_name == "slope":
        if thresholds.slope_min is not None and value < thresholds.slope_min:
            return False
        if thresholds.slope_max is not None and value > thresholds.slope_max:
            return False
        if thresholds.slope_min is not None or thresholds.slope_max is not None:
            return True
    if metric_name == "intercept" and thresholds.intercept_abs_max is not None:
        return abs(value) <= thresholds.intercept_abs_max
    return None


def metric_checks(metrics: dict[str, float], thresholds: CalibrationThresholds) -> dict[str, bool | None]:
    checks: dict[str, bool | None] = {}
    for name, value in metrics.items():
        checks[name] = _check_metric(name, value, thresholds)
    return checks


def passes_thresholds(checks: dict[str, bool | None]) -> bool:
    specified = [v for v in checks.values() if v is not None]
    if not specified:
        return True
    return all(specified)


def _group_metrics(
    aligned: pd.DataFrame,
    group_cols: Sequence[str],
    thresholds: CalibrationThresholds,
) -> pd.DataFrame:
    if not group_cols:
        return pd.DataFrame()

    rows: list[dict[str, Any]] = []
    grouped = aligned.groupby(list(group_cols), dropna=False)
    for group_key, group_df in grouped:
        if not isinstance(group_key, tuple):
            group_key = (group_key,)
        y_true = group_df["observed"].to_numpy(dtype=float)
        y_pred = group_df["predicted"].to_numpy(dtype=float)
        metrics = compute_fit_metrics(y_true, y_pred)
        checks = metric_checks(metrics, thresholds)
        row: dict[str, Any] = {
            col: val for col, val in zip(group_cols, group_key)
        }
        row["n"] = int(len(group_df))
        row.update(metrics)
        row["passes_thresholds"] = passes_thresholds(checks)
        for name, passed in checks.items():
            row[f"check_{name}"] = passed
        rows.append(row)
    return pd.DataFrame(rows)


def evaluate_calibration(
    predicted: pd.DataFrame,
    observed: pd.DataFrame,
    *,
    keys: Sequence[str] = ("site_id", "season_year"),
    predicted_col: str = "yield_t_ha",
    observed_col: str = "yield_t_ha",
    group_cols: Sequence[str] = ("site_id",),
    thresholds: CalibrationThresholds | None = None,
) -> dict[str, Any]:
    thresholds = thresholds or CalibrationThresholds()
    aligned = align_predicted_observed(
        predicted=predicted,
        observed=observed,
        keys=keys,
        predicted_col=predicted_col,
        observed_col=observed_col,
    )
    if aligned.empty:
        raise ValueError("No overlapping rows between predicted and observed tables after key join.")

    y_true = aligned["observed"].to_numpy(dtype=float)
    y_pred = aligned["predicted"].to_numpy(dtype=float)
    global_metrics = compute_fit_metrics(y_true, y_pred)
    global_checks = metric_checks(global_metrics, thresholds)
    by_group = _group_metrics(aligned, group_cols=group_cols, thresholds=thresholds)

    return {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "keys": list(keys),
        "predicted_col": predicted_col,
        "observed_col": observed_col,
        "n_points": int(len(aligned)),
        "thresholds": asdict(thresholds),
        "global_metrics": global_metrics,
        "global_checks": global_checks,
        "passes_thresholds": passes_thresholds(global_checks),
        "aligned": aligned,
        "by_group": by_group,
    }


def _markdown_report(result: dict[str, Any]) -> str:
    global_metrics: dict[str, float] = result["global_metrics"]
    global_checks: dict[str, bool | None] = result["global_checks"]
    thresholds: dict[str, Any] = result["thresholds"]
    by_group: pd.DataFrame = result["by_group"]

    lines = [
        "# APGym Calibration Report",
        "",
        f"- Created: {result['created_at_utc']}",
        f"- Keys: {', '.join(result['keys'])}",
        f"- Predicted column: `{result['predicted_col']}`",
        f"- Observed column: `{result['observed_col']}`",
        f"- Matched points: {result['n_points']}",
        f"- Passes thresholds: **{result['passes_thresholds']}**",
        "",
        "## Thresholds",
        "",
        "```json",
        json.dumps(thresholds, indent=2),
        "```",
        "",
        "## Global Metrics",
        "",
        "| metric | value | pass |",
        "|---|---:|:---:|",
    ]
    for metric_name, value in global_metrics.items():
        pass_value = global_checks.get(metric_name)
        pass_str = "" if pass_value is None else ("yes" if pass_value else "no")
        lines.append(f"| {metric_name} | {value:.6g} | {pass_str} |")

    if not by_group.empty:
        lines.extend(
            [
                "",
                "## Group Metrics",
                "",
                by_group.to_markdown(index=False),
            ]
        )
    return "\n".join(lines) + "\n"


def write_calibration_report(
    result: dict[str, Any],
    *,
    output_dir: str | Path,
    report_prefix: str = "calibration",
) -> dict[str, Path]:
    root = Path(output_dir).expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)

    aligned: pd.DataFrame = result["aligned"]
    by_group: pd.DataFrame = result["by_group"]

    json_out = {
        key: value
        for key, value in result.items()
        if key not in {"aligned", "by_group"}
    }
    json_path = root / f"{report_prefix}.json"
    with json_path.open("w", encoding="utf-8") as handle:
        json.dump(json_out, handle, indent=2)
        handle.write("\n")

    markdown_path = root / f"{report_prefix}.md"
    markdown_path.write_text(_markdown_report(result), encoding="utf-8")

    aligned_path = root / f"{report_prefix}_aligned.csv"
    aligned.to_csv(aligned_path, index=False)

    paths: dict[str, Path] = {
        "json": json_path,
        "markdown": markdown_path,
        "aligned_csv": aligned_path,
    }
    if not by_group.empty:
        by_group_path = root / f"{report_prefix}_by_group.csv"
        by_group.to_csv(by_group_path, index=False)
        paths["by_group_csv"] = by_group_path
    return paths


def run_calibration_from_files(
    *,
    predicted_path: str | Path,
    observed_path: str | Path,
    output_dir: str | Path,
    keys: Sequence[str] = ("site_id", "season_year"),
    predicted_col: str = "yield_t_ha",
    observed_col: str = "yield_t_ha",
    group_cols: Sequence[str] = ("site_id",),
    thresholds: CalibrationThresholds | None = None,
    report_prefix: str = "calibration",
) -> dict[str, Any]:
    predicted = load_tabular(predicted_path)
    observed = load_tabular(observed_path)
    result = evaluate_calibration(
        predicted=predicted,
        observed=observed,
        keys=keys,
        predicted_col=predicted_col,
        observed_col=observed_col,
        group_cols=group_cols,
        thresholds=thresholds,
    )
    outputs = write_calibration_report(
        result,
        output_dir=output_dir,
        report_prefix=report_prefix,
    )
    result["outputs"] = {k: str(v) for k, v in outputs.items()}
    return result


def _parse_csv_list(value: str | None) -> list[str]:
    if value is None:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run APGym predicted-vs-observed calibration and export reports."
    )
    parser.add_argument("--predicted", required=True, help="Predicted table path (.csv/.parquet)")
    parser.add_argument("--observed", required=True, help="Observed table path (.csv/.parquet)")
    parser.add_argument("--output-dir", required=True, help="Directory for calibration outputs")
    parser.add_argument("--keys", default="site_id,season_year")
    parser.add_argument("--predicted-col", default="yield_t_ha")
    parser.add_argument("--observed-col", default="yield_t_ha")
    parser.add_argument("--group-cols", default="site_id")
    parser.add_argument("--report-prefix", default="calibration")
    parser.add_argument("--rmse-max", type=float, default=None)
    parser.add_argument("--mae-max", type=float, default=None)
    parser.add_argument("--mean-bias-abs-max", type=float, default=None)
    parser.add_argument("--r2-min", type=float, default=None)
    parser.add_argument("--nse-min", type=float, default=None)
    parser.add_argument("--slope-min", type=float, default=None)
    parser.add_argument("--slope-max", type=float, default=None)
    parser.add_argument("--intercept-abs-max", type=float, default=None)
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    thresholds = CalibrationThresholds(
        rmse_max=args.rmse_max,
        mae_max=args.mae_max,
        mean_bias_abs_max=args.mean_bias_abs_max,
        r2_min=args.r2_min,
        nse_min=args.nse_min,
        slope_min=args.slope_min,
        slope_max=args.slope_max,
        intercept_abs_max=args.intercept_abs_max,
    )
    result = run_calibration_from_files(
        predicted_path=args.predicted,
        observed_path=args.observed,
        output_dir=args.output_dir,
        keys=_parse_csv_list(args.keys),
        predicted_col=args.predicted_col,
        observed_col=args.observed_col,
        group_cols=_parse_csv_list(args.group_cols),
        thresholds=thresholds,
        report_prefix=args.report_prefix,
    )
    print("Calibration complete")
    print(f"Passes thresholds: {result['passes_thresholds']}")
    for name, path in result["outputs"].items():
        print(f"- {name}: {path}")


if __name__ == "__main__":
    main()
