# DL-05: Add standard editing controls and syntax highlighting

Status: published as [#5](https://github.com/mrspacerobot/domain-lens/issues/5); implementation has not started.
Milestone: M1 | Suggested size: M | Type: implementation
Depends on: [DL-04](dl-04-implement-source-to-screen-mapping-for-inline-change-annotations.md)
Spec: [SPEC.md](../../SPEC.md), sections 2.

## Outcome

Make the current-source buffer usable with normal editor controls.

## Scope

Likely areas: src/editor/input.rs, src/editor/highlight.rs. These paths are proposed implementation locations, not a claim that those modules already exist. Keep the change within this issue; update the paths if the accepted architecture requires it.

## Acceptance criteria

- [ ] Support insertion, arrows, Page Up/Down, selection, paste, undo/redo, and mouse-wheel scrolling.
- [ ] Typing single-character app shortcuts never consumes source text.
- [ ] Syntax colors for Rust and Java are independent of addition/deletion markers.
- [ ] Keep unsaved state and cursor placement coherent while highlights refresh.

## Validation and evidence

- Use a representative editing sequence containing paste, multiline selection, undo, and redo.
- Verify added, unchanged, and deleted rows remain distinguishable with syntax colors enabled.
- Report the tested commit/working-tree state, commands, observed results, and acceptance evidence. Clearly identify checks not run.

## Outside this issue

Vim mode and save/conflict handling.
