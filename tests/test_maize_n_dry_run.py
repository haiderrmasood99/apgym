from __future__ import annotations

import unittest

from apgym.envs import MaizeNConfig, MaizeNEnv


class TestMaizeNDryRun(unittest.TestCase):
    def test_episode_rollout(self) -> None:
        env = MaizeNEnv(MaizeNConfig(dry_run=True))
        out = env.reset()
        if isinstance(out, tuple) and len(out) == 2:
            obs, info = out
        else:
            obs, info = out, {}

        self.assertEqual(obs.shape[0], 11)
        self.assertIn("yield_t_ha", info)

        steps = 0
        total_reward = 0.0
        while True:
            step_out = env.step(0)  # always "no additional N"
            if len(step_out) == 5:
                obs, reward, terminated, truncated, info = step_out
                done = terminated or truncated
            else:
                obs, reward, done, info = step_out
            total_reward += reward
            steps += 1
            if done:
                break

        self.assertGreater(steps, 0)
        self.assertIn("yield_t_ha", info)
        self.assertGreaterEqual(info["yield_t_ha"], 0.0)
        self.assertIsInstance(total_reward, float)


if __name__ == "__main__":
    unittest.main()
