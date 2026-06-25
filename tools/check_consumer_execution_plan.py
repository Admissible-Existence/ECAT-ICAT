#!/usr/bin/env python3
"""Check that the consumer execution plan exists and parses."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "CONSUMER_EXECUTION_PLAN.json"


def main() -> int:
    errors = []
    if not PLAN.exists():
        errors.append("missing_plan")
        payload = {}
    else:
        try:
            payload = json.loads(PLAN.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            payload = {}
            errors.append("invalid_json")
    if payload.get("entrypoint") != "MANAGEMENT_INTAKE.json":
        errors.append("invalid_entrypoint")
    if payload.get("manual_actions_required") != []:
        errors.append("manual_actions_present")
    if len(payload.get("steps", [])) < 5:
        errors.append("insufficient_steps")
    result = {"ready": not errors, "errors": errors, "scope": "consumer-execution-plan"}
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["ready"] else 1


if __name__ == "__main__":
    sys.exit(main())
