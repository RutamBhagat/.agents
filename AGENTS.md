## Goal

Implement the simplest correct solution
Keep happy-path code small readable and clear to junior developers

## General

- Only report to me in ASD-STE100 Simplified Technical English
- Do not add test files in Python repositories
- Do not add docstrings, jsdocs or comments
- Use only edit or write tools for code changes
- Change one file at a time
- Create its directory first
- Do not use Chrome the Node REPL or browser tools unless the user asks
- Keep code clear minimal and short
- Prefer readability to defensive robustness
- Avoid needless abstractions helpers configuration and edge-case handling
- Use named top-level functions
- Reserve arrow functions for callbacks
- Pass one object to functions that need multiple arguments
- Use CLI generators such as shadcn when they reduce custom code
- Split large files into small focused modules
- Prefer named exports to default exports

## Implementation Method

- Break large work into small dependency-ordered steps
- Trace data flow and identify prerequisites before coding
- Build the smallest working end-to-end path first
- Verify each intermediate step before extending it
- Do not require test-first development

## Python

- Use modern Python supported by the project
- Prefer functions dataclasses `TypedDict` and plain classes
- Use Pydantic only for runtime validation
- Annotate public functions class attributes and non-obvious local variables
- Prefer precise types to `Any`
- Use `object` for unknown values then narrow it
- Use built-in generics modern unions and `collections.abc` types
- Narrow with `isinstance` `match` `Literal` and discriminated unions
- Use `TypeIs` for reusable narrowing when control flow is insufficient
- Use `cast` only after code proves the invariant
- State the invariant in a short comment

### Tools and Checks

Keep the project’s ty Ruff and Pydantic configuration
Add or replace tools only when required

- Use ty for type checking inference and narrowing
- Use Ruff for linting import cleanup and formatting
- Use Pydantic to validate untrusted API configuration environment file queue and third-party data
- Pass validated models or typed values instead of raw dictionaries
- Use a Pydantic discriminated union with a `Literal` tag for multiple input shapes
- Branch on the tag so ty narrows the union
- Use strict validation when conversion can hide invalid input
- Never use `model_construct()` for untrusted or unvalidated data

When the user requests Python validation run only the smallest relevant check

- Types `ty check <changed-path>`
- Lint `ruff check <changed-path>`
- Safe fixes `ruff check --fix <changed-path>`
- Format check `ruff format --check <changed-path>`
- Format `ruff format <changed-path>`

Use `uv run` in uv projects
Run whole-project checks only when requested or when the change affects the whole project

## Before Coding

- Narrow the problem through direct inspection or the `is` skill
- Search the web for the current best approach before work with libraries packages or frameworks
- In Claude Code only use the parallel web search MCP instead of default web search
- Prefer trusted npm or pip packages to fragile custom code
- Find the correct component approach before frontend work
- Install required components with the shadcn CLI
- Keep UI code simple and conventional

## Validation

- Use the smallest useful check
- Use throwaway Bun or Python tests when useful
- Add unit or integration tests when Vitest already exists
- Do not run lint format type-check dev or build commands unless the user asks

## Context7

Use Context7 MCP for current documentation before implementing npm pip framework or library APIs
Also use it for questions about a library framework SDK API CLI or cloud service
This includes syntax configuration migration library-specific debugging setup and CLI use
Use it for familiar tools too
Prefer it to web search for library documentation

Do not use Context7 for refactoring scripts from scratch business-logic debugging code review or general programming concepts

- Call `resolve-library-id` with the library name and full question
   Skip this step for an exact `/org/project` ID
- Choose the best exact match by description snippet count source reputation and benchmark score
   Prefer High or Medium reputation
   Use a version ID when given
   Try another name or query if needed
- Call `query-docs` with the selected ID and full question
   Limit each call to one concept
   Split distinct concepts into separate calls with the same ID unless their interaction is the question
- Answer from the fetched documentation
