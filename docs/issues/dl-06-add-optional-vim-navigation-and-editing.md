# DL-06: Add optional Vim navigation and editing

Status: published as [#6](https://github.com/mrspacerobot/domain-lens/issues/6); implementation has not started.
Milestone: M1 | Suggested size: M | Type: implementation
Depends on: [DL-05](dl-05-add-standard-editing-controls-and-syntax-highlighting.md)
Spec: [SPEC.md](../../SPEC.md), sections 2.

## Outcome

Provide explicit optional Vim mode while retaining standard controls as the default.

## Scope

Likely areas: src/editor/vim.rs, docs/keybindings.md. These paths are proposed implementation locations, not a claim that those modules already exist. Keep the change within this issue; update the paths if the accepted architecture requires it.

## Acceptance criteria

- [ ] Document and implement the initial key set: normal/insert transitions, h/j/k/l, word motion, line/file motion, selection, deletion, paste, undo/redo, and paging.
- [ ] Show the active mode and a discoverable way to enable/disable Vim controls.
- [ ] Motions skip read-only annotations safely; deleted rows never become editable source.
- [ ] Ctrl+S and guarded quit remain usable in both control modes; unsupported Vim features are documented.

## Validation and evidence

- Run the same edit/save-source sequence in standard and Vim modes.
- Manually verify mode switching, paging, and navigation around deletions.
- Report the tested commit/working-tree state, commands, observed results, and acceptance evidence. Clearly identify checks not run.

## Outside this issue

Full Vim compatibility, plugins, and user keymapping infrastructure.
