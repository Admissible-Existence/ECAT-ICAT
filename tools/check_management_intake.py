#!/usr/bin/env python3
"""Check that the management intake artifact exists and parses."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INTAKE = ROOT / "MANAGEMENT_INTAKE.json"
REQUIRED_KEYS = [
    "schema_version",
    "repo",
    "intake_id",
    "intake_type",
    "goal_file",
    "handoff_file",
    "workflow_file",
    "receipt_artifact_name",
    "required_checks",
    "completion_policy",
    "handoff_ready",
]


def main() -> int:
    errors = []
    if not INTAKE.exists():
        errors.append("missing:MANAGEMENT_INTAKE.json")
        payload = {}
    else:
        try:
            payload = json.loads(INTAKE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            payload = {}
            errors.append("invalid_json:MANAGEMENT_INTAKE.json")
    for key in REQUIRED_KEYS:
        if key not in payload:
            errors.append(f"missing_key:{key}")
    if payload.get("handoff_ready") is not True:
        errors.append("handoff_ready_not_true")
    policy = payload.get("completion_policy", {})
    if policy.get("manual_validation_required") is not False:
        errors.append("manual_validation_required_not_false")
    result = {
        "schema_version": "0.1.0",
        "scope": "management-intake",
        "ready": not errors,
        "errors": errors,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["ready"] else 1


if __name__ == "__main__":
    sys.exit(main())
