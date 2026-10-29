# DL-17: Extract Rust declarations and candidate call sites

Status: published as [#17](https://github.com/mrspacerobot/domain-lens/issues/17); implementation has not started.
Milestone: M3 | Suggested size: M | Type: implementation
Depends on: [DL-16](dl-16-implement-the-rust-analyzer-runner-and-coverage-diagnostics.md)
Spec: [SPEC.md](../../SPEC.md), sections 4, 9.

## Outcome

Implement inspectable Rust source facts for the agreed first language.

## Scope

Likely areas: src/analysis/rust.rs, fixtures/rust/. These paths are proposed implementation locations, not a claim that those modules already exist. Keep the change within this issue; update the paths if the accepted architecture requires it.

## Acceptance criteria

- [ ] Extract functions, methods, traits, implementations, receivers, declared parameter/return types, generics, and source ranges.
- [ ] Record imports and syntactic call sites; keep trait dispatch, macros, and unresolved calls explicitly unresolved where appropriate.
- [ ] Distinguish missing type information from language-defined implicit return behavior.
- [ ] Publish partial-coverage diagnostics instead of inventing expanded macro or inferred type results.

## Validation and evidence

- Compare structured facts with hand-checked Rust fixtures covering generics, methods, traits, and macro-containing code.
- Edit a declaration and verify corresponding facts and ranges change.
- Report the tested commit/working-tree state, commands, observed results, and acceptance evidence. Clearly identify checks not run.

## Outside this issue

Compiler-backed type inference and macro expansion.
