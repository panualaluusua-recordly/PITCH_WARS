# Recordly capability profile (for bid/no-bid)

> **DRAFT. The team must verify.** Lines marked (verify) are assumptions. Correct them; the fit check is only as honest as this file. Claiming what we can't deliver risks `penalty` messages (chargebacks).

## Who we are
- Recordly Oy, Finnish data and AI consultancy, Helsinki HQ (verify other offices). "The Business Data Company".
- Size: mid-sized boutique (verify headcount). **Realistic team per project: 1–5 people.** We can't staff 10+ person programmes.
- Languages: Finnish (all consultants), English (all), Swedish (some; verify how many).
- Employees only; no subcontractors by default.

## Capability tiers

| Tier | What | Fit score |
|---|---|---|
| **Core (3)** | Modern data platforms (Snowflake, Databricks, Azure data stack, BigQuery), dbt and analytics engineering, data modelling incl. Data Vault, ingestion pipelines, BI and semantic models (Power BI and others), data governance and quality, master data cleanup, data strategy and roadmaps, architecture and tool assessments, FinOps for data platforms, MLOps, applied AI/ML and gen AI (RAG, agents) on data platforms | 3 |
| **Solid (2)** | ERP data as a **source** (SAP S/4HANA/Datasphere, Dynamics 365, Infor), finance and margin reporting, streaming/event ingestion, forecasting, predictive maintenance studies, staff augmentation of data/AI engineers, AI governance / EU AI Act readiness | 2 |
| **Edge (1)** | Legacy application modernisation beyond reporting, ERP-side configuration, CPQ, front-end apps (Streamlit OK), large multi-year migration programmes | 1 |
| **Not us (0)** | ERP implementation, ABAP/core-system development, hardware/OT installation, infrastructure operations, a human-staffed long-term AMS desk (run work on Snowflake + dbt is covered by the VDE run mode instead), pure software product development, non-data management consulting | 0 → no-bid |

(verify partner statuses and certifications: Snowflake, Databricks, Microsoft, dbt, Google Cloud, SAP)

## Industries with credible experience (verify)
Finance and insurance, retail, energy and utilities, manufacturing and forest industry, public sector, media, logistics. Healthcare and pharma: limited (verify).

## Things we never claim
- Experience on a buyer's **proprietary** platform (e.g. Enfuce's card-issuing platform). Instead say how fast we ramp up and who on their side we pair with.
- Named client references with contact persons we don't have. Use anonymised references; contacts on request.
- Real-time everything, zero defects, guaranteed AI accuracy.

## Roster
When `GET /api/me` returns `consultants`, **that list overrides this file** for who we can staff. Only propose people with `available: true` before `consultants_valid_until`, and match roles exactly.
