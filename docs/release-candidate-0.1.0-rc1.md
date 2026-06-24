# ECAT-ICAT Release Candidate 0.1.0-rc1

## Status

Status: **Release candidate seed**

This release candidate begins formal testing for the ECAT/ICAT governance formalism. It is not a certification framework, diagnostic system, or runtime execution-authority engine.

## Assumptions

- ECAT means Emotional / Experiential Constraint Analysis.
- ICAT means Interpersonal / Intuitive Constraint Analysis.
- ECAT/ICAT outputs are pre-boundary governance records.
- ECAT/ICAT outputs do not grant execution authority by themselves.
- BCAT/GCAT or another commit-time admissibility process must still determine whether authority exists at the moment reality would be touched.

## Done definition for this release candidate

This release candidate is complete when the repository contains:

- one ECAT schema;
- one ICAT schema;
- one passing ECAT fixture;
- one failing ECAT fixture;
- one passing ICAT fixture;
- one failing ICAT fixture;
- one deterministic validator;
- one expected validation report;
- README instructions explaining how to run the check.

## Validation command

Run from the repository root:

```bash
python3 tools/validate_profiles.py
```

Expected result:

- total fixtures: 4
- valid fixtures: 2
- invalid fixtures: 2
- process exit code: 0 when the expected pass/fail balance is preserved

## Current fixtures

| Fixture | Layer | Expected result | Reason |
| --- | --- | --- | --- |
| `examples/ecat/pass_declared_experience_recoverable.json` | ECAT | valid | Declares required experience, coherence, recoverability, boundary relevance, limits, and receipt. |
| `examples/ecat/fail_missing_recoverability.json` | ECAT | invalid | Intentionally omits `recoverability_status`. |
| `examples/icat/pass_shared_understanding_recoverable.json` | ICAT | valid | Declares required interaction context, shared understanding, recoverability, boundary relevance, limits, and receipt. |
| `examples/icat/fail_missing_entities.json` | ICAT | invalid | Intentionally omits `entities`. |

## Safety boundary

The RC1 test harness treats ECAT/ICAT as declared governance records. It does not infer private mental state, diagnose people, surveil emotions, or convert interpersonal context into authority.

Any later implementation must preserve the same boundary:

```text
ECAT / ICAT -> BCAT -> GCAT
```

Meaning:

```text
experience and relationship context -> boundary formation -> governance admissibility
```

## Release blocker list

The release candidate should not become a formal release until the repo adds:

- canonical glossary;
- schema comparison notes explaining what the schemas intentionally do not measure;
- fixture provenance receipts;
- `%Existence` example;
- ECAT -> BCAT -> GCAT example;
- ICAT -> BCAT -> GCAT example;
- automated comparison of validator output against `tests/expected/rc1_validation_report.json`.
