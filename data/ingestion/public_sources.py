"""Public-source connectors and download helpers for APGym datasets."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
from typing import Any
from urllib.parse import urlparse
import zipfile

import pandas as pd
import requests

NASS_QUICKSTATS_URL = "https://quickstats.nass.usda.gov/api/api_GET/"


@dataclass(frozen=True)
class DownloadArtifact:
    source: str
    url: str
    path: Path
    sha256: str
    extracted_dir: Path | None = None


def _sha256(path: str | Path) -> str:
    source = Path(path).expanduser().resolve()
    hasher = hashlib.sha256()
    with source.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def _infer_filename(url: str) -> str:
    parsed = urlparse(url)
    name = Path(parsed.path).name
    if name:
        return name
    return "downloaded_resource.bin"


def download_file(
    *,
    url: str,
    output_dir: str | Path,
    filename: str | None = None,
    timeout_sec: int = 120,
    headers: dict[str, str] | None = None,
) -> Path:
    target_dir = Path(output_dir).expanduser().resolve()
    target_dir.mkdir(parents=True, exist_ok=True)
    target_name = filename or _infer_filename(url)
    target = target_dir / target_name

    response = requests.get(url, stream=True, timeout=timeout_sec, headers=headers)
    response.raise_for_status()
    with target.open("wb") as handle:
        for chunk in response.iter_content(chunk_size=1024 * 128):
            if chunk:
                handle.write(chunk)
    return target


def maybe_extract_zip(path: str | Path, extract: bool = False) -> Path | None:
    source = Path(path).expanduser().resolve()
    if not extract:
        return None
    if source.suffix.lower() != ".zip":
        return None
    extracted_dir = source.parent / f"{source.stem}_extracted"
    extracted_dir.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(source, "r") as archive:
        archive.extractall(extracted_dir)
    return extracted_dir


def download_public_dataset(
    *,
    source: str,
    url: str,
    output_dir: str | Path,
    filename: str | None = None,
    extract_zip: bool = False,
    timeout_sec: int = 120,
    headers: dict[str, str] | None = None,
) -> DownloadArtifact:
    path = download_file(
        url=url,
        output_dir=output_dir,
        filename=filename,
        timeout_sec=timeout_sec,
        headers=headers,
    )
    extracted = maybe_extract_zip(path, extract=extract_zip)
    return DownloadArtifact(
        source=source,
        url=url,
        path=path,
        sha256=_sha256(path),
        extracted_dir=extracted,
    )


def download_g2f_file(
    *,
    url: str,
    output_dir: str | Path,
    filename: str | None = None,
    extract_zip: bool = False,
) -> DownloadArtifact:
    return download_public_dataset(
        source="g2f",
        url=url,
        output_dir=output_dir,
        filename=filename,
        extract_zip=extract_zip,
    )


def download_ltar_file(
    *,
    url: str,
    output_dir: str | Path,
    filename: str | None = None,
    extract_zip: bool = False,
) -> DownloadArtifact:
    return download_public_dataset(
        source="ltar",
        url=url,
        output_dir=output_dir,
        filename=filename,
        extract_zip=extract_zip,
    )


def download_ssurgo_file(
    *,
    url: str,
    output_dir: str | Path,
    filename: str | None = None,
    extract_zip: bool = False,
) -> DownloadArtifact:
    return download_public_dataset(
        source="ssurgo",
        url=url,
        output_dir=output_dir,
        filename=filename,
        extract_zip=extract_zip,
    )


def fetch_nass_quickstats(
    *,
    api_key: str,
    query: dict[str, Any],
    timeout_sec: int = 120,
) -> pd.DataFrame:
    params = {"key": api_key, "format": "JSON", **query}
    response = requests.get(NASS_QUICKSTATS_URL, params=params, timeout=timeout_sec)
    response.raise_for_status()
    payload = response.json()
    if "error" in payload and payload["error"]:
        raise RuntimeError(f"NASS Quick Stats error: {payload['error']}")
    data = payload.get("data", [])
    if not isinstance(data, list):
        raise RuntimeError("Unexpected NASS Quick Stats payload shape")
    return pd.DataFrame(data)


def load_nass_queries(path: str | Path) -> list[dict[str, Any]]:
    source = Path(path).expanduser().resolve()
    with source.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    if isinstance(payload, dict):
        if "queries" in payload:
            queries = payload["queries"]
            if not isinstance(queries, list):
                raise ValueError("`queries` must be a list")
            return [q for q in queries if isinstance(q, dict)]
        return [payload]
    if isinstance(payload, list):
        return [q for q in payload if isinstance(q, dict)]
    raise ValueError("NASS query JSON must be an object or list")
