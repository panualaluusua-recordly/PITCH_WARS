# Tech critic round 2: sanoma, deck v5 (sanoma-analytics-backlog-agent-v5.md)
Tech lens only. No price, euro, terms, names or storyline comments. No game API calls.
Sources: v5 deck, round-1 review, work/buyers_now.json (RFP and bio; conversation is empty).

## Verdict: strong
Every round-1 fix is in the deck. Remaining gaps are second-order: they sharpen the answer to the buyer's
two stated fears (basic edge cases, black-box adoption) and add a mid-pilot stop rule.

## Round-1 fixes: landed?
1. Slide 5 certifications made conditional on the platform confirmed day 1: YES (all three columns).
2. Slide 2 model hosting, retry cap 3, cost cap proposed day 2: YES ("Model hosting and caps" line).
3. Slide 4 phase 1 port check (<= 2 h, repo/CI access, dev schema, hand-built model change): YES.
Lower-priority items from round 1:
- Seed edge-case set from tickets that "always went wrong": NO (slide 3 says only "30-50 of your closed tickets").
- Name routine ticket classes as examples: NO (slide 2 says "2-3 classes agreed at the hackathon", none named).
- Masking approach named: PARTLY ("non-prod or masked data" on slide 2; slide 3 says rules agreed before day 1).

## Top 3 new tech fixes
1. Slide 3, "Edge case" row and "Wrong change passes the tests" row. A test-passing wrong change is
   caught only by human reading. Add an automatic evidence item and the seeding rule.
   Replace the Edge case cell with: "Scored first on 30-50 of your closed tickets, including those that
   went wrong before; every rejected merge request adds a case."
   Replace the agent cell of the last row with: "Cannot merge. Merge request attaches a before/after data diff
   (row counts, key columns) on masked data, plus its reasoning."
   Evidence: RFP "promised zero defects only to fail on basic edge cases".
2. Slide 3, "Technical unknowns, resolved on day 1" line. Model availability in the unnamed cloud is the
   one unknown that can break the plan and it is not listed. Slide 2 asserts "the model runs in your
   cloud tenant" without saying that must be checked. Replace the line with:
   "Technical unknowns, resolved on day 1: warehouse and transformation tool, Git and ticket host, which
   approved model is available in your tenant (if none, we say so and stop), personal data in tickets or
   samples (masking rules agreed before day 1)."
   Evidence: RFP "current data setup hosted on a public cloud".
3. Slide 4, phase 3 gate. The pilot has a weekly note but no stop rule between week 4 and week 16, so
   a failing agent keeps consuming engineer review time. Add to the phase 3 gate cell:
   "Week 8 checkpoint: if approved-without-rework share or review minutes miss the thresholds agreed in
   phase 2, we pause, fix on the test set, or stop. Sanoma decides."
   Evidence: RFP "pilot" and "keeping human oversight central"; deck already measures "review minutes".

## Lower priority
- Slide 2: replace "2-3 classes agreed at the hackathon" with "e.g. add a column, add a test, new metric from
  an existing source (2-3 classes agreed at the hackathon)". Makes "routine" concrete.
- Slide 2: the review agent and the drafting agent can share model blind spots. One clause: "the review
  agent is checked against the same test set, not trusted alone" if the team wants to pre-empt this.

## Missing technical answers
- Behaviour if no suitable model is available in the buyer's cloud: not answered (fix 2).
- Automatic evidence for a wrong-but-green change: not answered (fix 1).
- Mid-pilot stop trigger: not answered (fix 3).
- Ticket tool and chat tool: unmentioned beyond "Git and ticket host"; acceptable, buyer named only "a chat tool".

## Already good (keep)
- Diagram and "Only a person merges to main" banner; branch protection, no prod credentials, pause switch.
- "12 h to 30 min" labelled as not a promise. Hackathon-first with a stop point and scoped unknowns.
- No new tools, no AI extras, no sovereignty claims.
