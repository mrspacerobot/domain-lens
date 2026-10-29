# DL-32: Validate the complete workflow inside a Herdr pane

Status: published as [#32](https://github.com/mrspacerobot/domain-lens/issues/32); implementation has not started.
Milestone: M5 | Suggested size: S | Type: validation
Depends on: [DL-27](dl-27-verify-the-complete-workflow-in-claude-code.md), [DL-30](dl-30-clean-up-closed-reviews-after-confirmed-merges.md), [DL-31](dl-31-validate-windows-terminal-behavior-and-failure-recovery.md)
Spec: [SPEC.md](../../SPEC.md), sections 1–2, 8–9.

## Outcome

Verify the intended agent-and-viewer workflow in the user's actual pane environment.

## Scope

Likely areas: docs/validation/herdr.md. These paths are proposed implementation locations, not a claim that those modules already exist. Keep the change within this issue; update the paths if the accepted architecture requires it.

## Acceptance criteria

- [ ] Run an agent and viewer in separate panes/tabs on the same exact worktree, then verify separate-worktree isolation.
- [ ] Repeat essential narrow/wide, resize, keyboard/mouse, paste, Vim, and save/recovery checks.
- [ ] Verify accepted-flow refresh and stale indicators preserve unsaved source while agent activity changes disk.
- [ ] Record exact Herdr/terminal/harness versions, observed results, and any release-blocking gaps.

## Validation and evidence

- Perform the real workflow rather than substituting another terminal.
- If Herdr access is unavailable, mark this acceptance case pending and leave readiness unclaimed.
- Report the tested commit/working-tree state, commands, observed results, and acceptance evidence. Clearly identify checks not run.

## Outside this issue

A native Herdr extension and unsupported-platform guarantees.
