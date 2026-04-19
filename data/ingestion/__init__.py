"""Ingestion pipelines for external agronomic datasets."""

from apgym.data.ingestion.bundle import DataBundle
from apgym.data.ingestion.contracts import (
    SCHEMA_NAMES,
    get_required_columns,
    validate_dataframe_contract,
)
from apgym.data.ingestion.g2f import (
    build_g2f_bundle,
    ingest_g2f_observed_outputs,
    ingest_g2f_site_identity,
    ingest_g2f_weather,
)
from apgym.data.ingestion.nasa_power import fetch_nasa_power_daily, fetch_weather_for_sites
from apgym.data.ingestion.nass import normalize_nass_quickstats_yield
from apgym.data.ingestion.observed import normalize_observed_outputs
from apgym.data.ingestion.pipeline import assemble_bundle_with_manifest
from apgym.data.ingestion.public_sources import (
    DownloadArtifact,
    download_g2f_file,
    download_ltar_file,
    download_public_dataset,
    download_ssurgo_file,
    fetch_nass_quickstats,
    load_nass_queries,
)
from apgym.data.ingestion.ssurgo import ingest_ssurgo_chorizon

__all__ = [
    "DataBundle",
    "DownloadArtifact",
    "SCHEMA_NAMES",
    "assemble_bundle_with_manifest",
    "build_g2f_bundle",
    "download_g2f_file",
    "download_ltar_file",
    "download_public_dataset",
    "download_ssurgo_file",
    "fetch_nasa_power_daily",
    "fetch_nass_quickstats",
    "fetch_weather_for_sites",
    "get_required_columns",
    "ingest_g2f_observed_outputs",
    "ingest_g2f_site_identity",
    "ingest_g2f_weather",
    "ingest_ssurgo_chorizon",
    "load_nass_queries",
    "normalize_nass_quickstats_yield",
    "normalize_observed_outputs",
    "validate_dataframe_contract",
]
