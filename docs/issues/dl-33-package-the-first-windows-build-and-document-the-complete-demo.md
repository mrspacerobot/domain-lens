# DL-33: Package the first Windows build and document the complete demo

Status: published as [#33](https://github.com/mrspacerobot/domain-lens/issues/33); implementation has not started.
Milestone: M5 | Suggested size: M | Type: implementation
Depends on: [DL-21](dl-21-benchmark-rust-java-analysis-and-record-performance-budgets.md), [DL-27](dl-27-verify-the-complete-workflow-in-claude-code.md), [DL-30](dl-30-clean-up-closed-reviews-after-confirmed-merges.md), [DL-32](dl-32-validate-the-complete-workflow-inside-a-herdr-pane.md)
Spec: [SPEC.md](../../SPEC.md), sections 7–9.

## Outcome

Make the validated first version reproducible from a clean checkout and ready for review.

## Scope

Likely areas: README.md, docs/getting-started.md, .github/workflows/, packaging/. These paths are proposed implementation locations, not a claim that those modules already exist. Keep the change within this issue; update the paths if the accepted architecture requires it.

## Acceptance criteria

- [ ] Document build/run, target selection, analyzer languages/limitations, skill export/setup, explicit-file mode, controls, and cache lifecycle.
- [ ] Produce a local Windows build artifact and run a clean-install smoke sequence with all required parser assets.
- [ ] Add focused CI checks for formatting, lint/build, contracts, source safety, Git inventory, extraction, and cache invariants using isolated fixtures.
- [ ] Map every SPEC.md acceptance case to evidence or an explicitly unresolved issue; record dependency licenses and known platform limits.

## Validation and evidence

- Run the documented clean-checkout/demo sequence and configured required checks.
- Report tested commit, commands, results, manual evidence, and checks that could not run.
- Report the tested commit/working-tree state, commands, observed results, and acceptance evidence. Clearly identify checks not run.

## Outside this issue

Publishing binaries, marketplace distribution, macOS support, and automatic release deployment.
