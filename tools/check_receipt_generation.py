#!/usr/bin/env python3
"""Confirm RC1 receipt automation documentation is present."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    ROOT / "docs" / "receipt-plan.md",
    ROOT / "docs" / "receipt-automation.md",
    ROOT / "docs" / "rc1-artifact-list.md",
]


def main() -> int:
    missing = [path.relative_to(ROOT).as_posix() for path in REQUIRED if not path.exists()]
    if missing:
        print("receipt_generation_not_ready")
        for item in missing:
            print(item)
        return 1
    print("receipt_generation_documented")
    return 0


if __name__ == "__main__":
    sys.exit(main())
