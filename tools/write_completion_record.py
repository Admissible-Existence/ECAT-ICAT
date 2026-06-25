#!/usr/bin/env python3
"""Write a machine-readable RC1 completion record for workflow artifacts."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "completion" / "rc1-completion-record.json"


def main() -> int:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema_version": "0.1.0",
        "repo": "Admissible-Existence/ECAT-ICAT",
        "record_type": "rc1_completion_record",
        "management_entrypoint": "MANAGEMENT_INTAKE.json",
        "consumer_contract": "CONSUMER_CONTRACT.json",
        "consumer_plan": "CONSUMER_EXECUTION_PLAN.json",
        "consumer_acceptance": "CONSUMER_ACCEPTANCE_RECORD.json",
        "receipt_artifact": "rc1-artifact-receipts",
        "receipt_file": "receipts/rc1-artifact-receipts.sha256",
        "manual_validation_required": False,
        "next_state": "complete_without_manual_action"
    }
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("completion_record_written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
