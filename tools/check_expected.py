#!/usr/bin/env python3
"""Compare RC1 validation data against the expected report."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import validate_profiles  # noqa: E402

EXPECTED = ROOT / "tests" / "expected" / "rc1_validation_report.json"


def main() -> int:
    actual = validate_profiles.build_summary()
    expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
    if actual != expected:
        print("expected_mismatch")
        print(json.dumps({"actual": actual, "expected": expected}, indent=2, sort_keys=True))
        return 1
    print("expected_match")
    return 0


if __name__ == "__main__":
    sys.exit(main())
