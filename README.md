# Domain Lens

An early exploration of an agent-independent terminal tool for understanding a system's data flow, inspecting and editing source, and reviewing Git changes without first committing.

- [Product spec](SPEC.md): interview-confirmed requirements and a proposed agent/worktree integration.
- [Implementation roadmap](PLANS.md): milestone goals and sequencing. [GitHub issues](https://github.com/mrspacerobot/domain-lens/issues) track the work.
- [Codex workflow](docs/CODEX_WORKFLOW.md): researched guidance for implementing and reviewing one issue at a time.
- [Handoff](HANDOFF.md): earlier exploration, prototype limitations and original next steps.
- [Research](RESEARCH.md): Rust libraries, Git, temporary caches and agent integration.
- [Example flow](example-flow.json): a fictional ski weather example.
- [Example code](examples/ski_flow.py): the fictional classes used by the prototype.
- [Prototype snapshots](prototypes/): Python Textual editor, Windows terminal viewer and color previews. Retained as references until the Rust replacements are validated.

## Try the prototype

Requires Python. From this directory, install the prototype dependency in your Python environment, then run:

```powershell
python -m pip install -r requirements-prototype.txt
python prototypes/map-flow-editor.py
```

Click a component and edit the fictional code on the right. **Ctrl+S saves to the real example file**; Ctrl+Q quits. The prototype checks whether a file changed on disk before overwriting it. It is an experiment, not a complete editor.

Run `python prototypes/map-flow-tui.py` for the earlier Windows-only viewer; use `--ascii` if box-drawing characters are unsupported. `FLOW_EXPLORER_ROOT` can override the project root. The prototypes use a fixed example and are not connected to live agent activity.

A Rust version, agent skills, syntax highlighting, inline Git change highlights and a temporary flow cache remain proposed work. The current proposal uses a Rust analyzer for Rust and Java source facts, with agents connecting those facts and source evidence into domain flows. Read the product spec before implementation; the prototypes remain the interaction and visual reference.
