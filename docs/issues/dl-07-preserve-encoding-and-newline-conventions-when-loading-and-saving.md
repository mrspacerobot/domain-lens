# DL-07: Preserve encoding and newline conventions when loading and saving

Status: published as [#7](https://github.com/mrspacerobot/domain-lens/issues/7); implementation has not started.
Milestone: M1 | Suggested size: M | Type: implementation
Depends on: [DL-02](dl-02-define-versioned-review-source-fact-and-flow-contracts.md), [DL-04](dl-04-implement-source-to-screen-mapping-for-inline-change-annotations.md)
Spec: [SPEC.md](../../SPEC.md), sections 2, 9.

## Outcome

Implement source IO independently of display annotations.

## Scope

Likely areas: src/source/load.rs, src/source/save.rs. These paths are proposed implementation locations, not a claim that those modules already exist. Keep the change within this issue; update the paths if the accepted architecture requires it.

## Acceptance criteria

- [ ] Round-trip UTF-8, UTF-8 BOM, LF, CRLF, empty files, and missing final newline.
- [ ] Mixed/unsupported encodings and binary files produce explicit read-only states.
- [ ] Save atomically where supported, preserve file permissions, and detect external replacement/modification before writing.
- [ ] Constrain paths to the selected worktree, including symlink escapes; save failures retain the buffer.

## Validation and evidence

- Use disposable files for byte-for-byte round trips and simulated external changes.
- Force a save failure and confirm both disk contents and in-memory edits remain recoverable.
- Report the tested commit/working-tree state, commands, observed results, and acceptance evidence. Clearly identify checks not run.

## Outside this issue

Dirty navigation prompts and generic encoding conversion.
