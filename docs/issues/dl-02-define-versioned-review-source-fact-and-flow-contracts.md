# DL-02: Define versioned review, source-fact, and flow contracts

Status: published as [#2](https://github.com/mrspacerobot/domain-lens/issues/2); implementation has not started.
Milestone: M0 | Suggested size: M | Type: implementation
Depends on: [DL-01](dl-01-bootstrap-the-rust-workspace-and-repeatable-windows-checks.md)
Spec: [SPEC.md](../../SPEC.md), sections 4–7.

## Outcome

Define shared models and JSON examples before the viewer, analyzer, and skill start exchanging data.

## Scope

Likely areas: src/model/, docs/contracts/, examples/. These paths are proposed implementation locations, not a claim that those modules already exist. Keep the change within this issue; update the paths if the accepted architecture requires it.

## Acceptance criteria

- [ ] Define ReviewContext, snapshot references, file states, source facts, flow nodes/edges, coverage diagnostics, confidence, and accepted revisions.
- [ ] State source coordinate and newline conventions, stable symbol identity, unknown types, external nodes, and syntactic versus resolved calls.
- [ ] Provide a v1 adapter for example-flow.json; missing evidence/freshness remains unknown.
- [ ] Check in small Rust and Java source fixtures with expected facts and a mixed-language branch scenario; do not imply the Python demo is analyzer-supported.

## Validation and evidence

- Round-trip representative JSON; reject unsupported versions and malformed required fields.
- Review fixture source ranges and expected declarations manually.
- Report the tested commit/working-tree state, commands, observed results, and acceptance evidence. Clearly identify checks not run.

## Outside this issue

Extraction implementation and final semantic-resolution adapters.
