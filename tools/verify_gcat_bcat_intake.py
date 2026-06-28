#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INTAKE = ROOT / "integration" / "gcat-bcat-cost-intake.json"
OUT = ROOT / "tests" / "expected" / "gcat_bcat_intake_result.json"
REQUIRED_TERMS = ["C_g", "p_bad", "r", "recoverability", "FAIL-CLOSED"]


def main():
    data = json.loads(INTAKE.read_text(encoding="utf-8"))
    terms = data.get("mapped_terms", [])
    missing = [term for term in REQUIRED_TERMS if term not in terms]
    ok = not missing and data.get("source_repository") == "Admissible-Existence/GCAT-BCAT"
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"intake_id": data.get("intake_id"), "result": "PASS" if ok else "FAIL", "missing": missing}, indent=2) + "\n", encoding="utf-8")
    if ok:
        print("PASS GCAT BCAT intake")
        return 0
    print("FAIL GCAT BCAT intake", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
