# **LLM Orchestration Service – Requirements Document**

---

## **Abstract / Introduction**

The **LLM Orchestration Service** (proper working title pending) is a framework for custom LLM orchestration logic controlled by chat conversations with users through 
standard third-party OpenAI API clients.

---

## **Core Requirements**

### **1. Simplicity & Scope**

* The architecture must be as simple as possible, but not simpler.
* Do not overdesign or introduce speculative features; YAGNI applies.
* The system should be modular, with clear separation of concerns.

### **2. API Compatibility**

* Must expose endpoints fully compatible with the OpenAI API (including request/response format, error handling, and session identification).
* No non-standard or custom fields are allowed in client-facing payloads.
* Session/context referencing should use only standard OpenAI fields (e.g., `user`) or standard authentication mechanisms.

### **3. Orchestration & Business Logic**

* Support for flexible, evolving business logic (orchestration flows) is required.
* In some orchestration scenarios the system may be stateful (per-session or per-conversation).
* Each orchestration flow is responsible for its own business-specific state and toolset selection.

### **4. Model Routing**

* The `model` field in API requests is the primary selector for orchestration flow and its configuration.
* The value of the `model` field must use a URN (Uniform Resource Name) format, with key/value, order-agnostic segments (e.g., `urn:namespace:key=val:key2=val2`).

### **5. LLM Connectors**

* The system must support multiple LLM backends through isolated, provider-specific connectors.
* Connector selection is made by orchestration logic, as needed
* Configuration for connectors is centralized and declarative (file-based, e.g., YAML/JSON/TOML).

### **6. Tools & Toolsets**

* Tools (discrete callable capabilities) must be defined independently and made available for dynamic selection.
* Toolsets (groupings of tools) are not statically mapped to the model string but are selected and composed dynamically by the orchestration logic, generally for each LLM call.

### **7. Configuration**

* All configuration (connectors, tools, default settings, etc.) must be managed in a structured, declarative, and future-proof manner.
* Configuration files must never contain secrets.

### **8. Secret Storage**

* All secrets (e.g., API keys) **must** be stored in secure files as the primary mechanism.
* Loading secrets from environment variables is allowed only as a fallback for corner cases or compatibility.
* Secrets must never be embedded in application source code or general configuration files.
* Implementation must use well-established, stack-appropriate modules for secret handling; code reuse for security is strongly recommended.

### **9. Session Management**

* Session management (tracking context across requests) is required.
* Session information must be stored server-side and referenced via OpenAI-standard fields (e.g., `user`) or standard authentication.

### **10. Logging & Monitoring**

* Centralized logging is required for observability, audit, and troubleshooting.
* No sensitive data (including secrets) may be logged.

### **11. Template Engine**

* The system should include a component for templating, to support prompt/message construction for orchestration flows.

### **12. Extensibility**

* The design must not forbid the addition of future features (such as databases, advanced dynamic configuration, or multi-tenancy), but must not introduce abstractions for them unless and until there is a real requirement.
