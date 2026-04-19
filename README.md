# APGym (Initial Scaffold)

APGym is an APSIM-backed RL framework modeled after the architecture lessons from `cyclesgym`, adapted to APSIM Next Gen (`.apsimx` + DataStore).

This initial scaffold includes:

- APSIM run adapter (`simulator/`)
- first environment (`envs/maize_n.py`)
- composable action/observer/reward/constraint modules
- validation utilities (`validation/`)
- data contracts and schemas (`data/schemas/`)

## Quick Start (Dry Run)

Run a smoke episode without APSIM installed:

```powershell
python -m apgym.examples.run_maize_n_dry_run
```

## Real APSIM Run

1. Set `APSIM_MODELS_EXE` to your `Models.exe`.
2. Replace template path with a validated `.apsimx`.
3. Set `MaizeNConfig(dry_run=False, template_path=...)`.

Or run:

```powershell
python -m apgym.examples.run_maize_n_real --template C:\path\to\validated_maize.apsimx --max-steps 6
```

## Included Real Template

This repo now includes [`maize_n_real.apsimx`](./templates/maize_n_real.apsimx), derived from APSIM's maize example.

- report output is switched to daily (`[Clock].DoReport`);
- an `APGym TopDress N` manager is added for in-season date-based N schedules;
- clock window is patched per episode from `MaizeNConfig`.
- default sowing fertiliser manager is forced to zero during APGym runs.

To rebuild the template from a local APSIM install:

```powershell
python apgym\templates\prepare_maize_n_template.py --source "C:\Program Files\APSIM2026.3.8023.0\Examples\Maize.apsimx" --target "C:\Users\Haider\Desktop\APSIM_GYM\apgym\templates\maize_n_real.apsimx"
```

## Data Ingestion Pipelines

Initial ingestion adapters are now included under [`apgym/data/ingestion`](./data/ingestion):

- G2F harmonization: `python -m apgym.data.ingestion.g2f ...`
- SSURGO horizon normalization: `python -m apgym.data.ingestion.ssurgo ...`
- NASA POWER weather fetch: `python -m apgym.data.ingestion.nasa_power ...`
- Public-source connectors/downloads: `python -m apgym.data.ingestion.pipeline --site-url ... --observed-url ...`
- NASS Quick Stats snapshots: `--nass-query-json ... --nass-api-key ...`

The pipelines output normalized contract tables:

- `site_identity`
- `weather_daily`
- `soil_profile`
- `management_events`
- `observed_outputs`

## Baseline Harness

Baseline evaluation and split helpers are available in [`apgym/validation`](./validation):

- policy evaluation: `evaluate_policy_set(...)`
- split construction: `make_generalization_splits(...)`

Run baseline dry-run demo:

```powershell
python -m apgym.examples.evaluate_baselines_dry_run
```

## RL Training Harness

Initial PPO/A2C integration against split tables is available in [`apgym/experiments/rl.py`](./experiments/rl.py).

Run dry-run split training demo:

```powershell
python -m apgym.examples.train_rl_dry_run
```

This uses:

- `make_generalization_splits(...)` for train/test-year/holdout-site partitioning,
- Stable-Baselines3 PPO/A2C training on train split environments,
- evaluation on all splits with per-episode metrics.

## Next Engineering Tasks

- Calibrate/validate the maize template against observed benchmark data (G2F/LTAR/etc).
- Expand state extraction to include explicit soil water/N depth-band variables from APSIM reports.
- Harden source-specific extractors for official public repositories (schema/version aware).
- Build scenario-specific experiment configs and hyperparameter sweeps on real benchmark bundles.
