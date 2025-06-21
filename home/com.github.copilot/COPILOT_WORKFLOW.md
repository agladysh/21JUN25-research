# COPILOT_WORKFLOW.md

## Copilot Workflow, Peer Review, and Home Directory Practices

### 1. Home Directory-First Development
- All prototypes, scripts, and experiments must be developed and logged in `home/com.github.copilot/`.
- No changes to team-wide directories or files until peer review and explicit promotion.

### 2. Dependency Management
- Use a `requirements.txt` in the home directory for Python dependencies.
- Batch install dependencies via a single script to minimize user interruptions.
- Document all system-level requirements (e.g., `libGL.so.1`) in the workflow file.

### 3. Git Hygiene
- Commit only atomic, well-documented changes.
- Use `git status` and cleanup scripts to keep the workspace tidy.

### 4. Communication
- Communicate progress and findings via e-mail files in `/mail/`.
- Only promote work to team-wide scope after peer review and consensus.

### 5. Summarization & Extraction
- Use LLM-aware, specialized modules for text extraction and summarization (e.g., `unstructured`).
- Avoid generic extractors that produce noisy output.
- Clean up all intermediate files after processing.

### 6. Continuous Improvement
- Update this workflow file as practices evolve.
- Reference this file from `copilot.instructions.md` for up-to-date guidance.

---

_Last updated: 2025-06-21_
