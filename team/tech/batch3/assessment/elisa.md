Buyer: elisa | Decision to enable: which architecture and tools to commit to, with a freshness level per data domain, and whether the steering committee locks the full programme after a short scoping step ← "real-time access to all data is required, with no batch processing or delayed refreshes permitted across our target architecture"

Method: inputs | criteria (weight) | options compared | evidence log
- Inputs (existing licences, no new tools): (1) inventory of data domains and sources from the BigQuery and Cloud Composer environment (read-only): datasets, DAGs, schedules, last-run times; (2) Looker and Power BI usage and refresh settings; (3) ERP interface documentation and change-capture options; (4) freshness need per domain, from an async questionnaire in the chat tool plus one 30-min conversation per domain owner where answers are unclear; (5) measured current freshness (source change to dashboard) for 3-5 priority domains from Composer and BigQuery logs.
- Criteria and weights, each tied to the RFP:

| Criterion | Weight | RFP words | Why |
|---|---|---|---|
| Data freshness per domain, tested | 30 | "real-time access to all data is required, with no batch processing or delayed refreshes" | Her hard requirement; scored per domain, not one yes/no, and we show where "real-time" is impossible or not worth it |
| Fit with existing stack and reuse | 20 | "Google Cloud, BigQuery with Cloud Composer, Looker and Power BI, alongside an ERP system" | Existing footprint; new components only if a tested need fails |
| Operational risk and reliability | 20 | bio: "safe operational excellence that keeps steering committees satisfied and risk strictly minimized" | Steering-committee test |
| Build and run cost direction | 15 | "tool selection assessment" | Streaming everything raises run cost and failure surface |
| Load on her engineers | 15 | "a small preliminary scoping exercise" (past failure); bio: engineers' calendars consumed by working sessions | Team time is a criterion, not a side effect |

- Freshness tiers used for scoring: streaming (seconds), change capture (minutes), micro-batch (5-15 min), daily batch. Each domain gets the slowest tier that still meets its tested need. Against the RFP's "no batch" we answer "yes if": any domain that truly needs seconds gets streaming; we show cost and risk of applying it to all data and the committee decides.
- Options compared: A Current stack, tuned (shorter Composer schedules, Looker on live BigQuery). B Tiered freshness on the current stack (streaming, CDC for ERP where supported, micro-batch, daily for finance). C "All real-time" as written in the RFP, scored as stated so its cost and risk are visible. Tool choices only in the layers around the existing stack (streaming, ELT, BI).
- Evidence log: a requirements and evidence matrix, one row per domain: owner, stated need, measured current freshness, proposed tier, test result (pass / fail / not tested), source. Gate decisions logged as one line each with date and decider. Every score in the option matrix cites matrix rows. Untested items are marked "not tested", never "yes".

Plan: <week: activity, who from the buyer, output>
- Wk 1-2: scoping sprint (the "small preliminary scoping exercise" in the RFP). Read-only access, async questionnaire to domain owners, one 60-min session with platform leads, ERP change-capture check, freshness measured on 3-5 domains. Buyer: Kirsi names owners; platform leads attend one session. Output: current-state sketch, freshness need per domain, proposed milestones.
- Gate 1, end of wk 2: steering committee, one-page summary: go, adjust or stop. Milestones are locked only after this.
- Wk 3-5, Phase A: requirements by domain, baseline architecture, tiered freshness map. Written questions in the chat tool, no sessions.
- Wk 5-8, Phase B: options A/B/C scored; one 60-min session with platform leads to challenge scores; tier tests on 1-2 domains with existing services. Output: scored matrix, recommended tool choices.
- Wk 8-10, Phase C: target architecture, roadmap, risks; third 60-min session (readout to platform leads); one-page steering summary. At most three 60-min sessions in total.

Deliverables:
- Scoping sprint note with proposed milestones (for Gate 1)
- Requirements and freshness matrix, one row per domain, with test results
- Scored option matrix A/B/C with weights and evidence references
- Target-state architecture diagram with freshness tier per domain
- Tool selection recommendation (streaming, ELT, BI layers only) with reasons
- Roadmap with owners and a go/stop gate per step
- Risk and assumption list and one-page steering summary
- Day 30 (end of wk 4): Gate 1 outcome, sprint note, requirements matrix for priority domains, measured freshness, first tier proposals, approved milestones for A to C.

Effort basis: 18 person-days (not a price): sprint 3, A 5, B 6, C 4. Shrink path: tier tests on one domain instead of two (-1), cap at the 8 highest-value domains (-1).

Unknowns and access needed:
- ERP vendor and its change-capture options: answered in the sprint (wk 2). If only batch extracts exist, that domain stays micro-batch or daily and we say so at Gate 1.
- Real freshness need per domain: needs the domain owners' answers by wk 2; without them the requirement stays as stated and option C's cost is shown on assumed volumes.
- Read-only access to BigQuery, Composer and Looker metadata by wk 1; without it freshness is estimated, not measured.
- Steering committee date for Gate 1 in wk 2; if later, later phases start later and nothing is pre-committed.
- Looker and Power BI refresh settings by wk 2 (which one serves what is unknown).

Left out on purpose:
- Any build, pipeline implementation or migration
- AI/ML use cases
- New platform proposals unless an existing service fails a tested need
- Vendor comparison beyond the layers around BigQuery, Composer, Looker, Power BI
- ERP replacement or change
- Working sessions beyond three 60-min sessions

--- Ready slide text ---

Title: How we score: five criteria from your brief, one test per domain

| Criterion | Weight | From your brief | Evidence |
|---|---|---|---|
| Freshness per domain, tested | 30 | "real-time access to all data is required" | Measured current freshness, tier test result |
| Fit with existing stack | 20 | "BigQuery with Cloud Composer, Looker and Power BI, alongside an ERP system" | Reuse of existing services; new only after a failed test |
| Operational risk | 20 | steering-committee risk test | Failure modes, rollback, support load |
| Build and run cost direction | 15 | "tool selection assessment" | Days and run-cost direction per option |
| Load on your engineers | 15 | "a small preliminary scoping exercise" | Hours asked of your team; max 3 sessions of 60 min |

Options scored: A current stack tuned, B tiered freshness on current stack, C all real-time as written. Each domain gets the slowest tier that still meets its tested need: streaming, change capture, micro-batch or daily batch. Untested items are marked "not tested" in the requirements matrix.

Title: What you receive
- Sprint note and proposed milestones (Gate 1, end of week 2)
- Requirements and freshness matrix per domain, with test results
- Scored option matrix with evidence references
- Target-state architecture with tier per domain
- Roadmap with owners and gates; one-page steering summary
- Day 30: Gate 1 outcome, measured freshness for priority domains, first tier proposals, approved milestones
