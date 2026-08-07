#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "ecat-icat-principle-completeness-validation.json"

REQUIRED = [
    "formalism/principle-registry.yaml",
    "formalism/dependency-graph.yaml",
    "formalism/proof-candidates.yaml",
    "docs/WHOLE_REPO_THEORY_MAP.md",
    "docs/MATHEMATICAL_NOTATION.md",
    "docs/FALSIFICATION_AND_LIMITS.md",
    "README.md",
    "schemas/ecat-profile.schema.json",
    "schemas/icat-profile.schema.json",
    "tools/validate_profiles.py",
    "tests/expected/rc1_validation_report.json",
    "docs/ECAT_ICAT_MIRROR_HANDOFF.md",
]
EXPECTED_IDS = {"ECAT-001", "ICAT-001", "ECAT-ICAT-001", "ECAT-ICAT-002"}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    findings = []
    missing = [p for p in REQUIRED if not (ROOT / p).is_file()]
    if missing:
        findings.append({"code": "MISSING_REQUIRED_SURFACE", "paths": missing})

    try:
        registry = yaml.safe_load((ROOT / "formalism/principle-registry.yaml").read_text()) or {}
        graph = yaml.safe_load((ROOT / "formalism/dependency-graph.yaml").read_text()) or {}
        candidates = yaml.safe_load((ROOT / "formalism/proof-candidates.yaml").read_text()) or {}
    except Exception as exc:
        findings.append({"code": "YAML_PARSE_FAILURE", "detail": str(exc)})
        registry, graph, candidates = {}, {}, {}

    principles = registry.get("principles", []) if isinstance(registry, dict) else []
    ids = {p.get("id") for p in principles if isinstance(p, dict)}
    if ids != EXPECTED_IDS:
        findings.append({"code": "PRINCIPLE_ID_MISMATCH", "actual": sorted(x for x in ids if x), "expected": sorted(EXPECTED_IDS)})

    non_authority = registry.get("non_authority", {}) if isinstance(registry, dict) else {}
    for key in ("execution_authorized", "publication_authorized", "proofs_accepted"):
        if non_authority.get(key) is not False:
            findings.append({"code": "AUTHORITY_BOUNDARY_FAILURE", "field": key, "actual": non_authority.get(key)})

    graph_paths = {v.get("path") for v in (graph.get("nodes", {}) or {}).values() if isinstance(v, dict)} if isinstance(graph, dict) else set()
    for path in ("schemas/ecat-profile.schema.json", "schemas/icat-profile.schema.json", "tools/validate_profiles.py", "tests/expected/rc1_validation_report.json"):
        if path not in graph_paths:
            findings.append({"code": "DEPENDENCY_GRAPH_MISSING_CANONICAL_NODE", "path": path})

    candidate_rows = candidates.get("candidates", []) if isinstance(candidates, dict) else []
    if len(candidate_rows) < 3:
        findings.append({"code": "PROOF_CANDIDATE_COUNT_TOO_LOW", "actual": len(candidate_rows)})

    try:
        expected = json.loads((ROOT / "tests/expected/rc1_validation_report.json").read_text())
        actual_shape = (expected.get("total"), expected.get("valid"), expected.get("invalid"))
        if actual_shape != (4, 2, 2):
            findings.append({"code": "RC1_EXPECTED_SHAPE_DRIFT", "actual": actual_shape, "expected": (4, 2, 2)})
    except Exception as exc:
        findings.append({"code": "EXPECTED_REPORT_PARSE_FAILURE", "detail": str(exc)})

    input_hashes = {p: sha256(ROOT / p) for p in REQUIRED if (ROOT / p).is_file()}
    report = {
        "schema_version": "1.0.0",
        "goal_id": "ECAT-ICAT-PRINCIPLE-COMPLETENESS-001",
        "repository": "Admissible-Existence/ECAT-ICAT",
        "expected_principle_count": 4,
        "principle_count": len(principles),
        "findings": findings,
        "valid": not findings,
        "execution_authorized": False,
        "publication_authorized": False,
        "proofs_accepted": False,
        "input_sha256": input_hashes,
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if not findings else 1


if __name__ == "__main__":
    raise SystemExit(main())
