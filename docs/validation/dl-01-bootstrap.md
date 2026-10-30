# DL-01 bootstrap evidence

Issue: [#1](https://github.com/mrspacerobot/domain-lens/issues/1). Updated: 2026-10-30.

Starting revision: `0ed439075fa561c7baf955628d979fe660ee299c` on `main`. The prior bootstrap handoff recorded a clean starting tree. At this verification the bootstrap was already uncommitted: README.md was modified and .gitignore, AGENTS.md, Cargo.lock, Cargo.toml, docs/validation/, rust-toolchain.toml, and src/ were untracked. Results refer to that working tree, not the starting commit.

## Decisions and scope

- One root workspace and edition-2024 binary package, with stable Rust, rustfmt and Clippy. Rust 1.85 is the declared minimum, not a tested compatibility claim.
- The dependency-free CLI offers help and version output and rejects unsupported arguments. The viewer, editor, Git integration and analyzer remain future work.
- Cargo.lock contains the root package and is intended to be committed. Locked checks accepted it.
- The prototypes and example files remain reference material; no source-writing tests were run against them.

## Environment and checks

On Windows, `rustc 1.99.1 (58cf8f9c3 2026-10-13)` and `cargo 1.99.1 (5f94df478 2026-08-27)` are available. The active toolchain is `stable-x86_64-pc-windows-msvc`, with rustfmt and Clippy installed. Neither `link.exe` nor `cl.exe` was found on PATH; the Visual Studio Installer probe found no installation with the C++ tools.

| Command | Result |
|---|---|
| `cargo fmt --check` | Passed |
| `cargo check --locked` | Passed |
| `cargo test --locked` | Failed: MSVC linker `link.exe` not found |
| `cargo clippy --locked --all-targets -- -D warnings` | Passed |
| `cargo run --locked -- --help` | Failed: MSVC linker `link.exe` not found |
| `git diff --check` | Passed for tracked changes |

The earlier handoff reported that Rust was unavailable; the results above supersede that environment observation. Linking, executable output and exit behavior remain unverified. There are currently no behavioral tests. No interactive terminal, Herdr, macOS, or clean-checkout build has been verified.

## Remaining acceptance evidence

Install the Visual Studio Build Tools C++ workload and Windows SDK, then rerun the failed commands and check no arguments, `--version`, unsupported and extra arguments for output and exit status. Verify the documented build from a clean checkout. Do not claim issue completion until the binary runs and the remaining checks pass.
