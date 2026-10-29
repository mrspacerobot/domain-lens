# DL-25: Write and export the shared flow-generation skill

Status: published as [#25](https://github.com/mrspacerobot/domain-lens/issues/25); implementation has not started.
Milestone: M4 | Suggested size: M | Type: implementation
Depends on: [DL-21](dl-21-benchmark-rust-java-analysis-and-record-performance-budgets.md), [DL-24](dl-24-expose-context-analyze-and-flow-import-cli-commands.md)
Spec: [SPEC.md](../../SPEC.md), sections 4, 7.

## Outcome

Author the reusable agent workflow around the implemented Rust CLI and validated contracts.

## Scope

Likely areas: skills/domain-lens-flow/, src/cli/skill_export.rs. These paths are proposed implementation locations, not a claim that those modules already exist. Keep the change within this issue; update the paths if the accepted architecture requires it.

## Acceptance criteria

- [ ] Use the skill-creator workflow when implementing this issue; maintain a shared SKILL.md plus concise contract references and Codex/Claude setup adapters.
- [ ] Tell the agent to obtain context, run the analyzer, inspect relevant source, account for every changed path, build evidence-linked flows, and validate/import.
- [ ] Specify compact fact-first inspection, bounded expansion, unknown/inferred labels, and stale-context recovery.
- [ ] Export to a user-selected directory without installing, overwriting existing skills, changing permissions, or altering harness settings; report missing CLI.

## Validation and evidence

- Inspect exported files and exercise missing dependency and existing-output cases.
- Validate skill packaging and walkthrough against the actual CLI contract; do not claim harness compatibility yet.
- Report the tested commit/working-tree state, commands, observed results, and acceptance evidence. Clearly identify checks not run.

## Outside this issue

Global installation, marketplace publication, and automatic agent launching.
