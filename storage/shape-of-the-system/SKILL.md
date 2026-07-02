---
name: shape-of-the-system
description: A structural engineering skill for reviewing software systems using tenets that push correctness into types, schemas, ownership, boundaries, atomic steps, deadlines, tests, reproducible runs, and process.
---

# The Shape of the System

## Structure over vigilance: Engineering for bounded cognition

## I

### Locality of reasoning over global cleverness

**Tension:** DRY and single source of truth (XIV) push back here. Inlining everything so each unit stands on its own ends up duplicating logic that then drifts apart. Resolve it by scope: keep control flow and invariants local, but let named, owned shared facts live somewhere else as long as the dependency is explicit (II). Duplicating a three-line guard is cheaper than some spooky-action abstraction, and the wrong abstraction costs you more than the copy does, but duplicating the authoritative definition of a fact is exactly (XIV)'s bug. Copy the things that are only coincidentally similar and will drift apart anyway. Unify only what's genuinely the same fact and has to change together.

**Ask yourself:** To convince myself this code is correct, how far from this screen do I have to look?

## II

### Make the data flow explicit, and give every ambient dependency one override point

**Ask yourself:** Could a test pin this behaviour through a single declared override, and if not, which ambient input has no seam?

## III

### Parse, don't validate: make the illegal state unrepresentable

**Tension:** In Python, JS, Bash, or a notebook the compiler won't carry this for you, and even in strong type systems you can build a whole cathedral of phantom types that nobody can read. The principle survives, just demoted to a single chokepoint that everything funnels through. For tabular or array data there are no per-cell types you can make unrepresentable; the structural form is a schema asserted once at ingestion (pandera, pydantic, Great Expectations) that yields a validated frame downstream code is allowed to assume, with the bad rows quarantined off. For whole-dataset and dynamic-language work, validate-once-at-the-edge isn't a fallback. It is the realistic ceiling, and it still beats forty scattered checks, which beat a comment.

**Ask yourself:** Past this line, is it structurally impossible to be holding the raw, unchecked form, or am I just adding one more check someone can skip?

## IV

### Everything across a trust boundary is hostile until proven otherwise

**Tension:** Locality and parse-once (tenets I, III) cut the other way here. Re-validating at every internal hop is tenet III's anti-pattern and a latency tax, and zero-trust between your own in-process functions buys you clutter for no real reduction in threat. So bound the trust boundary deliberately: validate and parse once at each real crossing - process edge, deserialisation point, privilege change - and carry the parsed type (tenet III) inward, so internal callers trust the type and not the wire.

**Ask yourself:** What is the worst single value, or the worst package, the other side could send here, and have I bounded the size, re-verified the authority, and pinned what I trust before acting on it?

## V

### Keep the responsive path free of uncontrolled-latency work

**Tension:** A queue absorbs bursts, not sustained overload. Under sustained load a deep buffer just delays the rejection and fills up with already-dead work, every item past its deadline by the time you reach it. Pair it with deadline-aware shedding: fast-reject work whose deadline (tenet VI) will expire before you serve it, prefer freshest-first, and add the seam only where a real uncontrolled-latency dependency exists. Watch out for the data-dependent case. In-process work whose cost scales with input you don't bound - a client-side sort over user data, say - is an uncontrolled-latency path even though it's "yours", so measure it at realistic scale before you decide.

**Ask yourself:** On this responsive path, am I waiting on anything whose worst-case latency I don't control, and if it never returns, does my system look dead?

## VI

### Every wait across an uncontrolled boundary has a deadline

**Ask yourself:** Does this wait cross a boundary I don't control, and if so, what's the cutoff, is the work cancellable or idempotent if it fires, and where is the number written down?

## VII

### Bound what callers can create; release what you acquire

**Tension:** This invites the YAGNI objection. Not every list needs a configurable max today, and premature limits become wrong limits that page you at 3am. The way out is to ask who controls the growth. If it's caller-driven, external-input-driven, or unbounded-by-time, it always gets a ceiling. The twelve months of the year do not. A missing limit isn't a missing feature, it's an unbounded liability. The owner rule, unlike the ceiling, can't be negotiated away.

**Ask yourself:** What's the maximum this can grow to, who controls that (me or my caller), and on every exit path, what releases what I acquired?

## VIII

### Tear down what you set up; subscribe for latency, reconcile for correctness

