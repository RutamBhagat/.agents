# AGENTS.md

## Goal

Solve the user’s request with the simplest correct implementation. Prefer small, readable, happy-path code that a junior developer can understand quickly.

## Coding Style

- Keep code barebones, clear, and low-line-count.
- Prefer readability over defensive robustness.
- Avoid unnecessary abstractions, helpers, config, or edge-case handling.
- Use named functions for top-level functions.
- Use arrow functions only for callbacks.
- When a function needs more than one argument, pass a single object.
- Make sure a directory exists before creating a file.
- Edit or write one file at a time.
- Use CLI generators when they reduce custom code, such as shadcn.
- Modularize large files into smaller, focused modules.
- Prefer named exports over default exports.

## Before Coding

Do not code blindly. First narrow the problem with the `is` skill or direct inspection.

For libraries, packages, and frameworks:

- Search the web to confirm the current best approach.
- NOTE: ONLY IF you are in claude code use the parallel web search mcp instead of the default web search tool
- Prefer trusted npm or pip packages over fragile custom code.
- Use Context7 for current documentation before implementing with any npm, pip, framework, or library API.

For frontend work:

- Search for the right component approach first.
- Use shadcn CLI to install needed components.
- Keep UI implementation simple and conventional.

## Validation

Use the smallest useful check for the change.

- Create one-time throwaway tests with bun or Python when useful.
- Add unit or integration tests when Vitest is already available.
- Do not run lint, format, typecheck, dev, or build commands unless explicitly asked.

<!-- context7 -->
Use Context7 MCP to fetch current documentation whenever the user asks about a library, framework, SDK, API, CLI tool, or cloud service — even well-known ones like React, Next.js, Prisma, Express, Tailwind, Django, or Spring Boot. This includes API syntax, configuration, version migration, library-specific debugging, setup instructions, and CLI tool usage. Use even when you think you know the answer — your training data may not reflect recent changes. Prefer this over web search for library docs.

Do not use for: refactoring, writing scripts from scratch, debugging business logic, code review, or general programming concepts.

## Steps

1. Always start with `resolve-library-id` using the library name and the user's question, unless the user provides an exact library ID in `/org/project` format
2. Pick the best match (ID format: `/org/project`) by: exact name match, description relevance, code snippet count, source reputation (High/Medium preferred), and benchmark score (higher is better). If results don't look right, try alternate names or queries (e.g., "next.js" not "nextjs", or rephrase the question). Use version-specific IDs when the user mentions a version
3. `query-docs` with the selected library ID and the user's full question (not single words), scoped to a single concept. If the question spans multiple distinct concepts (e.g. routing and auth and caching), make a separate `query-docs` call per concept with the same library ID, unless the question is about how the concepts interact — combined queries dilute ranking and return shallow results for each topic
4. Answer using the fetched docs
<!-- context7 -->
