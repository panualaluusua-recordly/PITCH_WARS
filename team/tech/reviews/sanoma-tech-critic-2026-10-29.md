# Tech critic: sanoma, deck v4 (sanoma-analytics-backlog-agent-v4.md)
Tech lens only. Sources: team/buyers/sanoma.md, v4 deck, team/tech/slides/sanoma.md, batch3/sanoma.md,
ville-drafts-tech-review.md#sanoma. No price, terms, names or style comments. No game API calls.

## Verdict: strong (was adequate at v1)
The v1 findings are closed: Snowflake/dbt is now conditional, merge requests are named in the buyer's wording,
the sandbox and branch-protection bar is explicit, the edge-case set is scored before the pilot, and the
baseline is set at the hackathon with the pass share agreed after the first run (Oriola lesson).
What would still lose points with a sceptical architect is below.

## Top 3 tech fixes
1. Slide 5 (team table), certifications row. It still names Snowflake, dbt and Azure AI certs as "required".
   The buyer says only "a public cloud" (RFP) and "a chat tool". This contradicts the conditional on slide 2
   and is the Outokumpu anti-pattern (naming tools the buyer never named).
   Change to: "Certifications: held for the platform you confirm on day 1 (Snowflake/dbt, or your cloud's
   equivalent); matching profile confirmed before hackathon dates." Do the same for the AI engineer row.
2. Slide 2 (architecture), checks and sandbox boxes. Two numbers and one fact are missing that a data
   architect will look for: the retry cap value, the cost cap value, and where the model runs.
   The buyer's worry is edge cases and oversight, and "run log and cost cap per ticket" is unquantified.
   Add under the diagram banner: "Model runs in your cloud tenant on your credits; tickets and code leave it
   nowhere. Retry cap 3 attempts per ticket; cost cap per ticket proposed on day 2 from the hackathon runs."
   (Evidence: RFP "integrated with its current data setup hosted on a public cloud".)
3. Slide 4 (plan), phase 1 gate. "Go/no-go" has no stated test for "the pattern ports". If the stack is
   not Snowflake and dbt, the buyer cannot tell what we would check. Add to the Phase 1 gate cell:
   "Port check on day 1 (≤ 2 h): repo and CI access, a dev schema, a model change built and tested by hand.
   If any fails we say so and the plan stops there." (Evidence: slide 2 "otherwise the hackathon shows
   whether it ports"; RFP "test feasibility and align on developer workflows".)

## Lower priority (not in the top 3)
- Slide 3: add one sentence that the edge-case set is seeded from tickets that "always went wrong" on day 1
  (this is in tech/slides/sanoma.md gate table but not in the deck). It answers "fail on basic edge cases".
- Slide 2: the "12 h to 30 min" case is correctly labelled "not a promise for your tickets". Keep it as is.
- Slide 4: "routine share unknown until day 1" is honest. Name the 2-3 ticket classes as examples (add a
  column, new metric from an existing source, add a test) so "routine" is concrete.

## Missing technical answers
- Which LLM and where it is hosted in an unnamed public cloud: not answered (fix 2).
- How "ports" is tested on a non-Snowflake stack: not answered (fix 3).
- Personal data in subscriber analytics: slide 3 says masking is agreed before day 1. Good, but the
  masking approach is not named (non-prod copy or masked views). One clause would close it.

## What is already good
- Diagram: ticket to sandbox to checks to engineer, with "Only a person merges to main" as the visual climax.
  It answers "autonomously draft merge requests for our engineers to review and validate".
- Controls are concrete: branch protection with required approval, no agent merge right, no production
  credentials, run log, pause switch.
- Failure table covers unclear ticket, failed tests, stuck agent, edge case and wrong change that passes
  tests. The "no zero defects" wording answers "promised zero defects only to fail on basic edge cases".
- No black box: conventions, prompts and test set live in their repo (answers the adoption failure).
- Phase gates are numeric where possible without inventing targets: baseline first, pass share agreed after
  the first run, replay of the test set on any prompt or model change.
- Hackathon first, with a stop point after it and a scoped unknown list (stack, Git/ticket host, PII).
- No AI extras, no new BI tools, no sovereignty claims (no trigger), so none of the Aktia over-reach.
