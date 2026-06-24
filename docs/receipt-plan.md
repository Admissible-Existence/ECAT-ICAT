# Receipt Plan

## Purpose

RC1 needs receipt hashes before it can move from testing scaffold to formal release candidate.

## Receipt targets

Each release candidate should record hashes for:

- schemas;
- examples;
- validator tools;
- expected reports;
- release notes.

## Minimum receipt record

A receipt record should include:

```json
{
  "schema_version": "0.1.0-rc1",
  "receipt_id": "receipt-example",
  "artifact_path": "examples/ecat/pass_declared_experience_recoverable.json",
  "hash_method": "sha256",
  "hash": "pending",
  "created_at": "pending",
  "scope": "release-candidate-artifact"
}
```

## RC1 status

Receipt hashing is not yet active. Until hashes are generated, RC1 remains a testing scaffold rather than a fully receipt-bound release candidate.
