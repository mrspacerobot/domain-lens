# DL-04: Implement source-to-screen mapping for inline change annotations

Status: published as [#4](https://github.com/mrspacerobot/domain-lens/issues/4); implementation has not started.
Milestone: M1 | Suggested size: M | Type: implementation
Depends on: [DL-02](dl-02-define-versioned-review-source-fact-and-flow-contracts.md), [DL-03](dl-03-validate-the-inline-editor-library-with-a-disposable-demo.md)
Spec: [SPEC.md](../../SPEC.md), sections 2.

## Outcome

Implement the adopted model that maps editable source rows to visual rows containing read-only removals.

## Scope

Likely areas: src/editor/projection.rs, src/editor/render.rs. These paths are proposed implementation locations, not a claim that those modules already exist. Keep the change within this issue; update the paths if the accepted architecture requires it.

## Acceptance criteria

- [ ] Projection handles insertion, deletion, replacement, empty files, and missing final newline without changing source text.
- [ ] Mouse and keyboard coordinates map correctly around deleted rows; copy/selection never inserts deleted annotations into source.
- [ ] Render explicit +/- labels and old/current line numbers independently of token highlighting.
- [ ] Editing recomputes highlights against the fixed supplied baseline.

## Validation and evidence

- Exercise projection/serialization invariants on addition, deletion, replacement, and long deletion blocks.
- Verify cursor and selection movement across virtual rows in the adopted editor.
- Report the tested commit/working-tree state, commands, observed results, and acceptance evidence. Clearly identify checks not run.

## Outside this issue

Git baseline selection, disk saving, and Vim key coverage.
