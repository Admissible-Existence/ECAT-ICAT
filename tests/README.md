# Tests

## RC1 validation

Run from the repository root:

```bash
python3 tools/validate_profiles.py
```

Expected summary:

```text
total: 4
valid: 2
invalid: 2
```

## Expected-output comparison

Run:

```bash
python3 tools/check_expected.py
```

Expected output:

```text
expected_match
```

## Scope

These tests validate structural governance records only. They do not grant execution authority or prove external truth.
