#!/usr/bin/env python3
"""Compare RC1 validation data against the expected report without subprocess use."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import validate_profiles  # noqa: E402

EXPECTED = ROOT / "tests" / "expected" / "rc1_validation_report.json"


def build_actual() -> dict:
    paths = sorted((ROOT / "examples").glob("ecat/*.json")) + sorted((ROOT / "examples").glob("icat/*.json"))
    results = [validate_profiles.validate_path(path) for path in paths]
    return {
        "invalid": sum(1 for item in results if not item["valid"]),
        "results": results,
        "schema_version": "0.1.0-rc1",
        "total": len(results),
        "valid": sum(1 for item in results if item["valid"]),
    }


def main() -> int:
    actual = build_actual()
    expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
    if actual != expected:
        print("expected_mismatch")
        print(json.dumps({"actual": actual, "expected": expected}, indent=2, sort_keys=True))
        return 1
    print("expected_match")
    return 0


if __name__ == "__main__":
    sys.exit(main())
