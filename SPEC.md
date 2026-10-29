# Domain Lens: product spec and integration proposal

Status: draft, 2026-10-29. Product requirements below come from the design interview. Technical proposals are labeled separately and still need implementation validation.

The Python prototypes remain the interaction and visual reference. This document revises the earlier implementation draft; it does not describe features already shipped. No Rust app, flow-generation skill, or agent integration currently exists in this repository.

## 1. Confirmed product requirements

The developer writes a spec, asks an agent to implement it, and opens Domain Lens to understand and review the resulting branch. The intended unit of work is a deliberately manageable branch.

| Requirement | Agreed behavior |
|---|---|
| Review scope | Include everything changed on the branch, whether committed, staged, or still being worked on. Unexpected changes remain visible so the developer can correct them or ask the agent to do so. |
| Flow | Keep the prototype-style request/response flow: browser, handler, service, downstream components, and relevant domain boundaries. |
| Selection | Selecting a component opens its code beside the flow. Keep the flow visible; hierarchical navigation and expanding subgraphs are outside the initial scope. |
| Contracts | Explain interfaces or method names and input/output types. Example payloads and captured runtime values are not initial requirements. |
| Context | Include unchanged components when needed to explain the complete relevant data flow. Distinguish changed components from unchanged context. |
| Editing and review | One editable code view with inline change highlights. Source and diff are parts of the same experience. |
| Environment | Work alongside an agent in another Herdr tab/pane, including a workflow with multiple agents. |
| Source analysis | Implement the analyzer and viewer in Rust. Support Rust and Java source first, extracting interface and declared input/output facts for the agent to use when explaining domain flows. |

The flow explains the relevant request paths around the branch changes. It need not map every part of the application. If the branch affects multiple independent paths, show a small set of named flows and retain a complete changed-file inventory across them (proposed presentation).

## 2. Screen and interaction

Preserve the existing Forest Night direction: charcoal green background, mint and soft orange accents, restrained borders, visible selection, readable code.

At a useful terminal width, show the flow on the left and the selected component's code on the right. Show its interface, input/output types, and a short explanation near the selected component or code. Request and response direction must be explicit in words/arrows, as well as color.

Selecting a component should reveal the linked source range in its file, with surrounding code available by scrolling. Selecting another component in the same file must move to that component. A changed-file list also opens files not represented by a graph node; agent-generated flows must never hide changes.

Proposed editor behavior:

- Added and unchanged current-file lines are editable. Removed baseline lines appear as read-only annotations at their relevant positions.
- Only the current file contents enter the editable buffer. Deleted-line annotations, diff prefixes, and old line numbers must never be saved into source.
- Distinguish original and current line numbers. A replacement is a deleted annotation plus editable current text.
- Syntax highlighting describes tokens. Change markers use a separate gutter/background treatment and explicit `+`/`-` labels.
- Edits update inline highlights against the same review baseline. Clearly label unsaved buffers; the branch inventory and disk state remain distinct until save.
- Use explicit Save (Ctrl+S), normal text insertion, undo/redo, selection and paste. Single character app shortcuts must not consume typed code.
- Switching files, switching branches/worktrees, reloading, or quitting with a dirty buffer offers Save / Discard / Cancel.
- If another process changes a dirty file, preserve the buffer and offer a recovery path: save a separate copy, deliberately reload, or cancel. Never silently overwrite external work.
- New text files open as editable additions. Deleted files show baseline text read-only. Binary files, unsupported encodings, and unsupported file types get an explicit read-only state.

At narrow sizes, keep the selected component, source, and essential controls usable through a compact layout. Validate 80x24 and 140x40 separately; they should preserve the workflow rather than have identical layouts.

Full keyboard operation is required; retain mouse selection and scrolling. Standard editor controls are the default: arrow keys, Page Up/Down, and mouse-wheel scrolling. Offer an optional Vim mode for navigation and editing, with a visible mode indicator. Exact Vim key coverage, remaining key bindings, and the compact layout still need implementation validation.

## 3. Proposed branch comparison semantics

The user asked for all branch changes. The proposed default is the net difference between the branch's comparison base and its current files, with new files included separately. This is a review of the current result, rather than a chronological playback of every intermediate edit.

