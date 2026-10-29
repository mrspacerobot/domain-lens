# DL-01: Bootstrap the Rust workspace and repeatable Windows checks

Status: published as [#1](https://github.com/mrspacerobot/domain-lens/issues/1); implementation has not started.
Milestone: M0 | Suggested size: S | Type: implementation
Depends on: none
Spec: [SPEC.md](../../SPEC.md), sections 8.

## Outcome

Establish the minimal buildable application and project commands; retain the Python prototypes as references.

## Scope

Likely areas: Cargo.toml, rust-toolchain.toml, src/, AGENTS.md, README.md. These paths are proposed implementation locations, not a claim that those modules already exist. Keep the change within this issue; update the paths if the accepted architecture requires it.

## Acceptance criteria

- [ ] Document a supported Rust toolchain and Windows prerequisites, checking the actual machine before claiming anything is installed.
- [ ] A minimal binary prints help and exits cleanly; dependencies are pinned through Cargo.lock.
- [ ] Add concise repository guidance with real build/check commands, issue scope, and fixture-only editing for tests.
- [ ] Document how to build and run from a clean checkout; record the starting commit and existing changes.

## Validation and evidence

- Run cargo fmt --check, cargo check, and the minimal binary's --help after the workspace exists.
- Record missing prerequisites instead of silently installing tools or reporting unrun checks as passing.
- Report the tested commit/working-tree state, commands, observed results, and acceptance evidence. Clearly identify checks not run.

## Outside this issue

Editor, Git integration, analysis, user-level agent settings.
