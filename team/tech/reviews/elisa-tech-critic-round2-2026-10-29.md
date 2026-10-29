# Tech-critic round 2: elisa v6 (2026-10-29)
Tech lens only. No price, terms, names or style. Read-only; no game API calls.
Checked: team/decks/elisa/elisa-data-platform-architecture-and-tool-selection-as-v6.md against the RFP and bio in work/buyers_now.json and the round-1 review.

## Verdict: strong (lower end)
All three round-1 top fixes landed. The P10 trap is answered honestly, the stack is the buyer's (BigQuery, Composer, Looker, Power BI),
the latency proof now sits at Gate 1 with a sandbox and a fallback, and the unknowns table has settle-by steps.
The remaining gaps are about what "real-time" means in the serving layer and how scope is chosen.

## Round-1 fixes: landed?
1. Real latency test at Gate 1 (Pub/Sub to BigQuery to Looker, sandbox): YES. Slide 4, Gate 1 row. Checkpoint B keeps a second per-tier test.
2. Write-enabled sandbox in "Access ready" plus day-3 fallback ("not tested", streaming stays a proposal): YES. Slide 4, Access row and unknowns table.
3. ERP fallback tier (API polling, measured delay vs stated need): YES. Slide 3 tier box and slide 4 ERP row.

Round-1 smaller notes:
- BI tool per tier: PARTLY. Slide 3 says "Power BI: mode assessed per tier" but never says DirectQuery cannot give seconds.
- IAM and policy-tag test in Looker and Power BI: NO. Still only a line on slide 3. Final row has no existing-Composer-pipelines item.
- Phase B pass condition: PARTLY. Checkpoint B names latency against the Gate 1 range; failure mode and cost are in the option scoring.
- How the 3-5 domains are picked: NO.

## Top 3 new tech fixes
1. Slide 3 (serving box) and slide 4 (Power BI unknown row): the serving layer can quietly break "no delayed refreshes".
   - Evidence: RFP "real-time access to all data is required, with no batch processing or delayed refreshes".
   - Looker on BigQuery serves cached results by default, and Power BI import is scheduled. Either can add minutes or hours after a seconds-fast load. The latency test must end at the screen, not at the table.
   - Change, serving box: "Looker live path: cache policy set per tier. Power BI import serves daily and micro-batch tiers only; DirectQuery on BigQuery is not a seconds path".
   - Change, Gate 1 cell: "latency measured from event to a Looker tile with the cache setting stated".
2. Slide 4 (Gate 1 and Checkpoint B rows): "real-time" has no numeric definition and there is no rule for a failed test.
   - Evidence: RFP "real-time access to all data"; the deck says "target ranges agreed at Gate 1" but not how freshness is measured.
   - Change, Gate 1: "freshness defined as event time to visible in Looker, reported as median and 95th percentile, per tier". Add to the Checkpoint B row: "if the measured 95th percentile misses the Gate 1 range, the tier is re-scoped or Option C is costed for that domain, and the miss is shown to the committee".
3. Slide 4 (Gate 1 and Final rows): scope selection and access consistency are untested.
   - Evidence: RFP "all data" against the deck's "3-5 priority domains"; the buyer stresses safe operations.
   - Change, Gate 1: "3-5 domains chosen with you by sprint day 2, with the rest listed as out of scope".
   - Change, Checkpoint B: "same IAM and policy-tag behaviour tested in Looker and Power BI on the tested domain".
   - Change, Final: "plan for existing Composer pipelines: keep, change or retire, per DAG group".

## Missing technical answers
- Latency end point at the BI screen (Looker cache, Power BI mode): fix 1.
- Numeric definition of freshness and a failure rule: fix 2.
- Domain selection and tested access parity: fix 3.

## Not a gap (do not change)
- No new vendor added (Pub/Sub is labelled "proposed"; no ERP named; no dbt, Datastream or AI).
- Option C is scored with cost, not refused.
