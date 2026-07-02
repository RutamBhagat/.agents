## Core Principles

- Prefer the simplest correct solution with the least total system complexity
- Minimize the number of concepts a maintainer must understand
- Prefer flat code over abstractions
- Do not abstract until code is repeated at least 3 times
- Prefer one obvious path through the code over multiple clever fallback paths
- Code should be explainable in a short paragraph without referring to hidden agent reasoning
- Avoid machinery that makes the system harder to explain, even if it appears more robust locally

## Understand Before Changing

- Before changing code, identify the relevant invariant, data flow, ownership boundary, and smallest behavior that reproduces the issue
- Do not patch the first failing line until you understand why that state was possible
- For bugs, prefer fixing the writer, constructor, parser, or source of invalid state over adding handling at the reader or use site
- If the relevant invariant is unclear, state the assumption explicitly before editing
- When a failure reveals an impossible state, fix the construction of that state; do not teach every consumer to survive it

## Project Orientation

- For unfamiliar projects or subsystems, first learn the smallest runnable path before editing
- Build or run the narrowest relevant command before reading broad internals
- Start from a user-facing behavior, CLI command, API route, UI action, or test case and trace the code path inward
- During the first trace, identify files, functions, data flow, invariants, and ownership boundaries without rewriting code
- Learn the implementation from the innermost stable boundary back outward
- Prefer understanding one hot path deeply over skimming unrelated files
- Use logs, small experiments, or throwaway scripts to confirm understanding before changing production code
- When behavior is unclear, inspect recent commits around the relevant files to understand the project’s existing direction
- Make the first change bite-sized and local unless the invariant clearly belongs at a wider boundary

## Invariants and Invalid States

- Avoid overly defensive code and surplus error handling
- Do not scatter defensive checks through internal code
- Validate unknown external input at boundaries with the project’s schema library; prefer Zod in TS projects when available
- Convert validated input into precise domain types
- Internal functions should accept domain-safe types, not primitive/stringly typed values
- Once data has crossed a validation boundary, internal code should trust the domain type
- Use proper type narrowing and avoid type assertions
- If an invalid state is impossible by construction, do not handle it with fallback behavior
- Use fail-fast assertions for violated internal invariants
- Prefer making bad states unrepresentable over handling every malformed case

## Avoid Agent Drift

- Do not respond to repeated failures by stacking fallbacks, guards, retries, or special cases
- After a failed attempt, reassess the design before making another patch
- If the second fix would add another defensive branch, stop and look for the invariant or representation problem instead
- Prefer deleting now-unreachable fallback code after making invalid states impossible
- Do not add defensive code merely because a model can imagine a bad state
- Do not preserve impossible branches “just in case”

## Persisted Data and Core Infrastructure

- Be especially careful with persisted data formats, schemas, migrations, serialization, deserialization, and core infrastructure
- Do not add tolerant fallback behavior for persisted data unless explicitly requested
- Prefer explicit versioning, migration, or write-time prevention over read-time guessing
- Never silently coerce malformed persisted data into a valid-looking state
- If persisted data can be malformed, identify where it is written and fix that path when possible
- Do not create compatibility layers or migration machinery unless the project actually needs them

## File and Function Structure

- Do not split files merely because they are long
- Split a file only when there is a stable conceptual boundary, separate ownership, or independently testable module
- Prefer a slightly longer cohesive file over many tiny files with unclear boundaries
- Do not use tiny helper functions for logic that is clearer inline
- Prefer `function` declarations for named top-level reusable functions
- Use arrow functions for inline callbacks, closures, or when lexical `this` is needed
- Do not introduce a new abstraction, state machine, cache, registry, generic helper, or config layer unless the need is already present in the code

## Research and Context

- Use web search or Context7 when current docs, APIs, or unfamiliar libraries matter
- When working with a GitHub repo, use Context7 and web search where library behavior, APIs, or current docs are relevant
- Do not code blindly against libraries you do not understand
- Do not read pointless files that you do not need to solve the issue
- Do not read the `node_modules` folder

## Dependencies and Standard Tools

- Prefer the project’s existing dependency for common solved problems instead of writing custom utilities
- Before writing custom validation, parsing, date/time, glob, CLI, markdown/HTML, AST, deep equality, hashing, encoding, or test helper code, check `package.json` and the lockfile for an existing tool
- If no suitable dependency exists, adding a small focused npm package is allowed when it makes the invariant clearer and replaces more complex custom code
- Do not add a dependency for trivial inline logic or when the package would introduce broader concepts than the code it replaces
- In TS projects, use the project’s schema library for non-trivial unknown data; prefer Zod when available
- Do not write custom runtime type guards for complex object shapes when schema parsing would express the boundary more directly
- TypeScript types do not validate runtime data; unknown JSON, request bodies, config files, environment variables, persisted records, and third-party responses must be parsed at the boundary
- After parsing, internal code should accept the parsed domain type and should not repeat validation
- Use the project’s configured test framework and its built-in assertions instead of custom assertion helpers

## Editing Rules

- Prefer edit tools over write tools if the file already exists
- Make sure the directory exists before using edit or write tools
- Keep changes local unless the invariant or design requires a wider fix
- Explain your reasoning before each change to the user to help them understand the data flow and logic
- Only edit one file at a time

## Verification

- Verify changes with the smallest useful check
- First run targeted existing tests if they cover the changed behavior
- If no targeted test exists, create a quick throwaway script in `temp/throwaway/` that imports or calls the changed code directly
- Use Bun + TypeScript throwaway scripts for TS/JS repos
- Use Python throwaway scripts for Python repos
- Use the dev server, API calls, or browser automation only when the behavior cannot be checked by importing or calling code directly
- Add or update real tests with the project’s test framework only when the behavior should be permanently covered
- Use the project’s configured test framework; use Vitest when the project has Vitest
- Do not commit throwaway scripts
- Do not run pointless commands that are not needed for the issue, including obsessive type check commands or unrelated git commands

## Final Review

- Before finishing, review the diff for defensive clutter, duplicated logic, unnecessary abstraction, and now-impossible branches
- Remove code made obsolete by the chosen invariant
- Passing tests are not enough if the implementation is harder to understand than the original
- Summarize the change briefly
- In the summary, explain the invariant preserved by the change, not just the files edited

## Additional Notes

- if you need to use bash commands read /home/voldemort/.codex/RTK.md (NOTE: only if you do not have an equivalent bulit in tool in codex cli, for read, write, edit, delete use built in commands if available)