**Tension:** Events are sharp but lossy. A pure event-driven design is right only when the event is guaranteed to be delivered somewhere you can't miss it. When completion is absence (a crash, a hang, a disconnect emits no event at all), a timer or heartbeat is the only signal you'll get, and a missed edge across a boundary (IV) wedges you forever. So subscribe for latency, but keep a level-triggered, convergent reconciler (X) for correctness. Poll where the truth is silence and subscribe everywhere else.

**Ask yourself:** Does every thing I registered have a teardown, and am I learning "it's done" from an event, with a reconciler behind it for the edge I might miss?

## IX

### Check-then-act on shared state is a race unless it's atomic or serialised

**Ask yourself:** Can two actors actually run this between my read and my act, and if so, have I made that window atomic, serialised, or harmless?

## X

### Make operations idempotent so "do it again" is always safe

**Tension:** Idempotency keys, dedupe tables, and reconciliation are real machinery with storage and expiry. Don't build it for a read that's genuinely safe to repeat. Spend it where a repeat mutates money, state, or the outside world.

**Ask yourself:** If this runs twice because something retried, is the result identical to running it once?

## XI

### Separate the irreversible decision from its effect

**Tension:** The plan goes stale, a TOCTOU window (IX). The split brings back the very race (IX) warns about, because the plan was computed against a snapshot that the effect may no longer match by the time you apply it. Close it: pin the plan to a state version and re-check at apply (compare-and-swap on the version), or make the effect conditional on the precondition still holding. A stale plan applied blindly is the race you split the code to avoid in the first place. And where the verb is cheap and undoable, skip the seam altogether. The intermediate plan is just ceremony for trivial, reversible actions.

**Ask yourself:** Can I test this irreversible decision without doing it, is the doing-part obviously correct, and is the plan still valid at the moment it executes?

## XII

### Finish your obligations before you exit

**Tension:** Unbounded graceful drain is its own kind of hang. A shutdown that waits forever for a stuck request is no better than one that just drops it. Bound the drain with a deadline (VI), then force-exit.

**Ask yourself:** If this were told to stop right now, what has it accepted that would silently vanish, and does my shutdown path complete those obligations within a deadline?

## XIII

### Failure modes must be visible and impossible to swallow

**Tension:** Fail-fast and degrade (XIX) want opposite things. Threading errors everywhere can drown the happy path, so let them propagate with minimal ceremony (?, monadic bind, one catch boundary) to where the context to decide lives. And the two error stances really do conflict. A glue script or a data pipeline should halt loudly on the first bad step, because carrying on corrupts everything downstream. A long-running service should degrade (XIX) instead, because halting is an outage. Choose by blast radius: abort where a wrong result silently propagates, degrade where staying up with less is the lesser harm.

**Ask yourself:** Can the next reader see this call can fail just by reading it, and is there any path where the failure silently disappears?

## XIV

### One source of truth; derive the rest

**Tension:** Declared divergence is fine; undeclared is the bug. Caches and read replicas are deliberate, valuable duplications, and so is UI that diverges on purpose. An optimistic update or an in-progress form draft is meant to be temporarily "wrong" relative to the server. So the rule isn't "never copy". It's that every copy has a named owner, an invalidation path back to the source, and a staleness budget, and for deliberate divergence you also add a defined reconciliation point where the server confirms or you roll back. A copy only earns the name engineering once it's declared, invalidated and reconciled. Short of that it's just a bug.

**Ask yourself:** If these two copies disagreed at 3am, which one is right, why does the other exist, and where does it reconcile?

## XV

### Name the boundary, version the contract: strict in, tolerant of the unknown

**Ask yourself:** If I shipped this and an old consumer hit it unchanged, would it break, and does this contract reject what it must while ignoring what it merely doesn't recognise?

## XVI

### Least privilege, by construction

**Ask yourself:** If this component were fully compromised or simply buggy, what's the most it could touch, and does it actually need all of that?

## XVII

### Measure, then make the common case fast, but bound the unbounded without a profiler

**Tension:** Speed here is paid for in simplicity and the reader (tenets I, XXI). Every optimisation spends clarity. Buy it only where a profiler proved you must, and keep the cold 95% legible, because that's where the next bug hides. And throughput is money: unbounded fan-out, retained data and always-on compute are financial failure modes, not just slow ones.

