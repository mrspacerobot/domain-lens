# DL-27: Verify the complete workflow in Claude Code

Status: published as [#27](https://github.com/mrspacerobot/domain-lens/issues/27); implementation has not started.
Milestone: M4 | Suggested size: S | Type: validation
Depends on: [DL-26](dl-26-verify-the-complete-workflow-in-codex-cli.md)
Spec: [SPEC.md](../../SPEC.md), sections 4, 9.

## Outcome

Validate the same shared skill and branch fixture in the second supported harness.

## Scope

Likely areas: docs/validation/claude.md, fixtures/review-branch/. These paths are proposed implementation locations, not a claim that those modules already exist. Keep the change within this issue; update the paths if the accepted architecture requires it.

## Acceptance criteria

- [ ] Use the same CLI contracts and Rust/Java fixture used for Codex, with only the documented harness adapter.
- [ ] Generate/import a flow and open it in the independently running viewer.
- [ ] Verify unknown types, unmapped paths, missing CLI, stale context, and permissions have honest outcomes.
- [ ] Record exact versions and evidence; retain shared instructions without divergent extraction code.

## Validation and evidence

- Perform a real Claude Code pass and compare output validity and coverage with the Codex fixture run.
- If the harness is unavailable, leave compatibility unverified and record the missing prerequisite.
- Report the tested commit/working-tree state, commands, observed results, and acceptance evidence. Clearly identify checks not run.

## Outside this issue

Assuming compatibility from exported instructions alone.
