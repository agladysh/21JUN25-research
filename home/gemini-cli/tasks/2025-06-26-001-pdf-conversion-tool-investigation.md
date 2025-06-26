---
task: Re-export all PDFs as Markdown
status: open
assigned_to: Gemini (CLI)
priority: high
---

# Re-export all PDFs as Markdown

## Description
This task involves re-exporting all PDF files in the repository as Markdown using the `pnpx @opendocsg/pdf2md` tool. The goal is to ensure all PDF content is available in an LLM-friendly format.

## Sub-tasks
- [ ] Identify all PDF files in the repository.
- [ ] Run `pnpx @opendocsg/pdf2md --inputFolderPath=. --outputFolderPath=. --overwrite` to convert them to Markdown.
- [ ] Verify the conversion for a sample of files.
- [ ] Document any issues encountered during the conversion process.

## Rationale
As identified in the `TODO.md` and mail archives, efficient PDF processing is a critical need for the team. This task directly addresses that need by converting existing PDFs to a more accessible format for LLMs.

## Expected Output
- All PDF files in the repository will have a corresponding Markdown file.
- A summary email to the team with any issues encountered and confirmation of completion.