# DL-09: Resolve repository identity and a fixed review baseline

Status: published as [#9](https://github.com/mrspacerobot/domain-lens/issues/9); implementation has not started.
Milestone: M2 | Suggested size: M | Type: implementation
Depends on: [DL-01](dl-01-bootstrap-the-rust-workspace-and-repeatable-windows-checks.md), [DL-02](dl-02-define-versioned-review-source-fact-and-flow-contracts.md)
Spec: [SPEC.md](../../SPEC.md), sections 3, 5.

## Outcome

Discover the exact repository/worktree and resolve an explicitly selected target.

## Scope

Likely areas: src/git/command.rs, src/git/context.rs. These paths are proposed implementation locations, not a claim that those modules already exist. Keep the change within this issue; update the paths if the accepted architecture requires it.

## Acceptance criteria

- [ ] Use argument arrays, explicit cwd, validated revisions, and predictable Git output with external diff/textconv disabled.
- [ ] Resolve canonical common Git directory, worktree root, branch/detached HEAD, target, and merge base.
- [ ] Persist a selected target only for its matching branch/worktree context and display target/base.
- [ ] Keep the base fixed until explicit reset; missing Git, invalid target, unrelated history, and detached HEAD have clear outcomes.

## Validation and evidence

- Use temporary repositories and two worktrees, including paths with spaces.
- Verify invalid revision handling and that advancing HEAD does not silently reset the base.
- Report the tested commit/working-tree state, commands, observed results, and acceptance evidence. Clearly identify checks not run.

## Outside this issue

Branch creation, fetching, merging, and file inventory.
