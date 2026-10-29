<!-- title: Kemira · First 100 Days Data & AI Roadmap -->
# Kemira's first 100 days in data and AI

## A prioritised, costed roadmap on SAP S/4HANA, Datasphere, SAC and Azure, with first value delivered inside the 100 days

Proposal to Rasmus Vuorinen, Director of Digital Analytics · Recordly Oy · Helsinki

---

# The proposal in one page

| | |
|---|---|
| **Outcome** | A 100-day plan the Digital Analytics team can execute: 3–5 prioritised AI and data use cases with business cases, the platform moves they need on SAP and Azure, and a team capability plan |
| **Quick win** | One use case taken to a working proof of value on real Kemira data **by day 60**, so the roadmap starts with evidence |
| **Approach** | Four phases over 12 weeks, built on what Kemira already runs. No new platform, no new licences. |
| **Team** | Two senior people doing the work themselves, available from contract signature, plus an SAP architect on call |
| **Price** | **€16,500 fixed total** |
| **Contract** | No contractual deviations |

> Designed to cost your team **as little time as possible**: about 2 hours a week from you, a few targeted interviews, and no recurring status meetings. Written updates instead.

---

# What we understand

:::cols
### Background
- Kemira serves **water treatment and process industry customers globally**; operational efficiency, chemical dosing, supply reliability and sustainability reporting drive value
- The data foundation is in place: **SAP S/4HANA** for operations, **SAP Datasphere** for the semantic layer, **SAP Analytics Cloud** for reporting, **Microsoft Azure** for advanced analytics and AI
- The Digital Analytics team needs a **clear first 100 days**: where to focus, what to stop, and what to show leadership early
:::col
### Your aims
- **Immediate, high-impact milestones**, not a long strategy document
- **AI use cases that are prioritised by value and feasibility** on the existing SAP + Azure stack
- **Defined team capabilities**: what to build internally, what to buy, what to source
- A roadmap the team can run **without heroics or overtime**
:::

---

# Approach: four phases, twelve weeks

| Phase | Weeks | What happens | Deliverable |
|---|---|---|---|
| **1 · Baseline** | 1–2 | Review existing SAP, Datasphere, SAC and Azure setup and backlog; 8–10 focused interviews (45 min each) | Current-state snapshot (5 pages) |
| **2 · Use case sprint** | 3–5 | Long-list of 20–30 opportunities across supply chain, production and commercial analytics; scored on value, data readiness and effort | Ranked use-case portfolio with business cases for the top 5 |
| **3 · Proof of value** | 5–9 | Top use case built on real data in Azure, using Datasphere as the governed source | Working proof of value with measured results, **by day 60** |
| **4 · 100-day roadmap** | 9–12 | Sequenced plan, platform enablers, team capability and sourcing plan, KPIs | Roadmap, capability plan, leadership presentation |

---

# Data governance built into the roadmap, not left vague

| Area | What the roadmap fixes, concretely |
|---|---|
| **Ownership** | A named business owner and data steward for every dataset the prioritised use cases depend on (S/4HANA material, plant, batch, customer) |
| **Single governed source** | SAP Datasphere is the governed layer; Azure AI work reads only from certified Datasphere views, so there are no shadow copies |
| **Data quality rules** | Measurable rules per critical field (completeness, validity, timeliness), automated checks and a visible quality score in SAC |
| **Downstream access control** | Access to every SAC story, Datasphere space and Azure output is **role-based and inherited from SAP authorisations**: row-level security by plant, region and business unit; no direct table access for consumers; sensitive data classified and masked before any AI use; **quarterly access reviews** signed off by data owners; every access logged |
| **Definitions** | One business glossary for KPIs (e.g. dosing per m³, OTIF, yield) shared across SAC and Azure |
| **Decision rights** | A light data council: monthly, 45 minutes, decisions logged, owned by Digital Analytics |

Each governance item is tied to a use case, so governance work always serves a result.

---

# How it works on real data, not slides

## Example: proof of value for chemical dosing optimisation (if it ranks first)

| Step | Week | What we actually do with your data |
|---|---|---|
| **1 · Pull** | 5 | Read dosing set-points, flow, turbidity and lab results for one plant from Datasphere into Azure (no new tools, governed source) |
| **2 · Face the mess** | 5–6 | Profile gaps, sensor drift, unit mismatches and manual lab entries. Every issue logged with its row count, and **shown to your team, not hidden** |
| **3 · Baseline** | 6 | Measure today's dosing per m³ against water-quality outcomes, and agree the baseline with plant staff |
| **4 · Model** | 7–8 | Simple, explainable model first (regression or gradient boosting) recommending dosing within safe limits |
| **5 · Prove** | 9 | Back-test on 6–12 months of history: chemical saved per m³ at equal quality, and where the model fails |
| **6 · Decide** | 9 | Go/no-go on scaling, with numbers on the table and code in your repo |

> Each week you get a short written note with real charts from your data. If the data can't support the use case, you hear it in week 6, not in month 6.

---

# Key deliverables

| # | Deliverable | Format |
|---|---|---|
| D1 | Current-state snapshot of data, platform and team | 5-page document |
| D2 | Scored use-case portfolio with business cases for the top 5 | Workbook + 10-page summary |
| D3 | Working proof of value for the top use case on real data | Code in Kemira's Azure repo + results memo |
| D4 | Target architecture moves on SAP Datasphere, SAC and Azure (only what the use cases need) | Architecture note |
| D5 | Team capability and sourcing plan: roles, skills, build/buy/partner | Plan + role descriptions |
| D6 | 100-day roadmap with milestones, owners, KPIs and budget | Roadmap + leadership presentation |

All deliverables are Kemira's property. Everything is built so your team can continue without us.

---

# Team: small, senior, available on signature

:::cols3
### Engagement lead · Data & AI strategy
- 15 years in analytics leadership and process manufacturing
- Has run several data and AI roadmaps for Nordic industrials
- Finnish, English
- **Available: 40% from signature**
:::col
### Lead SAP data architect
- 12 years with SAP BW, Datasphere and SAC; S/4HANA data models
- **SAP Certified: Datasphere**, **SAP Analytics Cloud**
- Finnish, English
- **On call for architecture reviews (included)**
:::col
### Senior AI / ML engineer
- 9 years in ML for manufacturing and supply chain on Azure
- **Microsoft Certified: Azure AI Engineer Associate**, **Azure Data Scientist Associate**
- Finnish, English
- **Available: 80% weeks 3–10**
:::

CVs and certificate IDs are available for verification. Any replacement must be of equal seniority and is agreed with Kemira first.

---

# Financials

## Fixed total price: €16,500 (VAT 0%)

| Phase | Share of the fixed total |
|---|---|
| 1 · Baseline | 15% |
| 2 · Use case sprint | 25% |
| 3 · Proof of value | 40% |
| 4 · 100-day roadmap | 20% |

- **Payment:** invoiced per phase on acceptance; 21 days net
- **Fixed price:** effort above plan is Recordly's risk
- **No licences:** uses Kemira's existing SAP and Azure environments
- Travel within Finland included

### Contractual deviations
**None.** We accept Kemira's standard terms. All deliverables and code are Kemira's property.

---

<!-- statement -->
# A 100-day plan with a working result inside it.

## Fixed price. Senior people who do the work. Starting on signature.

Recordly Oy · Helsinki · Data and AI consultancy
