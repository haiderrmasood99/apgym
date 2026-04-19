from __future__ import annotations

import argparse
from pathlib import Path

from apgym.envs import MaizeNConfig, MaizeNEnv


def main() -> None:
    parser = argparse.ArgumentParser(description="Run one APGym maize-N episode against APSIM.")
    parser.add_argument("--template", required=True, help="Path to a validated maize .apsimx file")
    parser.add_argument("--models-exe", default=None, help="Optional explicit Models.exe path")
    parser.add_argument(
        "--max-steps",
        type=int,
        default=6,
        help="Maximum number of steps to execute before stopping (default: 6).",
    )
    args = parser.parse_args()

    config = MaizeNConfig(
        dry_run=False,
        template_path=Path(args.template).expanduser().resolve(),
        models_exe=None if args.models_exe is None else Path(args.models_exe),
    )
    env = MaizeNEnv(config=config)
    reset_out = env.reset()
    if isinstance(reset_out, tuple):
        obs, info = reset_out
    else:
        obs, info = reset_out, {}
    print("Reset info:", info)

    done = False
    step_count = 0
    while not done:
        action = 0
        step_out = env.step(action)
        if len(step_out) == 5:
            obs, reward, terminated, truncated, info = step_out
            done = terminated or truncated
        else:
            obs, reward, done, info = step_out
        step_count += 1
        print(
            f"step={step_count} date={info['date']} "
            f"reward={reward:.3f} totalN={info['total_n_applied_kg_ha']:.1f}"
        )
        if args.max_steps > 0 and step_count >= args.max_steps:
            break
    print("Final info:", info)


if __name__ == "__main__":
    main()
