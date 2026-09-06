#!/usr/bin/env python3
import json
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "formalism/triform-manifest.json"
INVENTORY = ROOT / "formalism/triform-counterpart-inventory.json"
PRINCIPLES = ROOT / "formalism/principle-registry.yaml"
PROOF_CANDIDATES = ROOT / "formalism/proof-candidates.yaml"
README = ROOT / "README.md"
EXPECTED_IDS = ["ECAT-001", "ICAT-001", "ECAT-ICAT-001", "ECAT-ICAT-002"]
EXPECTED_PC = {
    "ECAT-PC-001": "tested_candidate",
    "ICAT-PC-001": "tested_candidate",
    "ECAT-ICAT-PC-001": "bounded_candidate",
}


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    findings = []
    manifest = load_json(MANIFEST)
    inventory = load_json(INVENTORY)
    principles = yaml.safe_load(PRINCIPLES.read_text(encoding="utf-8"))
    proof = yaml.safe_load(PROOF_CANDIDATES.read_text(encoding="utf-8"))
    readme = README.read_text(encoding="utf-8")

    if manifest.get("goal_id") != "AEX-ECAT-ICAT-TRIFORM-001":
        findings.append("goal_id_mismatch")
    if manifest.get("maturity") != "EXECUTABLY_FORMALIZED":
        findings.append("maturity_mismatch")
    if manifest.get("historical_source_replacement") is not False:
        findings.append("historical_source_replacement_must_be_false")
    if manifest.get("final_cross_repository_validity") is not False:
        findings.append("final_cross_repository_validity_must_be_false")

    authority = manifest.get("authority", {})
    required_authority = {
        "execution_authorized": False,
        "publication_authorized": False,
        "proofs_accepted": False,
        "workflow_authority_effect": "NONE_VALIDATION_ONLY",
        "final_admissibility_authority": "Admissible-Existence/AE",
    }
    for key, value in required_authority.items():
        if authority.get(key) != value:
            findings.append(f"authority_boundary:{key}")

    boundaries = manifest.get("semantic_boundaries", {})
    for key in [
        "experiential_standing_is_execution_authority",
        "relational_standing_is_execution_authority",
        "ecat_icat_replace_commit_time_admissibility",
        "replayed_historical_standing_is_present_authority",
        "missing_required_evidence_is_authoritative_allow",
        "psychological_diagnosis_authority",
        "emotional_surveillance_authority",
        "blanket_relationship_authority",
    ]:
        if boundaries.get(key) is not False:
            findings.append(f"semantic_boundary:{key}")

    manifest_ids = [item.get("id") for item in manifest.get("principles", [])]
    source_ids = [item.get("id") for item in principles.get("principles", [])]
    inventory_ids = [item.get("id") for item in inventory.get("bindings", [])]
    if manifest_ids != EXPECTED_IDS:
        findings.append("manifest_historical_id_drift")
    if source_ids != EXPECTED_IDS:
        findings.append("source_historical_id_drift")
    if inventory_ids != EXPECTED_IDS:
        findings.append("inventory_historical_id_drift")

    source_non_authority = principles.get("non_authority", {})
    for key in ("execution_authorized", "publication_authorized", "proofs_accepted"):
        if source_non_authority.get(key) is not False:
            findings.append(f"source_non_authority_drift:{key}")

    proof_map = {item.get("id"): item.get("maturity") for item in proof.get("candidates", [])}
    manifest_pc = {item.get("id"): item for item in manifest.get("proof_candidates", [])}
    if proof_map != EXPECTED_PC:
        findings.append("source_proof_candidate_maturity_drift")
    for pid, maturity in EXPECTED_PC.items():
        item = manifest_pc.get(pid, {})
        if item.get("maturity") != maturity or item.get("universal_proof") is not False:
            findings.append(f"manifest_proof_candidate_drift:{pid}")

    for binding in inventory.get("bindings", []):
        for form in ("prose", "mathematics", "code", "evidence"):
            paths = binding.get(form, [])
            if not paths:
                findings.append(f"missing_form:{binding.get('id')}:{form}")
            for rel in paths:
                if not (ROOT / rel).exists():
                    findings.append(f"missing_counterpart:{binding.get('id')}:{rel}")

    required_readme_markers = [
        "IMPLEMENTATION_COMPLETE_HOSTED_VALIDATED",
        "Tri-Form",
        "ECAT-001",
        "ICAT-001",
        "ECAT-ICAT-001",
        "ECAT-ICAT-002",
        "tested_candidate",
        "bounded_candidate",
        "validation-only",
    ]
    for marker in required_readme_markers:
        if marker not in readme:
            findings.append(f"readme_reconciliation_missing:{marker}")
    if "Status: **Automated release candidate seed**" in readme:
        findings.append("stale_readme_status_seed")

    result = {
        "schema": "admissible-existence.ecat-icat.triform-validation/v1",
        "goal_id": manifest.get("goal_id"),
        "valid": not findings,
        "principle_count": len(manifest_ids),
        "principle_ids": manifest_ids,
        "proof_candidate_maturity": EXPECTED_PC,
        "authority_effect": "NONE_VALIDATION_ONLY",
        "final_admissibility_authority": "Admissible-Existence/AE",
        "findings": findings,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if not findings else 1)


if __name__ == "__main__":
    main()
