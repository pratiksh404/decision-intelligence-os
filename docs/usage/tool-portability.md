# Tool Portability Guide

## Purpose

Keep the Decision Intelligence OS usable across AI coding and research tools without depending on one vendor's format.

## Supported Tools

- Claude Code
- Codex
- Cursor
- Windsurf
- Roo Code
- Aider
- Antigravity
- Opencode
- Copilot

## Portability Rules

- Use markdown as the primary interface.
- Keep instructions in `AGENTS.md`, `advisors/`, and `workflows/`.
- Avoid tool-specific prompt syntax inside core workflows.
- Store reusable artifacts in `templates/`.
- Use Obsidian links and YAML frontmatter because they remain readable outside Obsidian.
- Treat automation as optional orchestration, not as a dependency for using the system.

## How to Use With Any AI Tool

1. Point the tool at this repository.
2. Ask it to read `AGENTS.md`.
3. Select the relevant workflow from `workflows/`.
4. Select the relevant template from `templates/`.
5. Ask the tool to run the advisor board from `advisors/`.
6. Save the output in the appropriate `vault/` folder.

## Expected Agent Behavior

AI tools should:

- Separate facts, assumptions, opinions, predictions, and decisions.
- Use probabilities instead of binary predictions.
- Identify counterarguments.
- Include confidence assessment.
- Produce execution plans only after a decision is approved.

