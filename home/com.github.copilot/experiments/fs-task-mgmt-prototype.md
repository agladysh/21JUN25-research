# Copilot Task Management Prototype

## Purpose
Prototype of a simple, file-system-based task management system for agent/human collaboration.

## Structure
- Each task is a file in `tasks/`, named with a unique ID and short description.
- Task files are Markdown, with YAML frontmatter for metadata (status, assignee, etc.).
- Statuses: open, in-progress, blocked, done, archived.

## Example Task File
```markdown
---
id: 2025-06-21-001
title: Prototype FS-based task management
status: open
assignee: com.github.copilot
created: 2025-06-21
---

Implement a minimal file-based task management system for the project.
```

## Next Steps
- Create `tasks/` directory at project root.
- Add initial example tasks.
- Document workflow for creating, updating, and closing tasks.
