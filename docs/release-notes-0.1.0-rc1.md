# Release Notes: 0.1.0-rc1

## Status

Status: **release candidate automation active**

RC1 establishes the first formal ECAT/ICAT testing scaffold.

## Scope

This release candidate defines ECAT/ICAT as:

- **ECAT**: Emotional / Experiential Constraint Analysis
- **ICAT**: Interpersonal / Intuitive Constraint Analysis

RC1 keeps ECAT/ICAT as pre-boundary governance records. They do not grant execution authority by themselves.

## Included

- ECAT profile schema
- ICAT profile schema
- passing and failing ECAT fixtures
- passing and failing ICAT fixtures
- deterministic fixture validator
- expected-output comparison
- schema-conformance checker
- release-readiness checker
- `%Existence` example
- ECAT -> BCAT -> GCAT example
- ICAT -> BCAT -> GCAT example
- CI workflow for automated validation
- iOS no-period workflow mirror
- MIT license

## Automated checks

The RC1 workflow runs:

```bash
python3 tools/validate_profiles.py
python3 tools/check_expected.py
python3 tools/check_schema_conformance.py
python3 tools/check_release_ready.py
```

## Non-authority statement

A passing ECAT or ICAT profile means the record is structurally valid for review. It does not mean the transition is allowed to affect reality.

## Remaining before formal release

- artifact receipt hashing
- optional GitHub release/tag publication