1. Select a target branch/ref on first use, or supply `--target`. A previously selected target can be reused for that branch. Show the actual target and resolved base commit; do not silently guess an upstream is the intended target.
2. Resolve the merge base between that target and HEAD and hold it fixed for the review session. Changing the target or resetting the baseline is an explicit action.
3. Compare that base with tracked files in the working tree. This includes the current effect of committed, staged, and unstaged edits.
4. Enumerate non-ignored untracked files as new work. Include renamed, deleted, binary, and conflicted paths in the inventory with explicit labels.
5. Build the file inventory from the union of base-to-HEAD, base-to-index, base-to-working-tree, local status, and untracked paths. A staged change that has been undone in the working tree must still be visible as an index discrepancy.
6. Keep staged/unstaged status as file information within the same review workspace. If the index contains different content, provide a read-only staged-content annotation/detail without making it the editable current file. Exact presentation needs a prototype.
7. Changes canceled out across those states may have no net line highlight. Explain that status rather than reporting no work. A per-commit history browser is deferred.
8. Include all changes in the selected worktree regardless of who made them. Git state alone does not identify which agent or human owns a change.

Use Git CLI subprocesses with argument arrays, an explicit working directory, and validated revisions. Disable external diff helpers/text conversions for machine parsing and request predictable output. Use NUL-delimited status/name records for paths. Show errors for missing Git, invalid targets, merge conflicts, or no usable base. Detached HEAD can use a selected target; it is not inherently an error.

A plain `git diff target...HEAD` is insufficient for the default because it only compares committed endpoints. Git's commit-to-working-tree comparison and separate status/index inspection supply the additional states. See the Git references below.

## 4. Proposed agent integration

### Responsibility split

The Rust analyzer extracts structured source facts; the agent uses those facts and relevant source to explain the domain flow. Domain Lens owns project identity, Git state, source loading/editing, analysis, flow validation, and freshness checks. Local JSON contracts connect the analyzer, agent, and viewer.

This avoids requiring an active-tab API or private agent conversation format. A Herdr pane runs the viewer in the same actual project directory used by the coding agent. Native Herdr extensions are not a prerequisite for this proposal; terminal behavior inside Herdr still needs testing.

### Rust analyzer and initial source languages

Rust and Java are the initial supported source languages. The analyzer itself is implemented in Rust and exposed through the Domain Lens CLI. Additional source languages are deferred. The Python skiing fixture remains a viewer demonstration, not evidence of Python analyzer support.

- Extract Rust functions, methods, trait/implementation declarations, and Java classes, interfaces, methods, and constructors, with source locations, parameter names, and declared parameter/return types where present.
- Record imports and syntactic call sites as evidence or candidate relationships. Parsing alone does not establish the exact call target, inferred types, dynamic dispatch, runtime values, or an entire cross-system request path. Report unavailable information as unknown and inferred relationships explicitly.
- The skill instructs the agent to run the shared analyzer, inspect relevant source where facts are incomplete, connect the facts into domain flows, and validate/import the explanation. Keep extraction logic in the Rust tool rather than asking each agent to invent a new scanner.
- Begin with the complete branch inventory and changed source, then expand into relevant unchanged callers and dependencies as needed. Preserve the full file inventory even for unsupported languages, parse failures, and unmapped paths; report analysis coverage and limitations.
- Reuse content-keyed facts for unchanged files and evaluate incremental parsing for edits. Include analyzer/grammar versions and analysis options in reuse keys. Changes to dependencies or the path inventory must invalidate affected relationship results even when a caller's own text is unchanged. All facts must correspond to the generation snapshot used for flow publication.
- Measure cold scans, warm rescans, peak memory, and the amount of context supplied to the agent on representative Rust and Java projects. Agree on benchmark fixtures and numerical budgets during the analyzer experiment; performance is not established by choosing Rust alone. Keep parsing and agent generation off the interactive UI event loop.

Tree-sitter with Rust bindings and Rust/Java grammars is the initial parsing candidate. Deeper type and call resolution may require language-specific compiler or language-server adapters; these are separate capabilities to validate, not assumed parser features. The first analyzer promises inspectable declared facts and clearly labeled gaps.

