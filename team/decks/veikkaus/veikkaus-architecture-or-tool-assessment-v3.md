<!-- title: Veikkaus · Data and AI Architecture Assessment -->
# An independent, evidence-based assessment of your analytics architecture

## Technical debt, model deployment and target-state patterns, with your existing licences used first. €19,200 fixed. Finnish and Swedish deliverables. No contractual deviations.

Proposal to Matias Lehtoranta, Development Manager, Data & Analytics · Recordly Oy · Helsinki

---

# Organizational background and aims

## What we read in your brief, and what the assessment does about it

| What you told us | What the assessment does |
|---|---|
| State-owned gaming operator: **compliance, governance and high-throughput data** come first | Compliance lens on every finding: access control, audit trail, lineage, player-data handling. **Named read-only accounts issued by Veikkaus; we work with metadata and counts, no player-level data leaves your environment;** working notes deleted at close. |
| "**Substantial untapped capacity** across existing multi-year software commitments" | **Licence-utilisation baseline first**: entitlement vs. actual use per commitment. Recommend existing capability before anything new. **No new tools by default.** |
| Cloud data platform + **in-house AI platform** + BI tool + ERP | We assess how they fit together and how models reach production. **No new AI features**; this is an assessment, not a build. |
| Earlier rollout: **sloppy Swedish translations** drew player complaints | Every deliverable in **Finnish and Swedish**; Swedish reviewed by a native speaker before it reaches you. One FI/SV/EN term glossary agreed in week 1. |
| You trust logs and **proof, not promises** | Each finding is a card with **evidence, source, impact and confidence**. No finding without evidence; where logs are missing, the card says "evidence requested". |

---

# Technical methodology and deliverables

## We read evidence at every layer of your stack, in your brief's own labels. Vendor-neutral: products confirmed in week 1.

<div style="display:flex;align-items:stretch;gap:12px;margin:0.1em 0 0.4em 0;font-size:0.6em;line-height:1.25"><div style="flex:1;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:12px"><b style="color:#E3FF87">SOURCES</b><br>Operational source systems · ERP system (feeds and receives)</div><div style="align-self:center;color:#E3FF87;font-size:2em">&rarr;</div><div style="flex:1.3;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:12px"><b style="color:#E3FF87">CLOUD DATA PLATFORM</b><br>Operational metrics, player reporting pipelines<br><b>D2</b> debt · <b>D1/D4</b> volumes, job durations, peak load</div><div style="align-self:center;color:#E3FF87;font-size:2em">&rarr;</div><div style="flex:1.3;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:12px"><b style="color:#E3FF87">IN-HOUSE AI PLATFORM</b><br>Train → register → approve → deploy → monitor<br><b>D3</b> lead time and hand-offs per step</div><div style="align-self:center;color:#E3FF87;font-size:2em">&rarr;</div><div style="flex:1;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:12px"><b style="color:#E3FF87">BI TOOL · ERP</b><br><b>D1</b> usage logs, interfaces</div></div>
<div style="background:#2A2A2A;border:2px dashed #E3FF87;border-radius:10px;padding:8px 14px;font-size:0.6em;margin-bottom:0.5em"><b style="color:#E3FF87">EVERY LAYER:</b> D1 entitlement vs. use per commitment · access control, audit trail, lineage, player-data handling checked per finding · a scope map, not your confirmed architecture</div>

| # | Deliverable (Finnish + Swedish) | Evidence and checks |
|---|---|---|
| **D1** | **Current-state map, licence-utilisation baseline** | Entitlement vs. use, volumes, job durations, from the admin and task logs you have; gaps listed in week 1 |
| **D2** | **Technical-debt register, ranked** | Failure rate, manual steps, duplicated logic, lineage gaps; counts from task logs |
| **D3** | **Model deployment review** | Lead time per step, manual hand-offs, rollback, monitoring; AI Act lens: model inventory, risk class, human oversight (we assess, not certify) |
| **D4** | **Target-state options, scored** | A keep and repair · B reuse first · C re-platform pattern. Weights: compliance 25 (also pass/fail), existing capacity 25, deployment 20, throughput 20, effort 10 |
| **D5** | **Roadmap and decision memo** | Owners, days, a go/stop gate per step; changes proposed, never applied |

---

# Implementation plan and timeline

## 8 weeks, 20 person-days, about 2 hours a week from your team

| Phase | Weeks | Person-days | Output and gate |
|---|---|---|---|
| **1 · Baseline** | 1–3 | 6 | **Gate, week 1:** named read-only accounts, access list and NDA signed. If approval is late, your admins export the logs and the plan moves by the delay. D1 draft |
| **2 · Debt and deployment** | 3–5 | 7 | D2 and D3. **Checkpoint, week 4:** target ≥80% of commitments with usage data and ≥10 log-evidenced debt items, confirmed with you after week 1; scoring anchors agreed. Otherwise re-scope before phase 3 |
| **3 · Target state** | 5–7 | 5 | D4 scored with your team. **Compliance gate:** an option that fails is not recommended, whatever its score |
| **4 · Roadmap and read-out** | 7–8 | 2 | D5, native Swedish review, final read-out |

- **Honest unknowns:** the products and licence terms behind "cloud data platform" and "in-house AI platform" (week-1 checklist); whether usage logs can be exported (gaps shown on D1 cards); under 6 months of deployment history means lead time is shown as a range; throughput is scored against measured load, with no real-time promise.
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
