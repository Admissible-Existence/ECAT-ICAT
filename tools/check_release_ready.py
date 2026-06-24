#!/usr/bin/env python3
"""Check whether RC1 has the required release-candidate artifacts."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_PATHS = [
    "README.md",
    "RELEASE_CANDIDATE.md",
    "LICENSE",
    "docs/glossary.md",
    "docs/license-decision.md",
    "docs/rc1-artifact-list.md",
    "docs/receipt-automation.md",
    "docs/schema-boundaries.md",
    "docs/release-candidate-0.1.0-rc1.md",
    "docs/release-notes-0.1.0-rc1.md",
    "docs/release-plan.md",
    "docs/receipt-plan.md",
    "schemas/ecat-profile.schema.json",
    "schemas/icat-profile.schema.json",
    "examples/ecat/pass_declared_experience_recoverable.json",
    "examples/ecat/fail_missing_recoverability.json",
    "examples/icat/pass_shared_understanding_recoverable.json",
    "examples/icat/fail_missing_entities.json",
    "examples/round-trip/ecat-to-bcat-to-gcat.json",
    "examples/round-trip/icat-to-bcat-to-gcat.json",
    "examples/existence/percent-existence-example.json",
    "tests/expected/rc1_validation_report.json",
    "tests/expected/rc1_release_ready_report.json",
    "tests/expected/rc1_schema_conformance_report.json",
    "tests/README.md",
    "tools/validate_profiles.py",
    "tools/check_expected.py",
    "tools/check_schema_conformance.py",
    "tools/check_receipt_generation.py",
    "tools/check_release_ready.py",
    ".github/workflows/rc1-validation.yml",
    "iosnoperiod/github/workflows/rc1-validation.yml",
    "iosnoperiod/README.md",
]


def main() -> int:
    missing = [path for path in REQUIRED_PATHS if not (ROOT / path).exists()]
    status = {
        "schema_version": "0.1.0-rc1",
        "required_count": len(REQUIRED_PATHS),
        "missing_count": len(missing),
        "missing": missing,
        "release_ready": not missing,
        "scope": "rc1-structure-readiness",
    }
    print(json.dumps(status, indent=2, sort_keys=True))
    return 0 if not missing else 1


if __name__ == "__main__":
    sys.exit(main())
