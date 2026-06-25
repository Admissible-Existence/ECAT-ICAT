#!/usr/bin/env python3
"""Check that the consumer acceptance record exists and parses."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "CONSUMER_ACCEPTANCE_RECORD.json"


def main() -> int:
    errors = []
    if not RECORD.exists():
        errors.append("missing_record")
        payload = {}
    else:
        try:
            payload = json.loads(RECORD.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            payload = {}
            errors.append("invalid_json")
    if payload.get("entrypoint") != "MANAGEMENT_INTAKE.json":
        errors.append("invalid_entrypoint")
    if payload.get("manual_validation_required") is not False:
        errors.append("manual_validation_not_false")
    if "complete_without_manual_action" not in payload.get("accepted_next_states", []):
        errors.append("missing_complete_state")
    result = {"ready": not errors, "errors": errors, "scope": "consumer-acceptance-record"}
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["ready"] else 1


if __name__ == "__main__":
    sys.exit(main())
