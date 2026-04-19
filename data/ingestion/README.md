# APGym Ingestion Notes

This folder now includes ingestion adapters for:

- `g2f.py`: harmonize local G2F-style tables into APGym normalized tables.
- `ssurgo.py`: convert SSURGO horizon attributes into APGym soil profile layers.
- `nasa_power.py`: fetch NASA POWER daily weather into APGym weather contract format.
- `observed.py`: normalize observed outcomes from generic tables.

All adapters target the contracts in [`/apgym/data/schemas`](../schemas).

## Normalized table targets

- `site_identity.parquet`
- `weather_daily.parquet`
- `soil_profile.parquet`
- `management_events.parquet`
- `observed_outputs.parquet`

## Example commands

Normalize G2F-like files:

```powershell
python -m apgym.data.ingestion.g2f --site .\raw\g2f_sites.csv --observed .\raw\g2f_observed.csv --weather .\raw\g2f_weather.csv --output-dir .\normalized --format parquet
```

With custom column mapping:

```powershell
python -m apgym.data.ingestion.g2f --site .\raw\sites.csv --observed .\raw\observed.csv --mapping-json .\apgym\data\ingestion\g2f_mapping.example.json --output-dir .\normalized
```

Convert SSURGO horizon table:

```powershell
python -m apgym.data.ingestion.ssurgo --input .\raw\ssurgo_chorizon.csv --output .\normalized\soil_profile.parquet
```

Fetch NASA POWER weather for site list:

```powershell
python -m apgym.data.ingestion.nasa_power --sites .\normalized\site_identity.parquet --start 2015-01-01 --end 2020-12-31 --output .\normalized\weather_daily.parquet
```

Run end-to-end assembly with provenance manifest:

```powershell
python -m apgym.data.ingestion.pipeline --site .\raw\g2f_sites.csv --observed .\raw\g2f_observed.csv --weather .\raw\g2f_weather.csv --ssurgo .\raw\ssurgo_chorizon.csv --output-dir .\benchmark_v1 --format parquet
```

This writes normalized tables plus `manifest.json` containing input/output checksums and run metadata.

Run assembly directly from remote files:

```powershell
python -m apgym.data.ingestion.pipeline --site-url https://example.org/g2f_site.csv --observed-url https://example.org/g2f_observed.csv --weather-url https://example.org/g2f_weather.csv --ssurgo-url https://example.org/ssurgo_chorizon.csv --output-dir .\benchmark_v1 --format parquet
```

Include NASS Quick Stats query snapshots in the manifest run:

```powershell
python -m apgym.data.ingestion.pipeline --site .\raw\g2f_sites.csv --observed .\raw\g2f_observed.csv --nass-query-json .\apgym\data\ingestion\nass_queries.example.json --nass-api-key YOUR_KEY --output-dir .\benchmark_v1
```
