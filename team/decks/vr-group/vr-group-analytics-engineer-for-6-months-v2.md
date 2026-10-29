<!-- title: VR Group · Analytics Engineer -->
# Data Vault 2.0 capacity that speaks Finnish rail, and respects the Q1 freeze

## A Finnish-speaking senior analytics engineer in your Helsinki team from 1 Dec 2026, with a Virtual Data Engineer for capacity. No production changes in Q1. €109,800 fixed (excl. VAT).

Proposal to Samuli Vainio, Head of Data Platform · Recordly Oy · Helsinki

---

# The proposal in one page

| | |
|---|---|
| **Outcome** | Every source feeding your platform has a named extraction method. New passenger and freight sources modelled in your Data Vault 2.0 on Snowflake, ready for your BI tool. |
| **Stack** | Your AWS + Snowflake + Data Vault 2.0. We reuse your conventions and loader. Nothing new unless you ask. |
| **People** | **Jari Lehtonen**, senior analytics engineer, native Finnish, 3 days a week from 1 Dec 2026. **Tuomas Rantanen**, solution architect, sets the conventions and reviews. |
| **Agents** | Recordly **Virtual Data Engineer**, Feb–Apr, in your Snowflake account. A person approves every change. |
| **Q1** | **No production changes in January–March.** Build and test in non-production only. |
| **Price** | **€109,800 fixed** (excl. VAT), 6 equal monthly fees. No contractual deviations. |

---

# Extraction for all sources: one method per source, assessed before we promise

| Source class | Proposed extraction (on AWS) | Unknown we resolve first |
|---|---|---|
| **Databases** (ticketing, freight orders, ERP) | Change-data-capture, e.g. AWS DMS where the database supports it | CDC support and access per database |
| **Traffic and timetable events** | API or event feed into S3 | Volumes, latency need, interface owner |
| **Partner files** | S3 file drop, schema check on arrival | File formats and delivery schedule |
| **Everything lands in** | Snowflake Raw Vault: hubs on business keys, links (train, wagon, order), satellites with full history | Your current loader. We use yours |

**Week 2 gate: source register.** Every source gets a method, owner, load frequency, and effort and risk. You set the build order. Config per source lives in Git, not one script per feed.

---

# What we read between the lines, and our safeguard

| Your history | Our safeguard |
|---|---|
| **Q1: strictly no production changes** | Nothing is promoted to production in Jan–Mar. Production only in Dec and from April, each release with a tested rollback |
| **Railway concepts lost in foreign-led workshops** | Workshops, business keys and documentation **in Finnish**. Train run, composition, timetable version and wagon are modelled with your operations experts |
| **Data Vault 2.0 in place** | Hubs, links and satellites follow your conventions. No model re-design |
| **Extraction for all sources** | Assessed per source in week 2, not promised blind |
| **Tech hype** | Plain gates with pass criteria agreed with you |

---

# Plan around the Q1 freeze

| When | Work | Production? |
|---|---|---|
| **Dec 2026** | Onboarding, source register (week-2 gate), first satellites live. **Gate:** row counts reconcile to source | **Yes, before year-end** |
| **Jan–Mar 2027** | Build and test remaining sources in non-production. VDE from Feb. Release package prepared | **No. Freeze respected** |
| **Apr 2027** | Release of the Q1 package in agreed weekend windows. **Gate:** reconciliation green, rollback tested | **Yes** |
| **May 2027** | Hardening, Finnish runbooks, handover to your team | Yes |

Knowledge transfer from week 1: pairing, and all code in your repositories.

---

# The engineer, the architect and the agents

:::cols
### The people
| Role | Certifications |
|---|---|
| **Jari Lehtonen**, senior analytics engineer. fi (native), en. **60% from 1 Dec 2026** | SnowPro Advanced: Data Engineer · dbt Analytics Engineering · AWS Data Engineer Associate |
| **Tuomas Rantanen**, solution architect. fi, en. About 12 days | Azure Solutions Architect Expert |

Availability confirmed in writing at signature.
:::col
### Virtual Data Engineer (Feb–Apr)
- Data engineer, review and auditor agents, with an audit trail
- Runs 24/7 **in VR's Snowflake** on your AI credits. Builds from your patterns, with tests
- **Opens pull requests only. A person approves every change.** In Q1, merges go to non-production only
- Real result: a semi-complex pipeline built, tested and validated in **30 min instead of 12 h**
- **Unknown:** it builds on dbt. We confirm in week 2 that this fits your loader
:::

---

# Price and terms

| Item | Effort | Amount |
|---|---|---|
| Jari Lehtonen, analytics engineer, 60% for 6 months | 78 days × €920 | €71,760 |
| Tuomas Rantanen, architecture and review | 12 days × €920 | €11,040 |
| Virtual Data Engineer, Feb–Apr | 3 months × €9,000 | €27,000 |
| **Fixed total** | | **€109,800 excl. VAT** |

- Invoiced as **6 equal monthly fees**.
- Snowflake AI credits used by the agents are billed by Snowflake to your account.
- Replacement at your request: equal seniority within 10 working days, 2-week overlap at our cost.
- No contractual deviations.

<!-- coverage: RFP asks: technical solution (slides 2,3,6), team profiles and certifications (6), delivery plan (5), price model (7). Hidden: Q1 freeze (1,2,4,5,6), extraction for ALL sources assessed not promised blind (2,3,4), Finnish railway concepts/workshops in Finnish (2,4,5), Data Vault 2.0 (2,3,4). Honest unknowns: slide 3 column 3, slide 6 (dbt). Sources: tech vr-group.md (flow, gates, unknowns), delivery vr-group.md (Finnish, timeline, replacement), VDE v1 (60%, price structure). Dropped: note fields, weekly hours, "Nov" start, Christmas freeze wording (not in RFP), fixed gate numbers (5 days). -->
