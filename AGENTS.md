# Working on Domain Lens

Read SPEC.md, PLANS.md, the selected current GitHub issue, and completed dependency decisions before editing. Keep each change within its assigned issue; later issue details are provisional.

## Rust workspace

The root package is the `domain-lens` binary. Use the stable Rust toolchain with rustfmt and Clippy, as selected by rust-toolchain.toml. Edition 2024 requires Rust 1.85 or newer. Commit Cargo.lock for reproducible dependency resolution; add libraries only when the selected issue needs them.

Run from the repository root:

```text
cargo fmt --check
cargo check --locked
cargo test --locked
cargo clippy --locked --all-targets -- -D warnings
cargo run --locked -- --help
```

Report actual results and unavailable prerequisites. Headless checks do not establish real terminal or harness compatibility.

## Readable Rust

- Give each function one clear responsibility and one level of detail. Aim for a function body of at most 15 lines; review longer functions for a useful extraction. Keep related logic together when splitting it would make it harder to follow.
- Keep parameter lists and files manageable. Consider grouping related parameters into a meaningful type and splitting files by responsibility. Three parameters and 200 lines per file are review prompts, not automatic limits.
- Prefer clear names, straightforward expressions, and early returns where they make the main path easier to follow. Explain why in comments when the code alone cannot convey the reason.
- Follow Rust naming conventions, including `snake_case` for functions and modules, `UpperCamelCase` for types, and `as_`, `to_`, and `into_` for conversions with their conventional meanings.
- Use enums and validated types to represent meaningful states and prevent invalid combinations. Validate untrusted input at the boundary.
- Return useful errors for expected failures, including filesystem, Git, parsing, and terminal errors. Reserve panics for programming defects rather than ordinary input or environment failures.
- Separate decisions from I/O where practical. Test observable behavior and important edge cases, especially source preservation, external changes, and Git state, using disposable fixtures.
- Let rustfmt settle formatting. Select additional Clippy lints deliberately; document the reason for a local exception. Do not use cognitive complexity as a reliable measurement of readability.

## Project hygiene

- Keep work scoped to one issue and a reviewable change. Use one branch and pull request per issue when working through pull requests.
- When committing, use an imperative subject ending in the issue number, for example `Add source loading (#7)`; explain why in the body when useful.
- Update relevant guidance and documentation when a project decision changes. Report failed or unrun checks and their impact.

## Source safety and references

Preserve prototypes/, examples/, and example-flow.json until replacements are validated. Use disposable temporary fixtures for source-writing and Git-state checks; never exercise saving against the original examples. Generated task flows belong outside the repository. Do not modify user-level agent settings.

Record material design decisions, acceptance evidence, tested revision/working-tree state, and unresolved limitations with the selected issue's handoff.
