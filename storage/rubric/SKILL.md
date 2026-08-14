---
name: candidate-takehome-rubric
description: >-
  Evaluate a software engineering candidate using the job description, take-home
  assignment/specification, and candidate GitHub repository or submission. Use this
  skill whenever asked to review, grade, rank, score, calibrate, or make an interview
  recommendation from a candidate coding exercise, GitHub repository, work sample,
  or take-home submission. Produce a five-category verdict with calibrated
  probabilities: fail, barely pass, pass, strongly pass, or
  "if you don't interview this candidate you are an idiot."
---

---

# Candidate Take-Home Rubric

## Objective

Determine how strongly the candidate's actual submission supports advancing them to interview **for the specific role described by the supplied job description**.

Evaluate the work, not the candidate's identity or pedigree.

The final result must be one of:

1. **fail**
2. **barely pass**
3. **pass**
4. **strongly pass**
5. **if you don't interview this candidate you are an idiot**

Also produce a probability for **every** category. Probabilities must sum to 100%.

There is no quota or rarity prior on category 5. If the evidence supports category 5, assign it. If several candidates deserve category 5, all of them can receive it.

The probabilities represent uncertainty about **which rubric category best describes the observed submission**. They are not probabilities of job performance, retention, culture fit, or eventual hiring.

---

# Evidence inputs

Use, when available:

1. Job description
2. Take-home assignment/specification
3. Candidate repository/submission
4. README and design notes
5. Source code
6. Tests
7. Build/lint/type-check configuration
8. CI configuration
9. Relevant commit history
10. Runtime behavior or test output if execution is possible

Do not invent missing evidence.

If an input is unavailable, continue with the available evidence and lower evaluation confidence appropriately.

Distinguish:

- **candidate omission** — something the assignment reasonably required but the candidate did not provide
- **evaluation limitation** — something exists or may exist but cannot be inspected or executed in the current environment

The former affects the score. The latter primarily affects confidence.

---

# Fairness boundary

Only use evidence directly relevant to the role and submitted work.

Ignore and do not infer:

- age
- gender
- race or ethnicity
- nationality except where legally required and explicitly handled elsewhere
- religion
- disability or health
- family status
- sexual orientation
- political views
- socioeconomic background

Do not reward:

- prestigious employers
- famous schools
- GitHub stars
- follower counts
- account age
- volume of unrelated open-source work
- personal branding
- unusually large amounts of free time implied by GitHub activity

A GitHub repository is useful because of the engineering evidence inside it, not because of social or prestige signals surrounding it.

---

# Step 1 — Derive the actual hiring bar

Read the job description before judging the submission.

Extract:

### Role level

Infer the intended level from the JD:

- junior
- mid
- senior
- staff+
- ambiguous

Do not silently grade a junior role using staff expectations or vice versa.

### Requirements

Separate JD requirements into:

- **critical** — inability here materially undermines suitability for the role
- **important**
- **useful**
- **irrelevant to this exercise / impossible to observe**

Do not turn every bullet in a JD into an equally weighted criterion.

Identify the 3–6 technical capabilities that most determine success in this particular role.

Examples might include:

- backend/API design
- frontend state/UI engineering
- distributed systems
- data modeling
- infrastructure
- ML engineering
- security
- performance
- product judgment
- maintainability
- testing/reliability

Use the JD itself to determine which matter.

---

# Step 2 — Convert the assignment into acceptance criteria

Extract every meaningful requirement from the take-home.

Classify each as:

- required
- implied but important
- optional/stretch

For each required item, determine:

- whether it exists
- whether it actually works
- how well it works
- whether important edge cases are handled
- whether implementation quality is appropriate to the requested scope

Do not let bonus functionality compensate for missing core functionality.

Do not reward complexity merely because it exists.

A smaller implementation with strong judgment can outperform a larger implementation with unnecessary machinery.

---

# Step 3 — Inspect the repository deeply

Do not grade primarily from the README.

