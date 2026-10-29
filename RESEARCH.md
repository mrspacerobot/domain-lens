# Domain Lens - research and prototype plan

Status: exploration, 2026-10-29. No implementation decision has been made.

## Purpose

An agent-independent terminal app that shows a task's code/data flow next to editable source and a Git diff. The flow is temporary local working data, not part of the pull request. A person can inspect components, inputs, outputs, actual source and changes while working with Codex, Claude or another agent.

## Candidate Rust stack

- **Ratatui + Crossterm** for terminal layout, colors, input and mouse. Ratatui offers composable terminal widgets; the application is responsible for event handling and state. https://docs.rs/ratatui/latest/ratatui/
- **Edtui** for an embedded editor: line numbers, mouse input, Emacs-style or Vim-style editing and optional syntax highlighting via syntect. It is a widget, not a full IDE; language-server features are not implied. https://docs.rs/edtui/latest/edtui/
- **Git CLI** initially for diffs and status. It matches the locally installed Git and avoids a separate Git implementation. Use argument arrays, never shell interpolation, and set the repository working directory explicitly. Alternatives such as git2 should be evaluated if needed. https://git-scm.com/docs/git-diff and https://docs.rs/git2/latest/git2/struct.Repository.html
- **Serde / JSON** for a versioned, agent-neutral flow exchange format. Agents create the data; the viewer does not depend on a particular harness.
- Compare **textual-rs** if its widget model is a better fit. Check maturity, dependencies, Windows mouse behavior and editor support before choosing. https://github.com/HoldMyBeer-gg/textual-rs

No Rust compiler or cargo was found on PATH in the current environment; building and testing this stack will require a Rust toolchain. Library compatibility, colors and mouse behavior inside Herdr on Windows are unverified.

## Visual direction

Use the Forest Night prototype as a starting point: neutral dark background, readable text, muted borders, and explicit request/response labels alongside color. Use syntax highlighting for code tokens, with a separate diff mode that explains added/removed lines and never uses color alone. Maintain visible focus and mouse/keyboard navigation. Adapt to narrow terminals without hiding the selected source or critical controls.

## Git review modes

Make the comparison explicit; do not call all changes a PR diff:

1. Unstaged: working tree vs index (`git diff`).
2. Staged: index vs HEAD (`git diff --cached`).
3. Branch: merge base of a user-selected target and HEAD vs HEAD (`git diff BASE...HEAD`); label target and checked commits.
4. Untracked files: list with `git status --porcelain` and display explicitly as new files; ordinary `git diff` omits them. Handle renames, deleted files, binary files, missing bases and worktrees explicitly.

Keep unsaved editor buffers separate from disk and label when a diff excludes them. Protect edits against external file changes; handle encoding, newlines and dirty buffers when switching or quitting.

## Flow exchange and cache

- Example format: `example-flow.json` is illustrative, not a complete generated graph.
- Each node has an ID, role and optional source location; edges identify actual data and direction. Include evidence links or locations and mark unknown or inferred information.
- Cache outside the repository, keyed by canonical repository identity and worktree path plus branch/task identity. Store commit, target base where relevant, timestamp and fingerprints of analyzed files. Branch names alone are insufficient for worktrees and uncommitted changes.
- Compare fingerprints when opening; label stale data and ask an agent to reanalyze. Do not imply the graph stays accurate automatically.
- A portable skill or harness instruction should tell an agent how to inspect source and populate the format. Share data, not agent-specific runtime state. Do not commit cached project data by default.

## Suggested proof of concept

1. Build a Windows-first Ratatui screen using a small static flow fixture: selectable nodes, typed input/output arrows, source panel, accessible colors and keyboard/mouse.
2. Add Edtui and verify syntax highlighting, selection, scrolling, save, unsaved-change handling and external-change detection.
3. Add a read-only Git diff mode for staged, unstaged, untracked and chosen branch base; test special file cases.
4. Replace the fixture with a versioned JSON flow in a local cache and show freshness information.
5. Test in Herdr and a normal Windows terminal, including small widths, resizing, Unicode and color. Then try an agent-generated flow from a different branch and validate source links.

## Existing local references

- `prototypes/map-flow-editor.py` - Textual editing prototype.
- `prototypes/map-flow-tui.py` - standalone Windows flow prototype.
- `prototypes/tui-color-options.html` - browser palette preview.

These are local workspace artifacts, not part of the planned shared product or an automatically generated source of truth.
