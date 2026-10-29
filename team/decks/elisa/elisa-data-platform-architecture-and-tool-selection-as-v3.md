<!-- title: Elisa · Data Platform Architecture and Tool Selection -->
# Data platform architecture and tool selection, starting with a short scoping sprint

## Built on BigQuery, Cloud Composer, Looker and Power BI. A gate before any milestone is locked. €20,240 fixed. Recruiting after 12 months accepted, no fee.

Proposal to Kirsi Suominen, Director of Enterprise Data Platforms · Recordly Oy · Helsinki

---

# What we read between the lines

## Each past problem in your brief becomes a safeguard

| What you told us | Our safeguard |
|---|---|
| Earlier advisory initiative **stalled: milestones locked before a scoping exercise** | **Paid scoping sprint first (4 days).** Milestones and scope are fixed only at **Gate 1**, after your steering committee has seen the sprint result. |
| Consultants' **billable hours stayed static** while automation sped them up | **Fixed price per deliverable**, no timesheets. If a deliverable is accepted in fewer days than planned, half of the unused days are credited. |
| Engineers' calendars eaten by **endless working sessions** | **Max 3 sessions of 60 min** in total, for named platform leads only. Everything else async: written questions and updates in your chat tool. |
| **Steering committees** and strict procurement | A one-page decision summary at each gate. Your standard procurement terms, **no deviations**. |
| Recruit consultants **after 12 months without a fee** | **Accepted as written.** |

---

# Solution approach: real-time where it pays, honest where it does not

## Your brief asks for real-time access to all data with no batch. Literal real-time for everything is neither achievable nor safe: finance close reconciles daily. We propose **a freshness target per domain**, confirmed at Gate 1 after measurement.

| Tier | Where it fits | Mechanism on your stack |
|---|---|---|
| **Streaming (seconds)** | Operational and network events, alerts | Pub/Sub into BigQuery (Storage Write API); Looker and Power BI DirectQuery on live BigQuery |
| **Change capture (minutes)** | ERP and transactional sources | CDC replication into BigQuery if the ERP supports it; otherwise API polling every 1–5 min |
| **Micro-batch (5–15 min)** | Joined, cleaned business models | Cloud Composer schedules with incremental loads |
| **Daily batch** | Finance close, reconciled figures | Composer; Power BI import refresh; correctness over speed |

- **Honest unknown:** which ERP you run, its change-capture options and each domain's real freshness need are unknown until the scoping sprint. We never promise a tier we have not tested.
- **Out of scope:** no AI or ML, no new platform proposed unless the assessment shows an existing service cannot meet a tested need.

---

# Implementation plan: sprint, gate, then assessment

| Phase | Weeks | Person-days | Output |
|---|---|---|---|
| **0 · Scoping sprint** | 1–2 | 4 | Current-state sketch, freshness need per domain, **measured latency test** (Pub/Sub → BigQuery → Looker, one real feed), ERP change-capture check, **proposed milestones** |
| **Gate 1** | end wk 2 | – | Steering committee decides: **go, adjust or stop**. If stop, you pay for the sprint only. |
| **A · Current state and requirements** | 3–5 | 6 | Architecture baseline, requirements by domain, tiered freshness map |
| **B · Options and tool selection** | 5–8 | 7 | Options scored on cost (streaming, live-query, quotas, Composer load), risk, latency and effort; recommendation |
| **C · Target architecture and roadmap** | 8–10 | 5 | Target architecture, sequenced roadmap, risks, one-page steering summary |

- Deliverables fixed per phase after Gate 1; documents in Finnish or English, as you prefer.
- **Your time:** about 3 hours per engineer in total.

---

# Team capabilities and availability

| | Lead Data Architect | Senior Data Engineer |
|---|---|---|
| **Required certifications** | Google Cloud Professional Cloud Architect · Google Cloud Professional Data Engineer | Google Cloud Professional Data Engineer · Microsoft Certified: Power BI Data Analyst Associate |
| **Required languages** | Finnish required, English | Finnish required, English |
| **Days** | 13 | 9 |
| **Availability** | **Target at signature; evidence pending** | **Target at signature; evidence pending** |

Two senior people who do the work themselves. No subcontractors. Replacement of any consultant at your request, equal seniority, overlap at our cost.

---

# Pricing and terms

## Fixed total: €20,240 (excl. VAT)

| Role | Person-days | Day rate (8 h) |
|---|---|---|
| Lead Data Architect | 13 | €920 |
| Senior Data Engineer | 9 | €920 |
| **Total** | **22 days** | **22 × €920 = €20,240** |

- **Fixed price per deliverable**, invoiced on acceptance (sprint, A, B, C); 21 days net
- **Gate 1 exit:** stop after the sprint and you pay for its 4 days only (4 × €920)
- **Licences:** none; your existing Google Cloud, Looker and Power BI
- Effort above plan is Recordly's risk. Travel in Helsinki included.

### Contract terms
**No contractual deviations.** Elisa may recruit deployed consultants after 12 months **without a fee**.

**Staffing review / Rauno:** role profiles are requirements, not verified people. Confirm CVs, certificates, languages and actual availability before submission. One day = 8 hours; DE minimum EUR 115/h, DA EUR 125/h, AI expertise adds EUR 5/h for the relevant specialist. Architect base EUR 115/h is proposed for owner confirmation, not a user-supplied minimum. At most two architects. Validate fixed scope and risk allowance before commitment.
