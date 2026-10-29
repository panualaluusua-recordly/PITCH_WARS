<!-- title: VR Group · Data Catalogue and Ownership Rollout -->
# A working data catalogue with named owners, built by your own team's tools and kept by your own maintainers

## See one domain catalogued first. Pay only if you accept it. Capped at €10,120 (excl. VAT). Nothing payable at kickoff. No contractual deviations.

Proposal to Samuli Vainio, Head of Data Platform · Recordly Oy · Helsinki

---

# Solution: Snowflake's built-in metadata and lineage, no bespoke services

| Part | How |
|---|---|
| **Catalogue** | Snowflake object tags and comments on your Data Vault 2.0 hubs, links and satellites (AWS account unchanged). Tags carry domain, owner, steward, sensitivity. |
| **Lineage** | Snowflake's built-in lineage and the ACCESS_HISTORY and OBJECT_DEPENDENCIES views, plus ERP source and BI report mapping in your existing BI tool |
| **Ownership model** | **Named data owner and named steward per domain** (passenger, freight, then ERP-linked shared data). VR names them; we run the workshops in Finnish and write the RACI. |
| **Change path** | Every tag and comment goes to your repository as a **pull request** that your crew approves. No automation writes directly. |
| **Out of scope** | Bespoke metadata services, new catalogue platforms, ML, anything touching rail operations systems |

> A previous initiative spent months on custom services. Here: **zero custom code to maintain**.

---

# What we read between the lines, and our safeguard

| Your history | Our safeguard |
|---|---|
| **Engineers tied up for months writing metadata services** | Only Snowflake features and tools you already run. If a gap appears, it is listed and **you decide**; we build nothing without your approval. |
| **Contractors rolled off, maintainers scrambled** | **Your maintainers own the catalogue from week 1:** they hold the repository and approve every PR. Runbooks in Finnish, written together with them. |
| **No proof it works at handover** | **Handover test:** your maintainer adds a new table, tags it, traces its lineage and fixes a broken tag alone, with us watching. Paid only if it passes. |
| **Operational stability** | Metadata only; no production data pipeline changes. Nothing is merged in your morning reporting peak. |
| **Foreign-led workshops lost rail concepts** | Native Finnish engineer, workshops and documentation in Finnish |

---

# Delivery plan: one domain at a time, each accepted before the next

| Step | Work | You accept |
|---|---|---|
| **Working sample (3 days)** | Passenger domain catalogued: tags, lineage view, named owner and steward, Finnish runbook draft | **A1:** sample reviewed by your team |
| **Freight domain (3 days)** | Same pattern, reused. Owners and stewards named. | **A2** |
| **ERP-linked shared data (3 days)** | ERP source and BI report lineage, ownership for shared assets | **A3** |
| **Handover test (2 days)** | Finnish runbooks final, maintainer test, ownership forum routine | **A4:** test passed |

- **Interview stage:** we can show the sample approach live in the interview.
- **Unknown:** your Snowflake edition decides how much lineage is built in. We check in week 1; if a feature is missing, we show the simple fallback (tags plus dependency views) before any work is paid.
- Knowledge transfer from week 1: pairing, all work in your repositories. No Q1 production changes by us.

---

# Team: available at signature, on site in Helsinki

| Role | Certifications | Languages | Days |
|---|---|---|---|
| **Jari Lehtonen**, senior analytics engineer | SnowPro Advanced: Data Engineer · AWS Data Engineer Associate · dbt Analytics Engineering | fi (native), en | 9 |
| **Data governance lead**, rail-operations literate | SnowPro Core · DAMA CDMP | fi, en | 2 |

- Majority of the team available from contract signature. On site in Helsinki when workshops need it.
- You may require replacement of any consultant; we overlap at our cost.
- All documentation and runbooks in Finnish.

---

# Price and terms: one cap, pay per accepted domain

| Item | Basis | Amount |
|---|---|---|
| **Working sample:** passenger domain (3 days × €920). **Payable only if you accept it** | | €2,760 |
| Freight domain (3 days × €920), payable on acceptance | | €2,760 |
| ERP-linked shared data (3 days × €920), payable on acceptance | | €2,760 |
| Handover test and Finnish runbooks (2 days × €920), payable when the test passes | | €1,840 |
| **Cap** | 11 days | **€10,120 excl. VAT** |

- **Nothing at kickoff, no lump sum.** Each item is invoiced only after you accept it. Stop after any step and pay only for what you accepted.
- No licences or tools to buy: Snowflake features you already have.
- Offer stands for direct award or competitive tendering.
- **No contractual deviations.** Your standard terms apply as they are.

<!-- coverage: RFP: solution (2), plan+milestones (4), team (5), pricing (6), interview (4). Hidden: bespoke metadata services -> built-in Snowflake, no custom code (2,3); contractors rolled off -> week-1 ownership, Finnish runbooks, handover test (3,4); ownership model per domain (2,4); price small, accepted-sample-first, no kickoff lump sum, cap (1,6); native Finnish (3,5); PR-only crew approval (2); stability (3). -->
