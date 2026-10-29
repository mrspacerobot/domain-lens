# DL-14: Handle explicit branch and worktree switches safely

Status: published as [#14](https://github.com/mrspacerobot/domain-lens/issues/14); implementation has not started.
Milestone: M2 | Suggested size: M | Type: implementation
Depends on: [DL-08](dl-08-guard-unsaved-edits-and-provide-external-change-recovery.md), [DL-09](dl-09-resolve-repository-identity-and-a-fixed-review-baseline.md), [DL-13](dl-13-connect-changed-file-navigation-and-staged-detail-to-the-viewer.md)
Spec: [SPEC.md](../../SPEC.md), sections 2, 5.

## Outcome

Select an existing worktree or respond to a context change without carrying over the wrong review.

## Scope

Likely areas: src/review/context_switch.rs. These paths are proposed implementation locations, not a claim that those modules already exist. Keep the change within this issue; update the paths if the accepted architecture requires it.

## Acceptance criteria

- [ ] List existing Git worktrees and select the requested path; do not create or merge branches.
- [ ] Run dirty-buffer guards before switching contexts.
- [ ] Select the matching review/flow or show a missing-flow state; never label the previous branch's flow current.
- [ ] Handle detached HEAD and reuse of a folder for another branch without identity collisions.

## Validation and evidence

- Use two worktrees and branch switches with both clean and dirty buffers.
- Verify that cancel retains the original context and selection.
- Report the tested commit/working-tree state, commands, observed results, and acceptance evidence. Clearly identify checks not run.

## Outside this issue

Watching for external switches, worktree creation, and cleanup.
