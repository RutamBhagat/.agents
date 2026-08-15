---
name: thin-vertical-slice
description: Use this skill when the user asks to plan, implement, decompose, rescue, or review software work that can be reduced to small end-to-end slices with observable results, including work split between human-only actions and actions an agent can perform.
---

# Thin Vertical Slice

Build the smallest observable behavior that crosses the boundaries needed for the requested outcome.

## Goal

Deliver useful evidence early. Each slice must produce behavior that a user, caller, reviewer, or external system can observe.

Slice by outcome, not by layer. Do not split the plan into frontend, backend, database, infrastructure, testing, or cleanup phases.

When execution responsibility differs, explicitly distinguish actions that require a human from actions the agent can perform.

## Start

1. State the requested outcome in one sentence.
2. Name the user, caller, reviewer, or external observer.
3. Define the smallest success signal that observer can see.
4. Identify the main uncertainty or integration risk.
5. Make the first slice exercise that risk when practical.
6. Identify any steps that cannot be performed by the agent because they require:
   - interactive access to an external admin console
   - credentials, secrets, MFA, or approval unavailable to the agent
   - physical access
   - account ownership or privileged human authorization
   - an irreversible or sensitive decision that must remain with the user

Do not label a step human-only merely because it is inconvenient. If the agent has the required tools and authorization, keep it agent-executable.

## Responsibility

Mark execution responsibility on individual checklist items when it matters.

Use:

```text
**HUMAN ONLY:**
```

for actions the agent cannot or should not perform.

Use:

```text
**AGENT:**
```

or:

```text
**AGENT CAN DO:**
```

for actions the agent can execute with available tools.

Prefer `**AGENT:**` for implementation work the agent is expected to perform.

Prefer `**AGENT CAN DO:**` when distinguishing an optional agent-executable verification or cleanup step from surrounding human-only work.

Do not put responsibility labels on slice titles unless the entire slice belongs exclusively to one actor.

A single slice may contain both human-only and agent-executable criteria when both are required to produce the same observable outcome.

Keep human setup and agent implementation in the same slice when separating them would create a non-observable setup-only phase.

For human-only steps:

- give the exact console path, command, value, or decision needed
- state what value or evidence the human should preserve for subsequent steps
- never claim the step is complete without evidence from the user or connected tooling

For agent steps:

- give exact files, commands, configuration changes, or verification actions when they are known
- execute them when the task is implementation rather than planning
- do not ask the human to perform work that the agent can perform with available tools

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

Human configuration is allowed inside an early slice when it is necessary to exercise the risky real boundary. Do not move required human setup into a separate preliminary phase merely to keep implementation steps together.

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

Use nested checklist items for a selected policy, assumption, behavior rule, command, configuration value, or execution responsibility.

When responsibility matters, prefix the criterion with one of:

```text
**HUMAN ONLY:**
**AGENT:**
**AGENT CAN DO:**
```

Example:

```text
- [ ] **HUMAN ONLY:** Create the federated identity in the provider console and save its Client ID.
- [ ] **AGENT:** Add the OIDC permission and provider action to the workflow.
- [ ] **AGENT CAN DO:** Verify the expected secret names exist without reading their values.
```

Do not defer a test needed to prove an earlier slice.

A later confidence slice can add broader tests that are not required for earlier acceptance.

## Plan

Show the full ordered slice sequence needed for the requested outcome.

Keep each slice thin. Add later slices only for behavior that the requested outcome still needs.

Put verification under the slice that it proves.

Put deployment in the earliest slice where the live environment matters to the risk.

Keep required human-only setup in the slice whose observable behavior depends on it.

Do not create separate "human setup", "agent implementation", "testing", or "cleanup" phases when those activities jointly prove one outcome.

Add a final deferred section for excluded work.

Move optional features, generalized abstractions, UI polish, broad refactors, unrelated security hardening, and premature scale work to that section.

Do not repeat the same work in a later testing or cleanup slice.

## Implementation

When implementing, complete the first incomplete slice before you expand scope.

Within that slice:

- perform all available `**AGENT:**` and `**AGENT CAN DO:**` work
- leave unperformed `**HUMAN ONLY:**` steps unchecked
- do not fabricate successful completion of external human actions
- continue past human-only steps when later agent work can safely be prepared independently
- stop only when missing human evidence actually blocks further correct execution

Add only the minimum code, schema, wiring, tests, configuration, and interface for that slice.

Reuse existing project patterns.

Do not create a framework for hypothetical later slices unless current duplication already causes friction.

After each slice:

- state what now works
- state what remains human-only, if anything
- state what you deliberately deferred
- state what you learned
- name the next thinnest slice, if more work remains

Stop when the requested outcome works. Do not continue into cleanup, optimization, hardening, or generalization unless correctness or safety requires it.

## Verification

Verify the slice from the viewpoint of the observer.

Use the narrowest reliable test that crosses the important boundaries.

Record the exact command, request, UI action, fixture, workflow dispatch, log signal, or test that reproduces the result.

Distinguish between:

- configuration that exists
- configuration whose name or metadata can be verified
- secrets whose values must not be exposed
- behavior that has actually been exercised end to end

If verification requires a human-only action, state the exact success signal the human should observe.

If a slice cannot stand on its own under verification, make it thinner or change its boundary.

## Output

Be terse. Use plain-text Markdown checklists for plans.

Use `-` for every Markdown list item. Never use `*` as a list marker.

Use this format:

```text
- [ ] Slice 1: <observable outcome>
  - [ ] **HUMAN ONLY:** <required human action>
  - [ ] **AGENT:** <agent implementation action>
  - [ ] **AGENT CAN DO:** <agent verification action>
  - [ ] <observable success signal>

- [ ] Slice 2: <next observable outcome>
  - [ ] **AGENT:** <completion criterion>
  - [ ] <completion criterion>

- [ ] Deferred until the required slices work
  - [ ] <deferred item>
    - [ ] <reason, constraint, or later policy when useful>
```

Use one top-level checklist item for each slice.

Use nested checklist items for completion criteria.

Prefer 3 to 8 criteria per slice, but use the count that the behavior needs.

Write slice titles as outcomes or proofs. Do not use subsystem names, actor names, or implementation phases as slice titles.

Use `[ ]` for work that is not verified.

Use `[x]` only when available evidence shows that the work is complete.

Human-only work remains `[ ]` until the user or an authoritative connected system provides evidence that it is complete.

When you reconstruct or summarize a completed plan, use `[x]` for completed items.

Preserve exact commands and configuration snippets when they materially reduce ambiguity.

For commands or configuration that belong to a checklist item, nest fenced code beneath that item instead of turning the code into a separate slice.

Do not expose secret values. It is acceptable to verify secret names, identifiers, references, or presence when that can be done without revealing secret material.

Do not add introductory prose, rationale sections, actor summary sections, or tables when the checklist can contain the same information.

Do not add a separate verification section when the checklist can contain the verification.

For implementation work, report only:

- the observable result
- verification evidence
- remaining human-only actions
- deliberate deferrals
- the next slice, when useful

Do not produce a large roadmap unless the user asks for one.
