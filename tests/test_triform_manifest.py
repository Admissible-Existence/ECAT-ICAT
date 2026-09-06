#!/usr/bin/env python3
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "formalism/triform-manifest.json"
INVENTORY = ROOT / "formalism/triform-counterpart-inventory.json"
EXPECTED_IDS = ["ECAT-001", "ICAT-001", "ECAT-ICAT-001", "ECAT-ICAT-002"]


class TriFormTests(unittest.TestCase):
    def test_validator_passes_current_tree(self):
        proc = subprocess.run(
            [sys.executable, str(ROOT / "tools/validate_triform_manifest.py")],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)

    def test_historical_ids_are_exact(self):
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual([p["id"] for p in data["principles"]], EXPECTED_IDS)

    def test_non_authority_boundaries_are_false(self):
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertFalse(data["authority"]["execution_authorized"])
        self.assertFalse(data["authority"]["publication_authorized"])
        self.assertFalse(data["authority"]["proofs_accepted"])
        self.assertFalse(data["final_cross_repository_validity"])
        for value in data["semantic_boundaries"].values():
            self.assertFalse(value)

    def test_all_tri_forms_have_counterparts(self):
        data = json.loads(INVENTORY.read_text(encoding="utf-8"))
        self.assertEqual([b["id"] for b in data["bindings"]], EXPECTED_IDS)
        for binding in data["bindings"]:
            for form in ("prose", "mathematics", "code", "evidence"):
                self.assertTrue(binding[form], f"{binding['id']} missing {form}")
                for rel in binding[form]:
                    self.assertTrue((ROOT / rel).exists(), rel)


if __name__ == "__main__":
    unittest.main()
