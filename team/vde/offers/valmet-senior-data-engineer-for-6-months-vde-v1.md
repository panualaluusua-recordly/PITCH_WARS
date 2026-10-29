<!-- title: Valmet · Senior Data Engineer -->
# A senior data engineer with AI-assisted delivery and architecture support

## Ingestion pipelines from Infor CloudSuite and mill operations into Snowflake. Built for constrained satellite links and kept inside your own environment.

Draft proposal to Milla Kaartinen, Data & AI Development Manager · Recordly Oy · Helsinki

---

# The proposal in one page

| | |
|---|---|
| **Outcome** | Reliable, monitored ingestion from Infor CloudSuite and operational sources into Snowflake, ready for reporting in your BI tool |
| **People** | **Proposed senior data engineer** (**SnowPro Advanced: Data Engineer**), 3 days a week in Espoo and on your chat tool targeting 1 Dec 2026, subject to confirmation, plus **Proposed AI solution architect** (14 days) |
| **Agents** | Recordly **Virtual Data Engineer** (months 4–6) runs 24/7 inside your Snowflake account and takes repetitive pipeline, test and monitoring work |
| **Price** | **€115,320 fixed**, 6 × €19,220 per month |
| **Visibility** | A monthly capacity and results report for your leadership: pipelines delivered, lead time, incidents avoided |

---

# Technical solution: light on the network, inside your perimeter

| Challenge from your RFP | Our answer |
|---|---|
| **Satellite links saturated by raw telemetry** | Filter and aggregate at the site: only changed records and agreed aggregates are sent, compressed, in incremental batches and scheduled off-peak. Raw high-frequency data stays local unless a use case needs it. |
| **Exposure to foreign jurisdiction** | Data stays in your Snowflake account and your cloud region. The VDE runs **inside your Snowflake account**, with no data copied to Recordly systems. |
| **Infor CloudSuite integration** | Incremental extraction through supported Infor APIs and data-lake exports, with delta loads and reconciliation counts per run |
| **Reliable reporting** | dbt models with automated tests, freshness checks and alerts to your chat tool |

---

# How the work is split

| Who | Does | Safeguard |
|---|---|---|
| **Senior data engineer** | Ingestion architecture, site-side filtering design, dbt conventions, the hard integrations, stakeholder work | Writes the "perfect examples" the agents copy |
| **Virtual Data Engineer** | New sources from agreed patterns, tests, failed-job root cause, schema-drift checks, docs | **Pull requests only. A person approves every change.** |
| **Your team** | Reviews and owns the code | Everything in Valmet's repositories |

**Plan:** month 1 site and source assessment · months 2–3 first sources live · month 4 VDE deployed and baseline measured · months 5–6 scale to remaining sources and hand over.

---

# Team credentials and price

:::cols
### Required profile: senior data engineer
- **SnowPro Core · SnowPro Advanced: Data Engineer** (required; candidate evidence pending)
- Finnish and English · **60% target from 1 Dec 2026; availability pending**
- **Proposed AI solution architect** (Azure Solutions Architect Expert required), 14 days
:::col
### Price
| Item | Amount |
|---|---|
| Proposed senior data engineer, 78 days × €960 | €74,880 |
| Proposed AI solution architect, 14 days × €960 | €13,440 |
| VDE, 3 months × €9,000 | €27,000 |
| **Fixed total** | **€115,320** |

Snowflake AI credits used by the agents are billed on Valmet's account and reported monthly. Draft for review; scope, staffing and commercial terms need owner confirmation.
:::

---

# Staffing basis and confirmation gate

- Planning assumption: six months = 26 weeks, five working days/week, eight hours/day; exact holiday and absence calendar to confirm. Engineer: 3 days/week = 78 days (60%).
- Architect: 8 setup days + 2 review days in each of the 3 VDE months = **14 days**, about 10.8% across 26 weeks. Setup precedes agent use.
- AI DE and AI architect: **EUR 120/h (EUR 960/day)**; analytics engineer: **EUR 125/h (EUR 1,000/day)**. Architect base EUR 115/h plus AI EUR 5/h is a proposed commercial rate, not an approved company minimum.
- Candidate names, CVs, certificates, languages, start dates and availability require written verification before submission. Named profiles in earlier drafts are not evidence.
- Fixed fee covers the stated capacity and prioritised backlog. Validate source effort and VDE offload in discovery; changes outside this boundary need written approval. AI credits, travel and licences are excluded. No additional production throughput is guaranteed.
