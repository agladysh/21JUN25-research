# Architecture Clarifications

Document status: Key insights and terminology refinements from design discussions

## URN Structure Refinement

**Format**: `urn:mvp:<ol-id>:<ol-specific-params>`

**Examples**:
- `urn:mvp:echo:enhancement=helpful`
- `urn:mvp:debug:verbose=true` 
- `urn:mvp:coder:path=/workspace/myproject:tools=filesystem`

**Benefits**:
- Router only needs to parse `<ol-id>` to select orchestration logic
- Each OL defines and parses its own parameter format
- Clean separation of concerns, extensible design

## State Management Clarification

**Eliminated concept**: Traditional "session management"
**Replaced with**:

### 1. Authentication Session
- Handled by HTTP/API layer (standard auth mechanisms)
- Not framework concern

### 2. Conversation 
- IS the conversation history (OpenAI messages array)
- Managed by client, passed in requests
- No server-side conversation state needed

### 3. Workspace Context
- Working directory path, environment settings, project scope
- Encoded in URN parameters: `path=/workspace/myproject`
- Similar to Claude Code's working directory concept

### 4. Orchestration State
- Persisted on filesystem: files created/modified, logs, artifacts, work in progress
- Each orchestration logic manages its own state via filesystem operations
- Common for development/coding workflows
- Not all OLs need filesystem access

## Component Architecture Update

**Removed**: Session Management component
**Updated**: Component 9 becomes "Workspace & Orchestration State"
- Workspace context from URN parsing
- Filesystem-based state persistence
- Working directory management

## Testing Implications

- Test workspace isolation (different paths)
- Test filesystem state persistence
- Test URN parameter parsing by orchestration logic
- No need for traditional session state testing