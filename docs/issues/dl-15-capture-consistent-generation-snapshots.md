# DL-15: Capture consistent generation snapshots

Status: published as [#15](https://github.com/mrspacerobot/domain-lens/issues/15); implementation has not started.
Milestone: M3 | Suggested size: M | Type: implementation
Depends on: [DL-02](dl-02-define-versioned-review-source-fact-and-flow-contracts.md), [DL-07](dl-07-preserve-encoding-and-newline-conventions-when-loading-and-saving.md), [DL-09](dl-09-resolve-repository-identity-and-a-fixed-review-baseline.md), [DL-10](dl-10-build-the-complete-branch-change-inventory.md)
Spec: [SPEC.md](../../SPEC.md), sections 4–6.

## Outcome

Create context-issued snapshots shared by source extraction and flow publication.

## Scope

Likely areas: src/analysis/snapshot.rs. These paths are proposed implementation locations, not a claim that those modules already exist. Keep the change within this issue; update the paths if the accepted architecture requires it.

## Acceptance criteria

- [ ] Capture HEAD, baseline, index, path inventory, options, and file-content fingerprints, including analyzed unchanged source.
- [ ] Use captured content or verified immutable references so facts correspond to what the agent analyzed.
- [ ] Detect files/context changing during capture and retry within a bound or return an explicit unstable-snapshot error.
- [ ] Record source additions/deletions and dependency coverage needed to reject stale imports.

## Validation and evidence

- Change a file, index entry, and path inventory during capture with deterministic fixture hooks.
- Confirm snapshot identifiers cannot be substituted across worktrees.
- Report the tested commit/working-tree state, commands, observed results, and acceptance evidence. Clearly identify checks not run.

## Outside this issue

Claiming an atomic filesystem snapshot without verification.
