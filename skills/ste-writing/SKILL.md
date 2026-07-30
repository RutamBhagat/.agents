---
name: ste-writing
description: Rewrite technical prose in ASD-STE100-inspired Simplified Technical English to remove AI-writing patterns and improve clarity. Use for documentation, READMEs, pull-request descriptions, release notes, error messages, runbooks, procedures, and code comments when the user asks for plain, concise, controlled, or human-sounding technical writing. Do not apply it to code, identifiers, command syntax, marketing copy, essays, or writing that must preserve a strong personal voice.
---

# STE Writing

Write clear technical prose with a small, consistent vocabulary and direct sentence structure. Preserve the facts, meaning, and requested format.

## Choose a mode

- Use **strict** mode for procedures, runbooks, safety text, and error messages. Apply every rule and both sentence-length limits.
- Use **STE-flavored** mode for READMEs, pull-request descriptions, release notes, documentation, and comments. Apply the structure and clarity rules, but allow necessary technical vocabulary and natural variation.

If the user does not select a mode, infer it from the document type.

## Rewrite

1. Preserve all concrete facts, constraints, commands, identifiers, and code.
2. Use one name for each thing. Do not switch between synonyms for variety.
3. Prefer short common words: use, start, help, make sure, before, after, about, get, show, and also.
4. Remove marketing claims and empty adjectives such as seamless, robust, powerful, effortless, world-class, and revolutionary.
5. Use active voice when the actor is known.
6. Use a verb for an action. Write "analyze the log," not "perform an analysis of the log."
7. Replace stacked auxiliaries, nominalizations, avoidable `-ing` main verbs, and phrasal verbs with direct verbs.
8. Put one instruction in each sentence. Keep instructions at 20 words or fewer. Keep descriptive sentences at 25 words or fewer.
9. Expand contractions. Use American spelling.
10. Replace semicolons with periods. Avoid em dashes when the user wants common AI-writing markers removed.
11. Keep one topic in each paragraph and no more than six sentences in a paragraph.
12. For procedures, use a numbered vertical list. Put one action in each item. Put a condition before its command.

Do not invent substance to fill gaps. This method improves form, not truth.

## Check the result

Run the bundled linter when the text is in a local file. Do not run it in a sandbox. Request elevated permissions before you run it, unless the user already granted them:

```bash
python3 ~/.agents/skills/ste-writing/scripts/ste_lint.py path/to/draft.md
```

Treat the score as a comparison signal, not a certification. A lower violations-per-100-words score usually means cleaner form. Review every flagged sentence because the linter uses heuristics.

Before returning the text, check:

1. Split sentences that exceed the selected limit.
2. Replace semicolons and unwanted em dashes.
3. Expand contractions.
4. Change avoidable passive voice to active voice.
5. Replace nominalizations, avoidable `-ing` forms, and phrasal verbs.
6. Use one name for each thing.
7. Confirm that no fact, command, identifier, or constraint changed.

Return only the requested text unless the user asks for notes, a diff, or a score.

## Limits

- Do not claim certified ASD-STE100 compliance. Full compliance requires human judgment and the official specification.
- Do not apply prose rules inside code blocks, inline code, identifiers, URLs, or command syntax.
- Do not force STE on copy that depends on persuasion, literary style, humor, or a distinct personal voice.
