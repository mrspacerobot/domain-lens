# Working with Codex on Domain Lens

Research checked: 2026-10-29. This is a project-specific recommendation based on official OpenAI documentation, not a mandatory Codex file layout or a claim that work is already implemented.

## What the official guidance supports

For complex work, plan before coding. Supply the task's goal, relevant context, constraints, and observable completion conditions. Keep durable repository guidance short and practical in AGENTS.md, including real build/check commands. [Codex best practices](https://learn.chatgpt.com/docs/learn/best-practices)

A checked-in plan is a useful optional convention for longer work. Milestones should produce independently verifiable behavior, with validation and material decisions recorded as work progresses. This repository uses PLANS.md plus issue drafts rather than adopting every part of the cookbook's larger execution-plan template. [Execution-plan guidance](https://developers.openai.com/cookbook/articles/codex_exec_plans)

Separate worktrees isolate independent coding tasks while retaining shared repository history. They also give Domain Lens distinct worktree contexts to review. [Codex worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees)

The issue-to-PR workflow emphasizes a scoped task, a prepared environment, and evidence for each acceptance criterion. Its cloud-specific setup is optional for our local Windows/Herdr workflow; the important handoff is a reviewable change with honest check results. [Issue-to-tested-PR guide](https://learn.chatgpt.com/use-cases/issue-to-tested-pr)

OpenAI's September 2026 guidance also cautions against bloated instructions and overly prescriptive recipes. Keep task context relevant and load supporting details only when needed. For this project, the practical consequence is a concise roadmap, provisional later issues, and detailed planning of the currently selected change. [Rethinking skills and prompts](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)

## Recommended project workflow

1. Review the [plan](../PLANS.md) and select one [issue](issues/README.md) whose dependencies are complete. GitHub is the source for current issue status and scope; local issue bodies are planning snapshots.
2. Use a branch/worktree for that coherent change. Keep its spec references, issue, dependency decisions, and relevant files in the task context.
3. Let Codex inspect and briefly explain its approach. For an ambiguous implementation, use Plan mode to settle the local design before building.
4. Implement the selected issue, run its focused checks plus required repository checks, and record evidence. Keep disposable source/Git/UI fixtures isolated from project examples.
5. Review the complete diff and evidence. A Codex review can supplement the human review. Integrate the selected change before assigning dependent work.
6. Update the GitHub issue with actual results; update the roadmap only when sequencing or milestone goals change. Start a new task for a different outcome; retain the conversation when continuing the same unfinished issue.

These are local recommendations drawn from the user's request for small reviewable changes. They do not activate autonomous execution of the backlog, create GitHub issues, start extra agents, or change the user's permissions.

## Issue handoff prompt

```text
Implement DL-XX: <title> only.

Goal:
<the issue's outcome>

Context:
Read SPEC.md, PLANS.md, the current GitHub issue, applicable AGENTS.md,
and the completed dependency changes. Starting revision: <commit>.
Worktree: <absolute path>.

Constraints:
Preserve the agreed unified editor and source-safety behavior.
Keep work within this issue. Treat proposed paths as suggestions until
you inspect the repository. Record material design decisions and gaps.
Use disposable fixtures for file-writing and Git-state checks.

Done when:
Meet every acceptance criterion in the selected issue.
Run its focused validation and required project checks.
Return a concise diff summary, tested revision/state, commands/results,
acceptance evidence, remaining risks, and checks not run.
Finish this issue without starting the next backlog issue.
<Specify whether a local diff or an explicitly authorized draft PR is wanted.>
```

## Practical setup

DL-01 establishes the actual toolchain, commands, minimal checks, and a concise AGENTS.md. This planning change does not install Rust, create repository agent instructions, modify global Codex settings, or invent existing test commands.

Use the client's default available model/reasoning settings initially and adjust to observed task difficulty. No custom agent framework, automatic hooks, or additional orchestration is needed to start this backlog. The flow-generation skill is a product feature to build in DL-25; it is distinct from the workflow used to implement Domain Lens.

## Review evidence to request

- Concrete before/after behavior and the spec/issue criterion it satisfies.
- Exact checks and observed results; unavailable or unrun checks stay explicit.
- For source editing: serialized bytes and recovery behavior.
- For Git: full inventory across all requested states.
- For analysis: source-backed declared facts, uncertainty, reuse correctness, and measured performance.
- For harness/terminal claims: actual Codex, Claude, Windows Terminal, and Herdr observations.
