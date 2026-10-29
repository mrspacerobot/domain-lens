# Domain Lens implementation roadmap

[SPEC.md](SPEC.md) defines product behavior. [GitHub issues](https://github.com/mrspacerobot/domain-lens/issues) track implementation scope, dependencies, acceptance evidence, and status. This roadmap records milestone goals and sequencing; it does not duplicate issue progress.

The [issue index](docs/issues/README.md) maps DL-01 through DL-33 to GitHub. Local issue bodies are planning snapshots; use the current GitHub issue when selecting work. [Working with Codex](docs/CODEX_WORKFLOW.md) provides the task handoff template.

## Starting point and sequence

As of 2026-10-29, the repository contains Python prototypes, a fixed skiing flow, research, and the product spec. Rust implementation has not started. Preserve the prototypes and example source as interaction and visual references until their replacements are validated. They are not evidence of analyzer or agent integration support.

Start with [#1: Rust workspace and Windows checks](https://github.com/mrspacerobot/domain-lens/issues/1), then [#2: shared contracts](https://github.com/mrspacerobot/domain-lens/issues/2), then [#3: inline editor feasibility](https://github.com/mrspacerobot/domain-lens/issues/3). Resolve the editor adopt/adapt/replace decision before production editor work. Check actual toolchain availability in #1.

The agreed direction is editor feasibility, Rust/Java analysis, then shared skill integration, with each issue's dependencies respected. After contracts, repository/baseline work (#9-10) can proceed independently of most editor work. Rust and Java extraction (#17 and #18) share the analyzer infrastructure from #16.

Select one ready issue at a time and refine its details against current code and completed dependencies. Later issue scopes remain provisional. Each issue should produce one coherent, reviewable change; split work if discovery makes that impractical.

## Milestones and exit evidence

| Milestone | Issues | Working result | Exit evidence |
|---|---|---|---|
| M0: foundation and feasibility | DL-01–03 | Buildable Rust shell, shared contracts, disposable inline editor experiment | Repeatable local checks; explicit editor adopt/adapt/replace decision |
| M1: safe editor | DL-04–08 | Unified editable current source with read-only deletions, standard/Vim controls, safe save/recovery | Projection invariants, byte round trips, and dirty/external-change recovery |
| M2: branch review | DL-09–14 | Real baseline and full file inventory alongside fixture flow, source navigation, staged detail | Disposable Git-state matrix; every path reachable; guarded context switches |
| M3: Rust/Java analysis | DL-15–21 | Consistent source facts, context expansion, correct reuse, measured performance | Hand-checked extraction fixtures, invalidation cases, cold/warm time and memory report |
| M4: agent handoff | DL-22–27 | Context/analyze/import, atomic publication, exported skill, both actual harnesses | Real Codex CLI and Claude Code generation/import/view passes on the same fixture |
| M5: release readiness | DL-28–33 | Refresh, bounded lifecycle, merge cleanup, target-terminal behavior, reproducible Windows artifact | Race/recovery checks, actual Windows Terminal and Herdr passes, documented clean demo |

Issue dependency lists govern execution order; milestone ranges are planning groups. M2 is the earliest useful branch-review demonstration, using an explicit flow fixture. M4 adds automatically generated domain flows. First-version readiness requires M5 evidence.

## Validation and handoff

Read the spec, selected issue, applicable repository instructions, and dependency results before implementation. DL-01 establishes actual build/check commands. Expected checks after bootstrap are `cargo fmt --check`, `cargo check`, `cargo test`, and `cargo clippy --all-targets -- -D warnings`; they have not been run for this documentation change.

Use disposable fixtures for source-writing, Git-state, and UI checks. Record the tested revision/working-tree state, changed behavior, acceptance evidence, commands/results, and unresolved limitations. Actual terminal and agent-harness checks remain pending until performed there. Finish the selected issue before taking on another.

Update GitHub for task progress. Update this roadmap when sequencing or milestone goals change, and the spec when product decisions change.

## Spec coverage

| Spec requirement | Owning issues |
|---|---|
| Editable current lines, immutable removal annotations, line mapping, source-only serialization | DL-03–05 |
| Standard controls, optional Vim, syntax colors independent of diff markers | DL-05–06 |
| New/deleted/binary/unsupported files, LF/CRLF/BOM and missing final newline | DL-07, DL-11 |
| Save/discard/cancel and external-file recovery | DL-07–08, DL-14, DL-28 |
| Fixed merge base, explicit target, identity and detached HEAD | DL-09, DL-14–15 |
| Committed/staged/local/untracked union, renames/conflicts, canceled changes | DL-10–11, DL-13 |
| Flow palette, contracts/directions, unchanged context, source-range selection, multiple named flows | DL-02, DL-12, DL-19 |
| Complete file navigation even with missing/partial flows | DL-12–13, DL-22, DL-26 |
| Rust and Java extraction, unknown/inferred labels, scope expansion | DL-16–19 |
| Snapshot consistency, source evidence, freshness and reuse invalidation | DL-15, DL-20, DL-22, DL-28 |
| Performance measurements and responsive UI | DL-16, DL-20–21, DL-28 |
| Context/analyze/import/explicit-file/ASCII/export interfaces | DL-01, DL-12, DL-24–25, DL-31 |
| Concurrent publishers, complete revisions, current/previous recovery | DL-23, DL-28–29 |
| Multiple worktrees and same-worktree combined review | DL-09–10, DL-14, DL-23, DL-26, DL-32 |
| Shared skill export and actual Codex/Claude compatibility | DL-25–27 |
| Bounded cache, manual cleanup and confirmed-merge cleanup | DL-29–30 |
| Windows Terminal, Herdr, 80x24/140x40, mouse/keyboard, resize, ASCII | DL-12, DL-31–32 |
| Build/run instructions, repeatable checks, dependency distribution and readiness evidence | DL-01, DL-33 |

## Decisions still to resolve

- DL-03: editor adaptation or replacement and compatible dependency versions.
- DL-02/DL-15/DL-24: exact contracts, source coordinates, capture strategy, and CLI options.
- DL-13: staged-content detail presentation inside the unified workspace.
- DL-16–19: grammar coverage and bounded analysis expansion. Compiler/LSP-backed inference remains an optional later capability, not required to emit declared facts.
- DL-21: representative benchmarks and numerical performance budgets.
- DL-23/DL-29: cross-process locking/leases, finite default disk budget, and accounting for temporary data.
- DL-30: conservative cleanup when worktrees/refs disappear or merge status is uncertain.

Resolve these in their owning issue and record the outcome with evidence. Additional source languages, runtime payload capture, native Herdr extensions, automatic agent launching, Git mutation controls, deep graph drill-down, and macOS readiness are outside the first implementation.
