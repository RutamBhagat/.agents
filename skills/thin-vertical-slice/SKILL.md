---
name: thin-vertical-slice
description: Use this skill when the user asks to plan, implement, decompose, rescue, or review software work that can be reduced to small end-to-end slices with observable results.
---

# Thin Vertical Slice

Build the smallest observable behavior that crosses the boundaries needed for the requested outcome.

## Goal

Deliver useful evidence early. Each slice must produce behavior that a user, caller, reviewer, or external system can observe.

Slice by outcome, not by layer. Do not split the plan into frontend, backend, database, infrastructure, testing, or cleanup phases.

## Start

1. State the requested outcome in one sentence.
2. Name the user, caller, reviewer, or external observer.
3. Define the smallest success signal that observer can see.
4. Identify the main uncertainty or integration risk.
5. Make the first slice exercise that risk when practical.

## Choose slices

Create an ordered set of thin vertical slices.

Each slice must:

- add one observable capability
- cross only the boundaries needed for that capability
- leave the system in a coherent state
- have its own completion criteria
- be reviewable without later slices

Make Slice 1 prove the core workflow with the least scope.

Remove optional branches, secondary roles, edge cases, polish, broad refactors, scale work, and speculative abstractions.

Use hard-coded values, fixtures, fake data, stubs, feature flags, or manual steps when they keep feedback fast.

Do not fake the boundary that contains the main risk.

If persistence is the risk, use the real persistence path. If an external API is the risk, use the real integration when safe. If UI behavior is the risk, make the UI drive the path.

Stub lower-risk surroundings instead.

## Acceptance criteria

Give each slice a short outcome title and a nested checklist of completion criteria.

Prefer criteria that describe observable behavior:

- User can ...
- System shows ...
- Server rejects ...
- Data remains ...
- Report matches ...
- Deployment exercises ...

Use implementation details only when they define correctness or a required constraint.

Use nested checklist items for a selected policy, assumption, or behavior rule.

Do not defer a test needed to prove an earlier slice.

A later confidence slice can add broader tests that are not required for earlier acceptance.

## Plan

Show the full ordered slice sequence needed for the requested outcome.

Keep each slice thin. Add later slices only for behavior that the requested outcome still needs.

Put verification under the slice that it proves.

Put deployment in the earliest slice where the live environment matters to the risk.

Add a final deferred section for excluded work.

Move optional features, generalized abstractions, UI polish, broad refactors, and premature scale work to that section.

Do not repeat the same work in a later testing or cleanup slice.

## Implementation

When implementing, complete the first incomplete slice before you expand scope.

Add only the minimum code, schema, wiring, tests, and interface for that slice.

Reuse existing project patterns.

Do not create a framework for hypothetical later slices unless current duplication already causes friction.

After each slice:

- state what now works
- state what you deliberately deferred
- state what you learned
- name the next thinnest slice, if more work remains

Stop when the requested outcome works. Do not continue into cleanup, optimization, or generalization unless correctness or safety requires it.

## Verification

Verify the slice from the viewpoint of the observer.

Use the narrowest reliable test that crosses the important boundaries.

Record the exact command, request, UI action, fixture, or test that reproduces the result.

If a slice cannot stand on its own under verification, make it thinner or change its boundary.

## Output

Be terse. Use plain-text Markdown checklists for plans.

Use this format:

- [ ] Slice 1: <observable outcome>
  - [ ] <completion criterion>
  - [ ] <completion criterion>
  - [ ] <completion criterion>

- [ ] Slice 2: <next observable outcome>
  - [ ] <completion criterion>
  - [ ] <completion criterion>

- [ ] Deferred until the required slices work
  - [ ] <deferred item>
            - [ ] <reason, constraint, or later policy when useful>

Use one top-level checklist item for each slice.

Use nested checklist items for completion criteria.

Prefer 3 to 8 criteria per slice, but use the count that the behavior needs.

Write slice titles as outcomes or proofs. Do not use subsystem names or implementation phases as slice titles.

Use `[ ]` for work that is not verified.

Use `[x]` only when available evidence shows that the work is complete.

When you reconstruct or summarize a completed plan, use `[x]` for completed items.

Do not add introductory prose, rationale sections, or tables when the checklist can contain the same information.

Do not add a separate verification section when the checklist can contain the verification.

For implementation work, report only:

- the observable result
- verification evidence
- deliberate deferrals
- the next slice, when useful

Do not produce a large roadmap unless the user asks for one.
