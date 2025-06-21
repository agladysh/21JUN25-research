# Concrete Test Scenarios

Document status: Concrete test scenarios that prove all 12 components work together

**Scope**: Mainline scenarios only - these are the primary happy-path flows that guide implementation and prove the system works. Error cases and edge cases are secondary.

## Test Scenario 1: Echo Flow with URN Parameters

**Purpose**: Prove basic orchestration pipeline with URN parameter parsing and prompt templating

**Request example**:
```json
POST /v1/chat/completions
{
  "model": "urn:mvp:test-echo:prefix=System says",
  "messages": [{"role": "user", "content": "Hello world"}]
}
```

**Expected behavior**:
1. API handler parses OpenAI request
2. Router extracts `test-echo` from URN and parses `prefix=System says` parameter
3. Echo logic receives prefix parameter, loads "echo-tools" toolset
4. Template engine builds system prompt: "Call echo tool with user message, prepend with: System says"
5. Claude calls echo(text: "System says Hello world")
6. Tool returns "System says Hello world"
7. Claude returns echo result
8. Response formatted as OpenAI completion

**Components verified**: API handler, router, URN parsing, orchestration logic, toolsets, tools, LLM connector, config, secrets, logging, templates (covers 11 of 12 components - missing auth)

## Test Scenario 2: Introspection Flow with Different Toolset

**Purpose**: Prove different orchestration logic and toolset selection works

**Request example**:
```json
POST /v1/chat/completions  
{
  "model": "urn:mvp:test-introspect",
  "messages": [{"role": "user", "content": "What flows are available?"}]
}
```

**Expected behavior**:
1. Router routes to introspect logic (different from echo)
2. Introspect logic loads "introspection-tools" toolset (different toolset)
3. Claude instructed to call list_orchestration_flows()
4. Tool returns ["test-echo", "test-introspect"]
5. Claude reports available flows

**Components verified**: Different routing, different toolset selection, introspection tools execution

## Success Criteria

Test scenarios are complete when they collectively prove all 12 components integrate and work as a system, using our defined test orchestration flows and tools.