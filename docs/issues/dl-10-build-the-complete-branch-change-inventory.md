# DL-10: Build the complete branch change inventory

Status: published as [#10](https://github.com/mrspacerobot/domain-lens/issues/10); implementation has not started.
Milestone: M2 | Suggested size: M | Type: implementation
Depends on: [DL-09](dl-09-resolve-repository-identity-and-a-fixed-review-baseline.md)
Spec: [SPEC.md](../../SPEC.md), sections 3, 9.

## Outcome

Enumerate every relevant path across baseline, HEAD, index, working tree, and non-ignored untracked files.

## Scope

Likely areas: src/git/inventory.rs. These paths are proposed implementation locations, not a claim that those modules already exist. Keep the change within this issue; update the paths if the accepted architecture requires it.

## Acceptance criteria

- [ ] Union all comparison/status sources so committed, staged, unstaged, and new work stays reachable.
- [ ] Label renames, deletions, binaries, conflicts, and paths with staged/working-tree discrepancies.
- [ ] Retain changes canceled in the working tree as an index discrepancy with a clear no-net-highlight explanation.
- [ ] Parse NUL-delimited records safely, including spaces, Unicode, and unusual valid path characters.

## Validation and evidence

- Construct a temporary repository matrix containing each state and mixed-state cases.
- Check inventory completeness against the fixture manifest rather than a single git diff.
- Report the tested commit/working-tree state, commands, observed results, and acceptance evidence. Clearly identify checks not run.

## Outside this issue

Graph coverage, history playback, and change ownership attribution.
