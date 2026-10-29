# DL-31: Validate Windows Terminal behavior and failure recovery

Status: published as [#31](https://github.com/mrspacerobot/domain-lens/issues/31); implementation has not started.
Milestone: M5 | Suggested size: M | Type: validation
Depends on: [DL-06](dl-06-add-optional-vim-navigation-and-editing.md), [DL-13](dl-13-connect-changed-file-navigation-and-staged-detail-to-the-viewer.md), [DL-28](dl-28-refresh-disk-git-and-accepted-flows-without-losing-buffers.md), [DL-29](dl-29-bound-cached-flows-and-analysis-artifacts-and-add-manual-cleanup.md)
Spec: [SPEC.md](../../SPEC.md), sections 2, 8–9.

## Outcome

Run the complete interactive review workflow in the first target terminal.

## Scope

Likely areas: docs/validation/windows-terminal.md, src/ui/terminal.rs. These paths are proposed implementation locations, not a claim that those modules already exist. Keep the change within this issue; update the paths if the accepted architecture requires it.

## Acceptance criteria

- [ ] Verify 140x40 and 80x24, resizing, mouse selection/wheel, keyboard-only operation, paste, standard/Vim modes, Unicode and --ascii UI.
- [ ] Verify Ctrl+S, dirty guards, encoding/newline preservation, and external-change recovery with disposable fixtures.
- [ ] Terminal modes/cursor are restored after normal quit and handled errors; source Unicode is preserved in ASCII UI mode.
- [ ] Record terminal/version-specific results and file small follow-up issues for failures; do not equate headless tests with interactive proof.

## Validation and evidence

- Execute a documented bounded manual matrix and relevant regression checks for fixes.
- Capture concise screenshots or terminal transcripts and observed limitations.
- Report the tested commit/working-tree state, commands, observed results, and acceptance evidence. Clearly identify checks not run.

## Outside this issue

Claiming macOS portability without running it.