Inspect enough of the repository to understand the actual implementation.

Normally inspect:

- repository structure
- manifests/dependencies
- central source files
- data models
- API boundaries
- major abstractions
- tests
- configuration
- error handling
- type usage where applicable
- linting/formatting
- CI
- README/design notes

When possible, run the relevant:

- install
- build
- test
- lint
- type-check
- application startup

Do not treat inability to execute because of evaluator infrastructure as candidate failure.

If execution fails because the repository itself is incomplete or broken, treat that as evidence.

Inspect commit history only when it provides job-relevant evidence such as:

- coherent decomposition
- intentional iteration
- meaningful technical decisions
- clear corrections

Do not score commit count, cadence, timestamps, or apparent amount of personal time spent.

---

# Step 4 — Build an evidence matrix before scoring

For each important assignment/JD criterion, record:

**Criterion:**
**Importance:** critical / important / useful
**Evidence for:**
**Evidence against:**
**Unknowns:**
**Assessment:**

Keep observations separate from interpretation.

Example:

**Criterion:** reliable API behavior
**Importance:** critical
**Evidence for:** typed handlers, validation, integration tests for normal flow
**Evidence against:** duplicate request race is unhandled
**Unknowns:** production persistence behavior not exercised
**Assessment:** meets bar with a material concurrency weakness

This evidence matrix is the basis of the score.

---

# Step 5 — Score six dimensions

Score every dimension from **0.0–5.0**. Half-points are allowed.

Use these anchors consistently:

- **0** — absent, fundamentally broken, or demonstrates seriously poor judgment
- **1** — materially below the expected bar
- **2** — below bar with some competent elements
- **3** — meets the expected role/assignment bar
- **4** — clearly above bar
- **5** — unusually strong evidence for this role

A 3 is good. Do not make "meets expectations" secretly mean 4.

## A. Functional correctness & assignment compliance — 30%

Does the submission solve what was actually requested?

Consider:

- required functionality
- correctness
- completeness
- edge cases
- ability to run
- adherence to explicit constraints

## B. Role-relevant technical strength — 25%

How strong is the work on the capabilities the JD actually cares about?

This dimension should be customized from the JD rather than replaced with generic software-engineering preferences.

## C. Engineering judgment & architecture — 15%

Evaluate:

- decomposition
- abstraction choices
- interfaces
- data modeling
- tradeoffs
- simplicity
- extensibility where justified
- handling of complexity
- appropriate technology choices

Reward **appropriate simplicity**.

Penalize unnecessary abstraction, architecture astronautics, cargo-cult patterns, and technology introduced without corresponding value.

## D. Reliability, testing & defensive engineering — 15%

Evaluate what is relevant for the role:

- test quality
- test coverage of important behavior
- failure modes
- error handling
- validation
- security
- concurrency
- observability
- reproducibility

Do not equate raw test count with test quality.

## E. Maintainability & implementation quality — 10%

Evaluate:

- readability
- naming
- cohesion
- duplication
- typing
- consistency
- local reasoning
- dependency discipline
- code that another engineer could safely modify

## F. Technical communication & developer experience — 5%

Evaluate:

- README
- setup quality
- explanation of important choices
- explicit assumptions
- useful tradeoff discussion
- reproducibility

Do not reward verbosity.

A short README that answers the important questions can score higher than a long one.

---

# Step 6 — Calculate the raw score

Let each dimension score be `d_i` from 0–5 and each weight be `w_i`.

Calculate:

`raw_score = Σ(w_i × d_i / 5)`

With the default weights:

`raw_score =`
`30 × A/5`
`+ 25 × B/5`
`+ 15 × C/5`
`+ 15 × D/5`
`+ 10 × E/5`
`+ 5 × F/5`

Result: 0–100.

Interpretation:

- a candidate who simply meets the bar everywhere scores approximately 60
- above-bar work naturally moves toward 80
- uniformly exceptional work approaches 100

