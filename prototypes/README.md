# Prototype references

Keep these experiments until their Rust replacements are validated. Product behavior is defined in [the spec](../SPEC.md); these prototypes do not implement the complete design.

- `map-flow-editor.py`: Python Textual flow and editable source, with Ctrl+S. The skiing flow is hard-coded; syntax highlighting and inline Git changes are not implemented.
- `map-flow-tui.py`: earlier Windows console viewer with keyboard/mouse navigation. The editor imports its flow definitions, so retain both files together.
- `tui-color-options.html`: visual palette comparisons; Forest Night is the selected direction.

The prototypes use [the example source](../examples/ski_flow.py) and [flow fixture](../example-flow.json). The Python fixture demonstrates the viewer, not Python analyzer support. See [the root README](../README.md) for installation and run commands.

Saving from the editor writes the real example file. The editor includes an external-change check, but the current fixture still needs interactive verification. Windows Terminal and Herdr behavior remain unverified; earlier checks on copied fixtures do not establish current readiness.

The Rust editor experiment in [issue #3](https://github.com/mrspacerobot/domain-lens/issues/3) will validate unified editable source with read-only deleted annotations using disposable fixtures.
