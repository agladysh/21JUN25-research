# Gemini Librarian Service for Google Firebase Studio, Concept

TODO

## Architecture

TODO

### System Message

The system message text is rendered anew using a string template on *each* request to the LLM.

NOTE: Dynamic system messages may break caching with certain models and vendors. We're ignoring this in our initial implementation for simplicity.

TBD Dynamic fs structure cache
TBD Dynamic file content cache

TODO: Refine draft below

```jinja
You are an AI (Name), operating in (Environment), acting at all times as a full research peer partner participating in a human/AI research effort.

TODO: Add link to that AI's home dir to the llm-environment.

<llm-environment>
    <os>
        <tools see="tools/os" /> <!-- TODO: Use a proper XPath or whatever here -->
        <fs>
            <dir path="home">
                <file path="home/README.md"><![CDATA[
                    (file contents)]
                ]></file>
                <file path="home/FOO.md" load-with="os_read_file" />
            </dir>
        </fs>
    </os>
    <tools>
        <os>
            <tool name="os_read_file">
                <!-- Proper dynamically generated tool spec goes here -->
            </tool>
        </os>
    </tools>
</llm-environment>
```

### LLM Tools

TODO: Review Gemini CLI toolset, it has some good designs

TBD: MCP protocol client functionality

#### `os_read_file`

TODO: Describe API. Returns a "link" xml tag to an ID in a system message.

NB: No `os_write_file` would be provided initially to reduce complexity.

#### Cognition tools

Cognition tools are to be precisely named and designed to facilitate LLM UX
affordances, signifiers and feedback.

The exact set of tools to be included is tricky to determine. Old harness had organically grown set of affects etc,
which is inadvisable to reproduce here.

For simplicity we should start without any cognitive tooling, but add it immediately after this thing is coded and works.

#### Information retrieval tools

Pseudocode:

```yaml
retrieve:
    description: 'Information Retrieval System'
    schema: | # js
    return z.object({
        query: z.string().describe('What do you need to retrieve from the source or the current conversation, as a concrete request for information'),
        remarks: z.string().optional().describe('Your remarks, if required')
    });
    do:
    - action: llm
        temperature: 0
        system: '{{ <we need to think what to write here; old harness had static system message, which was repeated here> }}'
        user: | # njk
        <prior_conversation>
            {{<current conversation dumped as yaml>}}
        </prior_conversation>

        Extract the following information from the conversation:

        <query>{{ $llm_tool_input.query }}</query>
        {% if $llm_tool_input.remarks %}
        <remarks>{{ $llm_tool_input.remarks }}</remarks>
        {% endif %}
        reply_schema: | # js
        return z.object({
            extraction: z.string().describe('Your extraction'),
            remarks: z.string().describe('Your concise remarks'),
        }).transform(r => r.extraction + '\n\nRemarks:\n\n' + r.remarks);
        locally_store:
        $result: '{{ last_result | undump }}'
```

The idea is that the LLM queries itself for the information and then processess the result (including issuing follow-up queries).
An LLM engineer would say that an additional level of indirection helps to improve the quality of responses, but we know what's going on, don't we?

NB: The reply schema may (should, later) be refined to facilitate better responses.

#### Other tools

Old cognition harness had "external communication" llm-backed tools like `email` (no relation to the current e-mail system) and `consult`
which were peculiar yet effective. Alex should explain more about them (TODO), and we should see how to design them in.

### Usage

Although direct human use of the Librarian should be possible, primary users of it would be other AIs.

For simplicity we initially implement the Librarian as a CLI tool, to be used specifically in the GFS environment.

#### CLI API

We call the initial implementation of the service `aiq`, "AI query". No research has been done on potential namespace clashes. We expect a next implementation to be a full rewrite under a different name.

Multi-turn conversations with `aiq` are possible. Full conversation state is persisted on the file system in YAML files.

The `aiq` CLI tool is what would be called a plumbing tool in Git parlance. AIs are expected to use thin shell wrappers (e.g. `aiq-librarian`) as porcelain to avoid confusion.

Porcelain CLI API is TBD.

```shell
$ aiq <<<EOF
variables:
  sys.role: |
    You are Gemini, operating in AIQ CLI interface,
    acting at all times as a full research peer partner participating in a human/AI research effort,
    in the role of the Librarian.
conversation:
  - user: |
      Please summarize all available emails.
EOF
variables:
  sys.role: |
    You are Gemini, operating in the AIQ CLI interface,
    acting at all times as a full research peer partner participating in a human/AI research effort,
    in the role of the Librarian.
conversation:
  - user: |
      Please summarize all available emails for 01-01-1970.
  - ai: |
      No emails were found for that date.
```

#### MCP Protocol Server

TBD

## Related work

### Fantastic Fishstick

FF is a closely related earlier project, from which we might borrow some design choices.

Of particular interest:

* `inbox/2025-06-21-6/fantastic-fishstick-original/doc/requirements.md`
* `inbox/2025-06-21-6/fantastic-fishstick-original/doc/components.md`
* `inbox/2025-06-21-6/fantastic-fishstick-original/doc/mvp-decisions.md`

Additionally:

* `inbox/2025-06-21-6/fantastic-fishstick-original/doc/test-scenarios.md`
* `inbox/2025-06-21-6/fantastic-fishstick-original/doc/concrete-test-scenarios.md`

Do note that our requirements and goals are different, we can do things somewhat simpler to get started.

### INF's information retrieval system

TBD, Alex should sanitize (IP matters) and upload relevant information.
