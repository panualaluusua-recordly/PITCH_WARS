Buyer: veikkaus | Decision to enable: which target-state pattern to adopt, and in what order, so debt is cleared and models reach production faster using capacity already paid for ← "identify technical debt, streamline model deployment workflows, and recommend target-state architectural patterns"

Method: inputs | criteria (weight) | options compared | evidence log
- Inputs (read-only, no player-level data leaves Veikkaus): (1) multi-year software commitment documents (entitlements, term, renewal dates); (2) admin and usage logs per commitment; (3) pipeline, job and model inventory from platform metadata and task logs; (4) deployment history of the in-house AI platform (trained model to production); (5) two 60-min walk-throughs (data platform, AI platform) and one with the BI/ERP owner; (6) up to 4 interviews of 30 min with the people who run and deploy. Matias "monitors task logs obsessively" (bio), so logs are primary evidence and interviews only explain them.
- Criteria and weights, each tied to the RFP:

| Criterion | Weight | RFP words | Why this weight | Measured by |
|---|---|---|---|---|
| Compliance and governance fit | 25 | "robust compliance, reliable governance" | State-owned gaming operator; a failing option is unusable | Access control, audit trail, lineage, player-data handling checked per option (pass/gap/fail) |
| Reuse of existing capacity | 25 | "substantial untapped capacity across our existing multi-year software commitments" | Internal reviews already point here; the cheapest option is the one already owned | Entitlement vs. actual use per commitment; share of option covered by existing entitlement |
| Model deployment improvement | 20 | "streamline model deployment workflows" | Second named task | Median lead time trained model to production from history; count of manual hand-offs |
| Throughput and reliability | 20 | "high-throughput data processing" | Paramount in RFP, but the platform was recently consolidated, so debt matters more than raw speed | Job failure rate, late runs, peak-load headroom from logs |
| Effort and migration risk | 10 | "modernize the technical landscape" | Tie-breaker, reported in days | Days per roadmap step, dependencies |

  Scale 0-4 per criterion with written anchors for 0, 2 and 4, agreed at the week-4 checkpoint before any option is scored. Compliance is also a gate: an option with a "fail" cannot be recommended whatever its score.
- Options compared: A "Keep and repair" (current architecture, debt register cleared); B "Reuse first" (consolidate onto existing entitlements, standard promotion pipeline in the in-house AI platform); C "Re-platform pattern" (a new component only where a tested need cannot be met by existing capacity). No vendor selection beyond tools already in the RFP landscape.
- Evidence log: one finding card per finding in a single register (Excel file in Veikkaus's own storage): ID, finding, evidence (log extract, count, date), source system, impact, effort in days, confidence high/medium/low, compliance note, FI and SV text. No card without evidence; unevidenced items go to an "unverified" tab, not into the roadmap. Each score in the option matrix links to card IDs. A sample card is brought to the 2-hour interview.

Plan: <week: activity, who from the buyer, output>
- Wk 1: scoping and access. 60-min kickoff, access checklist, FI/SV/EN glossary. Buyer: Matias plus one admin owner (~2 h). Output: access confirmed, glossary v1, evidence register skeleton. Existing licences and read-only accounts, no new tools.
- Wk 2-3: baseline. Admin and usage logs, commitment documents, platform walk-through (60 min). Buyer: platform admin (~2 h/wk). Output: D1 draft.
- Wk 3-5: debt and deployment. Job/model inventory scan, deployment history analysis, AI-platform walk-through, 2-3 team interviews. Buyer: engineers on call (~2 h/wk). Output: D2, D3. Wk 4 checkpoint (60 min): evidence quality and scoring anchors agreed; if logs are thin, scope is agreed there.
- Wk 5-7: options. Workshop 1 (90 min, Finnish): score A/B/C live against the anchors with Matias's team. Output: scored option matrix (D4).
- Wk 7-8: roadmap, native Swedish review of all deliverables against the glossary, workshop 2 (60 min) on roadmap and owners. Output: D5 in Finnish and Swedish.
- Readout wk 8 (60 min), Finnish, Swedish documents.

Deliverables:
- D1 Current-state map and licence-utilisation baseline (commitment, entitlement, used, gap)
- D2 Technical-debt register, ranked, every item with a finding card
- D3 Model deployment review: measured lead time, hand-off list, 3 fixes ranked
- D4 Scored option matrix (A/B/C, five criteria, weights, evidence IDs) and target-state diagram of the recommended option
- D5 12-month roadmap with owners, go/stop gates per step, one-page decision memo
- Evidence register (Excel) and FI/SV/EN glossary; all documents in Finnish and Swedish
- Day 30 (end of wk 4): D1 final, D2 and D3 drafts with finding cards, week-4 checkpoint held, scoring anchors signed off, first ranked list of the best-evidenced debt items.

Effort basis: 18 person-days (not a price): scoping and baseline 5, debt and deployment 6, options 5, roadmap, Swedish review and readout 2. Shrink path: option C as a paper sketch only (-1), merge workshop 2 into the readout (-1).

Unknowns and access needed:
- Read-only access to admin/usage logs of each commitment by wk 1; without it D1 rests on interviews, confidence drops to low and the checkpoint says so.
- Which vendors and licence terms sit behind "cloud data platform" and "in-house AI platform" (not in RFP): access checklist, wk 1.
- Commitment documents (entitlements, renewal dates) by wk 2; without them reuse is estimated from usage only and not scored on cost.
- Deployment history, at least 6 months, by wk 3; if shorter, lead time is shown as a range.
- Security approval for read-only accounts by wk 1; a delay shifts everything one week.
- Native Swedish reviewer confirmed on the roster before sending (Ville's verify item).

Left out on purpose:
- Any build, migration or implementation phase
- New AI features or a new AI platform (we assess the in-house one)
- Vendor selection or tool bake-off; option C names patterns, not products
- Player-level data access
- Assessing BI/ERP beyond how they connect to the platform

--- Ready slide text (technical methodology) ---

Title: Five criteria, weighted from your own brief

| Criterion | Weight | From your brief | Evidence |
|---|---|---|---|
| Compliance and governance fit (also a gate) | 25 | "robust compliance, reliable governance" | Access, audit trail, lineage checked per option |
| Reuse of existing capacity | 25 | "substantial untapped capacity across our existing multi-year software commitments" | Entitlement vs. actual use from admin logs |
| Model deployment improvement | 20 | "streamline model deployment workflows" | Lead time and manual hand-offs from deployment history |
| Throughput and reliability | 20 | "high-throughput data processing" | Failure rate and headroom from task logs |
| Effort and migration risk | 10 | "modernize the technical landscape" | Days per roadmap step |

Options scored: A Keep and repair, B Reuse first, C Re-platform pattern. Anchors for 0, 2, 4 are agreed at the week-4 checkpoint, before scoring. Every score links to a finding card (evidence, source, impact, confidence).

Title: What you hold on day 30
- Utilisation baseline per commitment (D1, final)
- Debt register and deployment review (D2, D3) with finding cards
- Scoring anchors signed off by you
- After week 8: scored option matrix, target-state diagram, 12-month roadmap with owners and gates, one-page decision memo, all in Finnish and Swedish
