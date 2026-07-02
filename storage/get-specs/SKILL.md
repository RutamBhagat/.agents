---
name: get-specs
description: Interview the user relentlessly about a vague issue, feature, plan, or design until it becomes a precise implementation prompt. Use when the user wants to stress-test a plan, get grilled on a design, refine an issue, shape a feature request, or mentions "grill me".
---

---

# Get Specs

Convert a vague requirement into a compact, implementation-ready prompt for a coding agent.

The goal is not to brainstorm forever. The goal is to uncover every decision that would otherwise cause the implementation agent to guess.

## Core behavior

- Start by restating the feature gap or bug in one sentence.
- Explore the codebase before asking whenever the answer may already exist in APIs, tests, docs, naming, errors, config, or project conventions.
- Interview the user only on decisions the codebase cannot answer.
- Resolve the decision tree one dependency at a time. Do not scatter unrelated questions.
- For every question, provide your recommended answer.
- Prefer concrete defaults over open-ended discussion.
- Keep going until the vague request has become a precise behavior contract.

## Question style

Ask one decision-blocking question at a time unless several decisions are inseparable.

Use this format:

```text id="vnuz7v"
Question: [specific decision]
Recommended answer: [concrete default]
Why: [short reason]
Blocks: [what this decides next]
```

Good questions pin down behavior that affects implementation, tests, compatibility, or user-visible results.

Avoid questions about things the codebase can answer.

## What to resolve

Drive the interview toward concrete answers for:

- user-visible behavior
- public API names, option shapes, defaults, and exports
- compatibility with existing behavior
- exact error cases and error text when relevant
- state, lifecycle, ordering, caching, concurrency, and retry rules
- persistence, serialization, parsing, formatting, or schema rules
- type-level behavior and inference expectations
- edge cases, invalid inputs, and no-op behavior
- integration points with existing modules
- testable acceptance criteria
- explicit non-goals

## Prompt style to produce

The final prompt should read like a compact task specification:

- Open with the limitation and the requested change.
- State the API and behavior directly.
- Use short paragraphs or tight bullets.
- Add headings only when the feature has multiple independent rule groups.
- Include exact strings, defaults, and edge cases when they matter.
- Say what remains unchanged when compatibility matters.
- Avoid implementation plans, timelines, motivational prose, and long tradeoff essays.

## Final output

When the decision tree is resolved, output only:

```text id="0vzv5k"
[compact implementation prompt]
```

If any assumption remains unresolved, put it before the prompt under `Assumptions`.
:::
