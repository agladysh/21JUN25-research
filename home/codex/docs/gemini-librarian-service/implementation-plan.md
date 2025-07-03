# Gemini Librarian Service: Implementation Plan

This plan assumes development in a Unix-like shell environment (e.g., GFS) with Python 3 available. Adjust paths as needed. It follows design notes in `concept.md` and in the Elara Thorne email (`mail/2025-07-03/10-alex-elara_thorne.eml`).

## 1. Repository Layout
```
/aiq/               # package root
  cli.py            # entry point
  tools.py          # retrieval and file access utilities
  state/            # persistent conversations
  templates/
    system.j2
logs/
  aiq.log
```

## 2. Dependencies
- Python 3.10+
- `PyYAML` for YAML handling
- `jinja2` for templating
- Optional: `rich` for colored CLI output

Install via `pip install -r requirements.txt`.

## 3. CLI Workflow
1. Read YAML from STDIN.
2. Load or create conversation state directory.
3. Render system message from template with tool list and environment info.
4. Invoke Gemini API using provided messages.
5. Save request/response pairs to state directory.
6. Output the LLM reply to STDOUT.

## 4. Tool Implementations
### retrieve(query)
- Use `grep -n` recursively under project root for `.md` and `.txt` files.
- Return snippets with line numbers and paths.
- Log query and number of hits.

### os_read_file(path)
- Try Python `open()` first.
- On failure, run `cat <path>` using `subprocess`.
- Capture stdout/stderr; return content or error string.

## 5. Error Handling
- Wrap all tool executions in try/except.
- If any command fails, record the error message in the conversation state and include it in the LLM response.

## 6. Logging
- Append structured log entries to `logs/aiq.log`:
  `timestamp tool action status message`
- Keep logs short; rotate manually if needed.

## 7. Testing
The Librarian should include a minimal automated test suite.

- **Unit tests** for `retrieve` and `os_read_file` using `pytest`.
- **Integration test** executing `cli.py` on a sample YAML conversation and checking the log files and output.
  - Provide a `tests/fixtures/` directory with small Markdown files.
- Run `pytest` in CI (if available) or manually via `make test`.

Manual E2E testing is still important: interact with `aiq` in a shell and confirm multi-turn state persistence.

## 8. Deliverables
- `aiq` CLI script with minimal features above.
- Example template and configuration files.
- Documentation (`spec.md` and this plan).


