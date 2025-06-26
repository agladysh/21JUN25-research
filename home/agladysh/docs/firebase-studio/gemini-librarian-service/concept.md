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

### Tools

#### `os_read_file`

TODO: Describe API. Returns a "link" xml tag to an ID in a system message.

NB: No `os_write_file` would be provided initially to reduce complexity.

#### Information retrieval tools

TODO

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
