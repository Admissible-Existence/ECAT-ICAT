# Release Candidate Status

## Current candidate

Version: `0.1.0-rc1`

Status: **testing scaffold active**

## Validation commands

```bash
python3 tools/validate_profiles.py
python3 tools/check_expected.py
```

## Current pass condition

The release candidate is internally consistent when:

- `tools/validate_profiles.py` reports 4 fixtures, 2 valid, and 2 invalid;
- `tools/check_expected.py` reports `expected_match`;
- README, glossary, schema boundary notes, examples, and expected output agree on RC1 vocabulary.

## Included proof artifacts

- `docs/glossary.md`
- `docs/schema-boundaries.md`
- `docs/release-candidate-0.1.0-rc1.md`
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
- `tools/validate_profiles.py`
- `tools/check_expected.py`

## Release blockers remaining

Before formal release, the repo still needs:

- fixture receipt hashes;
- schema validation against full JSON Schema instead of the minimal standard-library subset;
- CI workflow or documented manual verification receipt;
- tagged release notes;
- license decision.
