"""Helpers to resolve APSIM Next Gen executable paths."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Iterable


def _candidate_paths() -> Iterable[Path]:
    env_keys = ("APSIM_MODELS_EXE", "APSIM_MODELS_PATH")
    for key in env_keys:
        value = os.getenv(key)
        if not value:
            continue
        path = Path(value).expanduser()
        if path.name.lower() == "models.exe":
            yield path
        else:
            yield path / "Models.exe"

    windows_roots = (
        Path(r"C:\Program Files"),
        Path(r"C:\Program Files (x86)"),
    )
    patterns = (
        "APSIM*/bin/Models.exe",
        "APSIM*/Models.exe",
        "APSIM Next Generation*/bin/Models.exe",
    )
    for root in windows_roots:
        if not root.exists():
            continue
        for pattern in patterns:
            yield from root.glob(pattern)


def find_models_exe(explicit_path: str | Path | None = None) -> Path:
    """Return an existing `Models.exe` path or raise a clear error."""

    if explicit_path is not None:
        path = Path(explicit_path).expanduser().resolve()
        if path.exists():
            return path
        raise FileNotFoundError(
            f"APSIM executable not found at explicit path: {path}"
        )

    for candidate in _candidate_paths():
        if candidate.exists():
            return candidate.resolve()

    raise FileNotFoundError(
        "Could not locate APSIM Models.exe. Set APSIM_MODELS_EXE "
        "to the full path (for example "
        r"'C:\Program Files\APSIM2026.3.7832.0\bin\Models.exe')."
    )
