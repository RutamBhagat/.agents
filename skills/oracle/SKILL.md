---
name: oracle
description: "Use this skill when the user asks for a repository review, debugging help, architecture analysis, or an implementation plan that requires a focused set of local project files and Markdown context for manual ChatGPT review."
---

---

# Oracle (CLI)

Oracle bundles one prompt and selected local files into clipboard-ready Markdown.

The user pastes the bundle into ChatGPT and returns the answer for local verification.

## Workflow

1. Define the exact question and required output.

2. Select the smallest file set that contains the needed facts.

3. Preview broad scopes with a file report.

4. Review the selected files and token estimate.

5. Render and copy the bundle.

6. Tell the user that the bundle is on the clipboard.

7. Ask the user to paste the bundle into ChatGPT.

8. Continue after the user returns the answer.

9. Verify the answer against local files and tests.

Use this command for the final bundle:

```bash
oracle --render --copy -p "<task>" --file "<tight file set>"
```

Use `--copy-markdown` as the equivalent long-form option.

## File Scope

Choose the minimum files that contain the relevant facts.

Run this preview before a broad directory or glob:

```bash
oracle --dry-run summary --files-report -p "<task>" --file "src/**"
```

Use the preview for these scopes:

- More than about 10 files.

- A repository-root pattern.

- Generated files, logs, or dotfiles.

- An expected bundle above 100k tokens.

- A scope with unclear data sensitivity.

Target a total input below about 196k tokens.

## Prompt Design

Put the goal and required output first.

Add the minimum context needed to answer the question.

Include these details when they apply:

- Stack, platform, and runtime limits.

- Build, test, lint, and reproduction commands.

- Key directories, entry points, and dependency limits.

- Exact errors and reproduction steps.

- Previous attempts and their results.

- Public API limits and protected areas.

- Approval boundaries and success criteria.

- Required tests, risks, assumptions, and tradeoffs.

Ask for evidence, checks, and a clear recommendation.

Ask the reviewer to identify material ambiguities before making assumptions.

## Model Guidance

The user selects the model after pasting the bundle.

When the user asks for guidance, recommend the latest flagship model.

For difficult quality-first work, recommend Pro mode and the highest practical reasoning setting.

State that more reasoning can increase latency and cost.

Recommend tests on representative tasks for repeated use.

## Preview and Copy

Preview a focused bundle:

```bash
oracle --dry-run summary -p "<task>" --file "src/**" --file "!**/*.test.*"
```

Preview the full rendered bundle:

```bash
oracle --dry-run full -p "<task>" --file "src/**"
```

Review file and token use:

```bash
oracle --dry-run summary --files-report -p "<task>" --file "src/**"
```

Render and copy:

```bash
oracle --render --copy -p "<task>" --file "src/**"
```

## File Selection

`--file` accepts local files, directories, and globs.

Pass it more than once when the task needs separate paths.

Include files:

```bash
--file "src/**"
--file src/index.ts
--file docs --file README.md
```

Use exclusion patterns to remove unrelated or sensitive paths:

```bash
--file "src/**" --file "!src/**/*.test.ts" --file "!**/*.snap"
--file "src/**" --file "!.env" --file "!.env.*" --file "!**/*.pem" --file "!**/*.key" --file "!**/id_rsa*" --file "!**/*token*" --file "!**/*secret*" --file "!**/.aws/**" --file "!**/.ssh/**" --file "!**/logs/**"
```

Oracle applies these file rules:

- It ignores `node_modules`, `dist`, `coverage`, `.git`, `.turbo`, `.next`, `build`, and `tmp` by default.

- It honors `.gitignore` during glob expansion.

- It filters dotfiles unless a pattern includes them.

- It rejects files over 1 MB by default.

Use `ORACLE_MAX_FILE_SIZE_BYTES` or `maxFileSizeBytes` in `~/.oracle/config.json` to change the file limit.

Use `--files-report` or `--dry-run json` to find files that use many tokens.

## Safety Review

Before copying the bundle, confirm these points:

1. The user approved the Oracle review.

2. The file scope is exact and narrow.

3. Broad scopes have a dry-run file report.

Ask the user to narrow or redact the scope when any point is unclear.

Clear the clipboard after use when practical.

## Answer Verification

Treat the returned answer as advisory.

1. Check cited files and code paths.

2. Confirm claims with repository searches.

3. Run focused tests for proposed changes.

4. Check public API and compatibility risks.

5. State unsupported assumptions before implementation.
