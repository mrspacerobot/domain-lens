# DL-29: Bound cached flows and analysis artifacts and add manual cleanup

Status: published as [#29](https://github.com/mrspacerobot/domain-lens/issues/29); implementation has not started.
Milestone: M5 | Suggested size: M | Type: implementation
Depends on: [DL-20](dl-20-reuse-unchanged-analysis-facts-with-correct-invalidation.md), [DL-23](dl-23-publish-cached-flow-revisions-atomically-with-concurrency-checks.md), [DL-28](dl-28-refresh-disk-git-and-accepted-flows-without-losing-buffers.md)
Spec: [SPEC.md](../../SPEC.md), sections 6.

## Outcome

Prevent unbounded local storage across review contexts and analysis artifacts.

## Scope

Likely areas: src/cache/budget.rs, src/cache/leases.rs, src/cli/cache.rs. These paths are proposed implementation locations, not a claim that those modules already exist. Keep the change within this issue; update the paths if the accepted architecture requires it.

## Acceptance criteria

- [ ] Choose and document a finite configurable default disk budget; account for all managed flow/fact/parser artifacts.
- [ ] Evict least recently used inactive contexts on startup and publication while honoring open-review leases and publication locks.
- [ ] Reserve or bound temporary publication bytes; protected data exceeding the budget causes a clear limit error rather than unbounded growth.
- [ ] Provide manual inactive-cache cleanup and recovery from stale leases; preserve source, installed skills, and unsaved edits.

## Validation and evidence

- Use a deliberately tiny budget to force eviction and protected-data rejection.
- Race cleanup with publication and verify only inactive complete contexts are removed.
- Report the tested commit/working-tree state, commands, observed results, and acceptance evidence. Clearly identify checks not run.

## Outside this issue

Deleting source, active review buffers, or user-installed skills.
