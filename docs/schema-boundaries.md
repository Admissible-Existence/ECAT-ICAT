# Schema Boundaries

## Purpose

RC1 schemas are intentionally narrow. They validate declared governance records only. They do not attempt to measure, infer, diagnose, surveil, or certify human experience or relationships.

## What ECAT schema validates

The ECAT schema validates that an experiential governance profile declares:

- schema version;
- profile identifier;
- ECAT layer marker;
- entity identifier;
- context;
- declared experience;
- coherence status;
- recoverability status;
- boundary relevance;
- validity window;
- limitations;
- receipt identifier.

## What ICAT schema validates

The ICAT schema validates that an inter-entity governance profile declares:

- schema version;
- profile identifier;
- ICAT layer marker;
- entities;
- interaction context;
- declared relationship context;
- shared-understanding status;
- trust relevance;
- recoverability status;
- boundary relevance;
- validity window;
- limitations;
- receipt identifier.

## What the schemas do not validate

The schemas do not validate:

- whether a person's feelings are true;
- whether a relationship is healthy;
- whether trust is deserved;
- whether consent exists beyond the declared record;
- whether execution authority exists;
- whether a claim is externally true;
- whether later publication is authorized.

## Commit-time boundary

RC1 records may support later BCAT/GCAT review, but they do not replace commit-time admissibility.

The governance boundary remains:

```text
ECAT / ICAT -> BCAT -> GCAT
```

A valid ECAT or ICAT profile means the record is structurally valid for review. It does not mean the transition is allowed to affect reality.
