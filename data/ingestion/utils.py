"""Shared ingestion utilities."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable

import pandas as pd


def normalize_columns(frame: pd.DataFrame) -> pd.DataFrame:
    copy = frame.copy()
    copy.columns = [str(col).strip() for col in copy.columns]
    return copy


def lower_columns(frame: pd.DataFrame) -> pd.DataFrame:
    copy = normalize_columns(frame)
    copy.columns = [col.lower() for col in copy.columns]
    return copy


def load_tabular(path: str | Path, sep: str | None = None) -> pd.DataFrame:
    source = Path(path).expanduser().resolve()
    if not source.exists():
        raise FileNotFoundError(f"Input table not found: {source}")
    suffix = source.suffix.lower()
    if suffix == ".parquet":
        frame = pd.read_parquet(source)
    elif suffix in {".csv", ".txt"}:
        if sep is None:
            frame = pd.read_csv(source)
        else:
            frame = pd.read_csv(source, sep=sep)
    elif suffix in {".tsv"}:
        frame = pd.read_csv(source, sep="\t")
    elif suffix in {".xlsx", ".xls"}:
        frame = pd.read_excel(source)  # pragma: no cover
    else:
        raise ValueError(f"Unsupported file extension for {source}")
    return normalize_columns(frame)


def save_tabular(frame: pd.DataFrame, path: str | Path) -> Path:
    target = Path(path).expanduser().resolve()
    target.parent.mkdir(parents=True, exist_ok=True)
    suffix = target.suffix.lower()
    if suffix == ".parquet":
        frame.to_parquet(target, index=False)
    elif suffix in {".csv", ".txt"}:
        frame.to_csv(target, index=False)
    elif suffix == ".tsv":
        frame.to_csv(target, sep="\t", index=False)
    else:
        raise ValueError(f"Unsupported output extension for {target}")
    return target


def parse_date_column(series: pd.Series) -> pd.Series:
    parsed = pd.to_datetime(series, errors="coerce")
    return parsed.dt.date.astype("string")


def coalesce_column(frame: pd.DataFrame, candidates: Iterable[str]) -> str | None:
    normalized = {str(col).lower(): str(col) for col in frame.columns}
    for candidate in candidates:
        candidate_norm = candidate.lower()
        if candidate_norm in normalized:
            return normalized[candidate_norm]
    return None


def require_column(frame: pd.DataFrame, candidates: Iterable[str], label: str) -> str:
    col = coalesce_column(frame, candidates)
    if col is None:
        raise KeyError(
            f"Could not resolve {label!r} column. Tried candidates: {list(candidates)}"
        )
    return col


def optional_float(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def load_mapping_json(path: str | Path | None) -> dict[str, Any]:
    if path is None:
        return {}
    source = Path(path).expanduser().resolve()
    with source.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        raise ValueError("Mapping JSON must be an object")
    return payload
