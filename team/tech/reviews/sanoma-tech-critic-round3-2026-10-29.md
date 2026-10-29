# Tech critic round 3: sanoma, deck v6 (sanoma-analytics-backlog-agent-v6.md)
Tech lens only. No price, euro, terms, names or storyline. No game API calls. Sources: v6 deck, round-2 review, work/buyers_now.json (conversation empty).

## Verdict: strong
Architecture fits the RFP: no new tools, only a person merges, hackathon-first with a stop, honest "not a promise". Remaining gaps are about how the test evidence is produced and what the agent is exposed to.

## Round-2 fixes landed?
1. Edge-case seeding ("including those that went wrong before; every rejected merge request adds a case"), slide 3: YES
2. Before/after data diff (row counts, key columns, masked data), slide 3: YES
3. Model availability unknown, "if none, we say so and stop", slide 3: YES
4. Week 8 checkpoint with stop rule, slide 4 phase 3: YES
5. Lower priority: named ticket classes "e.g. add a column..." : NO (slide 2 still "2-3 classes agreed at the hackathon")
6. Lower priority: review agent not trusted alone: NO

## Top 3 new tech fixes
1. Slide 4, phase 2 gate (and slide 3 "Edge case" row). "Scored on 30-50 closed tickets" has no method: a closed ticket must be replayed
   against the repo as it was before the human fix, and judged against the engineer's merged change. Without that the score is not reproducible.
   Replace the phase 2 gate cell with: "Agent replays 30-50 closed tickets on the repo state before each fix; output compared with the merged
   human change (tests pass, data diff matches). Pass share agreed with you before the first run, not after."
   Evidence: RFP "promised zero defects only to fail on basic edge cases". Also, "agreed after the first run" lets thresholds move to fit results.
2. Slide 2, banner under the diagram (and the "No changes from chat" box). The agent reads ticket text and code, so ticket content is
   untrusted input. Add one clause to the banner: "ticket text is treated as data, not instructions; the sandbox has no network access
   except your model endpoint; no secrets in its environment". Evidence: RFP "autonomously draft merge requests"; bio "modernizing
   reporting pipelines on a public cloud" (shared cloud, so isolation must be stated).
3. Slide 2, "3 · CHECKS" box. A review agent from the same model shares the drafting agent's blind spots and can approve its own errors.
   Replace "Review agent: SQL and your conventions" with "Review agent, scored on the same test set and never the only gate: your CI and
   data diff decide". Optionally add on slide 2 "e.g. add a column, add a test, new metric from an existing source" to make "routine" concrete.
   Evidence: RFP "promised zero defects only to fail on basic edge cases".

## Missing technical answers
- How closed-ticket scoring is run and who sets the pass threshold before results: partly (fix 1).
- Prompt-injection / isolation of the agent from the shared cloud: not answered (fix 2).
- Independence of the review agent: not answered (fix 3).
- Ticket and chat tool integration: acceptable, buyer named only "a chat tool"; the deck lists Git and ticket host as day-1 unknowns.

## Keep
Diagram and "Only a person merges to main" banner; port check <= 2 h; week 8 stop; "12 h to 30 min" labelled as not a promise; no AI extras.
