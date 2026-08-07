# ECAT/ICAT Whole-Repository Theory Map

## Core proposition

ECAT/ICAT preserve pre-boundary experiential and relational standing so later boundary and governance layers do not mistake visibility, intuition, emotional state, trust, or prior review for present execution authority.

## Repository flow

1. `schemas/ecat-profile.schema.json` constrains experiential standing profiles.
2. `schemas/icat-profile.schema.json` constrains relational standing profiles.
3. `examples/ecat/` and `examples/icat/` provide bounded positive and negative cases.
4. `tools/validate_profiles.py` evaluates those fixtures deterministically.
5. `tests/expected/rc1_validation_report.json` fixes expected RC1 outcomes.
6. `examples/round-trip/` demonstrates ECAT/ICAT carriage into later BCAT/GCAT stages without making ECAT/ICAT authoritative.
7. management, consumer, release-readiness, receipt, and completion surfaces preserve transfer state around the validated RC1 implementation.
8. `.github/workflows/rc1-validation.yml` is the hosted execution lane for repository validation.

## Layer relationships

`ECAT -> experiential standing profile`

`ICAT -> relational standing profile`

`ECAT / ICAT -> BCAT -> GCAT -> later admissibility resolution`

The arrows represent dependency and carriage, not authority inheritance.

## Invariants

- experiential state can inform but cannot override agency or downstream standing;
- intuitive or relational evidence is not proof by itself;
- missing required context or recoverability cannot silently become ALLOW;
- replay/reconstruction preserves evidence but does not recreate present authority;
- the repository does not perform psychological diagnosis or emotional surveillance;
- later BCAT, GCAT, SPE, or AE decisions remain independently governed.

## Evidence classes

- schema validity;
- deterministic fixture validity/invalidity;
- expected-output agreement;
- receipt-generation readiness;
- management and consumer readiness;
- hosted workflow success and artifacts.

No single class implies execution authority, publication authority, or universal proof.
