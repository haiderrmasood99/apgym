"""Utilities to patch `.apsimx` JSON files before simulation runs."""

from __future__ import annotations

from dataclasses import dataclass
import json
import re
from pathlib import Path
from typing import Any, Iterable

_TOKEN_RE = re.compile(r"([^.[]+)|\[(\d+)\]")


@dataclass(frozen=True)
class ApsimPatch:
    """A single JSON path assignment on an APSIMX payload."""

    json_path: str
    value: Any


@dataclass(frozen=True)
class ApsimManagerParameterPatch:
    """Set a manager parameter using manager/parameter names."""

    manager_name: str
    parameter_key: str
    value: Any
    simulation_name: str | None = None
    zone_name: str | None = None
    apply_to_all: bool = False


@dataclass(frozen=True)
class ApsimModelPropertyPatch:
    """Set a top-level property on a named model."""

    model_name: str
    property_name: str
    value: Any
    type_contains: str | None = None
    simulation_name: str | None = None
    zone_name: str | None = None
    apply_to_all: bool = False


PatchLike = ApsimPatch | ApsimManagerParameterPatch | ApsimModelPropertyPatch


def _parse_path(path: str) -> list[str | int]:
    tokens: list[str | int] = []
    for name_token, index_token in _TOKEN_RE.findall(path):
        if name_token:
            tokens.append(name_token)
        else:
            tokens.append(int(index_token))
    if not tokens:
        raise ValueError(f"Invalid patch path: {path!r}")
    return tokens


def _set_path(root: Any, path: str, value: Any) -> None:
    cursor = root
    tokens = _parse_path(path)
    for token in tokens[:-1]:
        if isinstance(token, int):
            if not isinstance(cursor, list):
                raise TypeError(
                    f"Path expects list index {token} but found {type(cursor).__name__}"
                )
            if token >= len(cursor):
                raise IndexError(f"Index {token} out of range in {path!r}")
            cursor = cursor[token]
        else:
            if not isinstance(cursor, dict):
                raise TypeError(
                    f"Path expects object key {token!r} but found {type(cursor).__name__}"
                )
            if token not in cursor:
                raise KeyError(f"Missing key {token!r} in {path!r}")
            cursor = cursor[token]

    last = tokens[-1]
    if isinstance(last, int):
        if not isinstance(cursor, list):
            raise TypeError(
                f"Path expects list index {last} but found {type(cursor).__name__}"
            )
        if last >= len(cursor):
            raise IndexError(f"Index {last} out of range in {path!r}")
        cursor[last] = value
    else:
        if not isinstance(cursor, dict):
            raise TypeError(
                f"Path expects object key {last!r} but found {type(cursor).__name__}"
            )
        cursor[last] = value


def _type_contains(node: dict[str, Any], text: str) -> bool:
    node_type = str(node.get("$type", ""))
    return text in node_type


def _walk_nodes(
    node: Any, ancestors: list[dict[str, Any]] | None = None
) -> Iterable[tuple[dict[str, Any], list[dict[str, Any]]]]:
    if ancestors is None:
        ancestors = []
    if not isinstance(node, dict):
        return
    yield node, ancestors
    children = node.get("Children")
    if isinstance(children, list):
        for child in children:
            yield from _walk_nodes(child, ancestors + [node])


def _in_scope(
    ancestors: list[dict[str, Any]],
    simulation_name: str | None,
    zone_name: str | None,
) -> bool:
    if simulation_name is not None:
        sim_ok = any(
            _type_contains(a, "Models.Core.Simulation")
            and str(a.get("Name")) == simulation_name
            for a in ancestors
        )
        if not sim_ok:
            return False
    if zone_name is not None:
        zone_ok = any(
            _type_contains(a, "Models.Core.Zone") and str(a.get("Name")) == zone_name
            for a in ancestors
        )
        if not zone_ok:
            return False
    return True


def _resolve_single_or_many(
    matches: list[dict[str, Any]],
    apply_to_all: bool,
    patch_label: str,
) -> list[dict[str, Any]]:
    if not matches:
        raise KeyError(f"No match found for {patch_label}")
    if len(matches) > 1 and not apply_to_all:
        raise ValueError(
            f"Found multiple matches ({len(matches)}) for {patch_label}. "
            "Specify simulation/zone scope or set apply_to_all=True."
        )
    return matches if apply_to_all else [matches[0]]


def _apply_manager_parameter_patch(payload: Any, patch: ApsimManagerParameterPatch) -> None:
    matches: list[dict[str, Any]] = []
    for node, ancestors in _walk_nodes(payload):
        if (
            _type_contains(node, "Models.Manager")
            and str(node.get("Name")) == patch.manager_name
            and _in_scope(ancestors, patch.simulation_name, patch.zone_name)
        ):
            matches.append(node)

    targets = _resolve_single_or_many(
        matches,
        apply_to_all=patch.apply_to_all,
        patch_label=f"manager={patch.manager_name!r}",
    )
    for target in targets:
        parameters = target.setdefault("Parameters", [])
        if not isinstance(parameters, list):
            raise TypeError(
                f"Manager {patch.manager_name!r} has non-list Parameters: "
                f"{type(parameters).__name__}"
            )
        found = False
        for parameter in parameters:
            if str(parameter.get("Key")) == patch.parameter_key:
                parameter["Value"] = str(patch.value)
                found = True
                break
        if not found:
            parameters.append({"Key": patch.parameter_key, "Value": str(patch.value)})


def _apply_model_property_patch(payload: Any, patch: ApsimModelPropertyPatch) -> None:
    matches: list[dict[str, Any]] = []
    for node, ancestors in _walk_nodes(payload):
        if str(node.get("Name")) != patch.model_name:
            continue
        if patch.type_contains is not None and not _type_contains(node, patch.type_contains):
            continue
        if not _in_scope(ancestors, patch.simulation_name, patch.zone_name):
            continue
        matches.append(node)

    targets = _resolve_single_or_many(
        matches,
        apply_to_all=patch.apply_to_all,
        patch_label=f"model={patch.model_name!r}",
    )
    for target in targets:
        target[patch.property_name] = patch.value


def apply_patches(
    apsimx_path: str | Path,
    patches: Iterable[PatchLike],
    output_path: str | Path | None = None,
) -> Path:
    """Apply JSON patches to an APSIMX file and return the target path."""

    source = Path(apsimx_path).expanduser().resolve()
    if not source.exists():
        raise FileNotFoundError(f"APSIM template not found: {source}")

    target = source if output_path is None else Path(output_path).expanduser().resolve()

    with source.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)

    for patch in patches:
        if isinstance(patch, ApsimPatch):
            _set_path(payload, patch.json_path, patch.value)
        elif isinstance(patch, ApsimManagerParameterPatch):
            _apply_manager_parameter_patch(payload, patch)
        elif isinstance(patch, ApsimModelPropertyPatch):
            _apply_model_property_patch(payload, patch)
        else:
            raise TypeError(f"Unsupported patch type: {type(patch).__name__}")

    with target.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")

    return target