### First complete workflow

All names/commands in this section are proposed interfaces and are not implemented yet.

1. Open Domain Lens on the exact project/worktree being edited, for example `domain-lens . --target main`.
2. Include the flow-generation instruction with the implementation task, or explicitly ask for a flow when ready to review. Both call the same generation workflow; implicit skill matching is not a completion guarantee.
3. A proposed `domain-lens-flow` skill has the agent request a generation context, run the Rust analyzer for structured facts, inspect the complete branch change set and relevant unchanged callers/dependencies, and produce an evidence-linked flow tied to that snapshot.
4. The agent imports the generated JSON through the Domain Lens CLI. The tool validates it and writes the accepted flow to its local cache.
5. The open viewer notices the accepted revision and loads it while preserving selection and unsaved source buffers.
6. Further code changes update Git/source state and mark the explanation stale. Ask the agent to refresh the flow using the same workflow.

A Codex prompt could explicitly name the proposed skill: `After implementing the spec, use $domain-lens-flow to prepare the branch for review.` This becomes usable only after that skill is built and installed. Codex supports explicit skill invocation and user-scoped skills; see official documentation below.

Other harnesses can use the same flow format, CLI and instruction content, with harness-specific discovery/invocation packaging. Portability of one installed skill across harnesses must be tested rather than assumed.

### Skill packaging and initial compatibility targets

Propose Codex CLI and Claude Code as the first two supported producers. Maintain one shared Agent Skills bundle: a `SKILL.md` with standard name/description metadata, the generation instructions, and shared format references. Both agents call the same Domain Lens CLI and produce the same JSON contract. Keep harness-specific metadata or invocation guidance in small adapters; avoid depending on one harness's hooks or prompt substitutions in the shared instructions.

Export the bundle to a user-selected directory, with installation instructions for the chosen harness. For local use, Codex documents user skills under `~/.agents/skills/domain-lens-flow/` and explicit invocation as `$domain-lens-flow`; Claude Code documents `~/.claude/skills/domain-lens-flow/` and `/domain-lens-flow`. These are documented integration points, not evidence that our unbuilt skill already works in either product.

The agents load the skill instructions. Domain Lens imports the resulting flow JSON. Skill installation is a separate setup step from generating/importing a flow for a particular branch. Export must not silently install files into user settings, overwrite existing skills, or alter permissions. Wider plugin/marketplace distribution can follow after local compatibility is validated.

Acceptance requires an end-to-end generation/import pass in both Codex CLI and Claude Code on the same small branch, plus clear missing-CLI, permissions and stale-context errors. Exported instructions alone do not establish compatibility.

### What the skill must do

- Read the developer's spec when available, but derive claims about implemented behavior from actual source.
- Inspect all branch changes, including new files and local changes, not just its own last patch.
- Run the Rust analyzer for Rust and Java source, reuse its structured facts, and inspect relevant source to address gaps. Explain missing CLI, unsupported languages, and partial analysis explicitly.
- Trace the relevant request/response paths across domain boundaries and retain necessary unchanged context.
- Record interface/method names and input/output types. Use `unknown` for unavailable type information rather than inventing a contract.
- Link component source ranges and evidence for relationships. Mark inferred or unknown relationships explicitly.
- Account for changed paths absent from the map as unmapped or outside this flow; preserve them in the review inventory.
- Publish only after validation, and report any uncovered areas or stale snapshot instead of claiming completion.

The initial workflow uses an explicit skill request or an explicit instruction in the implementation task. Automatic finish hooks, automatic agent launch from the viewer, and live agent activity tracking are deferred.

## 5. Matching the right project and multiple agents

Proposed identity is derived by Domain Lens from Git and filesystem state, rather than chosen by the agent:

- Repository: canonical shared Git directory, obtained using `git rev-parse --path-format=absolute --git-common-dir`.
- Worktree: canonical worktree root from `git rev-parse --show-toplevel`.
- Review context: worktree plus branch identity (or detached HEAD), selected target, resolved baseline, and an opaque context ID. Store HEAD as snapshot metadata rather than relying on the branch name alone.
- Agent/harness identity: optional provenance, never the cache lookup key or proof of change ownership.

