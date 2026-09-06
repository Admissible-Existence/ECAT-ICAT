# ECAT-ICAT

ECAT-ICAT is the Admissible Existence repository for defining human-experience and inter-entity governance constraints before they harden into boundary rules, admissibility decisions, or execution authority.

## Current repository state

Status: **IMPLEMENTATION_COMPLETE_HOSTED_VALIDATED**

The bounded repository implementation and validation stack is complete and has hosted validation evidence recorded in `docs/ECAT_ICAT_MIRROR_HANDOFF.md`. This status does **not** mean theorem proof, runtime execution authority, publication authority, clinical authority, certification, or final admissibility. `Admissible-Existence/AE` remains the final commit-time admissibility resolver where applicable.

The prior `0.1.0-rc1 automated testing active` / `Automated release candidate seed` wording described an earlier repository state and is superseded by the canonical handoff and current validation evidence. Historical RC1 schema/version identifiers remain part of the existing data contract and are not silently rewritten by this documentation update.

## Tri-Form conformance

The repository now exposes a bounded **Tri-Form** conformance layer that binds existing prose, mathematical, and executable/code semantics through the historical source identifiers:

- `ECAT-001`
- `ICAT-001`
- `ECAT-ICAT-001`
- `ECAT-ICAT-002`

The binding is recorded in `formalism/triform-counterpart-inventory.json` and `formalism/triform-manifest.json` and checked by `tools/validate_triform_manifest.py` plus `tests/test_triform_manifest.py`. It reuses existing schemas, examples, validators, round-trip evidence, completeness receipts, and the existing `.github/workflows/rc1-validation.yml`; it is not a replacement source formalism or a second validation control plane.

Proof-candidate maturity remains bounded exactly as recorded by the source:

- `ECAT-PC-001` — `tested_candidate`
- `ICAT-PC-001` — `tested_candidate`
- `ECAT-ICAT-PC-001` — `bounded_candidate`

Candidate status is not universal proof. Tri-Form validation is **validation-only** and has `NONE_VALIDATION_ONLY` authority effect.

## Assumptions and vocabulary

This repository uses the following working meanings:

- **ECAT** — Emotional / Experiential Constraint Analysis.
- **ICAT** — Interpersonal / Intuitive Constraint Analysis.
- **BCAT** — Boundary Constraint Analysis.
- **GCAT** — Governance Constraint Analysis.
- **Admissibility** — whether a transition, claim, artifact, relationship, boundary, or state may carry standing under declared governance conditions.
- **Continuity** — whether a state, identity, claim, artifact, relationship, or proof path remains reconstructable across a boundary.
- **Standing** — the current admissible status of a transition, claim, state, or relationship at the moment it is evaluated.

Earlier ECAT/ICAT phrasing treated ECAT as external continuity and ICAT as internal continuity. That reading is superseded for this repository. External/internal continuity may still appear in proof-path discussions, but this repository's canonical focus is the emotional, experiential, interpersonal, and intuitive origin of governance constraints.

## Core distinction

| Layer | Question | Expected output |
| --- | --- | --- |
| ECAT | Is the entity's declared internal/experiential state sufficiently reconstructable to support later boundary analysis? | Experiential standing profile |
| ICAT | Are the inter-entity conditions sufficiently reconstructable to support later trust, delegation, witness, consent, or shared-meaning analysis? | Relational standing profile |
| BCAT | Can the boundary remain recoverable without inverting the purpose of the system? | Boundary admissibility profile |
| GCAT | Does governance authority exist now for the proposed transition? | `ALLOW`, `DENY`, or `FAIL-CLOSED` |

In shorthand:

```text
ECAT / ICAT -> BCAT -> GCAT -> AE commit-time resolution where applicable
```

The arrows denote dependency/carriage, not transfer of authority.

## Mathematical boundary

`docs/MATHEMATICAL_NOTATION.md` defines bounded experiential and interaction standing profiles and structural validity predicates. Within this repository:

```text
authority(E) = authority(I) = 0
reconstructable(q) != authority_now(q)
```

An observed, reconstructed, or replayed historical profile does not create present execution authority. ECAT/ICAT evidence remains pre-boundary support and does not replace downstream BCAT/GCAT/AE commit-time standing.

## Automated validation

The canonical workflow is `.github/workflows/rc1-validation.yml`. It runs the existing profile, expected-output, schema-conformance, receipt, management, consumer, GCAT/BCAT intake, release-readiness, completion, and principle-completeness checks. Tri-Form validation and tests are integrated into this same workflow rather than creating a duplicate control plane.

