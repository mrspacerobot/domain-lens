# GitHub implementation issues

All 33 issues for the [implementation plan](../../PLANS.md) are published in [mrspacerobot/domain-lens](https://github.com/mrspacerobot/domain-lens/issues). The table maps local planning IDs to actual GitHub issue numbers. The individual files preserve the original planning snapshots; GitHub owns current issue scope, dependencies, acceptance evidence, and status. Implementation had not started when these snapshots were published on 2026-10-29.

Each issue has one outcome, dependencies, acceptance criteria, focused validation, and an explicit boundary. S means a narrow change or validation pass; M means one coherent implementation change. These are relative scope labels, not time estimates. Split an M issue before implementation if its discovery shows that it cannot remain a reviewable change.

Each published issue includes scope, acceptance criteria, focused validation, and links to its actual dependency issues. Suggested milestone names below are planning groups, not existing GitHub milestones. Use the goal/context/constraints/done template in [the Codex workflow](../CODEX_WORKFLOW.md) to hand off one selected issue. Read the checked-in SPEC.md and PLANS.md when assigning implementation. The publication receipt is recorded in github-publication.json.

| ID | Local body | Milestone | Size | Depends on | GitHub |
|---|---|---|---|---|---|
| DL-01 | [Bootstrap the Rust workspace and repeatable Windows checks](dl-01-bootstrap-the-rust-workspace-and-repeatable-windows-checks.md) | M0 | S | — | [#1](https://github.com/mrspacerobot/domain-lens/issues/1) |
| DL-02 | [Define versioned review, source-fact, and flow contracts](dl-02-define-versioned-review-source-fact-and-flow-contracts.md) | M0 | M | DL-01 | [#2](https://github.com/mrspacerobot/domain-lens/issues/2) |
| DL-03 | [Validate the inline editor library with a disposable demo](dl-03-validate-the-inline-editor-library-with-a-disposable-demo.md) | M0 | M | DL-01, DL-02 | [#3](https://github.com/mrspacerobot/domain-lens/issues/3) |
| DL-04 | [Implement source-to-screen mapping for inline change annotations](dl-04-implement-source-to-screen-mapping-for-inline-change-annotations.md) | M1 | M | DL-02, DL-03 | [#4](https://github.com/mrspacerobot/domain-lens/issues/4) |
| DL-05 | [Add standard editing controls and syntax highlighting](dl-05-add-standard-editing-controls-and-syntax-highlighting.md) | M1 | M | DL-04 | [#5](https://github.com/mrspacerobot/domain-lens/issues/5) |
| DL-06 | [Add optional Vim navigation and editing](dl-06-add-optional-vim-navigation-and-editing.md) | M1 | M | DL-05 | [#6](https://github.com/mrspacerobot/domain-lens/issues/6) |
| DL-07 | [Preserve encoding and newline conventions when loading and saving](dl-07-preserve-encoding-and-newline-conventions-when-loading-and-saving.md) | M1 | M | DL-02, DL-04 | [#7](https://github.com/mrspacerobot/domain-lens/issues/7) |
| DL-08 | [Guard unsaved edits and provide external-change recovery](dl-08-guard-unsaved-edits-and-provide-external-change-recovery.md) | M1 | M | DL-05, DL-07 | [#8](https://github.com/mrspacerobot/domain-lens/issues/8) |
| DL-09 | [Resolve repository identity and a fixed review baseline](dl-09-resolve-repository-identity-and-a-fixed-review-baseline.md) | M2 | M | DL-01, DL-02 | [#9](https://github.com/mrspacerobot/domain-lens/issues/9) |
| DL-10 | [Build the complete branch change inventory](dl-10-build-the-complete-branch-change-inventory.md) | M2 | M | DL-09 | [#10](https://github.com/mrspacerobot/domain-lens/issues/10) |
| DL-11 | [Load baseline, current, staged, and deleted-file representations](dl-11-load-baseline-current-staged-and-deleted-file-representations.md) | M2 | M | DL-07, DL-09, DL-10 | [#11](https://github.com/mrspacerobot/domain-lens/issues/11) |
| DL-12 | [Build the flow viewer and source navigation](dl-12-build-the-flow-viewer-and-source-navigation.md) | M2 | M | DL-02, DL-05, DL-08 | [#12](https://github.com/mrspacerobot/domain-lens/issues/12) |
| DL-13 | [Connect changed-file navigation and staged detail to the viewer](dl-13-connect-changed-file-navigation-and-staged-detail-to-the-viewer.md) | M2 | M | DL-10, DL-11, DL-12 | [#13](https://github.com/mrspacerobot/domain-lens/issues/13) |
| DL-14 | [Handle explicit branch and worktree switches safely](dl-14-handle-explicit-branch-and-worktree-switches-safely.md) | M2 | M | DL-08, DL-09, DL-13 | [#14](https://github.com/mrspacerobot/domain-lens/issues/14) |
| DL-15 | [Capture consistent generation snapshots](dl-15-capture-consistent-generation-snapshots.md) | M3 | M | DL-02, DL-07, DL-09, DL-10 | [#15](https://github.com/mrspacerobot/domain-lens/issues/15) |
| DL-16 | [Implement the Rust analyzer runner and coverage diagnostics](dl-16-implement-the-rust-analyzer-runner-and-coverage-diagnostics.md) | M3 | M | DL-02, DL-15 | [#16](https://github.com/mrspacerobot/domain-lens/issues/16) |
| DL-17 | [Extract Rust declarations and candidate call sites](dl-17-extract-rust-declarations-and-candidate-call-sites.md) | M3 | M | DL-16 | [#17](https://github.com/mrspacerobot/domain-lens/issues/17) |
| DL-18 | [Extract Java declarations and candidate call sites](dl-18-extract-java-declarations-and-candidate-call-sites.md) | M3 | M | DL-16 | [#18](https://github.com/mrspacerobot/domain-lens/issues/18) |
| DL-19 | [Expand analysis into relevant unchanged source](dl-19-expand-analysis-into-relevant-unchanged-source.md) | M3 | M | DL-10, DL-17, DL-18 | [#19](https://github.com/mrspacerobot/domain-lens/issues/19) |
| DL-20 | [Reuse unchanged analysis facts with correct invalidation](dl-20-reuse-unchanged-analysis-facts-with-correct-invalidation.md) | M3 | M | DL-15, DL-19 | [#20](https://github.com/mrspacerobot/domain-lens/issues/20) |
| DL-21 | [Benchmark Rust/Java analysis and record performance budgets](dl-21-benchmark-rust-java-analysis-and-record-performance-budgets.md) | M3 | S | DL-20 | [#21](https://github.com/mrspacerobot/domain-lens/issues/21) |
| DL-22 | [Validate flow documents and adapt the original fixture](dl-22-validate-flow-documents-and-adapt-the-original-fixture.md) | M4 | M | DL-02, DL-15 | [#22](https://github.com/mrspacerobot/domain-lens/issues/22) |
| DL-23 | [Publish cached flow revisions atomically with concurrency checks](dl-23-publish-cached-flow-revisions-atomically-with-concurrency-checks.md) | M4 | M | DL-22 | [#23](https://github.com/mrspacerobot/domain-lens/issues/23) |
| DL-24 | [Expose context, analyze, and flow-import CLI commands](dl-24-expose-context-analyze-and-flow-import-cli-commands.md) | M4 | M | DL-15, DL-19, DL-22, DL-23 | [#24](https://github.com/mrspacerobot/domain-lens/issues/24) |
| DL-25 | [Write and export the shared flow-generation skill](dl-25-write-and-export-the-shared-flow-generation-skill.md) | M4 | M | DL-21, DL-24 | [#25](https://github.com/mrspacerobot/domain-lens/issues/25) |
| DL-26 | [Verify the complete workflow in Codex CLI](dl-26-verify-the-complete-workflow-in-codex-cli.md) | M4 | M | DL-13, DL-14, DL-23, DL-25 | [#26](https://github.com/mrspacerobot/domain-lens/issues/26) |
| DL-27 | [Verify the complete workflow in Claude Code](dl-27-verify-the-complete-workflow-in-claude-code.md) | M4 | S | DL-26 | [#27](https://github.com/mrspacerobot/domain-lens/issues/27) |
| DL-28 | [Refresh disk, Git, and accepted flows without losing buffers](dl-28-refresh-disk-git-and-accepted-flows-without-losing-buffers.md) | M5 | M | DL-14, DL-15, DL-23, DL-26 | [#28](https://github.com/mrspacerobot/domain-lens/issues/28) |
| DL-29 | [Bound cached flows and analysis artifacts and add manual cleanup](dl-29-bound-cached-flows-and-analysis-artifacts-and-add-manual-cleanup.md) | M5 | M | DL-20, DL-23, DL-28 | [#29](https://github.com/mrspacerobot/domain-lens/issues/29) |
| DL-30 | [Clean up closed reviews after confirmed merges](dl-30-clean-up-closed-reviews-after-confirmed-merges.md) | M5 | S | DL-09, DL-23, DL-29 | [#30](https://github.com/mrspacerobot/domain-lens/issues/30) |
| DL-31 | [Validate Windows Terminal behavior and failure recovery](dl-31-validate-windows-terminal-behavior-and-failure-recovery.md) | M5 | M | DL-06, DL-13, DL-28, DL-29 | [#31](https://github.com/mrspacerobot/domain-lens/issues/31) |
| DL-32 | [Validate the complete workflow inside a Herdr pane](dl-32-validate-the-complete-workflow-inside-a-herdr-pane.md) | M5 | S | DL-27, DL-30, DL-31 | [#32](https://github.com/mrspacerobot/domain-lens/issues/32) |
| DL-33 | [Package the first Windows build and document the complete demo](dl-33-package-the-first-windows-build-and-document-the-complete-demo.md) | M5 | M | DL-21, DL-27, DL-30, DL-32 | [#33](https://github.com/mrspacerobot/domain-lens/issues/33) |

## Suggested milestones

- M0: build foundation, contracts, and editor feasibility.
- M1: safe unified source editing.
- M2: complete branch review.
- M3: Rust and Java source analysis.
- M4: validated agent handoff in both harnesses.
- M5: refresh, bounded lifecycle, and target-terminal readiness.

The first issue to select for implementation is DL-01. DL-03 is an explicit feasibility gate: settle the editor architecture before proceeding with the product editor. Rust and Java share extraction infrastructure but have separate language issues. All later readiness claims require the actual interactive and harness evidence in their validation issues.
