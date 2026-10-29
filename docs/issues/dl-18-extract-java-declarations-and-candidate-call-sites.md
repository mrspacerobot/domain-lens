# DL-18: Extract Java declarations and candidate call sites

Status: published as [#18](https://github.com/mrspacerobot/domain-lens/issues/18); implementation has not started.
Milestone: M3 | Suggested size: M | Type: implementation
Depends on: [DL-16](dl-16-implement-the-rust-analyzer-runner-and-coverage-diagnostics.md)
Spec: [SPEC.md](../../SPEC.md), sections 4, 9.

## Outcome

Implement inspectable Java source facts for the agreed second language.

## Scope

Likely areas: src/analysis/java.rs, fixtures/java/. These paths are proposed implementation locations, not a claim that those modules already exist. Keep the change within this issue; update the paths if the accepted architecture requires it.

## Acceptance criteria

- [ ] Extract packages/imports, classes, interfaces, constructors, methods, declared parameters/returns, generics, and source ranges.
- [ ] Give overloaded/nested declarations distinct identities and preserve declared void results.
- [ ] Record syntactic calls with explicit uncertainty for overload resolution, inheritance, and dynamic dispatch.
- [ ] Annotations and incomplete source yield accurate facts where available plus diagnostics.

## Validation and evidence

- Compare facts with hand-checked Java fixtures containing overloads, constructors, interfaces, generics, and annotations.
- Verify declared inputs/outputs and exact source locations independently.
- Report the tested commit/working-tree state, commands, observed results, and acceptance evidence. Clearly identify checks not run.

## Outside this issue

JVM execution, annotation processing, and compiler-backed type inference.
