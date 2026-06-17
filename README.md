# APGym

APGym is a research-oriented Python toolkit for reinforcement learning experiments on APSIM crop simulation workflows.

The repository combines APSIM execution helpers, environment definitions, composable actions and rewards, public-data ingestion, calibration utilities, and dry-run examples for crop management experiments. The current reference environment is maize nitrogen management.

## What It Includes

- APSIM runner helpers, template patching, executable discovery, and DataStore reading.
- RL-style environments for crop management experiments.
- Modular actions for planting, fertilization, irrigation, and rotation.
- Observers for soil, weather, crop, economics, and compound state features.
- Reward functions for yield, profit, and multi-objective tradeoffs.
- Constraint helpers for water, nitrogen, timing, and environmental rules.
- Public data ingestion utilities for weather, soils, NASS, G2F, and observed outputs.
- Calibration, split-aware validation, predicted-vs-observed alignment, and benchmark tooling.

## Repository Structure

```text
.
|-- actions/        # Planting, fertilization, irrigation, rotation actions
|-- builders/       # Weather, soil, management, and economics builders
|-- constraints/    # Timing, water, nitrogen, and environmental constraints
|-- data/           # Ingestion contracts, schemas, and source adapters
|-- envs/           # Crop simulation environments
|-- examples/       # Dry-run, calibration, workflow, and sweep scripts
|-- experiments/    # RL training, workflow, and sweep orchestration
|-- observers/      # State observers
|-- rewards/        # Yield, profit, and multi-objective rewards
|-- simulator/      # APSIM integration helpers
|-- templates/      # APSIM template assets
|-- tests/          # Unit and smoke tests
`-- validation/     # Metrics, calibration, benchmarks, and split helpers
```

## Quickstart

Clone the repo and run the dry-run examples first. The dry-run path is designed to work without a local APSIM install.

```bash
git clone https://github.com/haiderrmasood99/apgym.git
cd apgym
python examples/run_maize_n_dry_run.py
python examples/run_benchmark_workflow_dry_run.py
python examples/train_rl_dry_run.py
```

Run the test suite:

```bash
python -m pytest
```

Some examples expect the parent directory to be on `PYTHONPATH` because the repository itself is the `apgym` package folder. If module-style commands fail locally, run them from the parent directory:

```bash
cd ..
python -m apgym.examples.run_maize_n_dry_run
```

## APSIM Workflows

Real APSIM runs require APSIM Next Generation and a valid `.apsimx` template.

```bash
python -m apgym.examples.run_maize_n_real --template apgym/templates/maize_n_real.apsimx
```

Useful entry points:

- Dry-run environment check: `python -m apgym.examples.run_maize_n_dry_run`
- Real APSIM run: `python -m apgym.examples.run_maize_n_real --template <path>`
- Calibration report: `python -m apgym.examples.run_calibration_report`
- Real observed-data calibration: `python -m apgym.examples.run_tutorial_calibration_real`
- Split training demo: `python -m apgym.examples.train_rl_dry_run`
- Sweep demo: `python -m apgym.examples.run_rl_sweep_dry_run`

## Data Notes

The data ingestion layer is built around explicit contracts and schemas. See:

- [data/DATA_REQUIREMENTS.md](data/DATA_REQUIREMENTS.md)
- [data/ingestion/README.md](data/ingestion/README.md)
- [templates/README.md](templates/README.md)

Keep generated artifacts, raw downloads, and machine-specific APSIM outputs out of git.

## Project Status

This is an active research codebase, not a polished pip package yet. The next professionalization step is to move the package into a standard `src/apgym/` layout, add `pyproject.toml`, and publish a reproducible install path.

## License

See [LICENSE](LICENSE).