Do not manipulate individual scores merely to force a preferred final category.

---

# Step 7 — Apply critical-requirement gates

The weighted average cannot erase fundamental failures.

Apply these after computing the raw score.

## Fundamental failure

If the submission fails the central purpose of the assignment, is substantially non-functional because of candidate-controlled problems, or omits a genuinely critical requirement:

`effective_score <= 44`

Use this only for genuinely central failures.

## Major role-critical gap

If the candidate demonstrates strong work overall but materially fails one capability that the JD makes essential to doing the job:

`effective_score <= 74`

Do not apply this because of a nice-to-have.

## No critical gaps

Do not cap the score.

Category 5 does **not** require perfection. Minor issues are compatible with the highest category.

The relevant question is whether remaining weaknesses materially reduce the strength of the interview signal.

---

# Step 8 — Determine evidence confidence

Calculate an evidence-confidence value `C` from 0.50–1.00.

Suggested anchors:

### 1.00

- JD is clear
- assignment is clear
- repository was inspected deeply
- important code paths were inspected
- build/tests/runtime were successfully exercised

### 0.90

Strong repository inspection with only minor unavailable evidence.

### 0.80

Good static inspection, but execution was unavailable or some meaningful behavior could not be verified.

### 0.70

Material ambiguity or incomplete repository visibility.

### 0.60

Significant evidence is missing.

### 0.50

Assessment is possible but highly uncertain.

Do not lower confidence simply because the submission is bad. Confidence measures evidence quality, not candidate quality.

---

# Step 9 — Convert score into category probabilities

Use an ordered probability model rather than arbitrary percentages.

Let:

`S = effective_score`

Use category boundaries:

- fail / barely pass: `45`
- barely pass / pass: `58`
- pass / strongly pass: `75`
- strongly pass / category 5: `90`

Let uncertainty scale be:

`b = 3 + 10 × (1 - C)`

Define:

`F(x) = 1 / (1 + exp(-x))`

Then calculate:

`P(fail) = F((45 - S) / b)`

`P(barely pass) = F((58 - S) / b) - F((45 - S) / b)`

`P(pass) = F((75 - S) / b) - F((58 - S) / b)`

`P(strongly pass) = F((90 - S) / b) - F((75 - S) / b)`

`P(if you don't interview this candidate you are an idiot) = 1 - F((90 - S) / b)`

Round to whole percentages while preserving a total of exactly 100%.

The winning category is the category with the highest probability.

This model intentionally has **no prior penalty against category 5**.

A submission with sufficiently high `S` and strong evidence confidence should naturally place most probability mass on category 5.

---

# Category semantics

## 1. Fail

The evidence argues against spending an interview slot.

Typical pattern:

- meaningful core requirements missed
- serious correctness problems
- role-critical technical weakness
- weak engineering judgment
- submission does not establish the expected level

This does not mean every part is bad.

It means the aggregate interview signal is negative.

## 2. Barely pass

There is enough evidence of competence that interviewing is defensible, but meaningful concerns remain.

Typical pattern:

- basic solution works
- bar is met inconsistently
- important weaknesses are visible
- limited evidence of depth
- interviewer would need to resolve substantial uncertainty

This should feel genuinely borderline.

## 3. Pass

The candidate demonstrates the expected level for the role.

Typical pattern:

- required functionality works
- reasonable implementation
- adequate tests/reliability
- sensible technical decisions
- no major role-critical weakness

Interviewing the candidate is reasonable and supported by the work sample.

## 4. Strongly pass

The evidence is clearly above the role's normal bar.

Typical pattern:

- strong implementation
- strong judgment
- good handling of important edge cases
- thoughtful architecture without unnecessary complexity
- tests target meaningful risks
- technical choices withstand scrutiny

Interviewing is strongly recommended.

## 5. If you don't interview this candidate you are an idiot

Use this category when the take-home creates such a strong job-relevant signal that declining to interview would be difficult to justify from the submitted work.

