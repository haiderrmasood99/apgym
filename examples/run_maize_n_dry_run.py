from __future__ import annotations

from apgym.envs import MaizeNConfig, MaizeNEnv


def main() -> None:
    env = MaizeNEnv(MaizeNConfig(dry_run=True))
    reset_out = env.reset()
    if isinstance(reset_out, tuple) and len(reset_out) == 2:
        obs, info = reset_out
    else:
        obs, info = reset_out, {}

    print("Initial observation shape:", obs.shape)
    print("Initial info:", info)

    total_reward = 0.0
    step = 0
    while True:
        action = env.action_space.sample()
        step_out = env.step(action)
        if len(step_out) == 5:
            obs, reward, terminated, truncated, info = step_out
            done = terminated or truncated
        else:
            obs, reward, done, info = step_out
        total_reward += reward
        step += 1
        if done:
            break

    print("Episode steps:", step)
    print("Total reward:", total_reward)
    print("Final info:", info)


if __name__ == "__main__":
    main()