| Situation | Proposed behavior |
|---|---|
| Multiple agents in separate worktrees | Separate contexts and flows. Open the appropriate worktree path or select it explicitly from Git's worktree list. |
| Multiple agents sharing one worktree | One combined branch review. A designated publishing/coordinating agent generates the complete flow after shared edits settle. Other agents do not silently overwrite it with partial maps. |
| Branch changes in the same folder | Detect the change, guard unsaved edits, and select the matching context or show a missing-flow state. Never label the previous branch's graph current. |
| Another publisher imports concurrently | Serialize publication and require the expected accepted revision. Reject an out-of-date publication rather than silently replacing newer analysis. |
| No flow exists | Show Git changes and editable source immediately, plus an explicit instruction for generating a flow. Never manufacture an authoritative map. |

Separate worktrees are the proposed way to keep independent tasks isolated. Domain Lens does not create branches, merge work, or attribute edits to individual agents in the initial scope.

## 6. Flow contract, cache and freshness

Proposed schema version 2 adds structured contracts, source ranges and evidence. The original `example-flow.json` remains a loadable version-1 demonstration through a compatibility adapter. Missing confidence/evidence in old documents means unknown; missing freshness metadata means freshness cannot be established.

An illustrative version-2 agent payload:

```json
{
  "schema_version": 2,
  "generation_context": "context-issued-by-domain-lens",
  "flows": [
    {
      "id": "ski-report",
      "label": "Ski report request",
      "nodes": [
        {
          "id": "handler",
          "label": "RequestHandler",
          "role": "component",
          "source": {
            "path": "examples/ski_flow.py",
            "symbol": "RequestHandler.handle",
            "line_start": 13,
            "line_end": 15
          }
        },
        {
          "id": "service",
          "label": "SnowService",
          "role": "component",
          "source": {
            "path": "examples/ski_flow.py",
            "symbol": "SnowService.report",
            "line_start": 21,
            "line_end": 23
          }
        }
      ],
      "edges": [
        {
          "from": "handler",
          "to": "service",
          "kind": "call",
          "interface": "SnowService.report",
          "inputs": [{ "name": "resort", "type": "str" }],
          "output": { "type": "WeatherReport" },
          "confidence": "evidenced",
          "evidence": [
            { "path": "examples/ski_flow.py", "line_start": 14, "line_end": 14 },
            { "path": "examples/ski_flow.py", "line_start": 21, "line_end": 23 }
          ]
        }
      ]
    }
  ]
}
```

This example illustrates one connection, not complete coverage of the skiing fixture. The import tool attaches the authoritative repository/worktree identity, base, HEAD, generation timestamp, file fingerprints, changed-file inventory, producer information, and accepted revision. It must not trust agent-supplied project identity as a replacement for the active context.

Validation must reject unsupported versions, duplicate IDs, missing edge endpoints, invalid ranges, wrong contexts, and paths escaping the selected worktree (including symlink escapes). External components may have no local source. Unknown or inferred edges remain visibly labeled. An `evidenced` edge requires inspectable evidence, but the label is an agent's source-backed claim, not proof of runtime behavior.

Freshness/publication proposal:

