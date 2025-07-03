# Gemini Librarian Service: Test Plan

This document outlines automated and manual tests for the `aiq` CLI. It expands on the brief notes in `implementation-plan.md`.

## 1. Unit Tests

Use `pytest` for unit tests.

- **`retrieve()`**
  - Works with sample Markdown files in `tests/fixtures/`.
  - Verifies snippets include correct paths and line numbers.
  - Simulate no matches to ensure graceful empty results.
- **`os_read_file()`**
  - Reads an existing file and returns its content.
  - Simulates a read error (e.g. permission denied) and checks fallback to `cat`.

## 2. Integration Test

A simple test exercising the whole CLI:

1. Create a temporary directory with fixture files and `state/`.
2. Pipe a YAML conversation to `cli.py` requesting a file summary.
3. Assert that the output contains expected text and that logs/state are written.
4. Run the command twice to confirm conversation persistence.

## 3. Manual Testing

- Interact with `aiq` directly in a shell. Ensure conversations continue across invocations.
- Test in a minimal GFS-like environment where tool calls occasionally fail to verify error handling.

## 4. Running Tests

```
$ pip install -r requirements.txt
$ pytest
```

If `pytest` is unavailable in CI, run tests manually before committing.
