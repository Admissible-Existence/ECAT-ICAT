# ECAT-ICAT

ECAT-ICAT is the Admissible Existence repository for defining the human-experience and inter-entity layers of governance constraints before they harden into boundary rules, admissibility decisions, or execution authority.

This repository is currently a formalism seed. Its purpose is to preserve the distinction between emotional/experiential standing, interpersonal/intuitive standing, boundary recoverability, and governance admissibility before implementation, automation, or downstream publication depends on it.

## Assumptions

This README uses the following working definitions until this repository contains canonical vocabulary files:

- **ECAT** means **Emotional / Experiential Constraint Analysis**.
- **ICAT** means **Interpersonal / Intuitive Constraint Analysis**.
- **BCAT** means **Boundary Constraint Analysis**.
- **GCAT** means **Governance Constraint Analysis**.
- **Admissibility** means a transition, claim, artifact, relationship, boundary, or state is allowed to carry standing under declared governance conditions.
- **Continuity** means a state, identity, claim, artifact, relationship, or proof path remains reconstructable across a boundary.
- **Standing** means the current admissible status of a transition, claim, state, or relationship at the moment it is evaluated.

Earlier ECAT/ICAT phrasing treated ECAT as external continuity and ICAT as internal continuity. That reading is now superseded for this repository. External/internal continuity may still appear in proof-path discussions, but this repository's canonical focus is the emotional, experiential, interpersonal, and intuitive origin of governance constraints.

## Purpose

ECAT-ICAT exists to separate two questions that are often skipped or compressed into later governance decisions:

1. **ECAT question:** What is happening inside the entity before governance is applied?
2. **ICAT question:** What is happening between entities before a boundary or authority claim is formed?

This matters because emotional state, intuition, perception, coherence, trust, relationship continuity, and shared understanding can affect whether a proposed transition should ever become admissible.

A governance system that ignores ECAT/ICAT may still produce clean-looking decisions while missing the human and relational conditions that made the boundary unstable, coercive, unrecoverable, or purpose-inverting.

## Core distinction

| Layer | Question | Expected output |
| --- | --- | --- |
| ECAT | Is the entity's internal state coherent enough to support a boundary or transition claim? | Experiential standing profile |
| ICAT | Are the inter-entity conditions coherent enough to support trust, delegation, witness, consent, or shared meaning? | Relational standing profile |
| BCAT | Can the boundary remain recoverable without inverting the purpose of the system? | Boundary admissibility profile |
| GCAT | Does governance authority exist now for the proposed transition? | `ALLOW`, `DENY`, or `FAIL-CLOSED` |

In shorthand:

```text
ECAT / ICAT -> BCAT -> GCAT
```

Meaning:

```text
experience and intuition -> boundary formation -> governance admissibility
```

## Relationship to Triad governance

Triad governance distinguishes proposal, commitment, and reconstruction:

| Component | Core question | Function |
| --- | --- | --- |
| Transition Governance | Can this transition be considered? | Determines whether a proposed state change is structurally valid. |
| Admissibility Governance | Can this transition be committed now? | Determines whether execution authority exists at the moment of commitment. |
| Continuity Governance | Can this transition be reconstructed later? | Determines whether the decision path remains replayable, receipt-bound, and independently reviewable. |

ECAT/ICAT operate before the triad's commit-time decision hardens into authority. They help explain why a transition may look valid at the structural level while remaining unstable, coercive, unrecoverable, or inadmissible once human and relational constraints are examined.

## Existence interpretation

The expression:

```text
GCAT / BCAT : ECAT / ICAT : %Existence
```

is a governed existence formulation.

`%Existence` is not merely whether something can be observed. It is the degree to which an entity, relationship, claim, transition, or state can be treated as existing under the relevant governance frame.

A stronger existence claim requires alignment across:

- **ECAT:** internal coherence, emotional standing, experiential standing, and meaning;
- **ICAT:** relational coherence, trust, intuition, witness standing, and inter-entity continuity;
- **BCAT:** boundary recoverability, constraint integrity, and non-inversion;
- **GCAT:** governance standing, policy, delegation, authority, and admissibility.

For commit-time effects, missing or failed layers should fail closed unless a policy explicitly defines a safe partial-standing condition.

## Minimal model

An ECAT/ICAT evaluation should preserve this shape:

```text
entity or interaction
  -> declared context
  -> experiential state
  -> relational state
  -> boundary condition
  -> recoverability profile
  -> admissibility relevance
  -> continuity notes
  -> receipt or record
```

The result must not be inferred from visibility, review, intent, historical approval, or external appearance alone.

## Intended role in the ecosystem

This repository should support:

