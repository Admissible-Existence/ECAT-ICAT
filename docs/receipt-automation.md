# Receipt Automation

## Purpose

RC1 artifact hashing is handled by the validation workflow instead of a local receipt-generation script.

## Automated path

The workflow hashes the declared RC1 artifact set during CI and writes the result to:

```text
receipts/rc1-artifact-receipts.sha256
```

The workflow then uploads that file as the `rc1-artifact-receipts` workflow artifact.

## Hash scope

The current workflow hashes files under:

```text
README.md
RELEASE_CANDIDATE.md
LICENSE
docs/
schemas/
examples/
tests/
tools/
iosnoperiod/
```

The canonical workflow file is excluded from the generated receipt because it is the generator of the receipt and includes the receipt-generation instructions. The workflow itself remains covered by the release-readiness structure check.

## Boundary

The receipt artifact is generated at validation time. It is not committed back into the repository because committing generated hashes would require a second mutation cycle after every content change.

## Canonical workflow path

Workflow path: `github/workflows/rc1-validation.yml`

Note: the workflow path above is displayed without the leading period for iOS compatibility. The canonical repository path begins with a leading period.
