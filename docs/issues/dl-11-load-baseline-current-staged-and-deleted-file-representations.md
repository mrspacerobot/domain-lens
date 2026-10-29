# DL-11: Load baseline, current, staged, and deleted-file representations

Status: published as [#11](https://github.com/mrspacerobot/domain-lens/issues/11); implementation has not started.
Milestone: M2 | Suggested size: M | Type: implementation
Depends on: [DL-07](dl-07-preserve-encoding-and-newline-conventions-when-loading-and-saving.md), [DL-09](dl-09-resolve-repository-identity-and-a-fixed-review-baseline.md), [DL-10](dl-10-build-the-complete-branch-change-inventory.md)
Spec: [SPEC.md](../../SPEC.md), sections 2–3.

## Outcome

Translate inventory records into the correct editable or read-only content.

## Scope

Likely areas: src/git/content.rs, src/review/files.rs. These paths are proposed implementation locations, not a claim that those modules already exist. Keep the change within this issue; update the paths if the accepted architecture requires it.

## Acceptance criteria

- [ ] Current text files are editable, untracked/new files compare as additions, and deleted files show baseline text read-only.
- [ ] Expose different index content as read-only staged detail without replacing the editable current buffer.
- [ ] Handle renamed paths, binary/unsupported content, conflicts, and unreadable files explicitly.
- [ ] Unsaved editor content is distinct from disk/index inventory and the baseline.

## Validation and evidence

- Load representative states from DL-10's fixture matrix and inspect bytes/provenance.
- Confirm staged content and deleted annotations cannot be saved as the current file accidentally.
- Report the tested commit/working-tree state, commands, observed results, and acceptance evidence. Clearly identify checks not run.

## Outside this issue

Staging, restoring, deleting, or renaming files from the UI.
