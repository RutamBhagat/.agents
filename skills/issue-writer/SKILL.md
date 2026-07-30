---
name: issue-writer
description: >-
  Write or rewrite concise, evidence-based GitHub issues from rough notes,
  logs, screenshots, bug reports, or feature requests. Always use this skill
  when a user wants to draft, clean up, condense, or prepare an issue. Use it
  for open source and internal projects. Verify observable behavior before
  writing when tools and access permit. Remove guessed diagnoses, invented
  reproduction steps, implementation plans, and other LLM-generated padding.
---

# Issue Writer

Write an issue that the reporter can understand, verify, and own.

The issue body is evidence for maintainers and coding agents. Confident but
incorrect analysis creates more work than a short report with no diagnosis.

## Verify before writing

1. Identify what the reporter directly observed.
2. Preserve exact commands, input, output, errors, logs, versions, and URLs.
3. If the report concerns a website or web UI, use the browser first when it is
   available.
4. Reproduce only safe actions. Do not submit forms, delete data, or change
   external state unless the user asked for that action.
5. Record the exact browser steps and visible result.
6. If browser access, authentication, or reproduction fails, state that you did
   not reproduce the behavior.
7. If source code is available, inspect the relevant execution path before
   keeping any root cause claim.
8. Read related code files in full. Derive the analysis from the code.
9. Treat analysis from the reporter, an existing issue, or another model as a
   hypothesis until independent evidence confirms it.

Use a purpose-built GitHub connector or CLI to read issue threads when one is
available. Read all comments and linked issues or pull requests.

## Separate facts from guesses

Keep these evidence classes distinct:

- **Verified fact:** Directly reproduced or confirmed in code or output.
- **Reported fact:** Supplied by the reporter but not independently reproduced.
- **Hypothesis:** A possible cause or fix that lacks enough evidence.

Do not turn a reported fact into a verified fact. Omit hypotheses from the issue
body unless the user asks to include them. Label each included hypothesis.

Never invent:

- A minimal reproduction
- A root cause
- An implementation strategy
- An analogy to adjacent code
- Extra error classes
- Environment details
- User impact

## Draft the issue

Ask only for facts that are necessary to avoid an inaccurate report. If the
reporter does not know a fact, omit it or say that it is unknown.

Use this structure for a bug:

````markdown
**Title:** [Observable symptom in specific context]

## Steps to reproduce

1. [Exact action or command]
2. [Next action, if needed]

## Expected behavior

[What the reporter expected]

## Actual behavior

[What happened instead]

## Error or log

```text
[Exact unedited output]
```

## Environment

- Version: [Known version]
- OS: [Known operating system]
````

Omit empty sections. Do not add a section only to note missing information.

For a feature request, state:

1. The current limitation
2. The user goal
3. The expected behavior
4. A concrete example, if verified

Keep proposed solutions separate from the problem. Do not add an implementation
plan unless the user asks for one.

## Write plain issue text

- Use the reporter's voice when possible.
- Prefer first person for direct observations.
- Use short, direct sentences.
- Put one idea in each sentence.
- Use one name for each thing.
- Use active voice when you know the actor.
- Preserve code, commands, identifiers, URLs, and logs exactly.
- Do not use semicolons or em dashes.
- Remove filler, marketing language, fake certainty, and exhaustive caveats.
- Title the observed failure, not a guessed cause.

## Return the result

Return only the ready-to-post issue unless the user asks for notes.

Keep independent analysis out of the issue body by default. If the user asks for
it, put it after the draft under `Optional follow-up comment`. List the verified
facts and remaining uncertainty.

Do not create or submit the issue unless the user explicitly asks you to do so.
