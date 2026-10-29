# DL-13: Connect changed-file navigation and staged detail to the viewer

Status: published as [#13](https://github.com/mrspacerobot/domain-lens/issues/13); implementation has not started.
Milestone: M2 | Suggested size: M | Type: implementation
Depends on: [DL-10](dl-10-build-the-complete-branch-change-inventory.md), [DL-11](dl-11-load-baseline-current-staged-and-deleted-file-representations.md), [DL-12](dl-12-build-the-flow-viewer-and-source-navigation.md)
Spec: [SPEC.md](../../SPEC.md), sections 1–3.

## Outcome

Make every changed file reachable independently of graph membership.

## Scope

Likely areas: src/ui/files.rs, src/ui/staged.rs. These paths are proposed implementation locations, not a claim that those modules already exist. Keep the change within this issue; update the paths if the accepted architecture requires it.

## Acceptance criteria

- [ ] Changed-file list opens all inventory paths, including unmapped files, and labels staged/local/conflict/read-only states.
- [ ] Read-only staged content is accessible inside the same review workspace without replacing the current-file editor.
- [ ] Unmapped or unwanted files remain visible when the graph omits them.
- [ ] Buffer guards apply when changing files; current unsaved state stays distinguishable from disk status.

## Validation and evidence

- Open every fixture inventory entry through keyboard navigation.
- Demonstrate a staged edit undone on disk and an unmapped new file.
- Report the tested commit/working-tree state, commands, observed results, and acceptance evidence. Clearly identify checks not run.

## Outside this issue

Per-commit history UI and Git mutation controls.
