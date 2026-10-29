# DL-26: Verify the complete workflow in Codex CLI

Status: published as [#26](https://github.com/mrspacerobot/domain-lens/issues/26); implementation has not started.
Milestone: M4 | Suggested size: M | Type: validation
Depends on: [DL-13](dl-13-connect-changed-file-navigation-and-staged-detail-to-the-viewer.md), [DL-14](dl-14-handle-explicit-branch-and-worktree-switches-safely.md), [DL-23](dl-23-publish-cached-flow-revisions-atomically-with-concurrency-checks.md), [DL-25](dl-25-write-and-export-the-shared-flow-generation-skill.md)
Spec: [SPEC.md](../../SPEC.md), sections 4, 9.

## Outcome

Establish actual Codex compatibility using the exported skill and an independently opened viewer.

## Scope

Likely areas: docs/validation/codex.md, fixtures/review-branch/. These paths are proposed implementation locations, not a claim that those modules already exist. Keep the change within this issue; update the paths if the accepted architecture requires it.

## Acceptance criteria

- [ ] Run the skill on the shared small Rust/Java branch fixture, including unchanged neighbors and unmapped changes.
- [ ] The separate viewer finds the correct worktree/context, displays accepted evidence-linked flow, and navigates to source.
- [ ] Document exact harness/tool versions, commands, result, uncovered areas, and stale/permissions failures.
- [ ] Keep installation explicit and distinguish manual setup from behavior provided by the exporter.

## Validation and evidence

- Perform one successful context/analyze/generate/import/view pass in real Codex CLI.
- Change source during analysis and confirm stale publication is rejected; report unavailable access as unverified.
- Report the tested commit/working-tree state, commands, observed results, and acceptance evidence. Clearly identify checks not run.

## Outside this issue

Substituting a fabricated agent payload for actual harness validation.