- The generation context captures HEAD, baseline, index state, path inventory and file fingerprints before analysis. Detect changes during capture and retry rather than presenting an inconsistent snapshot.
- At import, compare the analysis snapshot with current state, including analyzed unchanged source and newly added/deleted paths. Reject or require regeneration when it no longer matches. Fingerprints must refer to the captured source, not be retroactively attached to an old explanation.
- Store flows outside the repository under the OS local cache directory. Hash the canonical repository/worktree/context identities; never interpolate arbitrary agent IDs into cache paths.
- Write complete revisions atomically and retain the previous accepted revision for recovery. Serialize concurrent imports and check expected revision inside the publication lock.
- The viewer refreshes Git/file state using debounced watching or polling. Missing, incomplete, stale and freshness-unknown are distinct visible states. Watching source does not itself regenerate the explanation.
- Derive change markers from Git and linked source ranges. If only file-level matching is available, label `file changed` rather than asserting a particular component changed.
- Keep generated flow data local and out of pull requests by default. Retain at most the current and previous accepted revision per review context.
- After a review closes, remove its cached flows when Git confirms the reviewed branch tip is included in the selected target and there is no newer committed, staged, working-tree, or untracked work. Protect open reviews and unsaved buffers. If the worktree or merge state cannot be verified, retain the cache for routine cleanup.
- Squash/rebase merges do not require hosting-service integration for cleanup. When local Git ancestry cannot confirm a merge, keep the flow subject to the normal cache budget; do not infer completion from a deleted branch alone.
- Enforce a finite, configurable total disk budget across all cached review contexts and analysis artifacts. On startup and publication, evict the least recently used inactive contexts as needed. Coordinate eviction with publication and protect open reviews; if protected data would exceed the budget, report the limit instead of allowing unbounded growth. The default budget is an implementation decision.
- Provide a manual command to clear inactive cached flows. Cleanup removes generated cache data only; source files, installed skills, and unsaved edits are preserved. Evicted flows can be regenerated through the normal workflow.

Exact JSON Schema, snapshot performance limits, cache locking, the default disk budget, and cleanup scheduling must be finalized during the implementation experiments. The lifecycle and bounded-storage requirements above are agreed behavior.

## 7. Proposed CLI surface

| Interface | Purpose |
|---|---|
| `domain-lens [PATH] --target REF` | Open a review in a selected worktree; reuse a stored target only when its context matches. |
| `domain-lens context [PATH] --target REF` | Emit a machine-readable generation context and snapshot reference for the agent. |
| `domain-lens analyze [PATH] --context ID` | Extract snapshot-linked Rust/Java source facts and coverage diagnostics as JSON for the agent; exact options and fact schema need validation. |
| `domain-lens flow import FILE --context ID --expected-revision REV` | Validate and publish to the matching local context. First publication explicitly expects no prior revision. |
| `domain-lens [PATH] --flow FILE` | Load an explicit flow for demos, testing, or environments where cache access is unavailable. |
| `domain-lens [PATH] --ascii` | Use ASCII UI glyphs where needed. Source text remains intact. |
| `domain-lens skill export --agent codex\|claude --output DIR` | Export the shared skill bundle with the selected harness's setup/invocation instructions; do not install it automatically. |

Cache permissions must fit the agent's sandbox. Use explicitly accessible handoff locations or an explicit file mode when necessary; installing a skill does not grant filesystem permissions. Do not modify harness settings or user instructions automatically.

## 8. Implementation proposal and checkpoints

The [implementation plan](PLANS.md) expands these checkpoints into ordered milestones and [GitHub-ready issue drafts](docs/issues/README.md). It records dependencies and validation; implementation has not started.

Rust is the implementation language for the viewer and analyzer. Initial library candidates are Ratatui/Crossterm for the terminal UI, Edtui for editing, Tree-sitter with Rust/Java grammars for source facts, and Serde/serde_json for the exchange contracts. Use the Git CLI for repository state and comparisons initially. Pin compatible library versions after focused validation.

Edtui is an editor candidate, not a settled choice. Its ability to support standard controls, optional Vim mode, and the unified editable view with read-only deleted annotations must be proved early. A separate source/diff mode is not an acceptable fallback for the agreed product interaction.

Windows and the user's Herdr workflow are the first validation environment. macOS support, 80-column usability, keyboard/mouse and ASCII support remain proposed portability targets; they are not already verified.

1. **Unified editing experiment:** preserve the prototype flow and palette; show a real file beside it, with editable current lines and read-only deleted annotations. Validate cursor movement, selection, paste, undo, source-range navigation and save serialization.
2. **Branch review:** implement the complete file inventory and fixed baseline, including committed/local/new/deleted/renamed files and staged discrepancies. Ensure every changed path is reachable even without a graph.
3. **Analyzer and real flow handoff:** validate Rust/Java fact extraction, snapshot reuse, and performance, then implement context/analyze/import and the generator instructions/skill together. Generate and review a flow for an actual small branch in each supported source language, including unchanged components and evidence.
4. **Refresh and concurrency:** verify stale detection, branch switches, live updates without losing unsaved edits, separate worktrees and conflicting publishers.
5. **Terminal hardening:** test Windows Terminal and a Herdr pane, narrow sizes, resize, mouse, encoding/newlines and failure recovery; then validate additional platforms.

