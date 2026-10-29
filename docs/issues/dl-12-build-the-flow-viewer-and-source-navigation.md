# DL-12: Build the flow viewer and source navigation

Status: published as [#12](https://github.com/mrspacerobot/domain-lens/issues/12); implementation has not started.
Milestone: M2 | Suggested size: M | Type: implementation
Depends on: [DL-02](dl-02-define-versioned-review-source-fact-and-flow-contracts.md), [DL-05](dl-05-add-standard-editing-controls-and-syntax-highlighting.md), [DL-08](dl-08-guard-unsaved-edits-and-provide-external-change-recovery.md)
Spec: [SPEC.md](../../SPEC.md), sections 1–2.

## Outcome

Create the recognizable Forest Night review layout with an explicit-file flow fixture.

## Scope

Likely areas: src/ui/flow.rs, src/ui/layout.rs, src/review/selection.rs. These paths are proposed implementation locations, not a claim that those modules already exist. Keep the change within this issue; update the paths if the accepted architecture requires it.

## Acceptance criteria

- [ ] Keep flow and editable source side by side at 140x40; preserve selected component/source controls in a compact 80x24 layout.
- [ ] Show interface/method names, inputs/outputs, explicit SEND/RETURN direction, explanation, and changed/context labels.
- [ ] Selecting different nodes in one file jumps to their source ranges with surrounding code scrollable.
- [ ] Support keyboard and mouse selection, named-flow switching, external nodes, and unknown/inferred relationship labels.

## Validation and evidence

- Run with v1 and v2 explicit flow fixtures and select multiple symbols in one file.
- Perform basic wide/narrow keyboard and mouse passes; record target-terminal gaps for later hardening.
- Report the tested commit/working-tree state, commands, observed results, and acceptance evidence. Clearly identify checks not run.

## Outside this issue

Agent generation, cache discovery, and implying Python analyzer support.
