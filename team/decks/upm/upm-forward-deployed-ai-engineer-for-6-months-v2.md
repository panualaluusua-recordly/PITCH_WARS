<!-- title: UPM · Forward-Deployed AI Engineer -->
# Production ML pipelines that survive quarter close

## One forward-deployed AI engineer in your Helsinki team from 1 Dec 2026, a Virtual Data Engineer for the repetitive work, and a fixed monthly fee. €107,400 fixed (excl. VAT) · UPM standard terms, no deviations.

Proposal to Tapio Rantala, Vice President of Enterprise Data & Analytics · Recordly Oy · Helsinki

---

# The proposal in one page

| | |
|---|---|
| **Outcome** | Up to 3–4 ML use cases moved from notebook to monitored production pipelines. Predictions written back to SAP S/4HANA through one tested pattern. |
| **Stack** | Your Snowflake + dbt and Databricks ML. Code in UPM's repositories. No new platforms or licences. |
| **People** | **Henna Kallio**, forward-deployed ML engineer, embedded 3 days a week from 1 Dec 2026. **Tuomas Rantanen**, solution architect, for design review. |
| **Agents** | Recordly **Virtual Data Engineer** in months 4–6, inside your Snowflake account. A person approves every change. |
| **Price** | **€107,400 fixed** (excl. VAT), invoiced as 6 equal monthly fees. No timesheet reconciliation. |
| **Contract** | Standard purchase agreement **as is, no deviations**. Direct recruitment after 12 months **without a fee: accepted**. |

---

# Models reach SAP through one tested pipeline pattern, not one-off scripts

| Stage | What runs | Control |
|---|---|---|
| **1 · Features** | Snowflake + dbt models, tested feature tables | Data contract and dbt tests on every input |
| **2 · Databricks ML** | Training from one template, model registry | Registry approval by your named owner. Drift and accuracy monitoring |
| **3 · Scoring** | Scheduled batch scoring, tests on every output | Retry and alert, so nothing fails silently. Paused in the quarter-close window |
| **4 · SAP S/4HANA** | Staged write-back, reconciled before posting | Owner per integration. Rollback to the previous model version |

The engineer builds the template in your repos in the first 30 days and reuses it for every model. Run cost is capped per pipeline and reported monthly.

---

# What we read between the lines, and our safeguard

| Your history | Our safeguard |
|---|---|
| A bespoke pipeline collapsed at quarterly close | One template, one release checklist. **No releases in the 5 working days around quarter close**; dates come from your finance calendar |
| Billing drifted past department estimates | **Fixed monthly fee, same amount every month.** No hourly overage. Scope changes only by written note approved by your budget owner |
| Direct hiring after 12 months | **Accepted, no fee.** Knowledge sits in your repos from day 1 |
| Standard terms, deviations as tracked changes | **No tracked changes. No deviations.** |
| Key-person risk | Replacement of equal seniority within 10 working days, 2-week overlap at our cost |

---

# Six-month plan: start with the pattern, release outside quarter close

| Month | Focus | Gate / result |
|---|---|---|
| **1** | Onboarding, use-case selection, template, conventions. Handover pairing from week 1 | **Go/no-go:** a use case enters build only with passing input tests and a named owner |
| **2–3** | First use case to production, paired with your engineers | First monitored predictions in SAP |
| **4** | VDE deployed in your Snowflake. Baseline measured: lead time, review load | Agents take repetitive models, tests, monitoring |
| **5–6** | Use cases 2–4, drift monitoring, handover | Your team runs it. Quarter-close rehearsal passed |

**Honest unknown:** which use cases are production-ready, and the SAP write-back interface, are confirmed in month 1. If one fails the gate, we swap it in the backlog. The fee does not change.

---

# The engineer, the architect and the agents

:::cols
### The people
| Role | Certifications |
|---|---|
| **Henna Kallio**, forward-deployed ML engineer. fi, en. **60% from 1 Dec 2026** | Databricks ML Professional · SnowPro Core · dbt Analytics Engineering |
| **Tuomas Rantanen**, solution architect. fi, en. About 6 days: design review, escalation | Azure Solutions Architect Expert |

Availability is confirmed in writing at signature.
:::col
### Virtual Data Engineer (months 4–6)
- A team of agents: data engineer, review and auditor agents, with an audit trail
- Runs 24/7 **inside UPM's Snowflake** on your AI credits
- Takes dbt models, tests, failed-job analysis. The architect sets the patterns and reviews its work
- **Opens pull requests only. A person approves every change.** It cannot merge its own work
- Real result: a semi-complex pipeline built, tested and validated in **30 min instead of 12 h**
:::

---

# Price and terms

| Item | Effort | Amount |
|---|---|---|
| Henna Kallio, ML engineer, 60% for 6 months | 78 days × €960 | €74,880 |
| Tuomas Rantanen, architecture and governance | 6 days × €920 | €5,520 |
| Virtual Data Engineer, months 4–6 | 3 months × €9,000 | €27,000 |
| **Fixed total** | | **€107,400 excl. VAT** |

- Invoiced as **6 equal monthly fees**. No hourly billing, no timesheets.
- Snowflake AI credits used by the agents are billed by Snowflake to your account.
- Standard purchase agreement accepted with **no contractual deviations**. Recruitment after 12 months accepted without a fee.

<!-- coverage: RFP asks: solution (slides 2-3, 6), assigned specialist and team certifications (6), delivery plan (5), price structure (7). Hidden: fragile pipeline/quarter close (3,4,5), billing drift -> fixed fee, no timesheets (2,4,7), recruit after 12 months accepted (2,4,7), standard terms no deviations (1,2,4,7). Honest unknown: slide 5 + availability note slide 6. Sources: tech slides upm.md (pipeline flow, checklist), delivery upm.md (replacement terms, quarter-close 5 days, fixed fee), VDE v1 (price structure, VDE months 4-6, 60%). Dropped: weekly hours report (reintroduces timesheet friction), note fields. -->