No Rust toolchain was found on PATH during the project review. Toolchain setup, the proposed CLI and the generator skill are implementation work still to do.

## 9. Acceptance cases

- Starting from a spec-driven small feature branch, an agent generates a flow and an independently opened viewer finds the correct worktree/context without reading agent conversation logs.
- Rust and Java analyzer fixtures establish correct source locations and declared input/output extraction, with explicit gaps for ambiguous calls, unsupported syntax, and unavailable types. Warm rescans reuse unchanged facts; edits, dependency changes, analyzer upgrades, and analysis-option changes invalidate affected results. Cold/warm timings, peak memory, and agent-context size are recorded against agreed benchmark budgets.
- Browser -> handler -> service -> downstream relationships show interface names, inputs, outputs, request/response direction and necessary unchanged context.
- Selecting a node reveals the correct component's code beside the same flow, including multiple components in one file.
- Editing added/unchanged lines changes only current file contents; selecting/copying across removed annotations cannot inject them into saved source. Save/undo/redo preserve this distinction.
- Committed, staged, unstaged and untracked work is reachable. Mixed index/working-tree states and net cancellations remain visible and accurately labeled.
- Unmapped or unwanted changed files remain reachable. Removing a path from the flow does not remove it from branch review.
- Basic LF, CRLF, UTF-8 BOM, missing final newline and external-change cases are handled without silent content loss. Mixed newline/unsupported encodings require a deliberate read-only or preservation policy.
- Dirty-buffer guards cover file selection, reload, branch/worktree switch and quit. Conflict recovery does not trap the user with an unsaveable buffer.
- Missing/invalid flows, missing Git/base, deleted/binary files, merge conflicts, incomplete analysis, detached HEAD and stale evidence produce usable states rather than crashes or misleading claims.
- Two worktrees never share an active flow accidentally. Two publishers cannot silently replace a newer map. Files changing during analysis prevent publication as current.
- Confirmed merged reviews are cleaned up after closure when no newer work remains. Squash-merged or unverifiable reviews remain subject to the total cache budget. Eviction and manual cleanup preserve open reviews and source data, and cache-limit failures never cause unbounded disk growth.
- Keyboard-only and mouse passes work at 140x40 and 80x24 and survive resizing in the actual target terminals.

## 10. Evidence and remaining decisions

Current prototypes are fixed skiing examples and do not load the JSON fixture. Headless review checks confirmed selection, dirty guards, basic LF/CRLF/BOM round trips, and blocking a save after external modification. These checks do not establish interactive Herdr behavior or complete editor safety. The standalone viewer loses its source panel at 80x24; the revised layout must address that.

Remaining engineering decisions are the editor/rendering approach, staged-content presentation inside the unified workspace, compatible library versions, the analyzer fact schema and semantic-resolution adapters, benchmark fixtures and performance budgets, exact schema/CLI details, snapshot costs, cache permissions, the default cache budget and cleanup scheduling, terminal portability and skill packaging for additional harnesses. These require focused experiments, not invented user requirements.

References:

- [Tree-sitter: incremental parsing and Rust bindings](https://tree-sitter.github.io/tree-sitter/).
- [Ratatui: terminal UI](https://ratatui.rs/).
- [Edtui: editor widget and editing modes](https://docs.rs/edtui/latest/edtui/).
- [Build skills: explicit invocation and local discovery](https://learn.chatgpt.com/docs/build-skills).
- [Claude Code skills: shared standard, local installation and invocation](https://code.claude.com/docs/en/skills).
- [Codex worktrees: isolated project checkouts](https://learn.chatgpt.com/docs/environments/git-worktrees).
- [Git diff: commit, index and working-tree comparisons](https://git-scm.com/docs/git-diff).
- [Git status: machine-readable status and untracked paths](https://git-scm.com/docs/git-status).
- [Git rev-parse: repository and worktree discovery](https://git-scm.com/docs/git-rev-parse).
- [Prototype references](prototypes/README.md) and [historical research notes](RESEARCH.md).
