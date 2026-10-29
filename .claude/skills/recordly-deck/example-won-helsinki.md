<!-- title: City of Helsinki · Data Engineering Squad -->
# Two-person data engineering squad: technical briefing

## SAP S/4HANA Cloud and municipal register pipelines, built with your team from week 1. €84,000 fixed. Standard purchase agreement, no deviations.

Proposal to Kari Voutilainen, Head of Data and Analytics Architecture · Recordly Oy · Helsinki

---

# Solution and deliverables

:::cols
### Technical solution
- **SAP S/4HANA Cloud:** extraction through released CDS views and OData APIs with incremental deltas. No custom ABAP, nothing fragile.
- **Municipal registers:** **probed first** (test extract, key and quality profiling), then built only if approved at the gate
- **Existing cloud platform and BI tool only.** No new licences.
- Layered model (raw → cleaned → business-ready), automated data tests on every load, monitoring with alerts into your channels, CI/CD in your repositories
:::col
### Deliverables
- **D1 · Month 1:** source-risk report for every SAP and register source, plus a go/no-go gate where the City decides what is built
- **D2 · Months 2–3:** SAP S/4HANA Cloud pipelines in production
- **D3 · Months 3–5:** approved register pipelines in production
- **D4 · Months 2–5:** BI-ready data models with automated tests
- **D5 · Continuous:** Finnish-language runbooks written as each pipeline goes live
- **D6 · Continuous:** every dataset registered in a **data catalog** with owner, description, refresh schedule and lineage
:::

---

# Findable and understandable for years to come

## Every pipeline output can be found, understood and traced, without asking the people who built it

| What | How |
|---|---|
| **Data catalog** | Every table registered in the City's existing catalog (or a catalog in the current platform, no new licences) with a Finnish business description, owner, refresh schedule and quality status |
| **Lineage** | Automatic lineage from SAP S/4HANA Cloud / register source → raw → cleaned → BI dataset, so analysts and auditors can see where every figure comes from |
| **Naming and structure** | One documented naming convention: `source_domain_entity`, with schemas by layer, so outputs are predictable to find |
| **Data dictionary** | Field-level definitions in Finnish for business-ready tables, generated from code so it never goes stale |
| **Quality visibility** | Test results and freshness shown next to each dataset, so users know whether to trust it today |

Definition of done for every pipeline: catalogued, described, lineage visible, runbook written.

---

# Plan: your engineers build it with us from week 1

| Month | Work | Knowledge sharing (continuous, not at the end) |
|---|---|---|
| **1** | Source-risk check and go/no-go gate | City engineers join source probing and design decisions |
| **2–3** | SAP pipelines into production | **Pair programming:** every pipeline has a City co-owner; all code reviewed by City engineers |
| **3–5** | Register pipelines, models and tests | **City engineers lead** the later pipelines while we review |
| **6** | Hardening and optimisation | City team runs operations; we support. Nothing to "hand over" because they already own it. |

Short written status every two weeks and a monthly demo. No extra meetings.

---

# Squad: two seniors, certified, available on signature

| | Senior Data Engineer (lead) | Senior Data Engineer |
|---|---|---|
| **Experience** | 11 years; SAP S/4HANA extraction, public-sector integrations | 8 years; API and register ingestion, data quality testing, CI/CD |
| **Certifications** | Azure Data Engineer Associate · Databricks Data Engineer Professional · dbt | Azure Data Engineer Associate · SnowPro Core · dbt |
| **Languages** | Finnish (native), English | Finnish (native), English, Swedish |
| **Availability** | **100% from contract signature, confirmed** | **100% from contract signature, confirmed** |

The City may require replacement of either engineer at any time; any replacement is of equal seniority, with overlap at Recordly's cost.

---

# Price and terms

| | |
|---|---|
| **Fixed total** | **€84,000 (VAT 0%)** for two senior engineers, six months |
| **Invoicing** | 6 × €14,000 monthly, payment per the City's standard agreement |
| **Included** | Travel, on-site days in Helsinki, architect review, documentation |
| **Licences** | None. Built on the City's existing platform. |
| **Contract** | **City's standard purchase agreement as is. No deviations, no tracked changes.** |

> Fixed price: any hours above plan are Recordly's risk, not the City's.

---

<!-- statement -->
# Test the sources first. Build with your team. Leave nothing brittle behind.

## Two senior engineers · six months · €84,000 fixed · standard terms

Recordly Oy · Helsinki
