<!-- title: LähiTapiola · First 100 Days Data and AI Roadmap -->
# LähiTapiola's first 100 days: trusted data first, then the AI roadmap

## A roadmap for the Data Platforms and Analytics team that starts from a data quality baseline on your central Snowflake. On site in Espoo, entirely in Finnish. €17,040 fixed total, excl. VAT. No contract deviations.

Proposal to Samuli Rinne, Head of Data Platforms and Analytics · Recordly Oy · Helsinki

---

# Background, aims and goals

## We prioritise use cases only after the data underneath them has passed a check.

| What we read in your brief | What the roadmap does about it |
|---|---|
| Policy and claims records still have **discrepancies** | **Phase 1 is a data foundation baseline**: policy and claims reconciled in Snowflake. No use case is ranked before it. |
| Standalone tools created **shadow stacks** beside the warehouse | One rule: **every analytical workload runs on the central Snowflake warehouse**; inventory and retirement plan for the shadow stacks |
| Audits question **single-origin offshore cloud APIs** | EU-hosted options and an **exit plan** for every AI service in the roadmap |
| Risk and supervisory committees resist automated determinations | AI in the roadmap **supports people**. It never decides on a policy or a claim. |
| Initiatives stall if they drift from the **insurance-system renewal** | Every roadmap item is tied to a renewal milestone |

---

# Solution architecture: one warehouse, governed AI

| Layer | Target state | Boundary |
|---|---|---|
| **Source systems** | Current insurance systems and the renewal programme's new core, both feeding Snowflake | No new integration platform |
| **Central warehouse** | **Snowflake on Azure** is the single analytical home: policy, claims, customer | Standalone tools read from it, never copy out of it |
| **Quality layer** | Automated reconciliation of policy against claims on every load, results shown beside each dataset | Roadmap items depend on its pass rate |
| **BI** | Your existing BI tool on governed Snowflake views | No new licences |
| **AI** | Use cases that assist handlers and analysts; model access through **EU-hosted endpoints in your Azure tenant** or in-warehouse options, behind a swappable interface | **Human decides**; exit plan per service |

> Later build work on Snowflake and dbt could use Recordly's Virtual Data Engineer, with your staff approving every change. It is an option for the roadmap, **not part of this price**.

---

# Implementation plan: 8 weeks to a 100-day roadmap

| Weeks | Phase | Output | Gate |
|---|---|---|---|
| **1–3** | **1 · Data foundation baseline.** Reconcile policy and claims records, count and classify discrepancies, inventory shadow stacks | Quality baseline report, shadow-stack list | **Gate 1:** your team agrees which domains are trustworthy now |
| **4–5** | **2 · Use-case prioritisation**, only on domains that passed. Others are scheduled after their fix. | Scored portfolio, risk-committee view | **Gate 2:** you choose the top use cases |
| **6–8** | **3 · 100-day roadmap**, sequenced against renewal milestones | Roadmap, EU-hosting and exit options, team plan | Final review |

- All workshops **on site in Espoo, entirely in Finnish**; written updates instead of recurring meetings
- **Honest unknown:** the size of the discrepancies. The baseline measures it in week 3, and the roadmap order depends on it.

---

# Key deliverables

| # | Deliverable | Format (Finnish) |
|---|---|---|
| D1 | Policy and claims data quality baseline, discrepancies by cause | Report and Snowflake queries in your repo |
| D2 | Shadow-stack inventory with retirement plan onto Snowflake | Table, owner per item |
| D3 | Scored use-case portfolio; AI items marked decision-support only | Workbook and summary |
| D4 | AI hosting options: EU-hosted choices and exit plan per service | Options note, you decide |
| D5 | 100-day roadmap aligned to the insurance-system renewal | Plan with owners and milestones |
| D6 | Team capability plan | Roles and skills |

All deliverables are LähiTapiola's property. Two-hour interview: we show the baseline method on a sample of your data.

---

# Proposed roles: Finnish delivery and Espoo attendance required

| Role | Required expertise | Required certificates | Availability |
|---|---|---|---|
| **Data and AI strategy lead (architect)** | insurance and finance data platforms, Snowflake on Azure | SnowPro Advanced: Architect · Microsoft Certified: Azure Solutions Architect Expert | From signature, 10 days |
| **Senior data engineer** | reconciliation and data quality in Snowflake and dbt | SnowPro Core · dbt Analytics Engineering Certification | From signature, 6 days |
| **AI engineer** | governed AI on Azure | Microsoft Certified: Azure AI Engineer Associate | From signature, 2 days |

Finnish and English are required; profiles and availability are unverified. Employees only. Any replacement is of equal seniority and needs your approval first.

---

# Financials and contract deviations

## Fixed total: €17,040 excl. VAT = 18 person-days

| Role | Days | Rate per day |
|---|---|---|
| Data and AI strategy lead (AI architect) | 10 | €960 |
| Senior data engineer | 6 | €920 |
| AI engineer | 2 | €960 |

- **Included:** on-site days and travel in Espoo, all deliverables in Finnish, no licences
- **Fixed price:** effort above plan is Recordly's risk. Invoiced on Gate 1 and on final acceptance, per your standard terms.
- **Contract deviations: none.** Your terms apply as they stand. The price is a bottom-up days × rate calculation, so you can benchmark it line by line.


**Staffing basis:** one person-day is 8 hours. DE EUR 115/h; DA EUR 125/h; required AI expertise adds EUR 5/h for the relevant role. Architect and other-role base EUR 115/h is a proposed commercial rate for owner review. The team has at most one architect and complementary roles. CVs, credentials, language proficiency, actual availability and exact start dates remain unverified. These are role requirements, not booked people. Fixed-price scope, client dependencies and risk allowance need agreement before commitment.

The strategy lead assesses AI hosting and governance: 10 days at EUR 120/h, including AI premium. DE 6 days at EUR 115/h and AI engineer 2 days at EUR 120/h give EUR 17,040 total. No AI build is added to this advisory scope.

<!-- coverage: RFP sections: background+aims (s2), approach+implementation plan (s4), key deliverables (s5), team profiles w/ certifications+availability (s6), contract deviations (s7: none), transparent financials (s7), solution architecture (s3), delivery methodology (s4), team composition (s6), price (s7), 2-hour interview (s5 note), BAFO (s7). v1 praise kept: on site Espoo, entirely Finnish. v1 fixes: data foundation baseline before use-case prioritisation + quick wins removed; no automated determinations; renewal alignment; shadow stacks -> central Snowflake; EU-hosted options + exit plan; sharpen terms -> transparent days x rate, lower scope. VDE: MENTION only (Snowflake; dbt unconfirmed; advisory scope), not priced. -->
