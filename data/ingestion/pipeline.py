"""Reproducible data assembly pipeline with provenance manifest output."""

from __future__ import annotations

import argparse
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import os
from typing import Any

import pandas as pd

from apgym.data.ingestion.bundle import DataBundle
from apgym.data.ingestion.g2f import build_g2f_bundle
from apgym.data.ingestion.nasa_power import fetch_weather_for_sites
from apgym.data.ingestion.public_sources import (
    DownloadArtifact,
    download_g2f_file,
    download_public_dataset,
    download_ssurgo_file,
    fetch_nass_quickstats,
    load_nass_queries,
)
from apgym.data.ingestion.ssurgo import ingest_ssurgo_chorizon
from apgym.data.ingestion.utils import load_tabular


def _sha256(path: str | Path) -> str:
    source = Path(path).expanduser().resolve()
    hasher = hashlib.sha256()
    with source.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


@dataclass(frozen=True)
class FileRecord:
    path: str
    sha256: str


def _record(path: str | Path) -> FileRecord:
    source = Path(path).expanduser().resolve()
    return FileRecord(path=str(source), sha256=_sha256(source))


def _resolve_local_or_url(
    *,
    name: str,
    local_path: str | Path | None,
    url: str | None,
    download_dir: Path,
    source: str,
    download_artifacts: list[DownloadArtifact],
) -> Path | None:
    if local_path is not None:
        resolved = Path(local_path).expanduser().resolve()
        if not resolved.exists():
            raise FileNotFoundError(f"{name} path does not exist: {resolved}")
        return resolved
    if url is None:
        return None
    if source == "g2f":
        artifact = download_g2f_file(url=url, output_dir=download_dir, extract_zip=False)
    elif source == "ssurgo":
        artifact = download_ssurgo_file(url=url, output_dir=download_dir, extract_zip=False)
    else:
        artifact = download_public_dataset(
            source=source,
            url=url,
            output_dir=download_dir,
            extract_zip=False,
        )
    download_artifacts.append(artifact)
    return artifact.path


def _merge_weather(primary: pd.DataFrame | None, secondary: pd.DataFrame | None) -> pd.DataFrame | None:
    if primary is None:
        return secondary
    if secondary is None:
        return primary
    combined = pd.concat([primary, secondary], ignore_index=True)
    combined = combined.drop_duplicates(subset=["site_id", "date"], keep="first")
    return combined.sort_values(by=["site_id", "date"]).reset_index(drop=True)


