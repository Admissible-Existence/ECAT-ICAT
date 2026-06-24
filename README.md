# ECAT-ICAT

ECAT-ICAT is the Admissible Existence repository for defining and testing the boundary between external continuity claims and internal continuity standing.

This repository is currently a formalism seed. Its purpose is to make the ECAT/ICAT boundary explicit before implementation, automation, or downstream publication depends on it.

## Assumptions

This README uses the following working definitions until this repository contains a canonical vocabulary file:

- **ECAT** means **External Continuity Admissibility Test**.
- **ICAT** means **Internal Continuity Admissibility Test**.
- **Admissibility** means a transition, claim, artifact, or state is allowed to carry standing under declared governance conditions.
- **Continuity** means a state, identity, claim, artifact, or proof path remains reconstructable across a boundary.
- **Standing** means the current authority of a transition or claim at the moment it is evaluated.

If the canonical ecosystem vocabulary changes, update this README and add a glossary entry before adding test fixtures.

## Purpose

ECAT-ICAT exists to separate two different questions that are often incorrectly merged:

1. **External continuity question:** Can an outside artifact, claim, receipt, witness, or system output be admitted into the ecosystem?
2. **Internal continuity question:** Once admitted, does that artifact, claim, receipt, witness, or system output retain standing inside the ecosystem?

A transition may pass one side and fail the other.

For example:

- An external artifact may be reconstructable but not internally authoritative.
- An internal state may be coherent but fail when compared against external evidence.
- A claim may be historically valid but lack commit-time standing.
- A proof path may be visible but still inadmissible.

## Core distinction

| Boundary | Question | Expected result |
| --- | --- | --- |
| ECAT | Is the external input admissible for ecosystem consideration? | `ALLOW`, `DENY`, or `FAIL-CLOSED` |
| ICAT | Does the internally represented state retain admissible standing? | `ALLOW`, `DENY`, or `FAIL-CLOSED` |
| ECAT → ICAT | Does admitted external material preserve standing after internal transformation? | Deterministic continuity result |
| ICAT → ECAT | Can internal state be exposed externally without overstating authority? | Bounded claim result |

## Intended role in the ecosystem

This repository should support:

- admissibility testing for external claims before they enter internal governance paths;
- internal standing checks before execution, publication, or delegation;
- proof-path separation between observation, review, authority, and commitment;
- explicit fail-closed behavior when continuity cannot be reconstructed;
- comparison between external frameworks and StegVerse-style commit-time admissibility;
- vocabulary alignment across Admissible Existence, StegVerse, Standing-Proof-Engine, and related governance repos.

## Non-goals

This repository does not claim to provide:

- certification of external systems;
- endorsement of third-party frameworks;
- universal truth determination;
- runtime execution authority by itself;
- replacement of policy, delegation, receipt, or manifest layers;
- private evaluation results unless explicitly scoped by a separate agreement.

## Minimal model

An ECAT/ICAT evaluation should preserve this shape:

```text
input or state
  → declared boundary
  → referenced policy
  → referenced authority
  → referenced evidence
  → continuity reconstruction
  → admissibility decision
  → receipt
```

The decision must not be inferred from visibility, review, animation, intent, or historical approval alone.

## Decision vocabulary

Use the same high-level result vocabulary across ECAT and ICAT:

| Result | Meaning |
| --- | --- |
| `ALLOW` | The claim, artifact, state, or transition is admissible under the declared scope. |
| `DENY` | The claim, artifact, state, or transition is not admissible under the declared scope. |
| `FAIL-CLOSED` | The evaluator cannot establish enough standing to allow the transition. |

A partial failure should not become execution authority unless a policy explicitly defines that partial state as allowable.

## Suggested repository structure

The repository is intentionally small today. As it develops, use this structure unless a more specific implementation requirement emerges:

```text
/
  README.md
  docs/
    glossary.md
    boundary-model.md
    ecat.md
    icat.md
    ecat-to-icat.md
    icat-to-ecat.md
  schemas/
    ecat-request.schema.json
    icat-request.schema.json
    admissibility-result.schema.json
    receipt.schema.json
  examples/
    ecat/
    icat/
    round-trip/
  tests/
    fixtures/
    expected/
  tools/
    validate_ecat.py
    validate_icat.py
```

## Minimum request fields

An ECAT request should declare:

- external source;
- claim or artifact identifier;
- evidence references;
- provenance references;
- scope;
- policy reference;
- authority reference;
- validity window;
- requested admissibility class;
- recoverability profile.

An ICAT request should declare:

- internal state identifier;
- transition identifier;
- actor;
- target;
- requested action;
- policy reference;
- delegation reference;
- evidence references;
- execution context;
- validity window;
- recoverability profile.

## Done criteria for first formal release

The first formal release should be considered complete only when the repository includes:

- canonical glossary;
- ECAT request schema;
- ICAT request schema;
- shared admissibility result schema;
- at least one passing ECAT fixture;
- at least one failing ECAT fixture;
- at least one passing ICAT fixture;
- at least one failing ICAT fixture;
- one ECAT → ICAT round-trip example;
- one ICAT → ECAT bounded-claim example;
- deterministic validator output;
- receipt examples for `ALLOW`, `DENY`, and `FAIL-CLOSED`.

## Current status

Status: **Formalism seed**

The current repository state is sufficient for vocabulary anchoring and README-level scope definition, but not yet sufficient for schema validation, automated testing, or release claims.

## Safety posture

ECAT-ICAT should fail closed when:

- policy cannot be resolved;
- authority cannot be reconstructed;
- evidence references are missing or stale;
- provenance is ambiguous;
- internal transformation changes the claim without a declared boundary;
- external publication would imply broader standing than the evaluation supports.

## Relationship to commit-time admissibility

ECAT-ICAT should be treated as boundary support for commit-time admissibility, not as a replacement for it.

The critical question remains:

```text
Does authority still exist now, at the boundary where the transition would touch reality?
```

Historical review, prior approval, external evidence, and internal coherence can support that answer, but none of them automatically replace a commit-time standing determination.

## License

No license is declared in this README. Add a repository license before encouraging third-party reuse.

## Maintainer note

This repository should stay narrow.

Do not let ECAT become a general external validation brand, and do not let ICAT become a blanket internal approval mechanism. Their value is in preserving the boundary between external admissibility and internal standing.
