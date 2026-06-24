# RC1 Artifact List

## Purpose

This document declares the release-candidate files covered by automated validation and receipt generation.

## Included files

- README.md
- RELEASE_CANDIDATE.md
- LICENSE
- docs/glossary.md
- docs/schema-boundaries.md
- docs/release-candidate-0.1.0-rc1.md
- docs/release-notes-0.1.0-rc1.md
- docs/receipt-plan.md
- docs/receipt-automation.md
- schemas/ecat-profile.schema.json
- schemas/icat-profile.schema.json
- examples/ecat/pass_declared_experience_recoverable.json
- examples/ecat/fail_missing_recoverability.json
- examples/icat/pass_shared_understanding_recoverable.json
- examples/icat/fail_missing_entities.json
- examples/round-trip/ecat-to-bcat-to-gcat.json
- examples/round-trip/icat-to-bcat-to-gcat.json
- examples/existence/percent-existence-example.json
- tests/expected/rc1_validation_report.json
- tests/expected/rc1_release_ready_report.json
- tests/expected/rc1_schema_conformance_report.json
- tests/README.md
- tools/validate_profiles.py
- tools/check_expected.py
- tools/check_schema_conformance.py
- tools/check_release_ready.py
- iosnoperiod/github/workflows/rc1-validation.yml
- iosnoperiod/README.md

The canonical workflow path is excluded from this displayed list because it begins with a leading period. The canonical workflow is still validated by the release-readiness checker.
