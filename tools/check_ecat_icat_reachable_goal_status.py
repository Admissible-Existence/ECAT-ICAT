from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "docs" / "ECAT_ICAT_REACHABLE_GOAL_STATUS.md"
required = [
    "repo: ECAT-ICAT",
    "formalism: ECAT / ICAT",
    "reachable_goal: rc1_automated_testing_state_recorded",
    "state: ready",
    "manual_tasks_remaining: false",
    "release_candidate: false",
    "rc1_automated_testing: active",
    "total_fixtures: 4",
    "valid_fixtures: 2",
    "invalid_fixtures: 2",
    "expected_comparison: expected_match",
    "normal_validation_manual_dependency: false",
    "status_record_only: true",
    "creates_authority: false",
    "commits_execution: false",
    "claims_final_cross_repo_validity: false",
]
ok = path.exists()
if ok:
    text = path.read_text(encoding="utf-8")
    for term in required:
        if term not in text:
            print(f"missing: {term}")
            ok = False
else:
    print("missing: docs/ECAT_ICAT_REACHABLE_GOAL_STATUS.md")
print("valid: ECAT-ICAT reachable goal status" if ok else "ECAT-ICAT reachable goal status check failed")
raise SystemExit(0 if ok else 1)
