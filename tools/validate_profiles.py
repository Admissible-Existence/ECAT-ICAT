#!/usr/bin/env python3
"""Minimal ECAT/ICAT release-candidate validator.

This validator intentionally uses only the Python standard library. It checks the
subset of schema constraints needed by the RC fixtures and prints deterministic
JSON so the repository can produce comparable expected output without external
dependencies.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

ECAT_REQUIRED = [
    "schema_version",
    "profile_id",
    "layer",
    "entity_id",
    "context",
    "declared_experience",
    "coherence_status",
    "recoverability_status",
    "boundary_relevance",
    "validity_window",
    "limitations",
    "receipt_id",
]

ICAT_REQUIRED = [
    "schema_version",
    "profile_id",
    "layer",
    "entities",
    "interaction_context",
    "declared_relationship_context",
    "shared_understanding_status",
    "trust_relevance",
    "recoverability_status",
    "boundary_relevance",
    "validity_window",
    "limitations",
    "receipt_id",
]

ALLOWED = {
    "schema_version": {"0.1.0-rc1"},
    "ecat_layer": {"ECAT"},
    "icat_layer": {"ICAT"},
    "coherence_status": {"coherent", "partial", "incoherent", "unknown"},
    "shared_understanding_status": {"aligned", "partial", "conflicted", "unknown"},
    "recoverability_status": {"recoverable", "conditional", "unrecoverable", "unknown"},
}


def profile_paths() -> list[Path]:
    """Return only ECAT/ICAT profile fixtures for RC1 validation."""
    return sorted((ROOT / "examples" / "ecat").glob("*.json")) + sorted(
        (ROOT / "examples" / "icat").glob("*.json")
    )


def load_json(path: Path) -> tuple[dict[str, Any] | None, list[str]]:
    try:
        with path.open("r", encoding="utf-8") as handle:
            value = json.load(handle)
    except Exception as exc:  # pragma: no cover - deterministic CLI output path
        return None, [f"invalid_json:{exc.__class__.__name__}"]
    if not isinstance(value, dict):
        return None, ["root_not_object"]
    return value, []


def require_fields(data: dict[str, Any], required: list[str]) -> list[str]:
    return [f"missing:{field}" for field in required if field not in data]


def check_common(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if data.get("schema_version") not in ALLOWED["schema_version"]:
        errors.append("invalid:schema_version")
    window = data.get("validity_window")
    if not isinstance(window, dict):
        errors.append("invalid:validity_window")
    else:
        for field in ("from", "until"):
            if not isinstance(window.get(field), str) or not window.get(field):
                errors.append(f"invalid:validity_window.{field}")
    limitations = data.get("limitations")
    if not isinstance(limitations, list) or not limitations:
        errors.append("invalid:limitations")
    return errors


def validate_ecat(path: Path, data: dict[str, Any]) -> list[str]:
    errors = require_fields(data, ECAT_REQUIRED)
    errors.extend(check_common(data))
    if data.get("layer") not in ALLOWED["ecat_layer"]:
        errors.append("invalid:layer")
    if data.get("coherence_status") not in ALLOWED["coherence_status"]:
        errors.append("invalid:coherence_status")
    if data.get("recoverability_status") not in ALLOWED["recoverability_status"]:
        errors.append("invalid:recoverability_status")
    return sorted(set(errors))


def validate_icat(path: Path, data: dict[str, Any]) -> list[str]:
    errors = require_fields(data, ICAT_REQUIRED)
    errors.extend(check_common(data))
    if data.get("layer") not in ALLOWED["icat_layer"]:
        errors.append("invalid:layer")
    entities = data.get("entities")
    if not isinstance(entities, list) or len(entities) < 2 or not all(isinstance(item, str) and item for item in entities):
        errors.append("invalid:entities")
    if data.get("shared_understanding_status") not in ALLOWED["shared_understanding_status"]:
        errors.append("invalid:shared_understanding_status")
    if data.get("recoverability_status") not in ALLOWED["recoverability_status"]:
        errors.append("invalid:recoverability_status")
    return sorted(set(errors))


def validate_path(path: Path) -> dict[str, Any]:
    data, load_errors = load_json(path)
    layer_hint = "ECAT" if "/ecat/" in path.as_posix() else "ICAT" if "/icat/" in path.as_posix() else "UNKNOWN"
    if data is None:
        errors = load_errors
    elif layer_hint == "ECAT":
        errors = validate_ecat(path, data)
    elif layer_hint == "ICAT":
        errors = validate_icat(path, data)
    else:
        errors = ["unknown_layer_path"]
    return {
        "path": path.relative_to(ROOT).as_posix(),
        "layer": layer_hint,
        "valid": not errors,
        "errors": errors,
    }


def build_summary() -> dict[str, Any]:
    results = [validate_path(path) for path in profile_paths()]
    return {
        "schema_version": "0.1.0-rc1",
        "total": len(results),
        "valid": sum(1 for item in results if item["valid"]),
        "invalid": sum(1 for item in results if not item["valid"]),
        "results": results,
    }


def main() -> int:
    summary = build_summary()
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0 if summary["valid"] == 2 and summary["invalid"] == 2 else 1


if __name__ == "__main__":
    sys.exit(main())
