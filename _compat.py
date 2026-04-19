"""Compatibility helpers for gymnasium/gym imports."""

from __future__ import annotations

try:
    import gymnasium as gym
    from gymnasium import spaces

    IS_GYMNASIUM = True
except ImportError:  # pragma: no cover - runtime fallback
    import gym  # type: ignore
    from gym import spaces  # type: ignore

    IS_GYMNASIUM = False

__all__ = ["gym", "spaces", "IS_GYMNASIUM"]
