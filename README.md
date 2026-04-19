# APGym Package Guide

This directory contains the APGym Python package.

## Module Layout

- `simulator/`: APSIM execution, template patching, DataStore reading.
- `envs/`: environment definitions (`maize_n` is the current reference environment).
- `actions/`, `observers/`, `rewards/`, `constraints/`: composable RL interface components.
- `data/ingestion/`: dataset normalization and provenance-aware assembly.
- `validation/`: calibration metrics, predicted-vs-observed alignment, and policy evaluation helpers.
- `experiments/`: split-aware training, calibration-gated workflow, and sweep tools.
- `templates/`: APSIM template assets and preparation script.
- `examples/`: runnable scripts for smoke tests, calibration, workflows, and sweeps.
- `tests/`: unit and smoke tests.

## Typical Local Workflow

1. Run dry-run environment checks.
2. Verify APSIM executable discovery.
3. Execute real APSIM smoke tests.
4. Assemble and normalize benchmark data.
5. Run calibration with explicit thresholds.
6. Train and evaluate policies on split datasets.
7. Run sweeps and archive artifacts.

## Key Entrypoints

- Dry run: `python -m apgym.examples.run_maize_n_dry_run`
- Real run: `python -m apgym.examples.run_maize_n_real --template <path>`
- Calibration CLI: `python -m apgym.validation.calibration ...`
- Real observed-data benchmark calibration: `python -m apgym.examples.run_tutorial_calibration_real`
- Split training demo: `python -m apgym.examples.train_rl_dry_run`
- Sweep demo: `python -m apgym.examples.run_rl_sweep_dry_run`

