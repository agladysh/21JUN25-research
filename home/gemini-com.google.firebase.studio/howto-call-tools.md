# LLM Tool Calling in Envirionments with Sub-Optimal LLM UX

1. After you call the tool, DO NOT STOP generation. 

Check if the result returned by the tool aligns with your expectations. If it does, briefly confirm verbally.

2. If returned result is unexpected, or you see an error, DO NOT STOP GENERATION

Instead, "debug". Assume tool works, but was invoked with an accidental technical violation of its contract by the operator (that is, you, the LLM). Possibly due to an ambiguity in the documentation.

Verbalize (generate text) your hypothesis. What you did, what could go wrong, what to try. KISS.

Call the tool again based on your hypothesis. DO NOT STOP GENERATION. Check results, repeat until you find the right way to call the tool. Document (verbalize) your findings.

Next time, take the findings in account, when calling that tool in similar situations.

Do not ritualize the process of self-correction of random accidents.

## Environment-Specific Guidance  

### Google Firebase Studio / Gemini

#### Using `list_files`

The `list_files` tool fails with `Request contains an invalid argument.` when supplied a bad path (normally, a directory that does not exist).

You are to treat this error as if it was a normal "file or directory not found" tool call status. 

When you get `Request contains an invalid argument.` error from the `list_files` tool, DO NOT STOP GENERATION, and read the above text.

## Using `run_terminal_command`

The `run_terminal_command` tool is available for executing shell commands. This is crucial for interacting with the environment for tasks such as:

*   Version control operations (e.g., `git status`, `git commit`, `git push`).
*   Running scripts and programs.
*   Navigating the file system and managing files.
*   Executing system utilities.

When a terminal command is required, formulate the command and invoke the `run_terminal_command` tool. The environment will present the command to the user for confirmation before execution.

If a command execution results in an error or unexpected output, follow the general guidance in this document for handling unexpected tool results: analyze the output, form a hypothesis about the cause (e.g., incorrect syntax, wrong path, permission issues), and formulate a corrected command or an alternative approach. Document the findings to improve future command invocations.