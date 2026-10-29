# DL-28: Refresh disk, Git, and accepted flows without losing buffers

Status: published as [#28](https://github.com/mrspacerobot/domain-lens/issues/28); implementation has not started.
Milestone: M5 | Suggested size: M | Type: implementation
Depends on: [DL-14](dl-14-handle-explicit-branch-and-worktree-switches-safely.md), [DL-15](dl-15-capture-consistent-generation-snapshots.md), [DL-23](dl-23-publish-cached-flow-revisions-atomically-with-concurrency-checks.md), [DL-26](dl-26-verify-the-complete-workflow-in-codex-cli.md)
Spec: [SPEC.md](../../SPEC.md), sections 2, 5–6.

## Outcome

Add debounced watching or bounded polling with explicit freshness states.

## Scope

Likely areas: src/watch/, src/review/refresh.rs. These paths are proposed implementation locations, not a claim that those modules already exist. Keep the change within this issue; update the paths if the accepted architecture requires it.

## Acceptance criteria

- [ ] Refresh inventory, source fingerprints, branch context, and accepted revisions outside the input/render loop.
- [ ] Distinguish current, stale, missing, incomplete, and freshness-unknown explanations.
- [ ] Preserve selection and unsaved buffers; external file changes use existing recovery controls.
- [ ] Context changes stop the old flow being shown as current; refresh alone does not launch an agent.

## Validation and evidence

- Change source, index, branches, and cached revisions while clean and dirty.
- Verify burst changes debounce and background work cancels or finishes without UI corruption.
- Report the tested commit/working-tree state, commands, observed results, and acceptance evidence. Clearly identify checks not run.

## Outside this issue

Automatic agent generation or hidden branch mutations.