The deterministic profile fixture baseline remains:

```text
total fixtures: 4
valid fixtures: 2
invalid fixtures: 2
expected comparison: expected_match
```

The canonical handoff records hosted validation run/job `31147813783` / `92770919160` as successful for the completed source implementation. New Tri-Form work must establish its own exact-head hosted validation before merge; prior hosted evidence is not reused as proof of a later head.

## Historical principle semantics

`ECAT-001` — Declared experiential standing may inform later governance but cannot itself grant execution authority.

`ICAT-001` — Relational standing requires reconstructable declared entities, interaction context, shared-understanding context, and recoverability; intuition alone is not proof.

`ECAT-ICAT-001` — ECAT/ICAT outputs are pre-boundary support inputs and do not replace BCAT, GCAT, or final AE commit-time standing.

`ECAT-ICAT-002` — Missing required coherence, consent, entity, context, recoverability, or evidence references must not be promoted to authoritative `ALLOW`; malformed or incomplete required input remains fail-closed under the bounded contract.

## Minimum profile fields

An ECAT profile declares an entity identifier, context, declared experience, coherence status, recoverability status, boundary relevance, validity window, limitations, and receipt reference.

An ICAT profile declares the entities involved, interaction context, declared relationship context, shared-understanding status, trust relevance, recoverability status, boundary relevance, validity window, limitations, and receipt reference.

The canonical schemas are `schemas/ecat-profile.schema.json` and `schemas/icat-profile.schema.json`.

## Existing implementation and evidence

The repository preserves and reuses:

- positive and negative ECAT/ICAT fixtures;
- ECAT/ICAT -> BCAT -> GCAT round-trip examples;
- profile schemas and deterministic validators;
- `tools/validate_profiles.py` and the existing validation/check tools;
- `formalism/principle-registry.yaml`, `formalism/dependency-graph.yaml`, and `formalism/proof-candidates.yaml`;
- `reports/ecat-icat-principle-completeness-validation.json`;
- management, consumer, handoff, activation, readiness, and completion records;
- the canonical `.github/workflows/rc1-validation.yml` hosted validation lane.

Tri-Form adds binding and drift-detection metadata around these existing surfaces; it does not duplicate or replace them.

## Safety and non-authority posture

ECAT-ICAT does not claim to provide psychological diagnosis, emotional surveillance legitimacy, universal truth determination, certification of people or relationships, blanket relationship authority, or execution authority by itself.

The bounded system must remain non-authoritative or fail closed when required evidence is missing, stale, contradictory, or unreconstructable; when coercion or consent conditions cannot be resolved under the applicable policy; when intuition is treated as proof without supporting context; or when historical standing is substituted for current commit-time authority.

No ECAT/ICAT output may silently bypass downstream standing evaluation. No Tri-Form validation result promotes candidate mathematics into theorem proof, grants runtime authority, or creates publication/release authority.

## Relationship to Triad and commit-time governance

Triad-style governance separates proposal, commitment, and reconstruction. ECAT/ICAT operate before the commit-time decision hardens into authority. They help preserve the human and relational conditions that later boundary and governance systems must evaluate, constrain, or fail closed around.

The critical commit-time question remains:

```text
Does authority exist now, at the boundary where the transition would touch reality?
```

Emotional state, intuition, trust, relationship continuity, prior review, external evidence, and internal coherence may support that evaluation, but none automatically replace it.

## Validation commands

```bash
python3 tools/validate_profiles.py
python3 tools/check_expected.py
python3 tools/check_schema_conformance.py
python3 tools/check_receipt_generation.py
python3 tools/check_management_intake.py
python3 tools/check_consumer_execution_plan.py
python3 tools/check_consumer_acceptance_record.py
python3 tools/check_management_handoff.py
python3 tools/verify_gcat_bcat_intake.py
python3 tools/check_release_ready.py
python tools/validate_principle_completeness.py
python tools/validate_triform_manifest.py
python -m unittest tests/test_triform_manifest.py
```

## Release, publication, and reuse boundary

Repository implementation completeness and hosted validation do not themselves create a formal publication, ecosystem release, or runtime activation. Any downstream publication, release, Site/Publisher/wiki propagation, or Master Records transition requires separately admitted destination-owned work and its own evidence.

A repository license exists in `LICENSE`; third-party reuse remains subject to that license and the documented semantic/authority boundaries.
