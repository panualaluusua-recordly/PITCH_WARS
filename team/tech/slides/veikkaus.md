# Tech & architecture slides for the Veikkaus deck
_Veikkaus Oy: Two slides for deck-writer: slide 1 is the 'Technical methodology and deliverables' section, slide 2 merges into 'Implementation plan and timeline'_

## 2. We read evidence at every layer of your stack, labelled the way your brief labels it
- **Licence baseline first:** entitlement vs. actual use per multi-year commitment, from the admin and usage logs you have. A new component is proposed only where existing capacity fails a tested need.
- **Proof, not promises:** every finding is a card with log evidence and a compliance note, or is marked "confidence low, evidence requested". Options are scored on five weighted criteria from your brief; compliance is also a pass/fail gate.
- **Model deployment is measured, not rebuilt:** lead time and manual hand-offs per step on your in-house AI platform. Vendor-neutral: products are confirmed in week 1.
[Sources: Operational source systems, ERP system (feeds and receives)] → [Cloud data platform: Consolidated operational metrics, Player reporting pipelines, D2 debt: failures, manual steps, duplicate logic, lineage gaps, D1 / D4: volumes, job durations, peak load] → [In-house AI platform: Train → register → approve → deploy → monitor, D3: lead time and hand-offs per step; rollback and monitoring checked] → [Consumers: BI tool: D1 usage logs, ERP-facing outputs]
(Scope map in your brief's own labels, not your confirmed architecture. Every finding: access control, audit trail, lineage, player-data handling.)

## 3. Three gates keep the assessment honest: access, evidence quality, compliance
| Gate | When | Pass criterion |
| --- | --- | --- |
| Access and data handling | Week 1 | Named read-only accounts issued by Veikkaus, access list and NDA signed; metadata and counts only. If approval is late, your admins export the logs and the plan moves by the delay |
| Evidence quality | Week 4 checkpoint | Target: ≥80% of commitments have usage data and ≥10 debt items are log-evidenced, confirmed with you after week 1. Scoring anchors agreed. Otherwise re-scope before phase 3 |
| Compliance | Option scoring, weeks 5–7 | An option that fails on access control, audit trail, lineage or player-data handling is not recommended, whatever its score |
| Roadmap | Week 8 | Changes are proposed, never applied; every cut-over step has an owner and your approval |

_Technical unknowns: the products and licence terms behind "cloud data platform" and "in-house AI platform" (week-1 checklist); whether usage logs can be exported (gaps shown on the D1 cards); deployment history shorter than 6 months (lead time shown as a range); current volumes (throughput scored against measured load, no real-time promise)._

---

## Rationale (solution-architect, 2026-10-29)

- **Stack:** only the RFP's own labels ("cloud data platform", "in-house AI platform", "BI tool", "ERP system", "public cloud"). No vendor or product is named, because none is stated; products are confirmed in week 1 (P3). Answers tech-critic veikkaus v1 #1 and #4.
- **Patterns applied:** P7 (licence baseline first, "substantial untapped capacity"), P13 (finding cards with log evidence, week-4 evidence gate, "tangible proof over vendor promises"), P15 (lineage gaps in D2), P5 (named read-only accounts, access control checked per finding), P4 (week-1 access gate before any analysis), P10 only as a measured throughput baseline (no streaming or real-time promise), P6 not used as a build: D3 measures the deployment flow, it does not template or replace it.
- **Gate numbers:** ≥80% / ≥10 are targets confirmed with the buyer after week 1 (anti-pattern: hard metrics fixed before measurement).
- **Compliance:** mechanism from work/compliance/veikkaus.md (named read-only accounts, metadata and counts only, notes deleted at close; AI Act lens on the in-house models: inventory, risk class, human oversight; we assess, we do not certify). No gaming-law expertise claimed.
- **Assessment method:** options A/B/C and the five weights from work/assessment/veikkaus.md, quoted in D4.
- **Deck fit:** in the v4 deck (built on committed v3, 2c89941), slide 1 becomes the "Technical methodology and deliverables" section (diagram above the D1–D5 table), slide 2 is merged into the "Implementation plan and timeline" phase table and its unknowns. Cover + 5 is kept.
- **Effort basis (not a price):** the deck keeps 20 person-days (6 / 7 / 5 / 2). The assessment designer's basis is 18 (5 / 6 / 5 / 2); the shrink path is option C as a paper sketch (−1) and workshop 2 merged into the read-out (−1). Price owner decides.
- **Left out on purpose:** any build or migration, new AI features or platform, vendor/tool bake-off, streaming design, player-level data access, BI/ERP beyond their interfaces to the platform, VDE (not Snowflake + dbt).
