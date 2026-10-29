# DL-30: Clean up closed reviews after confirmed merges

Status: published as [#30](https://github.com/mrspacerobot/domain-lens/issues/30); implementation has not started.
Milestone: M5 | Suggested size: S | Type: implementation
Depends on: [DL-09](dl-09-resolve-repository-identity-and-a-fixed-review-baseline.md), [DL-23](dl-23-publish-cached-flow-revisions-atomically-with-concurrency-checks.md), [DL-29](dl-29-bound-cached-flows-and-analysis-artifacts-and-add-manual-cleanup.md)
Spec: [SPEC.md](../../SPEC.md), sections 6.

## Outcome

Remove completed review caches when local Git can establish completion.

## Scope

Likely areas: src/cache/merged.rs. These paths are proposed implementation locations, not a claim that those modules already exist. Keep the change within this issue; update the paths if the accepted architecture requires it.

## Acceptance criteria

- [ ] After closure, confirm the reviewed tip is included in the selected target and no newer committed, staged, unstaged, or untracked work remains.
- [ ] Use the recorded reviewed tip/context rather than branch name alone; protect active reviews and handle missing worktrees conservatively.
- [ ] Keep squash/rebase or unverifiable cases subject to ordinary budget/manual cleanup; branch deletion alone is insufficient.
- [ ] Record why cleanup happened or was skipped without requiring a hosting-service connection.

## Validation and evidence

- Exercise normal merge, squash merge, branch reuse, new local work, active lease, and missing-worktree cases.
- Confirm cleanup only touches the intended generated context data.
- Report the tested commit/working-tree state, commands, observed results, and acceptance evidence. Clearly identify checks not run.

## Outside this issue

Fetching, merging, deleting branches, and GitHub PR integration.
