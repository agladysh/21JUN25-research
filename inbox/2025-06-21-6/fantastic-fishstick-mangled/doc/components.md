# **LLM Orchestration Service – Component Overview**

Document status: Working component specifications with cross-references (evolving).

## **1. OpenAI API Protocol Handler**

* **Responsibility:**
  Handles all incoming and outgoing HTTP traffic according to the OpenAI API standard.
  Parses requests, validates payloads, extracts session/context info, manages response formatting and error handling. Extracts URN from model field and routes to Orchestration Logic Router (Component 5). Extracts auth headers for Authentication & Authorization (Component 12). Distributes session context to User Session Management (Component 9a), workspace parameters to Workspace Context Management (Component 9b), and conversation data to Conversation Session Management (Component 9c).
  
  **Error Handling**: Uses simple crash behavior for MVP - if it crashes, it dies. No complex error recovery or transformation. OpenAI error format compliance is nice-to-have, not required for prototype.

## **2. LLM Connectors**

* **Responsibility:**
  Isolated adapters for interacting with various LLM providers (e.g., OpenAI, Ollama, local models).
  Handles request/response translation, authentication, and provider-specific features.

## **3. Tools**

* **Responsibility:**
  Discrete callable capabilities or plugins (e.g., function calls, calculators, knowledge base lookups) available for orchestration logic.

## **4. Toolsets**

* **Responsibility:**
  Collections of tools, selected and composed dynamically by orchestration logic for each LLM call as required.
  Not statically mapped to the `model` string or client request.

## **5. Orchestration Logic Router**

* **Responsibility:**
  Selects the appropriate orchestration logic implementation for each request based on the `model` URN (received from OpenAI API Protocol Handler - Component 1) and possibly other session/context data.
  
  **URN Structure**: `urn:mvp:<ol-id>:<ol-specific-params>`
  - Router parses `<ol-id>` to select orchestration logic
  - Each OL defines and parses its own `<ol-specific-params>`
  - Clean separation of concerns, extensible without changing router

## **6. Orchestration Logic**

* **Responsibility:**
  Implements custom business logic flows (orchestration flows).

## **7. Configuration Manager**

* **Responsibility:**
  Loads, merges, and validates all declarative configuration (connectors, tools, toolsets, settings).
  Ensures future-proof, structured, and secure configuration management.

## **8. Secrets Management**

* **Responsibility:**
  Securely loads and provides access to sensitive values (API keys, tokens) from files as the primary source, with environment variables as a fallback.
  Ensures no secrets are exposed in logs or configs.
  
  **Multiple Secret Types**:
  - **Connector API keys**: Anthropic API key for Claude connector
  - **User credentials**: Authentication tokens/credentials (implementation TBD)
  
  **Fallback Chain**: Check environment variable → load from file (path in config) → fail with clear error

## **9. Session Management Components**

This section describes several distinct components concerning state and context management.

### **9a. User Session Management**

* **Responsibility:**
  Manages user identity context and usage tracking within requests. Receives session context from OpenAI API Protocol Handler (Component 1) and validated user identity from Authentication & Authorization (Component 12). Provides user context to orchestration logic. Tracks usage accumulation per user across requests and handles billing integration. Enables OL-specific pricing models, usage rules, and billing policies.

### **9b. Workspace Context Management**

* **Responsibility:**
  Manages OL-specific workspace context. Receives workspace parameters from OpenAI API Protocol Handler (Component 1) via URN parameters in OL-determined format. Examples:
  - `urn:mvp:test-echo:workspace=/path/to/project`
  - `urn:company:coder:repo=github.com/user/project:branch=main`
  - `urn:personal:assistant:workspace=/home/user/documents`
  
  Framework parses URN parameters and provides workspace context to orchestration logic. Each OL defines its own workspace parameter format and interpretation.

### **9c. Conversation Session Management**

* **Responsibility:**
  Manages conversation state persistence for orchestration logic. Receives conversation data from OpenAI API Protocol Handler (Component 1). The conversation IS the request (message array). Storage is OL-specific (YAML files in workspace, database, etc.). Framework provides APIs for OLs to store/retrieve conversation-scoped state between requests. Job identification handled by OL (e.g., agent emits "I spawned a job for you: <job>{id}</job>" and manages job-to-conversation mapping). Framework facilitates but doesn't prescribe conversation state management approach.

## **10. Logging & Monitoring**

* **Responsibility:**
  Provides centralized, structured logging and monitoring for observability, auditing, and troubleshooting.
  Enforces that no sensitive data (including secrets) are ever logged.
  
  **Implementation Approach**: Use established dependency, avoid NIH syndrome. Select appropriate logging library rather than building from scratch.

## **11. Template Engine**

* **Responsibility:**
  Enables prompt/message construction for orchestration flows.
  (Selection and complexity of the engine are implementation details, not architectural requirements.)
  
  **Implementation Approach**: Use established dependency, avoid NIH syndrome. Select appropriate templating library rather than building from scratch.

## **12. Authentication & Authorization**

* **Responsibility:**
  Provides authentication and authorization infrastructure for the framework. Receives auth headers from OpenAI API Protocol Handler (Component 1). Manages shared operational concerns (token validation, rate limiting, access control) while supporting OL-specific policies. Handles user credential validation and determines what resources users can access. Provides validated user identity to User Session Management (Component 9a). Provides APIs for orchestration logic to define custom access rules and user namespaces. Balances operational scalability (shared auth infrastructure) with business flexibility (OL-specific access policies).
