# Domain Lens

An early exploration of an agent-independent terminal tool for understanding a system's data flow, inspecting and editing source, and reviewing Git changes without first committing.

- [Product spec](SPEC.md): interview-confirmed requirements and a proposed agent/worktree integration.
- [Implementation roadmap](PLANS.md): milestone goals and sequencing. [GitHub issues](https://github.com/mrspacerobot/domain-lens/issues) track the work.
- [Codex workflow](docs/CODEX_WORKFLOW.md): researched guidance for implementing and reviewing one issue at a time.
- [Research](RESEARCH.md): Rust libraries, Git, temporary caches and agent integration.
- [Example flow](example-flow.json): a fictional ski weather example.
- [Example code](examples/ski_flow.py): the fictional classes used by the prototype.
- [Prototype references](prototypes/README.md): Python Textual editor, Windows terminal viewer and color previews. Retained as references until the Rust replacements are validated.

## Build the Rust workspace

The Rust app currently provides help and version output only. The terminal UI, editor, analyzer, and Git integration are future issues.

Install [Rust through rustup](https://rust-lang.org/tools/install/) and use the stable toolchain with rustfmt and Clippy (selected by rust-toolchain.toml). The package uses Rust edition 2024, requiring Rust 1.85 or newer. On Windows, use the native MSVC toolchain and install the Visual Studio Build Tools **Desktop development with C++** workload, including an appropriate Windows SDK. Restart the terminal after installation so Cargo is on PATH.

From a clean checkout:

```powershell
git clone https://github.com/mrspacerobot/domain-lens.git
cd domain-lens
rustc --version
cargo --version
cargo build --locked
cargo run --locked -- --help
cargo run --locked -- --version
```

Run project checks from the repository root:

```powershell
cargo fmt --check
cargo check --locked
cargo test --locked
cargo clippy --locked --all-targets -- -D warnings
```

For an optimized binary, run `cargo build --locked --release`. Windows produces `target/release/domain-lens.exe`; macOS produces `target/release/domain-lens`. Build on the target OS initially. macOS builds and interactive terminal behavior have not been verified.

The bootstrap has no third-party Rust dependencies. Keep Cargo.lock tracked as dependencies are introduced. See the [bootstrap evidence](docs/validation/dl-01-bootstrap.md) for actual checks and missing prerequisites on this machine.

## Try the prototype

Requires Python. From this directory, install the prototype dependency in your Python environment, then run:

```powershell
python -m pip install -r requirements-prototype.txt
python prototypes/map-flow-editor.py
```

Click a component and edit the fictional code on the right. **Ctrl+S saves to the real example file**; Ctrl+Q quits. The prototype checks whether a file changed on disk before overwriting it. It is an experiment, not a complete editor.

Run `python prototypes/map-flow-tui.py` for the earlier Windows-only viewer; use `--ascii` if box-drawing characters are unsupported. `FLOW_EXPLORER_ROOT` can override the project root. The prototypes use a fixed example and are not connected to live agent activity.

The Rust workspace is a CLI skeleton. Agent skills, syntax highlighting, inline Git change highlights and a temporary flow cache remain proposed work. The current proposal uses a Rust analyzer for Rust and Java source facts, with agents connecting those facts and source evidence into domain flows. Read the product spec before implementation; the prototypes remain the interaction and visual reference.
