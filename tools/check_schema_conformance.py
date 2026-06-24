#!/usr/bin/env python3
"""Validate RC1 ECAT/ICAT fixtures against the repository schema files.

This is a dependency-free schema-conformance checker for the JSON Schema subset
used by RC1. It reads the schema documents directly and validates required
fields, constants, enums, arrays, objects, strings, and additionalProperties.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PAIRS = [
    (ROOT / "schemas" / "ecat-profile.schema.json", ROOT / "examples" / "ecat"),
    (ROOT / "schemas" / "icat-profile.schema.json", ROOT / "examples" / "icat"),
]
EXPECTED = {
    "examples/ecat/fail_missing_recoverability.json": False,
    "examples/ecat/pass_declared_experience_recoverable.json": True,
    "examples/icat/fail_missing_entities.json": False,
    "examples/icat/pass_shared_understanding_recoverable.json": True,
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(value: Any, schema: dict[str, Any], pointer: str) -> list[str]:
    errors: list[str] = []
    expected_type = schema.get("type")

    if expected_type == "object":
        if not isinstance(value, dict):
            return [f"{pointer}:type:object"]
        required = schema.get("required", [])
        for field in required:
            if field not in value:
                errors.append(f"{pointer}:missing:{field}")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for field in value:
                if field not in properties:
                    errors.append(f"{pointer}:additional:{field}")
        for field, child_schema in properties.items():
            if field in value:
                errors.extend(validate(value[field], child_schema, f"{pointer}/{field}"))
        return errors

    if expected_type == "array":
        if not isinstance(value, list):
            return [f"{pointer}:type:array"]
        min_items = schema.get("minItems")
        if min_items is not None and len(value) < min_items:
            errors.append(f"{pointer}:minItems:{min_items}")
        item_schema = schema.get("items")
        if item_schema:
            for index, item in enumerate(value):
                errors.extend(validate(item, item_schema, f"{pointer}/{index}"))
        return errors

    if expected_type == "string":
        if not isinstance(value, str):
            return [f"{pointer}:type:string"]
        if "const" in schema and value != schema["const"]:
            errors.append(f"{pointer}:const")
        if "enum" in schema and value not in schema["enum"]:
            errors.append(f"{pointer}:enum")
        min_length = schema.get("minLength")
        if min_length is not None and len(value) < min_length:
            errors.append(f"{pointer}:minLength:{min_length}")
        return errors

    return errors


def main() -> int:
    results = []
    for schema_path, fixture_dir in PAIRS:
        schema = load_json(schema_path)
        for fixture_path in sorted(fixture_dir.glob("*.json")):
            relative = fixture_path.relative_to(ROOT).as_posix()
            errors = validate(load_json(fixture_path), schema, "")
            valid = not errors
            expected_valid = EXPECTED[relative]
            results.append(
                {
                    "path": relative,
                    "schema": schema_path.relative_to(ROOT).as_posix(),
                    "valid": valid,
                    "expected_valid": expected_valid,
                    "matches_expected": valid == expected_valid,
                    "errors": sorted(errors),
                }
            )
    summary = {
        "schema_version": "0.1.0-rc1",
        "scope": "schema-conformance",
        "total": len(results),
        "matches": sum(1 for item in results if item["matches_expected"]),
        "mismatches": sum(1 for item in results if not item["matches_expected"]),
        "results": results,
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0 if summary["mismatches"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