def assemble_bundle_with_manifest(
    *,
    output_dir: str | Path,
    site_path: str | Path | None = None,
    observed_path: str | Path | None = None,
    weather_path: str | Path | None = None,
    management_path: str | Path | None = None,
    ssurgo_path: str | Path | None = None,
    site_url: str | None = None,
    observed_url: str | None = None,
    weather_url: str | None = None,
    management_url: str | None = None,
    ssurgo_url: str | None = None,
    mapping_json: str | Path | None = None,
    output_format: str = "parquet",
    fetch_nasa_power: bool = False,
    nasa_start: str | None = None,
    nasa_end: str | None = None,
    nass_query_json: str | Path | None = None,
    nass_api_key: str | None = None,
    download_dir: str | Path | None = None,
) -> tuple[DataBundle, Path]:
    out_root = Path(output_dir).expanduser().resolve()
    stage_dir = (
        Path(download_dir).expanduser().resolve()
        if download_dir is not None
        else out_root / "_downloads"
    )
    stage_dir.mkdir(parents=True, exist_ok=True)

    download_artifacts: list[DownloadArtifact] = []

    site_resolved = _resolve_local_or_url(
        name="site",
        local_path=site_path,
        url=site_url,
        download_dir=stage_dir,
        source="g2f",
        download_artifacts=download_artifacts,
    )
    observed_resolved = _resolve_local_or_url(
        name="observed",
        local_path=observed_path,
        url=observed_url,
        download_dir=stage_dir,
        source="g2f",
        download_artifacts=download_artifacts,
    )
    weather_resolved = _resolve_local_or_url(
        name="weather",
        local_path=weather_path,
        url=weather_url,
        download_dir=stage_dir,
        source="g2f",
        download_artifacts=download_artifacts,
    )
    management_resolved = _resolve_local_or_url(
        name="management",
        local_path=management_path,
        url=management_url,
        download_dir=stage_dir,
        source="g2f",
        download_artifacts=download_artifacts,
    )
    ssurgo_resolved = _resolve_local_or_url(
        name="ssurgo",
        local_path=ssurgo_path,
        url=ssurgo_url,
        download_dir=stage_dir,
        source="ssurgo",
        download_artifacts=download_artifacts,
    )

    if site_resolved is None or observed_resolved is None:
        raise ValueError("Both site and observed inputs are required (path or URL).")

    bundle = build_g2f_bundle(
        site_path=site_resolved,
        observed_path=observed_resolved,
        weather_path=weather_resolved,
        management_path=management_resolved,
        mapping_json=mapping_json,
    )

    if ssurgo_resolved is not None:
        ssurgo_frame = load_tabular(ssurgo_resolved)
        bundle.soil_profile = ingest_ssurgo_chorizon(ssurgo_frame)

    if fetch_nasa_power:
        if nasa_start is None or nasa_end is None:
            raise ValueError("nasa_start and nasa_end are required when fetch_nasa_power is enabled")
        if bundle.site_identity is None:
            raise ValueError("site_identity is required to fetch NASA POWER weather")
        nasa_weather = fetch_weather_for_sites(
            bundle.site_identity[["site_id", "latitude", "longitude"]].drop_duplicates(),
            start_date=pd.to_datetime(nasa_start).date(),
            end_date=pd.to_datetime(nasa_end).date(),
        )
        bundle.weather_daily = _merge_weather(bundle.weather_daily, nasa_weather)

    outputs = bundle.save(output_dir, fmt=output_format)

    nass_outputs: list[Path] = []
    if nass_query_json is not None:
        queries = load_nass_queries(nass_query_json)
        resolved_api_key = nass_api_key or os.getenv("NASS_API_KEY")
        if not resolved_api_key:
            raise ValueError(
                "NASS query JSON provided but no api key found. Set --nass-api-key or NASS_API_KEY."
            )
        for idx, query in enumerate(queries):
            frame = fetch_nass_quickstats(api_key=resolved_api_key, query=query)
            out_path = out_root / f"nass_query_{idx}.csv"
            frame.to_csv(out_path, index=False)
            nass_outputs.append(out_path)

    input_paths: list[Path] = [Path(site_resolved), Path(observed_resolved)]
    for path in (weather_resolved, management_resolved, ssurgo_resolved, mapping_json):
        if path is not None:
            input_paths.append(Path(path))
    for artifact in download_artifacts:
        input_paths.append(Path(artifact.path))
    for path in nass_outputs:
        input_paths.append(Path(path))

    unique_inputs: dict[str, Path] = {}
    for path in input_paths:
        resolved = path.expanduser().resolve()
        unique_inputs[str(resolved)] = resolved
    inputs: list[FileRecord] = [_record(path) for path in unique_inputs.values()]
    output_records = [_record(path) for path in outputs.values()]

    manifest = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "pipeline": "apgym.data.ingestion.pipeline",
        "output_dir": str(Path(output_dir).expanduser().resolve()),
        "format": output_format,
        "inputs": [asdict(record) for record in inputs],
        "outputs": [asdict(record) for record in output_records],
        "downloaded_sources": [
            {
                "source": artifact.source,
                "url": artifact.url,
                "path": str(artifact.path),
                "sha256": artifact.sha256,
                "extracted_dir": None if artifact.extracted_dir is None else str(artifact.extracted_dir),
            }
            for artifact in download_artifacts
        ],
        "nass_outputs": [str(path) for path in nass_outputs],
        "options": {
            "fetch_nasa_power": fetch_nasa_power,
            "nasa_start": nasa_start,
            "nasa_end": nasa_end,
            "site_url": site_url,
            "observed_url": observed_url,
            "weather_url": weather_url,
            "management_url": management_url,
            "ssurgo_url": ssurgo_url,
            "nass_query_json": None if nass_query_json is None else str(Path(nass_query_json).expanduser().resolve()),
        },
        "row_counts": bundle.summary(),
    }
    manifest_path = Path(output_dir).expanduser().resolve() / "manifest.json"
    with manifest_path.open("w", encoding="utf-8") as handle:
        json.dump(manifest, handle, indent=2)
        handle.write("\n")
    return bundle, manifest_path


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Assemble normalized APGym benchmark tables with provenance manifest."
    )
    parser.add_argument("--site", default=None)
    parser.add_argument("--observed", default=None)
    parser.add_argument("--weather", default=None)
    parser.add_argument("--management", default=None)
    parser.add_argument("--ssurgo", default=None)
    parser.add_argument("--site-url", default=None)
    parser.add_argument("--observed-url", default=None)
    parser.add_argument("--weather-url", default=None)
    parser.add_argument("--management-url", default=None)
    parser.add_argument("--ssurgo-url", default=None)
    parser.add_argument("--mapping-json", default=None)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--download-dir", default=None)
    parser.add_argument("--format", choices=("parquet", "csv"), default="parquet")
    parser.add_argument("--fetch-nasa-power", action="store_true")
    parser.add_argument("--nasa-start", default=None)
    parser.add_argument("--nasa-end", default=None)
    parser.add_argument("--nass-query-json", default=None)
    parser.add_argument("--nass-api-key", default=None)
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    _, manifest_path = assemble_bundle_with_manifest(
        output_dir=args.output_dir,
        site_path=args.site,
        observed_path=args.observed,
        weather_path=args.weather,
        management_path=args.management,
        ssurgo_path=args.ssurgo,
        site_url=args.site_url,
        observed_url=args.observed_url,
        weather_url=args.weather_url,
        management_url=args.management_url,
        ssurgo_url=args.ssurgo_url,
        mapping_json=args.mapping_json,
        output_format=args.format,
        fetch_nasa_power=args.fetch_nasa_power,
        nasa_start=args.nasa_start,
        nasa_end=args.nasa_end,
        nass_query_json=args.nass_query_json,
        nass_api_key=args.nass_api_key,
        download_dir=args.download_dir,
    )
    print(f"Wrote manifest: {manifest_path}")


if __name__ == "__main__":
    main()
