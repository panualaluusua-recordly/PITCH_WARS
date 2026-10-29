<!-- title: UPM · Forward-Deployed AI Engineer -->
# A forward-deployed AI engineer, backed by a Virtual Data Engineer

## Production-grade ML pipelines on Snowflake + dbt and Databricks, feeding SAP S/4HANA. Six months, fixed monthly fee, UPM's standard terms with no deviations.

Draft proposal to Tapio Rantala, VP Enterprise Data & Analytics · Recordly Oy · Helsinki

---

# The proposal in one page

| | |
|---|---|
| **Outcome** | 3–4 ML use cases taken from notebook to monitored production pipelines, with predictions written back to SAP S/4HANA |
| **People** | **Proposed forward-deployed ML engineer**, embedded in your Helsinki team **3 days a week** targeting 1 Dec 2026, subject to confirmation, plus **Proposed AI solution architect**, for architecture setup and agent review (14 days) |
| **Agents** | Recordly **Virtual Data Engineer** (months 4–6): runs 24/7 inside your Snowflake account and takes the repetitive dbt, testing and monitoring work |
| **Price** | **€115,320 fixed**, invoiced as **6 × €19,220 per month**. Weekly hours and capacity reporting; monthly invoice is fixed. |
| **Contract** | UPM standard purchase agreement **as is, no deviations, no tracked changes**. Right to recruit the engineer after 12 months without a fee: **accepted**. |

---

# How the work is split, and why it doesn't break at quarter close

| Who | Does | Safeguard |
|---|---|---|
| **AI engineer (human)** | Architecture, feature design, model choice in Databricks, SAP write-back design, dbt conventions and "perfect examples" for the agents | Designs for quarter close first: idempotent loads, back-fill and rerun runbooks |
| **Virtual Data Engineer** | Repetitive dbt models and tests from agreed patterns, failed-job root-cause analysis, schema-drift checks, documentation | **Opens pull requests only. Your engineers or ours approve every change.** It can't merge its own work. |
| **Your team** | Reviews, owns the code, learns by pairing | All code in UPM's repositories from day 1 |

> Lesson from your earlier fragile pipeline: **no bespoke one-off scripts**. Every pipeline follows the same tested dbt + Databricks pattern, and the agents are only allowed to build within it.

---

# Six-month plan

| Month | Focus | Result |
|---|---|---|
| **1** | Onboarding, use-case selection with your team, architecture and conventions | Agreed pattern for Snowflake/dbt → Databricks ML → SAP write-back |
| **2–3** | First use case to production; pairing with your engineers | First predictions in SAP, monitored |
| **4** | VDE deployed in your Snowflake account; baseline measured (lead time, review load) | Agents take the repetitive model, test and monitoring work |
| **5–6** | Use cases 2–4; drift monitoring and retraining; handover to your team | Your team runs everything; quarter-close rehearsal passed |

Fixed scope boundary: if priorities change, we swap use cases in the backlog. **The monthly fee does not change.**

---

# The engineer and the agents

:::cols
### Required profile: forward-deployed ML engineer
- Snowflake, dbt, Databricks ML, SAP S/4HANA integration
- **Required certifications:** Databricks ML Professional · SnowPro Core · dbt Analytics Engineering
- Finnish and English · **60% target from 1 Dec 2026; availability pending**
- With **Proposed AI solution architect** (Azure Solutions Architect Expert required), 14 days for setup and agent review
:::col
### Virtual Data Engineer (Recordly product)
- A team of agents: data engineer, review and auditor agents, with a full audit trail
- Runs **inside UPM's Snowflake account** on your Snowflake AI credits
- Measured in real projects: a semi-complex pipeline built, tested and validated in **30 min instead of 12 h**
- **Guardrails:** cannot approve or merge its own work, and stops and escalates when stuck
:::

---

# Price and terms

| Item | Effort | Amount |
|---|---|---|
| Proposed forward-deployed ML engineer, ML engineer, 3 days/week × 6 months | 78 days × €960 | €74,880 |
| AI solution architect and governance | 14 days × €960 | €13,440 |
| Virtual Data Engineer, months 4–6 | 3 months × €9,000 flat | €27,000 |
| **Fixed total** | | **€115,320 (VAT 0%)** |

- Invoiced monthly: **6 × €19,220**. No hourly overage; weekly hours and capacity reporting remain available.
- Snowflake AI credits used by the agents are billed by Snowflake on UPM's account. We report them monthly.
- Standard purchase agreement accepted with **no deviations**. Recruit-after-12-months clause accepted.
- **Honest unknown:** which use cases are production-ready is confirmed in month 1. Delivery is capped at 78 engineer days and 14 architect days; reprioritisation stays within that capacity.

---

# Staffing basis and confirmation gate

- Planning assumption: six months = 26 weeks, five working days/week, eight hours/day; exact holiday and absence calendar to confirm. Engineer: 3 days/week = 78 days (60%).
- Architect: 8 setup days + 2 review days in each of the 3 VDE months = **14 days**, about 10.8% across 26 weeks. Setup precedes agent use.
- AI DE and AI architect: **EUR 120/h (EUR 960/day)**; analytics engineer: **EUR 125/h (EUR 1,000/day)**. Architect base EUR 115/h plus AI EUR 5/h is a proposed commercial rate, not an approved company minimum.
- Candidate names, CVs, certificates, languages, start dates and availability require written verification before submission. Named profiles in earlier drafts are not evidence.
- Fixed fee covers the stated capacity and prioritised backlog. Validate source effort and VDE offload in discovery; changes outside this boundary need written approval. AI credits, travel and licences are excluded. No additional production throughput is guaranteed.
