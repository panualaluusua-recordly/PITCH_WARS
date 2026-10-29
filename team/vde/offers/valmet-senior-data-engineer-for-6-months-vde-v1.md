<!-- title: Valmet · Senior Data Engineer -->
# A certified senior data engineer, with a Virtual Data Engineer for capacity

## Ingestion pipelines from Infor CloudSuite and mill operations into Snowflake. Built for constrained satellite links and kept inside your own environment.

Proposal to Milla Kaartinen, Data & AI Development Manager · Recordly Oy · Helsinki

---

# The proposal in one page

| | |
|---|---|
| **Outcome** | Reliable, monitored ingestion from Infor CloudSuite and operational sources into Snowflake, ready for reporting in your BI tool |
| **People** | **Laura Heikkilä**, senior data engineer (**SnowPro Advanced: Data Engineer**), 3 days a week in Espoo and on your chat tool from 1 Dec 2026, plus **Tuomas Rantanen**, solution architect (5%) |
| **Agents** | Recordly **Virtual Data Engineer** (months 4–6) runs 24/7 inside your Snowflake account and takes repetitive pipeline, test and monitoring work |
| **Price** | **€104,280 fixed**, 6 × €17,380 per month |
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
### Laura Heikkilä, senior data engineer
- **SnowPro Core · SnowPro Advanced: Data Engineer** (certificate IDs provided for verification)
- Finnish and English · **60% from 1 Dec 2026**
- **Tuomas Rantanen**, solution architect (Azure Solutions Architect Expert), 5%
:::col
### Price
| Item | Amount |
|---|---|
| Laura Heikkilä, 78 days × €920 | €71,760 |
| Tuomas Rantanen, 6 days × €920 | €5,520 |
| VDE, 3 months × €9,000 | €27,000 |
| **Fixed total** | **€104,280** |

Snowflake AI credits used by the agents are billed on Valmet's account and reported monthly. No contractual deviations.
:::
