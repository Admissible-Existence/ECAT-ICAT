#!/usr/bin/env python3
"""Check that ecosystem management handoff files exist and parse."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    ROOT / "GOAL_ACTIVATION.v2.json",
    ROOT / "HANDOFF_PACKET.json",
    ROOT / "docs" / "ecosystem-management-handoff.md",
]
JSON_FILES = FILES[:2]


def main() -> int:
    missing = [path.relative_to(ROOT).as_posix() for path in FILES if not path.exists()]
    invalid_json = []
    for path in JSON_FILES:
        if path.exists():
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                invalid_json.append(path.relative_to(ROOT).as_posix())
    ready = not missing and not invalid_json
    print(json.dumps({
        "schema_version": "0.1.0",
        "scope": "ecosystem-management-handoff",
        "ready": ready,
        "missing": missing,
        "invalid_json": invalid_json
    }, indent=2, sort_keys=True))
    return 0 if ready else 1


if __name__ == "__main__":
    sys.exit(main())