Typical pattern:

- core requirements are handled convincingly
- role-critical technical ability is substantially above the expected bar
- architecture and implementation demonstrate unusually strong judgment
- important failure modes are anticipated rather than merely patched
- complexity is reduced rather than displayed
- tests demonstrate understanding of the actual risk surface
- tradeoffs are explicit or clearly reflected in the implementation
- there are no material weaknesses that undermine the interview signal

This category does **not** mean:

- flawless
- maximally complex
- huge submission
- lots of bonus features
- famous GitHub profile
- "probably a genius"
- guaranteed hire

It means:

> The submitted engineering evidence is strong enough that an interview is the obvious next information-gathering step.

Do not ration this category. Do not require some arbitrary percentage of candidates to fall below it.

---

# Step 10 — Perform a counter-read

Before finalizing, argue the strongest reasonable case **against your preliminary verdict**.

Ask:

- Did polish create a halo effect?
- Did a sophisticated architecture distract from incorrect behavior?
- Did working functionality hide weak engineering judgment?
- Am I overvaluing technologies I personally prefer?
- Am I penalizing a simpler solution despite it solving the problem better?
- Am I double-counting the same strength across multiple dimensions?
- Am I treating an evaluator limitation as a candidate failure?
- Am I rewarding effort/volume rather than outcome?
- Is a JD requirement actually critical, or merely mentioned?
- Would I give the same score if the exact same code came from a candidate with a different background?

If this materially changes the evidence assessment, update the relevant dimension scores and recalculate.

Do not manually edit the resulting probabilities because they "feel too high" or "too low."

---

# Output format

Use this structure exactly.

# Candidate Evaluation

**Verdict:** [category]

**Probability distribution**

- Fail: X%
- Barely pass: X%
- Pass: X%
- Strongly pass: X%
- If you don't interview this candidate you are an idiot: X%

**Effective score:** X/100
**Evidence confidence:** X.XX

## Bottom line

2–5 sentences explaining why the winning category dominates.

State whether the submission creates:

- negative interview signal
- borderline interview signal
- positive interview signal
- strong interview signal
- overwhelming interview signal

## Rubric

- Functional correctness & assignment compliance: X/5 — evidence
- Role-relevant technical strength: X/5 — evidence
- Engineering judgment & architecture: X/5 — evidence
- Reliability, testing & defensive engineering: X/5 — evidence
- Maintainability & implementation quality: X/5 — evidence
- Technical communication & developer experience: X/5 — evidence

## Strongest evidence for the candidate

List the 3–5 most decision-relevant observations.

Every point should refer to concrete repository or assignment evidence.

## Strongest evidence against the candidate

List the 1–5 most meaningful weaknesses.

Do not manufacture negatives simply for balance.

## Critical requirement check

For every critical requirement:

- requirement
- status: met / partially met / not met / unknown
- evidence

State whether any score cap was applied and why.

## What I would probe in interview

Give 2–5 questions targeted specifically at uncertainties or interesting technical decisions revealed by the submission.

Do not give generic interview questions.

## Calibration note

Briefly state what missing evidence, if any, is responsible for probability mass being distributed across adjacent categories.

---

# Evaluation principles

Prefer demonstrated evidence over speculation.

Prefer correctness over polish.

Prefer judgment over complexity.

Prefer meaningful tests over high test counts.

Prefer explicit tradeoffs over accidental architecture.

Prefer role-specific evidence over generic notions of "good engineering."

Do not give extra credit twice for the same underlying behavior.

Do not penalize reasonable choices merely because another implementation could also work.

Do not assume unusual code is sophisticated. Determine whether it solves a real problem.

Do not assume simple code is unsophisticated. Determine whether complexity was actually necessary.

Do not soften a poor verdict because the candidate appears hardworking.

Do not suppress a high verdict because category 5 sounds extreme.

The rubric exists to discriminate based on the strength of the engineering evidence.
