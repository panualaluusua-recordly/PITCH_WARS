<!-- title: Veikkaus · Data and AI Architecture Assessment -->
# An independent, evidence-based assessment of your analytics architecture

## Technical debt, model deployment and target-state patterns, with your existing licences used first. €19,200 fixed. Finnish and Swedish deliverables. No contractual deviations.

Proposal to Matias Lehtoranta, Development Manager, Data & Analytics · Recordly Oy · Helsinki

---

# Organizational background and aims

## What we read in your brief, and what the assessment does about it

| What you told us | What the assessment does |
|---|---|
| State-owned gaming operator: **compliance, governance and high-throughput data** come first | Compliance lens on every finding: access control, audit trail, lineage, player-data handling. **Read-only access; no player-level data leaves your environment.** |
| "**Substantial untapped capacity** across existing multi-year software commitments" | **Licence-utilisation baseline first**: entitlement vs. actual use per commitment. Recommend existing capability before anything new. **No new tools by default.** |
| Cloud data platform + **in-house AI platform** + BI tool + ERP | We assess how they fit together and how models reach production. **No new AI features**; this is an assessment, not a build. |
| Earlier rollout: **sloppy Swedish translations** drew player complaints | Every deliverable in **Finnish and Swedish**; Swedish reviewed by a native speaker before it reaches you. One FI/SV/EN term glossary agreed in week 1. |
| You trust logs and **proof, not promises** | Each finding is a card with **evidence, source, impact and confidence**. No finding without evidence. |

---

# Technical methodology and deliverables

## Four lenses, one rule: every finding carries its evidence

| Cloud data platform | → In-house AI platform | → BI tool | → ERP |
|---|---|---|---|
| D1 map · D2 debt · D4 load and lag | D3: train → approve → deploy → monitor | D1 usage logs | D1 interfaces |

| # | Deliverable (Finnish + Swedish) | How we build it, and the evidence behind it |
|---|---|---|
| **D1** | **Current-state map and licence-utilisation baseline** | Map from configs and metadata; entitlement vs. usage per commitment from admin and usage logs |
| **D2** | **Technical-debt register, ranked** | Pipelines and models ranked by failure rate, manual steps, duplicated logic; counts from task logs |
| **D3** | **Model deployment workflow review** | Lead time to production from deployment history; manual hand-offs, rollback and monitoring checked |
| **D4** | **Target-state patterns (2–3 options)** | Written for the platforms found. Scored on compliance, throughput (peak load, batch/stream lag; streaming only where it pays), cost per tier, effort, licence reuse; **existing capacity first** |
| **D5** | **Roadmap and decision memo** | Effort in days and owners; one page for management. Changes proposed, never applied; each cut-over needs your approval |

> **Finding card (sample brought to the interview):** Finding · Evidence (log extract, count, date) · Impact · Effort · Confidence · Compliance note.

---

# Implementation plan and timeline

## 8 weeks, 20 person-days, about 2 hours a week from your team

| Phase | Weeks | Person-days | Output |
|---|---|---|---|
| **1 · Baseline** | 1–3 | 6 | Read-only access in week 1; D1 draft; licence utilisation measured |
| **2 · Debt and deployment** | 3–5 | 7 | D2 and D3. **Checkpoint, week 4:** target ≥80% of commitments with usage data and ≥10 log-evidenced debt items, confirmed with you after week 1; otherwise re-scope before phase 3 |
| **3 · Target state** | 5–7 | 5 | D4 options scored with your team |
| **4 · Roadmap and read-out** | 7–8 | 2 | D5, native Swedish review, final read-out |

- **Honest unknown:** which platform vendors and licence terms sit behind "cloud data platform" and "in-house AI platform" is not in the brief. A vendor-neutral access checklist in week 1 settles it.
- **Interview (2 hours):** we walk one finding card end to end, the method and the team answer your questions.

---

# Proposed team credentials and availability

| | Lead Data Architect | Senior Data Engineer (MLOps) |
|---|---|---|
| **Required certifications** | Microsoft Certified: Azure Solutions Architect Expert · Databricks Certified Data Engineer Professional · SnowPro Core | Microsoft Certified: Azure Data Engineer Associate · Google Cloud Professional Data Engineer · Databricks Certified Machine Learning Professional |
| **Required languages** | Finnish required, English | Finnish required, Swedish proficiency required, English |
| **Days** | 12 | 8 |
| **Availability** | **Target at signature; evidence pending** | **Target at signature; evidence pending** |

Two people who do the work themselves. Recordly sells no licences and takes no vendor commissions. Any replacement is of equal seniority and agreed with you first.

---

# Detailed pricing and contract deviations

## Fixed total: €19,200 (excl. VAT)

| Role | Person-days | Day rate (8 h) |
|---|---|---|
| Lead Data Architect | 12 | €960 |
| Senior Data Engineer (MLOps) | 8 | €960 |
| **Total** | **20 days** | **20 × €960 = €19,200** |

- **Invoicing:** half at the week-4 checkpoint, half on final acceptance of D5; 21 days net
- **Fixed price:** effort above plan is Recordly's risk. Travel in Helsinki included.
- **Licences:** none. Everything runs on your existing environment.
- **Deliverables** are Veikkaus' property, in Finnish and Swedish

### Contract deviations
**None.** We accept Veikkaus' standard terms as they are.

**Staffing review / Rauno:** role profiles are requirements, not verified people. Confirm CVs, certificates, languages and actual availability before submission. One day = 8 hours; DE minimum EUR 115/h, DA EUR 125/h, AI expertise adds EUR 5/h for the relevant specialist. Architect base EUR 115/h is proposed for owner confirmation, not a user-supplied minimum. At most two architects. Validate fixed scope and risk allowance before commitment.

The two assessment profiles require AI-platform / MLOps expertise: 20 days at EUR 120/h, including the EUR 5/h premium. This adds no new AI feature to the scope.
