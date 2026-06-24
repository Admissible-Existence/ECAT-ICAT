# Release Candidate Status

## Current candidate

Version: `0.1.0-rc1`

Status: **automated testing and receipt publication active**

## Automated validation

RC1 validation now runs through GitHub Actions on:

- push to `main`;
- pull request;
- workflow dispatch.

Workflow path: `github/workflows/rc1-validation.yml`

Note: the workflow path above is displayed without the leading period for iOS compatibility. The canonical repository path begins with a leading period.

## Validation commands

The workflow runs:

```bash
python3 tools/validate_profiles.py
python3 tools/check_expected.py
python3 tools/check_schema_conformance.py
python3 tools/check_receipt_generation.py
python3 tools/check_release_ready.py
```

The workflow then generates and uploads:

```text
receipts/rc1-artifact-receipts.sha256
```

as the `rc1-artifact-receipts` workflow artifact.

## Current pass condition

The release candidate is internally consistent when:

- `tools/validate_profiles.py` reports 4 fixtures, 2 valid, and 2 invalid;
- `tools/check_expected.py` reports `expected_match`;
- `tools/check_schema_conformance.py` reports 4 matches and 0 mismatches;
- `tools/check_receipt_generation.py` reports `receipt_generation_documented`;
- `tools/check_release_ready.py` reports `release_ready: true`;
- README, glossary, schema boundary notes, examples, expected output, and release notes agree on RC1 vocabulary;
- the RC1 validation workflow completes successfully;
- the workflow publishes the `rc1-artifact-receipts` artifact.

## Included proof artifacts

- `docs/glossary.md`
- `docs/schema-boundaries.md`
- `docs/release-candidate-0.1.0-rc1.md`
- `docs/receipt-plan.md`
- `docs/receipt-automation.md`
- `docs/rc1-artifact-list.md`
- `docs/release-notes-0.1.0-rc1.md`
- `docs/license-decision.md`
- `docs/release-plan.md`
- `schemas/ecat-profile.schema.json`
- `schemas/icat-profile.schema.json`
- `examples/ecat/pass_declared_experience_recoverable.json`
- `examples/ecat/fail_missing_recoverability.json`
- `examples/icat/pass_shared_understanding_recoverable.json`
- `examples/icat/fail_missing_entities.json`
- `examples/round-trip/ecat-to-bcat-to-gcat.json`
- `examples/round-trip/icat-to-bcat-to-gcat.json`
- `examples/existence/percent-existence-example.json`
- `tests/expected/rc1_validation_report.json`
- `tests/expected/rc1_release_ready_report.json`
- `tests/expected/rc1_schema_conformance_report.json`
- `tests/README.md`
- `tools/validate_profiles.py`
- `tools/check_expected.py`
- `tools/check_schema_conformance.py`
- `tools/check_receipt_generation.py`
- `tools/check_release_ready.py`
- `github/workflows/rc1-validation.yml`
- `iosnoperiod/github/workflows/rc1-validation.yml`
- `iosnoperiod/README.md`
- `LICENSE`

Note: any path above that corresponds to a canonical leading-period repository path is displayed without the leading period for iOS compatibility.

## Manual task reduction

Manual validation is no longer required for normal repo changes. A push or pull request now invokes profile validation, expected-output comparison, schema-conformance checking, receipt-readiness checking, release-readiness structure checking, and receipt artifact publication automatically.

## Release blockers remaining

Before formal release, the repo still needs:

- optional GitHub release/tag publication after workflow success.
