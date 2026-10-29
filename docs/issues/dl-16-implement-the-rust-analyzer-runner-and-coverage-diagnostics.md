# DL-16: Implement the Rust analyzer runner and coverage diagnostics

Status: published as [#16](https://github.com/mrspacerobot/domain-lens/issues/16); implementation has not started.
Milestone: M3 | Suggested size: M | Type: implementation
Depends on: [DL-02](dl-02-define-versioned-review-source-fact-and-flow-contracts.md), [DL-15](dl-15-capture-consistent-generation-snapshots.md)
Spec: [SPEC.md](../../SPEC.md), sections 4.

## Outcome

Build shared extraction infrastructure using the candidate parser after checking its compatible versions.

## Scope

Likely areas: src/analysis/runner.rs, src/analysis/facts.rs. These paths are proposed implementation locations, not a claim that those modules already exist. Keep the change within this issue; update the paths if the accepted architecture requires it.

## Acceptance criteria

- [ ] Load language adapters for Rust and Java and emit versioned facts linked to the generation snapshot.
- [ ] Carry source locations, stable symbol IDs, analyzer/grammar versions, and explicit coverage diagnostics.
- [ ] Honor worktree boundaries and bounded input sizes; handle malformed or unsupported input as partial analysis.
- [ ] Run outside the interactive UI loop and support cancellation without corrupting output.

## Validation and evidence

- Exercise unsupported language, oversized file, syntax error, cancellation, and valid fixture cases.
- Verify deterministic facts for the same source/options/tool versions.
- Report the tested commit/working-tree state, commands, observed results, and acceptance evidence. Clearly identify checks not run.

## Outside this issue

Language-specific extraction rules and complete semantic resolution.
