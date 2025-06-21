# Copilot Inbox Triage & Metadata Extraction Prototype

## Purpose
Draft workflow and script outline for automated triage and metadata extraction from `/inbox/`.

## Workflow
1. Monitor `/inbox/` for new files.
2. For each file:
   - Extract metadata: filename, date, type, brief summary (if possible).
   - Write metadata to a `metadata.json` file alongside the original.
   - Move processed files to `/archive/` or agent-specific folders.
3. Log actions and errors.

## Script Outline (Python)
```python
import os, json, datetime
INBOX = 'inbox/'
for fname in os.listdir(INBOX):
    meta = {
        'filename': fname,
        'date': str(datetime.datetime.now()),
        'type': fname.split('.')[-1],
        'summary': ''  # TODO: auto-summarize
    }
    with open(os.path.join(INBOX, fname + '.metadata.json'), 'w') as f:
        json.dump(meta, f)
```

## Next Steps
- Implement and test script.
- Propose integration with team workflow.
- Document results and lessons learned.