- vocabulary for emotional and experiential constraint analysis;
- vocabulary for interpersonal and intuitive constraint analysis;
- modeling of how human state affects boundary formation;
- modeling of how relationship state affects trust, consent, delegation, witness standing, and shared meaning;
- comparison between human-governance constraints and later admissibility decisions;
- fail-closed treatment when coherence, recoverability, or authority cannot be reconstructed;
- alignment across Admissible Existence, StegVerse, Standing-Proof-Engine, Triad governance, and related governance repos.

## Non-goals

This repository does not claim to provide:

- psychological diagnosis;
- emotional surveillance;
- universal truth determination;
- certification of people, relationships, or external systems;
- endorsement of third-party frameworks;
- runtime execution authority by itself;
- replacement of policy, delegation, receipt, manifest, or commit-time admissibility layers;
- private evaluation results unless explicitly scoped by a separate agreement.

## Decision vocabulary

ECAT/ICAT do not directly grant execution authority. They produce standing profiles that may support later BCAT/GCAT evaluation.

When ECAT/ICAT output is carried into admissibility evaluation, use the same high-level result vocabulary:

| Result | Meaning |
| --- | --- |
| `ALLOW` | The claim, state, relationship, boundary, or transition is admissible under the declared scope. |
| `DENY` | The claim, state, relationship, boundary, or transition is not admissible under the declared scope. |
| `FAIL-CLOSED` | The evaluator cannot establish enough standing to allow the transition. |

A partial ECAT/ICAT failure should not become execution authority unless a policy explicitly defines that partial state as allowable.

## Suggested repository structure

The repository is intentionally small today. As it develops, use this structure unless a more specific implementation requirement emerges:

```text
/
  README.md
  docs/
    glossary.md
    ecat.md
    icat.md
    boundary-model.md
    existence-model.md
    triad-governance.md
  schemas/
    ecat-profile.schema.json
    icat-profile.schema.json
    existence-profile.schema.json
    admissibility-relevance.schema.json
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

## Minimum ECAT profile fields

An ECAT profile should declare:

- entity identifier;
- context;
- observed or declared internal state;
- emotional/experiential indicators;
- coherence notes;
- intuition or perception notes;
- recoverability profile;
- boundary relevance;
- evidence or witness references, if applicable;
- validity window;
- limitations;
- receipt reference.

## Minimum ICAT profile fields

An ICAT profile should declare:

- entities involved;
- relationship or interaction context;
- trust/delegation/consent relevance;
- shared-understanding notes;
- intuition or interpersonal signal notes;
- continuity notes;
- boundary relevance;
- recoverability profile;
- evidence or witness references, if applicable;
- validity window;
- limitations;
- receipt reference.

## Done criteria for first formal release

The first formal release should be considered complete only when the repository includes:

- canonical glossary;
- ECAT profile schema;
- ICAT profile schema;
- shared existence/admissibility relevance schema;
- at least one ECAT example;
- at least one ICAT example;
- one ECAT -> BCAT -> GCAT example;
- one ICAT -> BCAT -> GCAT example;
- one `%Existence` example;
- deterministic validator output;
- receipt examples for `ALLOW`, `DENY`, and `FAIL-CLOSED` when ECAT/ICAT output is carried into admissibility evaluation.

## Current status

Status: **Formalism seed**

The current repository state is sufficient for README-level vocabulary anchoring and scope definition, but not yet sufficient for schema validation, automated testing, or release claims.

## Safety posture

ECAT-ICAT should fail closed or remain non-authoritative when:

- coercion cannot be ruled out;
- consent is ambiguous;
- emotional state is being used to override agency;
- intuition is treated as proof without supporting context;
- relationship standing is asserted but not reconstructable;
- a boundary remains enforceable only while an operator is coherent;
- maintaining the boundary blocks convergence to the intended state;
- evidence references are missing or stale;
- authority cannot be reconstructed;
- external publication would imply broader standing than the evaluation supports.

## Relationship to commit-time admissibility

ECAT-ICAT should be treated as pre-boundary support for commit-time admissibility, not as a replacement for it.

The critical question remains:

```text
Does authority still exist now, at the boundary where the transition would touch reality?
```

Emotional state, intuition, trust, relationship continuity, prior review, external evidence, and internal coherence can support that answer, but none of them automatically replace a commit-time standing determination.

## License

No license is declared in this README. Add a repository license before encouraging third-party reuse.

## Maintainer note

This repository should stay narrow.

Do not let ECAT become emotional surveillance, and do not let ICAT become a blanket relationship-authority mechanism. Their value is in preserving the pre-boundary human and inter-entity conditions that later governance systems must either respect, constrain, or fail closed around.
