# PDF/Text Extraction Pipeline for LLM Summarization

## Purpose

Prototype a pipeline using specialized, LLM-aware modules for extracting high-quality, LLM-ready text from PDFs and other formats.

## Principles

- Use modules designed for LLM input (e.g., unstructured, textract, llama-index, pdfplumber with heuristics, etc.).
- Avoid generic extraction that produces noisy or contextless output.
- Clean up all intermediate files and metadata artifacts after processing.
- Work only in `home/com.github.copilot/` until peer review.

## Pipeline Outline

1. **Extract**: Use `unstructured` or similar to extract structured elements (titles, sections, tables, etc.) from PDFs.
2. **Preprocess**: Clean and format extracted text for LLM consumption (remove headers/footers, fix encoding, chunk logically).
3. **Summarize**: Pass cleaned text to a local LLM (e.g., via `llama.cpp`, `ollama`, or API) for summarization.
4. **Cleanup**: Remove all temporary/intermediate files (JSON/YAML) after use.
5. **Log**: Document all steps and results in this directory.

## Next Steps

- Implement and test extraction on sample PDFs using `unstructured` or similar.
- Script cleanup of old metadata files in `/inbox/`.
- Document findings and prepare for peer review.
