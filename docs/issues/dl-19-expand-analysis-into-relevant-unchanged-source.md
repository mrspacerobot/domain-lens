# DL-19: Expand analysis into relevant unchanged source

Status: published as [#19](https://github.com/mrspacerobot/domain-lens/issues/19); implementation has not started.
Milestone: M3 | Suggested size: M | Type: implementation
Depends on: [DL-10](dl-10-build-the-complete-branch-change-inventory.md), [DL-17](dl-17-extract-rust-declarations-and-candidate-call-sites.md), [DL-18](dl-18-extract-java-declarations-and-candidate-call-sites.md)
Spec: [SPEC.md](../../SPEC.md), sections 1, 4.

## Outcome

Give the agent a useful neighborhood around changed components without hiding unrelated changes.

## Scope

Likely areas: src/analysis/scope.rs, src/analysis/index.rs. These paths are proposed implementation locations, not a claim that those modules already exist. Keep the change within this issue; update the paths if the accepted architecture requires it.

## Acceptance criteria

- [ ] Start from changed source and allow bounded expansion through declarations, imports, and candidate callers/dependencies.
- [ ] Include unchanged context required to explain a flow, with deterministic selection and recorded source evidence.
- [ ] Report scope limits, unsupported files, and unresolved relationships; retain the complete changed-file inventory.
- [ ] Provide a way for the skill to request additional source neighborhoods when the first result is insufficient.

## Validation and evidence

- Use Rust and Java changed-middle-component fixtures and verify unchanged neighbors are discoverable.
- Verify a disconnected changed file remains in inventory even when outside the selected flow.
- Report the tested commit/working-tree state, commands, observed results, and acceptance evidence. Clearly identify checks not run.

## Outside this issue

An authoritative whole-program call graph and automatic runtime tracing.
