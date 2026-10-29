# Tech-critic review: elisa v5 (2026-10-29)
Tech lens only. No price, terms, names or style. Read-only; no game API calls.
Checked: team/decks/elisa/elisa-data-platform-architecture-and-tool-selection-as-v5.md against team/buyers/elisa.md, team/tech/slides/elisa.md, team/tech/batch3/elisa.md.

## Verdict: adequate (upper end)
The P10 trap is answered honestly and the stack matches the buyer's (BigQuery, Composer, Looker, Power BI). The ERP, Power BI mode and DAG location are named as unknowns with a settle-by step. Three regressions from the tech slide spec weaken the proof of the real-time claim.

## Top 3 tech fixes

1. Slide 4 (gates), Gate 1 row and Checkpoint B row: the real latency test moved from the sprint to week 8.
   - The spec had "one real feed run Pub/Sub to BigQuery to Looker, end-to-end latency measured" at Gate 1. v5 keeps it only at Checkpoint B.
   - Result: the steering committee agrees "target range per tier" at Gate 1 with no streaming measurement. That is the numeric-before-measurement pattern.
   - Change: add to the Gate 1 "Passes when" cell: "one real feed run Pub/Sub to BigQuery to Looker in a sandbox dataset, end-to-end latency measured". Keep the Checkpoint B test as the second, per-tier test.

2. Slide 4, "Access ready" row: it contradicts the planned latency test.
   - v5 says "read-only Elisa-issued roles" and "no subscriber rows leave your GCP project". It dropped the spec's "a sandbox dataset for the latency test".
   - A Pub/Sub to BigQuery test needs a write-enabled sandbox dataset and a feed Elisa can point at it. Read-only roles cannot run it.
   - Change: append "plus a write-enabled sandbox dataset and one feed, in your project, for the latency test (synthetic or masked data only)". Add the fallback to the unknowns table: "if no sandbox by day 3, the latency test is marked not tested and streaming stays a proposal".

3. Slides 3 and 4, ERP change-capture fallback: it vanished.
   - The spec had "otherwise API polling". Slide 3 now says "only where the ERP supports it". The unknowns table says "stays micro-batch or daily". The mid-tier option (API polling at a Gate 1 interval) and its effect on the "no delayed refreshes" demand are no longer stated.
   - Change, slide 3 tier box: "Change capture, minutes: where the ERP supports it; otherwise API polling at an interval set at Gate 1". Change, slide 4 ERP row: "Without change capture the ERP domain runs polling or micro-batch, and Gate 1 shows its measured delay against the stated need".

## Smaller notes (not in the top 3)
- Slide 3: Power BI "DirectQuery or import" is handled well. Add a risk line: Power BI DirectQuery on BigQuery cannot meet "seconds" freshness. Looker is the live path, so say which tier each BI tool serves.
- Slide 4: access and lineage appear only as a "same IAM and policy tags" line. Add a Checkpoint B criterion: same IAM and policy-tag behaviour tested in Looker and Power BI on one domain. Add "what happens to existing Composer pipelines" to the Final row.
- Slide 5: the Phase B one-tier test (7 days) now carries the whole proof. Name its pass condition: latency measured against the Gate 1 range, failure mode and cost per tier recorded.
- The deck does not say how the 3-5 priority domains are picked. Add "chosen with you by sprint day 2" to limit scope drift.

## What is already good
- Title and slide 3 name the buyer's "no batch" demand and answer with "real-time where a domain needs it". This matches the P10 honesty that fingrid praised.
- The architecture diagram exists (sources, freshness tiers, BigQuery, serving) with "proposed" and "confirmed in sprint" labels. Pub/Sub is not presented as Elisa's stack.
- No tool the buyer never mentioned is added as a product: no named ERP, no Datastream, no dbt, no AI or ML. "No new licence or platform unless an existing service fails a tested need" fits P7.
- P4 is applied well: a 4-day sprint, Gate 1 with go, adjust or stop, milestones locked only after it. It maps to the stalled-initiative quote.
- Gate table with measurable passes (owner, stated need, measured current freshness from logs). Untested items are marked "not tested".
- Honest unknowns table: ERP, Power BI connectivity, location of Composer code and CI/CD, each with a settle-by step.
- Compliance posture is technically concrete: metadata only, read-only roles, no rows leaving the project, NDA first.
- Option C (all real-time) is scored with its cost rather than refused, so the committee decides.

## Missing technical answers
- Streaming latency proof before Gate 1 (fix 1).
- Sandbox and write access for the test (fix 2).
- ERP fallback tier and its effect on the "no delayed refreshes" demand (fix 3).
- Which BI tool serves which tier (smaller note).
