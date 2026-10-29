# DL-03: Validate the inline editor library with a disposable demo

Status: published as [#3](https://github.com/mrspacerobot/domain-lens/issues/3); implementation has not started.
Milestone: M0 | Suggested size: M | Type: feasibility experiment
Depends on: [DL-01](dl-01-bootstrap-the-rust-workspace-and-repeatable-windows-checks.md), [DL-02](dl-02-define-versioned-review-source-fact-and-flow-contracts.md)
Spec: [SPEC.md](../../SPEC.md), sections 2, 8.

## Outcome

Evaluate Ratatui/Crossterm and Edtui against the required unified editable view before committing the application to that editor.

## Scope

Likely areas: experiments/inline-editor/, docs/decisions/editor.md. These paths are proposed implementation locations, not a claim that those modules already exist. Keep the change within this issue; update the paths if the accepted architecture requires it.

## Acceptance criteria

- [ ] Show current source plus separately rendered deleted annotations beside a static flow, with distinct old/current line numbers.
- [ ] Demonstrate cursor movement, selection/copy across deletion rows, paste, undo/redo, standard controls, and optional Vim controls.
- [ ] Serialize only current source to a disposable fixture; original repository examples remain untouched.
- [ ] Record compatible versions, Windows results, limitations, and an adopt/adapt/replace decision. If the library cannot satisfy the interaction, document a replacement design before dependent editor work.

## Validation and evidence

- Run a bounded headless smoke check plus a short actual-terminal pass.
- Compare the saved bytes with the expected current source and verify fixture cleanup.
- Report the tested commit/working-tree state, commands, observed results, and acceptance evidence. Clearly identify checks not run.

## Outside this issue

Full product editor, agent integration, and a separate source/diff fallback.
