---
name: thin-vertical-slice
description: Build software in the thinnest useful end-to-end increments. Use this skill whenever the user asks to implement, plan, decompose, rescue, or review a feature, MVP, prototype, refactor, migration, API, workflow, or AI-assisted coding task where scope can be reduced to a small observable result. Prefer this even when the user does not say “vertical slice” if the work risks being split by frontend/backend/infra layers, has a long feedback loop, or is too large to review confidently.
---
Goal
Deliver the smallest observable behavior that crosses the necessary system boundaries and can be tested, reviewed, or shown before expanding scope.

Operating rule
Slice by outcome, not by layer. A slice should produce evidence that the system does something useful or meaningfully validates a risky assumption. Avoid separate frontend, backend, database, infrastructure, or cleanup phases when a thinner end-to-end path can prove the behavior sooner.

Start
Restate the requested outcome in one sentence. Identify the user, caller, or external observer. Define the smallest success signal they could observe. Note the main uncertainty or integration risk that should be exercised early.

Choose the slice
Select one path through the system that reaches the success signal. Remove optional branches, secondary roles, edge cases, polish, generalized abstractions, scale work, broad refactors, and speculative extensibility. Use hard-coded values, fixtures, fake data, stubs, feature flags, or manual steps when they preserve the feedback loop and do not hide the risk being tested.

Keep it real where risk lives
Do not fake the boundary that contains the main uncertainty. If the risky part is database persistence, use the real persistence path. If it is an external API, exercise the real integration when safe and practical. If it is UI behavior, make the UI actually drive the path. Stub lower-risk surroundings instead.

Plan
Express the work as a short sequence of independently verifiable slices. Each slice should add one observable capability and leave the system in a coherent state. Prefer the smallest slice that could change a reviewer’s understanding of the product or technical risk.

Implementation
Implement the first slice completely before expanding. Add only the minimum code, schema, wiring, tests, and interface needed for that path. Reuse existing patterns. Avoid creating frameworks or abstractions for hypothetical future slices unless duplication is already causing friction.

Verification
Prove the slice from the observer’s point of view. Use the narrowest reliable test that crosses the important boundaries. Record the exact command, request, UI action, or fixture needed to reproduce the result. If the slice cannot be demonstrated or tested independently, make it thinner or redefine the boundary.

Review checkpoint
After each slice, summarize what now works, what was deliberately deferred, what was learned, and what the next thinnest slice is. Stop when the user’s requested outcome is met. Do not continue into cleanup, hardening, optimization, or generalization unless requested or required for correctness or safety.

Failure modes
Reject horizontal progress that produces no testable behavior, such as building all infrastructure first, finishing all backend endpoints before any caller can use them, or creating abstractions before one concrete path works. Reject slices that are technically small but still require many later pieces before feedback is possible. Reject fake end-to-end demos that stub the exact uncertainty the work is meant to validate.

Output style
Be terse. For planning, return the target outcome, the first slice, deferred scope, verification, and next slice. For implementation, make the changes and report only the observable result, verification evidence, deliberate deferrals, and next slice if useful. Do not produce a large roadmap unless requested.
