<!-- title: Fingrid Oyj · Financial and Margin Reporting Automation -->
# Trusted financial and margin reporting, as live as the data allows

## Reconcile D365 and the lakehouse first, then report. 21 person-days, €19,320 total excl. VAT, standard terms, no deviations.

Proposal to Leena Vainio, Head of Data and Analytics · Recordly Oy · Helsinki

---

# Compliance response: Yes, Yes but not included, Yes if

## Your requirement list was not attached, so we answered the 10 we expect from the RFP. Tell us any we missed.

| Requirement | Answer | How |
|---|---|---|
| Reports built on your D365 F&SC + Databricks + Power BI | **Yes** | No new platform, no new licences |
| Ledger duplicates between D365 and lakehouse removed before reporting | **Yes** | Phase 0, with a gate |
| Every figure traceable to a ledger entry | **Yes** | Lineage in Unity Catalog, finance data product with named owner |
| Real-time access to all underlying data | **Yes if** | Streaming (seconds to minutes) for operational monitoring data; reconciled batch for finance close. A "no batch ever" ledger would cost always-on compute and break reconciliation |
| Margin reports available intraday | **Yes if** | Incremental refresh from D365 change feed; latency table on slide 3 |
| Data quality checks and alerts | **Yes** | Automated tests on every load, alerts to your channel |
| Human sign-off on published figures | **Yes** | Finance owner approves each release |
| Finnish documentation and runbooks | **Yes** | All material in Finnish |
| D365 configuration changes | **Yes but not included** | We read from D365 only |
| Gen AI / forecasting features | **Yes but not included** | Not requested, not priced |

---

# Technical solution: where "real time" holds and where it stops

| Data | Path | Typical latency | Why |
|---|---|---|---|
| Operational monitoring | Structured Streaming into Delta | seconds to minutes | Needs freshness |
| D365 ledger and margin | Incremental change capture, reconciled | minutes to hourly | Duplicates must be resolved before a number is shown |
| Finance close | Reconciled batch, then locked | daily | A closed period must not move |

- Finance data product in your data-mesh: owner, quality tests, lineage
- Power BI reads the reconciled layer only
- Run-cost guard: compute budget agreed in Phase 0, alert at 80%, auto-stop on idle clusters

> Unknown: how many duplicate ledger entries exist. Phase 0 counts them in week 1; the gate decides scope.

---

# Rollout plan: no report before the baseline is verified

| Phase | Days | Work | Gate |
|---|---|---|---|
| **0 Reconcile** | 7 | Match D365 and lakehouse ledger records, remove duplicates, sign-off report | Finance accepts baseline. No reporting starts before. |
| **1 Report** | 10 | Margin and financial reports in Power BI, latency tiers, data tests | Finance reconciles 3 sample periods to ledger |
| **2 Own it** | 4 | Finnish runbooks, run-cost review, handover | Your engineers run it |

Your engineers pair with us from week 1. Written status every two weeks.

---

# Delivery team: two seniors, available from contract signature

| | Senior Data Architect | Senior Data Engineer |
|---|---|---|
| **Experience** | 12 years, lakehouse and data-mesh design, finance data | 9 years, Databricks pipelines, reconciliation, Power BI |
| **Certifications** | Databricks Data Engineer Professional · Azure Solutions Architect Expert | Databricks Data Engineer Associate · Azure Data Engineer Associate · PL-300 Power BI Data Analyst |
| **Languages** | Finnish (native), English | Finnish (native), English |
| **Availability** | From contract signature | From contract signature |

You may replace either person at any time; replacement of equal seniority, overlap at our cost.

---

# Price and total cost of ownership

| Role | Days | Day rate | Amount |
|---|---|---|---|
| Senior Data Engineer | 15 | €920 | €13,800 |
| Senior Data Architect | 6 | €920 | €5,520 |
| **Total, fixed, excl. VAT** | **21** | | **€19,320** |

- **Run cost after handover:** Databricks compute on your account, capped and alerted as set in Phase 0. No Recordly licence, no new tool.
- **Invoicing:** 50% at Phase 0 gate, 50% at handover. Prices firm for 9 months.
- **Contract:** your standard agreement as is. **No contractual deviations.**
- Hours above plan are Recordly's risk.

<!-- coverage: RFP sections compliance matrix(s2)/solution(s3)/team(s5)/rollout(s4)/TCO pricing(s6); fear ledger duplicates->Phase 0 gate; integrity->data product+lineage; spend limits->fixed low total+compute cap; unproven modernisation->no AI, existing stack; real-time trap->Yes if; praise latency honesty kept; budget complaint->price cut -->
