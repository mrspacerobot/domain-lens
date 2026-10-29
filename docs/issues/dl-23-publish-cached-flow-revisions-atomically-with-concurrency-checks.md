# DL-23: Publish cached flow revisions atomically with concurrency checks

Status: published as [#23](https://github.com/mrspacerobot/domain-lens/issues/23); implementation has not started.
Milestone: M4 | Suggested size: M | Type: implementation
Depends on: [DL-22](dl-22-validate-flow-documents-and-adapt-the-original-fixture.md)
Spec: [SPEC.md](../../SPEC.md), sections 5–6.

## Outcome

Store accepted flow revisions outside the repository under canonical context identities.

## Scope

Likely areas: src/cache/store.rs, src/cache/publish.rs. These paths are proposed implementation locations, not a claim that those modules already exist. Keep the change within this issue; update the paths if the accepted architecture requires it.

## Acceptance criteria

- [ ] Write complete revisions atomically and retain current/previous accepted revisions.
- [ ] Serialize imports and check expected revision inside the publication lock, including explicit first publication.
- [ ] Recover safely after interrupted writes or corrupt/incomplete revisions.
- [ ] Make open-review leases and publication locks available to later eviction work; provide explicit-file operation for cache-restricted environments.

## Validation and evidence

- Race two publishers and confirm one receives a revision-conflict result.
- Interrupt a write and verify the previous complete accepted flow remains readable.
- Report the tested commit/working-tree state, commands, observed results, and acceptance evidence. Clearly identify checks not run.

## Outside this issue

Eviction policy and creating user skills automatically.
