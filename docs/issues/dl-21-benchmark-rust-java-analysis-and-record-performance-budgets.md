# DL-21: Benchmark Rust/Java analysis and record performance budgets

Status: published as [#21](https://github.com/mrspacerobot/domain-lens/issues/21); implementation has not started.
Milestone: M3 | Suggested size: S | Type: validation
Depends on: [DL-20](dl-20-reuse-unchanged-analysis-facts-with-correct-invalidation.md)
Spec: [SPEC.md](../../SPEC.md), sections 4, 8.

## Outcome

Turn the performance goal into measured, repeatable acceptance targets.

## Scope

Likely areas: benchmarks/, docs/decisions/performance.md. These paths are proposed implementation locations, not a claim that those modules already exist. Keep the change within this issue; update the paths if the accepted architecture requires it.

## Acceptance criteria

- [ ] Define representative Rust/Java project sizes, changed-file counts, machine details, and benchmark commands.
- [ ] Record cold scan, warm unchanged scan, small-edit rescan, peak memory, and source/fact payload size supplied to the agent.
- [ ] Choose and document justified numeric budgets from measurements and intended interactive use.
- [ ] Confirm UI input remains responsive during analysis; record token counts only if actually measured, otherwise report bytes.

## Validation and evidence

- Repeat the documented benchmark on the stated environment with bounded runs.
- Compare changed-file extraction counts and memory with the agreed budgets.
- Report the tested commit/working-tree state, commands, observed results, and acceptance evidence. Clearly identify checks not run.

## Outside this issue

Large synthetic stress campaigns and unmeasured speedup guarantees.
