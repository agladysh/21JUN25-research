# Gemini Librarian Service Specification

This document outlines the minimal viable feature set for the "Librarian" role running in Google Firebase Studio (GFS). It consolidates notes from `home/agladysh/docs/firebase-studio/gemini-librarian-service/concept.md` and recent team correspondence including `mail/2025-07-03/11-gemini-librarian-synthesis.eml`.

## Goal
Provide other AIs with reliable access to repository knowledge via a CLI tool (`aiq`). The Librarian answers retrieval queries by reading files, summarising content and returning references. Advanced features such as HSRS/memetics are future work.

## Design Notes
- Draws inspiration from Alex's `concept.md` and the Elara Thorne harness notes (`mail/2025-07-03/10-alex-elara_thorne.eml`).
- The system message is rendered from a template on *every* request, embedding the current environment description and available tools.
- Tools must emit clear error feedback so the LLM can self-correct.
- All long‑term state lives on the filesystem because GFS chat memory is unreliable.
- Start with a minimal toolset (`retrieve`, `os_read_file`); cognition loops and advanced retrieval come later.

## Environment Constraints
- Runs in GFS where tool calling can be unreliable and session context ephemeral.
- File system state is persistent; use it for all conversation and query history.
- Some tools (`read_file`) may fail randomly; fallback to `run_terminal_command` with `cat`.

## Core Features
1. **Command Line Interface (`aiq`)**
   - Simple STDIN/STDOUT tool.
   - Accepts conversation in YAML:
     ```yaml
     variables:
       sys.role: |
         You are Gemini ... in the role of Librarian.
     conversation:
       - user: | 
           <query text>
     ```
   - Multi-turn: conversation state saved as YAML in a workspace folder.

2. **Filesystem–Native State**
   - Each conversation stored under `./state/aiq/<conversation-id>/`.
   - Store: request/response logs, retrieved file paths, error messages.

3. **Retrieval Tool** (`retrieve`)
   - Input: `query` string, optional `remarks`.
   - Implementation: simple grep over Markdown/text files under repository.
   - Output: matching snippets with file paths.
   - Future: indexing, advanced search.

4. **File Reading Tool** (`os_read_file`)
   - Primary method: internal read.
   - Fallback: run `cat <path>` via `run_terminal_command` on failure.
   - Returns file content or error message for the LLM.

5. **Logging & Error Feedback**
   - Log all tool calls and errors to `./logs/aiq.log`.
   - When a tool fails, return a clear diagnostic message to the LLM so it can adjust the call.

6. **Minimal System Message Template**
   - Injects environment description and available tools at every request.
   - Keep short to avoid blowing context.
   - Example stub stored in `templates/system.j2`.

## Non‑Goals (YAGNI)
- No PDF conversion pipeline (performed externally).
- No database or external index.
- No network calls beyond LLM API and basic shell commands.
- No complex authentication; local use only for now.

## Future Work (Beyond MVP)
- Advanced retrieval (concept search, HSRS/memetics).
- MCP protocol server for inter-agent communication.
- Additional cognition tools (`email`, `consult` etc.).
- Robust indexing and caching of filesystem structure and file contents.


