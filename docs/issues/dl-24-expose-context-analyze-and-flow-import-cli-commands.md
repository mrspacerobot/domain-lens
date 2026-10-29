# DL-24: Expose context, analyze, and flow-import CLI commands

Status: published as [#24](https://github.com/mrspacerobot/domain-lens/issues/24); implementation has not started.
Milestone: M4 | Suggested size: M | Type: implementation
Depends on: [DL-15](dl-15-capture-consistent-generation-snapshots.md), [DL-19](dl-19-expand-analysis-into-relevant-unchanged-source.md), [DL-22](dl-22-validate-flow-documents-and-adapt-the-original-fixture.md), [DL-23](dl-23-publish-cached-flow-revisions-atomically-with-concurrency-checks.md)
Spec: [SPEC.md](../../SPEC.md), sections 4, 7.

## Outcome

Connect the analyzer and publication workflow through documented machine-readable interfaces.

## Scope

Likely areas: src/cli/context.rs, src/cli/analyze.rs, src/cli/import.rs. These paths are proposed implementation locations, not a claim that those modules already exist. Keep the change within this issue; update the paths if the accepted architecture requires it.

## Acceptance criteria

- [ ] Implement context creation, Rust/Java analysis, and validated import with context/expected revision arguments.
- [ ] Provide stable JSON success/error structures, useful exit statuses, and human-readable help.
- [ ] Use explicit accessible handoff paths when sandbox/cache permissions prevent normal operation.
- [ ] Document fixed-baseline handling and fail clearly for missing Git, invalid context, stale evidence, or conflicting publication.

## Validation and evidence

- Run a full context -> analyze -> import command sequence on a disposable Rust/Java branch.
- Run the same commands with stale context, invalid JSON, and inaccessible cache.
- Report the tested commit/working-tree state, commands, observed results, and acceptance evidence. Clearly identify checks not run.

## Outside this issue

Launching coding agents or automatic generation hooks.
