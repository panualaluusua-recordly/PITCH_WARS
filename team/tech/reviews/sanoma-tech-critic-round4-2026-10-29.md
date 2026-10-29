# Tech critic round 4: sanoma, deck v7 (sanoma-analytics-backlog-agent-v7.md)
Tech lens only. No price, euro, terms, names or storyline. No game API calls. Sources: v7 deck, round-3 review, work/buyers_now.json (conversation empty).

## Verdict: strong
Every RFP technical ask has a slide: safe automation, human merge, hackathon first, no black box, edge cases, unknown "public cloud". Remaining gaps are small: one absolute claim, one untested data assumption, one dependency of the replay gate.

## Round-3 fixes landed?
1. Replay on repo state before each fix, compared with merged human change (slides 3, 4): YES
2. Ticket text as data, no network except model endpoint, no secrets (slide 2 banner): YES
3. Review agent never the only gate, CI and data diff decide (slide 2 box): YES
4. Lower priority: named ticket classes ("add a column, add a test..."): NO (slide 2 still "2-3 classes agreed at the hackathon"; acceptable, but concrete examples help)

## Top 3 new tech fixes
1. Slide 2, "Model hosting and caps" line. "tickets and code leave it nowhere" is an absolute claim made before the model, tenant and cloud are known, and
   it conflicts with the day-1 unknown "which approved model is available". Replace with: "the model runs in your cloud tenant on your credits; we
   confirm on day 1 that ticket and code data stay inside it, and stop if the available model cannot do that."
   Evidence: RFP "integrated with its current data setup hosted on a public cloud"; bio "a public cloud".
2. Slide 4, phase 1 gate and phase 2 gate. The 30-50 ticket replay assumes Sanoma has that many closed, routine tickets with a linked human change. Unmeasured.
   Add to the feasibility note: "count of closed tickets with a linked merged change; if fewer than 30, replay uses all available and the pass share
   is set on that smaller sample, stated as such."
   Evidence: RFP "routine internal analytics requests sit in the backlog for weeks"; "fail on basic edge cases".
3. Slide 3, row "Wrong change passes the tests". A data diff on masked data can hide or invent errors if masking changes join keys or value ranges.
   Add: "masking keeps keys and distributions needed for joins; rules agreed before day 1; diff also run on a dev-schema sample when policy allows."
   Evidence: RFP "autonomously draft merge requests for our engineers to review"; deck "personal data in tickets or samples".

## Missing technical answers
- Agent merge requests colliding with engineers' open changes on the same models (rebase, conflict, who wins): not answered. Optional one line on slide 2: "agent rebases on main; a conflict stops it and goes to the engineer."
- Everything else asked in the RFP: answered.

## Keep
Diagram and "Only a person merges to main"; port check <= 2 h; week 8 stop; "12 h to 30 min" labelled not a promise; no new tools; no AI extras.
