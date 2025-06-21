# MVP Implementation Decisions

Document status: Working notes for implementation decisions

## Testing Strategy

**Primary approach**: Black box testing
- Test OpenAI API compatibility end-to-end
- Other testing types (unit, integration) used where they add specific value
- Focus on verifying the service behaves correctly from external perspective
- Success criteria: Concrete test scenarios that prove the 12 components work together as a system

## Error Handling Philosophy

**MVP approach**: Simple crash behavior
- If it crashes, it dies
- No complex error recovery or transformation for MVP
- OpenAI error format compliance is nice-to-have, not required for prototype
- Test basic error cases: missing config, invalid URN, missing secrets

## Architecture Philosophy

**Configuration vs Description**:
- Orchestration logic should be described in code (simple functions) rather than configured through complex data structures
- Simpler implementation preferred over flexible configuration for MVP

**Dependencies**:
- Use established libraries where appropriate to avoid unhealthy NIH syndrome
- Key dependency categories: OpenAI-compatible server framework, config parsers, secret management

## MVP Scope (Preliminary)

**Core Principle**: Implement minimal version of all 12 components with testability in mind

### Component Implementations

1. **OpenAI API Protocol Handler** - Chat completions endpoint only
2. **LLM Connectors** - Claude API connector (one connector)
3. **Tools** - Test-oriented tools:
   - For test-echo: echo(text: string) - returns input text unchanged
   - For test-introspect: list_toolsets(), list_orchestration_flows(), describe_toolset(toolset_id: string), describe_orchestration_flow(orchestration_flow_id: string)
4. **Toolsets** - Two sets for testing selection:
   - "echo-tools" toolset: contains echo tool
   - "introspection-tools" toolset: contains the 4 introspection tools
5. **Orchestration Logic Router** - Parse URN format and route to logic
6. **Orchestration Logic** - Two flows for testing routing:
   - `urn:mvp:test-echo` - System prompt instructs LLM to call echo(text) tool with user's message, LLM returns exactly what tool returns. Tests: tool calling pipeline, parameter passing, function calling integration.
   - `urn:mvp:test-introspect` - System prompt instructs LLM to call introspection tools and report framework state. Tests: different toolset selection, system introspection, framework validation.
7. **Configuration Manager** - YAML config loading
8. **Secrets Management** - File-based secret storage with fallback chain for multiple secret types:
   - **Connector API keys**: Anthropic API key for Claude connector
   - **User credentials**: TBD - research Open Web UI auth mechanism
   - Fallback chain: Check environment variable → load from file (path in config) → fail with clear error
9. **Session Management Components** - 
   - 9a. User Session Management: User identity context, usage tracking, billing
   - 9b. Workspace Context Management: OL-specific workspace context via URN parameters  
   - 9c. Conversation Session Management: OL-specific conversation state persistence
10. **Logging & Monitoring** - Use established dependency, no NIH
11. **Template Engine** - Use established dependency, no NIH
12. **Authentication & Authorization** - Auth infrastructure with OL-specific policies

### Design Philosophy
- Tools should be useful for testing the system itself
- Need multiple flows/toolsets to test routing logic
- Use good dependencies for logging and templating rather than building from scratch

## URN Structure (Refined)

**Format**: `urn:mvp:<ol-id>:<ol-specific-params>`
- Router parses `<ol-id>` to select orchestration logic
- Each OL defines and parses its own `<ol-specific-params>`
- Clean separation of concerns, extensible without changing router

## Key Architectural Simplifications

**Eliminated concepts**:
- Traditional "session management" - replaced with workspace context + filesystem state
- Complex error boundaries - MVP uses simple crash behavior
- Speculative features - build only what's needed for testing framework

**Clarified concepts**:
- **Conversation** = OpenAI message history (client-managed)
- **Workspace context** = working directory, environment (URN-encoded)
- **Orchestration state** = filesystem artifacts (files, logs, work products)
- **Authentication** = handled by HTTP/API layer, not framework concern

## Outstanding Decisions

1. **Tech Stack Selection** (Todo: tech-stack)
   - Primary language/runtime (Node.js/TypeScript implied by .gitignore?)
   - OpenAI-compatible server framework options
   - Configuration parsing libraries
   - Secret management libraries
   - Logging and templating dependencies

2. **Session Management Strategy** (Completed)
   - Implemented as Session Management Components (9a/9b/9c)
   - Eliminated traditional session management in favor of component-based approach