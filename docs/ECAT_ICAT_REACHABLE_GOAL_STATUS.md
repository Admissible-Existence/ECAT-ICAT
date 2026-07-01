# ECAT-ICAT Reachable Goal Status

```text
repo: ECAT-ICAT
formalism: ECAT / ICAT
reachable_goal: rc1_automated_testing_state_recorded
state: ready
manual_tasks_remaining: false
release_candidate: false
```

## Ready Surfaces

```text
README.md
RELEASE_CANDIDATE.md
docs/glossary.md
docs/schema-boundaries.md
docs/release-candidate-0.1.0-rc1.md
docs/receipt-plan.md
schemas/ecat-profile.schema.json
schemas/icat-profile.schema.json
examples/ecat/pass_declared_experience_recoverable.json
examples/ecat/fail_missing_recoverability.json
examples/icat/pass_shared_understanding_recoverable.json
examples/icat/fail_missing_entities.json
examples/round-trip/ecat-to-bcat-to-gcat.json
examples/round-trip/icat-to-bcat-to-gcat.json
examples/existence/percent-existence-example.json
tools/validate_profiles.py
tools/check_expected.py
tests/expected/rc1_validation_report.json
iosnoperiod/README.md
iosnoperiod/github/workflows/rc1-validation.yml
```

## Current Integration State

```text
rc1_automated_testing: active
total_fixtures: 4
valid_fixtures: 2
invalid_fixtures: 2
expected_comparison: expected_match
normal_validation_manual_dependency: false
canonical_focus: emotional_experiential_interpersonal_intuitive_constraints
```

## Boundary

```text
status_record_only: true
creates_authority: false
commits_execution: false
claims_final_cross_repo_validity: false
```

## Next Repo Step

```text
next_step: inspect validators, schemas, and expected report before changing RC1 behavior; otherwise proceed to the next Admissible-Existence repo using the same handoff-first pattern.
```