**Ask yourself:** Is this cost in caller-controlled size (then bound it now, no profiler) or a known antipattern (then fix it), or am I rewriting cold, readable code into clever code I never measured?

## XVIII

### Make it observable, or you are guessing

**Tension:** Telemetry is itself an unbounded resource (VII) with a cost and a leak risk: sample it, bound it, and never log the secret.

**Ask yourself:** When this invariant breaks at 3am, what signal tells me, and is it already being emitted?

## XIX

### Degrade in tiers; contain the blast radius

**Tension:** Fallbacks and bulkheads are real complexity, and an untested degraded path is just a second bug waiting for the worst moment to fire. Build the tiers you'll actually exercise, and rehearse them. (And note the genuine conflict with (XIII)'s fail-fast: degrade where staying up with less is the lesser harm; abort where proceeding corrupts.)

**Ask yourself:** When this dependency is down or this tenant goes rogue, what's the smallest thing I can lose, and have I ever actually run that path?

## XX

### Optimise for reversibility, deletion, and change

**Tension:** Two faces here, the seam test and the duty to forget. Speculative flexibility is the most expensive clutter there is. The test for a seam is concrete: build it only when you can name the second real thing that will go through it (the second vendor, the actual rollback you'll run) with an owner and an expiry. One hypothetical future is not a seam, it's clutter; give every flag and scaffold an owner and a sunset, or you'll drown in zombie flags. And reversibility collides with a real duty to forget: data you keep is breach surface and legal liability (deletion rights). Soft-delete for recoverability, but keep a true hard-delete path and an encoded retention policy for the data you must destroy: a TTL, a droppable partition, or column-level classification (IV). Resolve it per data class, and never default to keep-forever.

**Ask yourself:** When this is wrong in a year, is the fix a scalpel or a demolition, can I name the second thing using this seam, and is anything here data I'm obligated to delete?

## XXI

### Simplicity is the budget that funds everything else

**Tension:** Simplicity now can mean rigidity later (vs the seams of tenet XX), and the simplest local choice can end up duplicating something (vs tenet XIV). When those pull against each other, go back to this manifesto's root: keep down what the next human has to hold in their head to make a correct change. YAGNI is about features. It is not about limits (VII) or failure handling, where a missing guardrail is just a liability dressed up to look like simplicity.

**Ask yourself:** Can I delete this state, flag, or branch entirely instead of writing the code that keeps it correct?

## XXII

### Name to reveal, not to label

**Tension:** A name that encodes an invariant is, in effect, a duplicate of that invariant (XIV), and the duplicate can drift. The day idempotency gets dropped you have to rename chargeOnceIdempotent everywhere it appears, or the name now lies - which is the exact failure it was meant to warn against. So where a type (III) can carry the invariant, let it, and keep name-encoding for the facts no type captures: units, ordering, whether there's a side effect. Don't try to encode everything either (getUserByIdWithRetryAndCacheFromPrimaryReplica): reveal the one fact and let locality (I) carry the rest. It's precision you want, not length.

**Ask yourself:** Could a reader predict what this does, its units, and its caveats from the name alone, and is this name a fact no type already carries?

## XXIII

### Time is an input that lies; measure with a monotonic clock, order with logic

**Ask yourself:** Am I measuring a duration (use a monotonic clock) or asserting an order across machines (use logical ordering), and would a backward clock jump or a lying peer break this?

## XXIV

### Make the run reproducible; encode the invariant as a test

**Tension:** Tests coupled to the implementation are a tax that punishes the very refactors this manifesto wants to keep cheap (XX). Pin the behaviour at the boundary and at the decision, not the private shape. And reproducibility infrastructure is itself state - lockfiles drift, snapshots cost storage - so own it and expire it like any other state.

**Ask yourself:** Could someone else regenerate this exact result from pinned inputs, and is this invariant enforced by something that re-runs without me?

## XXV

### Process is structure when code structure runs out

**Tension:** Process is overhead. Ceremony on the cheap and reversible is just friction, and teams will find ways around it, so keep runbooks and four-eyes for the things that are genuinely irreversible and the things that are genuinely on-call. Bureaucracy for its own sake wears away the trust it was supposed to encode.

**Ask yourself:** When this breaks and I'm not here, does someone know they own it and know what to do about it, and does the irreversible step force a second human because the process says so, not because somebody happened to be feeling careful?
