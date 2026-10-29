# DL-08: Guard unsaved edits and provide external-change recovery

Status: published as [#8](https://github.com/mrspacerobot/domain-lens/issues/8); implementation has not started.
Milestone: M1 | Suggested size: M | Type: implementation
Depends on: [DL-05](dl-05-add-standard-editing-controls-and-syntax-highlighting.md), [DL-07](dl-07-preserve-encoding-and-newline-conventions-when-loading-and-saving.md)
Spec: [SPEC.md](../../SPEC.md), sections 2, 9.

## Outcome

Connect safe IO to file selection, reload, quit, and context-switch actions.

## Scope

Likely areas: src/review/buffers.rs, src/ui/dialogs.rs. These paths are proposed implementation locations, not a claim that those modules already exist. Keep the change within this issue; update the paths if the accepted architecture requires it.

## Acceptance criteria

- [ ] Dirty transitions offer Save, Discard, or Cancel; failed saves do not complete the transition.
- [ ] External changes preserve local edits and offer save-copy, deliberate reload/discard, or cancel.
- [ ] A successful save updates dirty state without changing the review baseline.
- [ ] Recovery leaves the user able to exit or save elsewhere rather than trapping an unsaveable buffer.

## Validation and evidence

- Exercise every dirty transition, including a failed save and canceled action.
- Modify the backing file externally while dirty and verify save-copy recovery.
- Report the tested commit/working-tree state, commands, observed results, and acceptance evidence. Clearly identify checks not run.

## Outside this issue

Git watchers and automatic merging of conflicting edits.
