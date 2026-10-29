# DL-20: Reuse unchanged analysis facts with correct invalidation

Status: published as [#20](https://github.com/mrspacerobot/domain-lens/issues/20); implementation has not started.
Milestone: M3 | Suggested size: M | Type: implementation
Depends on: [DL-15](dl-15-capture-consistent-generation-snapshots.md), [DL-19](dl-19-expand-analysis-into-relevant-unchanged-source.md)
Spec: [SPEC.md](../../SPEC.md), sections 4, 6.

## Outcome

Cache extraction results and reuse parser state where useful without reusing stale relationship conclusions.

## Scope

Likely areas: src/analysis/reuse.rs. These paths are proposed implementation locations, not a claim that those modules already exist. Keep the change within this issue; update the paths if the accepted architecture requires it.

## Acceptance criteria

- [ ] Key reuse by content, language, analyzer/grammar versions, and relevant options.
- [ ] Invalidate dependent relationship results when imports, declarations, dependencies, or path inventory changes.
- [ ] An unchanged caller does not retain a resolved link to a changed/deleted callee.
- [ ] Cache regeneration and corruption recovery remain explicit; all analysis artifacts count toward the eventual global budget.

## Validation and evidence

- Instrument cold/warm runs to show unchanged extraction is reused.
- Change a callee, add/remove a path, and change tool/options versions; verify correct invalidation.
- Report the tested commit/working-tree state, commands, observed results, and acceptance evidence. Clearly identify checks not run.

## Outside this issue

Final cache eviction policy and speculative performance claims.
