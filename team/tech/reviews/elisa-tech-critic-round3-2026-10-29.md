# Tech-critic round 3: elisa v7 (2026-10-29)
Tech lens only. No price, terms, names or style. Read-only; no game API calls.
Checked: team/decks/elisa/elisa-data-platform-architecture-and-tool-selection-as-v7.md against the RFP and bio in work/buyers_now.json and the round-2 review.

## Verdict: strong
The stack is the buyer's (BigQuery, Composer, Looker, Power BI). P10 is answered honestly, with the test ending at the Looker tile.
Gates, the day-3 fallback and the unknowns table are in place. The remaining gaps are about operating the streaming tier safely and about Gate 1 load.

## Round-2 fixes landed?
1. Serving box: Looker cache policy per tier, Power BI import for slow tiers only, DirectQuery not a seconds path: YES (slide 3, slide 4 unknowns row).
2. Freshness as event time to visible in Looker, median and p95, with a miss rule at Checkpoint B: YES (slide 4).
3. Domains chosen by sprint day 2, rest out of scope: YES. IAM and policy-tag parity test at Checkpoint B: YES. Composer keep/change/retire per DAG group in Final: YES.
All round-2 items landed. No new vendor was added; Pub/Sub is still labelled "proposed".

## Top 3 new tech fixes
1. Slide 4 (Checkpoint B row): the streaming tier is tested for speed only, not for correctness.
   - Evidence: bio "safe operational excellence that keeps ... risk strictly minimized"; RFP "real-time access to all data".
   - Pub/Sub delivers at-least-once, so duplicates, late events and schema drift can corrupt marts while latency looks fine.
   - Add to Checkpoint B: "tier test also replays duplicate and late events and one schema change; marts must stay correct, and the daily reconciled figure must match the streamed figure within a stated tolerance".
2. Slide 4 (Final row) and slide 5 (phase C output): the roadmap has no safe-cutover rule and no freshness monitoring.
   - Evidence: bio "safe operational excellence"; RFP "no batch processing or delayed refreshes permitted across our target architecture".
   - A target that promises freshness needs an alarm when it is missed, and every step needs a way back.
   - Add to Final: "each roadmap step has a parallel run, a rollback step, and a freshness alert on the Gate 1 range (p95) using Composer and BigQuery logs".
3. Slide 4 (Gate 1 row) and slide 5 (phase 0, 4 days): Gate 1 carries too much for a 4-day sprint.
   - Evidence: RFP "stalled after broad project milestones were locked in before ... a small preliminary scoping exercise".
   - Gate 1 holds access, 3-5 domains, a measured baseline, a live feed test and an ERP check. If it slips, the deck repeats the failure the buyer named.
   - Add to the unknowns table: "If sandbox access arrives after day 3, Gate 1 closes on baseline, domains and ERP only; the live latency test moves to Checkpoint B and is shown as 'not tested' at Gate 1".

## Missing technical answers
- Streaming correctness (duplicates, late data, schema change) and tier-to-reconciled consistency: fix 1.
- Cutover, rollback and freshness alerting for the target architecture: fix 2.
- What Gate 1 contains when the sandbox is late: fix 3. Part of this exists in the day-3 row; the fix makes the Gate 1 consequence explicit.

## Minor, optional
- The Gate 1 latency test ends in Looker only. Say "Power BI import refresh interval measured on one report" so the second BI path has a measured number.
- Retention of traffic data is named as a risk on slide 3 but has no test. Add "retention and deletion rule per tier checked against Elisa policy" to Checkpoint B.

## Not a gap (do not change)
- Option C is scored with cost, not refused.
- No AI or ML scope; no ERP vendor named.
