<!-- title: UPM · From AI prototypes to production (MLOps) -->
# From ML prototypes to monitored production, with releases that stay clear of quarter close

## MLOps best practices, automated deployment and monitoring on your Snowflake + dbt, Databricks ML and SAP S/4HANA. A fixed validation phase, then each pipeline transition priced on its own merits: at most €56,960 (excl. VAT), firm and binding for 9 months. UPM standard terms, no deviations.

Proposal to Tapio Rantala, Vice President of Enterprise Data & Analytics · Recordly Oy · Helsinki

---

# Technical approach: one release path from notebook to SAP

| Stage | What we set up | Control |
|---|---|---|
| **1 · Features** | Snowflake + dbt models with tested feature tables | dbt tests and data contract on every input |
| **2 · Train and register** | Databricks ML from one template, model registry, versioning | Registry approval by your named model owner |
| **3 · Automated deployment** | CI/CD in your repositories: test, promote, deploy, rollback to the previous version | No manual deploys. Every release has a checklist |
| **4 · Monitoring** | Drift, accuracy, freshness and cost per pipeline, alerts into your chat tool | Retry and alert, so nothing fails silently |
| **5 · SAP S/4HANA** | Staged write-back, reconciled before posting | Named owner per integration |

**Out of scope:** new platforms or licences, new use cases, custom ABAP. Your existing stack only.

---

# The same platform serves assistants: frontline mill vs enterprise chat

| | **Frontline mill assistant** | **Enterprise chat interface** |
|---|---|---|
| **Users, content** | Operators and maintenance staff; answers grounded in mill procedures and shift data | Office staff, broad questions across functions |
| **Priority** | Accuracy, speed, Finnish and English, read-only | Access control, breadth, usage cost |
| **Our view** | **Start here.** Narrow scope is testable and operationally valuable | Later, once access rules are agreed |

**What the MLOps platform gives both, with no extra build in this price:** the same registry and approval, model serving behind one deployment path, an evaluation set run before every release, and monitoring of quality, usage and cost.

---

# Your history and our safeguards

| Your concern | Our safeguard |
|---|---|
| A bespoke pipeline collapsed at quarterly close | **Quarter-close-safe releases:** no deployments in the 5 working days around close, dates from your finance calendar. A rehearsal passes before the first production release. Rollback in one step |
| Accountability across the administrative matrix | **Tuomas Rantanen is your dedicated coordinator:** one accountable contact, a monthly steering note, escalation path |
| Billing drift and calendar billing | **Payment per accepted stage only.** No timesheets, no hourly overage |
| Mill time vs central commitments | Staff time table below, agreed at kick-off |
| Direct hiring after 12 months | Accepted, no fee. Everything lives in your repos from day 1 |

> **Honest unknown:** which prototypes are production-ready, and the SAP write-back interface, are confirmed at the week-3 gate. If one fails, we swap it. The fee does not change.

---

# Plan, and the staff time we need from you

| Weeks | Work | Gate |
|---|---|---|
| **1–3** | Template, conventions, prototype review. Pairing starts in week 1 | **Go/no-go:** a prototype enters build only with passing input tests and a named owner |
| **4–7** | First model through CI/CD, monitoring and SAP write-back | Quarter-close rehearsal passed |
| **8–12** | Models 2–3, drift alerts, runbooks, handover to your team | Your team runs a release alone |

| Your people (planning assumption, agreed at kick-off) | Time |
|---|---|
| **Mill operational staff**, per pilot mill (max 2) | **About 8 h in total:** 2 h interview, 2 h workshop, 4 h acceptance checks. Never during shifts critical to production |
| **Central domain liaison** | **About 0.5 day per week** for 12 weeks (6 days): priorities, approvals, SAP contact |
| **Model owner and SAP owner** | 1 h per week each |

---

# Team: an ML engineer and a coordinator

| Role | Certifications | Time |
|---|---|---|
| **Henna Kallio**, forward-deployed ML engineer. fi, en | Databricks ML Professional · SnowPro Core · dbt Analytics Engineering | 44 days from 1 Dec 2026 |
| **Tuomas Rantanen**, solution architect and **dedicated coordinator**. fi, en | Azure Solutions Architect Expert | 16 days: steering, design review, escalation |

**Nordic process-industry experience:** reference calls with process-manufacturing clients offered at shortlist, with their consent. Replacement of equal seniority within 10 working days, overlap at our cost.

**Optional, not in the price:** Recordly **Virtual Data Engineer** (€9,000/month, fixed term) can take repetitive dbt work inside your Snowflake. A person approves every change. Real result: a pipeline built, tested and validated in 30 min instead of 12 h. Only if you decide so.

---

# Price and terms

| Item | Effort | |
|---|---|---|
| **Phase 1, validation (fixed):** MLOps template, deployment workflow, monitoring, first model live | Henna 17 d × €960 + Tuomas 7 d × €920 | €22,760 |
| **Each further pipeline transition, ordered separately** (up to 3) | Henna 9 d × €960 + Tuomas 3 d × €920 | €11,400 each |
| **Maximum, if all 3 are ordered** | | **€56,960 excl. VAT** |

- **Firm and binding for 9 months** from submission (until 29 July 2027)
- **No single indivisible sum.** After Phase 1 you decide pipeline by pipeline, on its own merits and on your administrative calendar. Each transition is a separate order, paid on acceptance; you can stop after any of them.
- Payment never by calendar: Phase 1 on acceptance of the first live model; each transition on acceptance of that pipeline in production
- Standard purchase agreement **as is, no deviations**. Recruitment after 12 months without a fee accepted.
- Snowflake and Databricks consumption stays on your accounts. No new licences.

<!-- coverage: RFP: MLOps best practices/automated deployment/monitoring (s2), stack Snowflake+dbt/Databricks/SAP (s2), approach (s2), delivery plan (s4), team profiles (s5), commercial terms (s6), firm 9 months (s1,s6). Review gaps: chatbots/conversational frontline vs enterprise (s3); mill staff vs central liaison (s4); Nordic credentials (s5 reference calls, unverified); regional rates (day rates shown, s6). Earlier feedback: coordinator (s3,s5), milestone payments (s3,s6), quarter close (s3,s4), budget tight (€56,960). VDE optional mention only (s5). -->
