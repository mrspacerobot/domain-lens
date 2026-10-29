# Domain Lens: project handoff

## Goal

Help a developer understand the architecture and data flow of a task while reviewing code produced by an agent. Show components, actual input/output types or values, source code, and Git changes together without requiring a commit. Work across projects and agent harnesses, including Claude and Codex.

Task-specific flows should be temporary local data, not automatically included in a pull request.

## Desired experience

- A clickable and keyboard-accessible flow; clearly label request and response direction, values, types and domain boundaries.
- Select a node for its explanation and source. Edit and explicitly save; detect external changes and unsaved edits.
- Offer a Git diff mode and identify staged, unstaged, untracked and branch comparisons accurately. Color additions and removals with labels as well as color.
- Show syntax-highlighted source in a separate view; colors must not suggest a line was added when it was not.
- Forest Night palette: dark green/charcoal background, soft mint and warm orange, restrained borders, readable text and selection indicators. Allow narrow terminals and keyboard use; avoid relying on color alone.
- Explore running the tool in a Herdr terminal pane. No Herdr integration or Pi extension has been implemented.

## Proposed workflow

A developer can start with a concept describing user goals, inputs, outputs and constraints. An agent inspects the actual repository and writes a flow file with evidence. The viewer reads an agent-neutral representation. A portable skill or harness instruction could standardize this work for Claude, Codex and other agents.

Store generated task flows in a temporary local cache outside repositories. Key by repository, worktree and task/branch; record commit, file fingerprints, timestamp and comparison base. If missing, generate a flow; if stale, reanalyze it. Agent-generated relationships may be incomplete or inferred: make that visible and allow review.

This is a design proposal. No generic analyzer, cache, format contract, watcher, integration or skill exists yet. Decide cache retention, refresh behavior, evidence conventions and how multiple harnesses invoke the tool as the design matures.

## Prototype status

- The Textual prototype provides a clickable flow and a source editor with Ctrl+S. Its fictional skiing example is hard-coded. No source highlighting or diff is implemented.
- The standalone Windows terminal prototype provides a colored flow, selection, keyboard/mouse navigation and a source view. It uses Windows console APIs and has not been tested inside Herdr.
- The color preview captures several theme options. Forest Night was preferred.
- Both prototypes are experiments, not a production editor. Saving writes actual example files. The copied editor's disk-change check and newline behavior were tested in an earlier iteration; the sanitized fixture still needs its own interactive verification.

## Source and diff safety

Distinguish in-memory unsaved changes from disk and Git state. Avoid overwriting external changes, support dirty-buffer decisions, and preserve text encoding and newline conventions. Handle new, renamed, deleted and binary files. Git diff normally omits untracked files, so list them separately. Choose and display the actual branch comparison base.

## Next step

Build a small Rust experiment: Ratatui plus an editor widget, showing the included skiing fixture beside editable highlighted source and a read-only Git diff. Validate real mouse, resize and color behavior on Windows and in a Herdr pane. Then evaluate a versioned flow format and agent skill.
