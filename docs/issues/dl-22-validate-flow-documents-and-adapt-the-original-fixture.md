# DL-22: Validate flow documents and adapt the original fixture

Status: published as [#22](https://github.com/mrspacerobot/domain-lens/issues/22); implementation has not started.
Milestone: M4 | Suggested size: M | Type: implementation
Depends on: [DL-02](dl-02-define-versioned-review-source-fact-and-flow-contracts.md), [DL-15](dl-15-capture-consistent-generation-snapshots.md)
Spec: [SPEC.md](../../SPEC.md), sections 5–6.

## Outcome

Validate imported graph structure and evidence against the active generation context.

## Scope

Likely areas: src/flow/validate.rs, src/flow/compat.rs. These paths are proposed implementation locations, not a claim that those modules already exist. Keep the change within this issue; update the paths if the accepted architecture requires it.

## Acceptance criteria

- [ ] Reject unsupported schemas, duplicate IDs, missing endpoints, invalid ranges, wrong contexts, and path/symlink escapes.
- [ ] Require inspectable source evidence for evidenced links; retain explicit inferred/unknown and external-component states.
- [ ] Reject stale snapshots including changes to analyzed unchanged files and newly added/deleted paths.
- [ ] Load the v1 demo with unknown confidence/freshness and account for paths not mapped by the graph.

## Validation and evidence

- Use valid and invalid graph fixtures, cross-worktree contexts, symlink escape cases, and stale-source scenarios.
- Verify errors identify the offending document field or path.
- Report the tested commit/working-tree state, commands, observed results, and acceptance evidence. Clearly identify checks not run.

## Outside this issue

Proving runtime behavior from static evidence.
