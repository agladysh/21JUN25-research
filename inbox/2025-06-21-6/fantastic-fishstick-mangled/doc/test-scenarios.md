# MVP Test Scenarios

Document status: Testing requirements and mainline scenarios

## Testing Requirements per Component

What proves each component is implemented:

1. **OpenAI API Protocol Handler**: Valid OpenAI chat completion request gets parsed correctly and returns valid OpenAI response format
2. **LLM Connectors**: Claude API gets called with correct parameters and response is received 
3. **Tools**: Tool functions execute and return expected results when invoked
4. **Toolsets**: Different toolsets get selected based on orchestration logic
5. **Orchestration Logic Router**: Different URN model values route to different orchestration flows
6. **Orchestration Logic**: Each flow executes its specific logic and produces different outputs
7. **Configuration Manager**: YAML config gets loaded and parsed into usable configuration
8. **Secrets Management**: 
   - Claude API key loaded via fallback chain: env var → file (path in config) → failure
   - API key successfully used for Claude API authentication
   - Config file contains no sensitive data
9. **Workspace & Orchestration State**: 
   - Workspace context (working directory, environment) encoded in URN
   - Orchestration state persisted on filesystem (files, logs, artifacts)
   - No traditional "session management" needed for MVP
10. **Logging & Monitoring**: System events get logged in structured format
11. **Template Engine**: Prompt templates get processed with variables to generate final prompts

## Secrets Management Details (MVP)

**Purpose**: Load Claude API key securely
**Fallback chain**:
1. Check environment variable (e.g., `CLAUDE_API_KEY`)
2. If not found, load from file (path specified in config, e.g., `secrets.claude_api_key_file`)
3. If file not found, fail with clear error

**Testing**: API calls succeed with key loaded correctly, config remains clean of sensitive data

## Mainline Test Scenarios

These scenarios drive implementation and prove the system works end-to-end:

### Scenario 1: Different Orchestration Flows
- Send request with `urn:mvp:flow=echo` → verify echo enhancement behavior
- Send request with `urn:mvp:flow=debug` → verify debug info with tools
- Verify different outputs prove routing works

### Scenario 2: Tool Selection by Orchestration
- Echo flow uses "test-utilities" toolset
- Debug flow uses "system-info" toolset  
- Verify correct tools available in each context

### Scenario 3: Workspace Context & State Persistence
- Send request with workspace path in URN: `urn:mvp:coder:path=/workspace/test`
- Verify orchestration logic operates in correct working directory
- Verify filesystem state persists between requests (files created, modified)
- Verify different workspace paths remain isolated

### Scenario 4: System Observability
- Process requests while monitoring logs
- Verify structured logging captures key events
- Verify no sensitive data appears in logs