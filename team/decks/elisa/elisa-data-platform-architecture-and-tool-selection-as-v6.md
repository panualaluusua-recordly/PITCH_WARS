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

## Your brief requires real-time access to all data with no batch. Our honest answer: **real-time where a domain needs it**; literal zero-batch is not achievable for reconciled finance. Freshness per domain, agreed at Gate 1.

<div style="display:flex;align-items:stretch;gap:10px;margin:0.1em 0 0.35em 0;font-size:0.6em;line-height:1.2"><div style="flex:1;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:10px"><b style="color:#E3FF87">YOUR SOURCES</b><div style="border:1px solid #737373;border-radius:6px;padding:6px;margin-top:6px">Network and operational events</div><div style="border:1px solid #737373;border-radius:6px;padding:6px;margin-top:6px">ERP: vendor and change capture <i>confirmed in sprint</i></div><div style="border:1px solid #737373;border-radius:6px;padding:6px;margin-top:6px">Other transactional sources, listed in sprint</div></div><div style="align-self:center;color:#E3FF87;font-size:1.8em">&rarr;</div><div style="flex:1.35;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:10px"><b style="color:#E3FF87">FRESHNESS TIER</b><div style="border:1px solid #737373;border-radius:6px;padding:6px;margin-top:6px"><b>Streaming, seconds:</b> Pub/Sub to BigQuery Storage Write API <i>(proposed)</i></div><div style="border:1px solid #737373;border-radius:6px;padding:6px;margin-top:6px"><b>Change capture, minutes:</b> where the ERP supports it; otherwise API polling at an interval set at Gate 1</div><div style="border:1px solid #737373;border-radius:6px;padding:6px;margin-top:6px"><b>Micro-batch:</b> Cloud Composer incremental loads</div><div style="border:1px solid #737373;border-radius:6px;padding:6px;margin-top:6px"><b>Daily:</b> Composer, reconciled finance</div></div><div style="align-self:center;color:#E3FF87;font-size:1.8em">&rarr;</div><div style="flex:0.85;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:10px"><b style="color:#E3FF87">BIGQUERY</b><div style="border:1px solid #737373;border-radius:6px;padding:6px;margin-top:6px">Raw, as received</div><div style="border:1px solid #737373;border-radius:6px;padding:6px;margin-top:6px">Curated and joined</div><div style="border:1px solid #737373;border-radius:6px;padding:6px;margin-top:6px">Marts per domain</div></div><div style="align-self:center;color:#E3FF87;font-size:1.8em">&rarr;</div><div style="flex:1;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:10px"><b style="color:#E3FF87">SERVING</b><div style="border:1px solid #737373;border-radius:6px;padding:6px;margin-top:6px">Looker on live BigQuery</div><div style="border:1px solid #737373;border-radius:6px;padding:6px;margin-top:6px">Power BI: DirectQuery or import, <i>mode assessed per tier</i></div></div></div>
<div style="background:#2A2A2A;border:2px dashed #E3FF87;border-radius:10px;padding:8px 14px;font-size:0.6em;margin-bottom:0.5em"><b style="color:#E3FF87">CODE AND ACCESS:</b> Composer DAGs and CI/CD in your repositories · same IAM and policy tags in Looker and Power BI · cost tracked per tier · we read metadata only; no subscriber rows leave your GCP project</div>

- **Each domain gets the slowest tier that still meets its tested need.** Target ranges per tier are agreed at Gate 1, after current freshness is measured.
- **Why not everything real-time:** finance close reconciles daily; streaming all data raises run cost, failure surface and retention exposure of traffic data. "All real-time" is scored with its cost; your committee decides.
- **Out of scope:** no AI or ML, no new licence or platform unless an existing service fails a tested need.

---

# Technical gates: nothing is locked before it is measured

| Gate | When | Passes when |
|---|---|---|
| **Access ready** | Before sprint day 1 | NDA and secrecy undertaking signed; read-only Elisa-issued roles on BigQuery, Composer and Looker metadata and logs. No subscriber rows leave your GCP project; plus a write-enabled sandbox dataset and one feed, in your project, for the latency test (synthetic or masked data only) |
| **Gate 1** | End wk 2 | Each priority domain (3–5) has an owner, a stated freshness need and current freshness measured from Composer and BigQuery logs; one real feed run Pub/Sub to BigQuery to Looker in the sandbox dataset, end-to-end latency measured; ERP named with its change-capture options; target range per tier agreed |
| **Checkpoint B** | Wk 8 | Options A current stack tuned, B tiered, C all real-time scored on latency, cost and quota per tier, failure mode and effort; one tier test on one domain, end-to-end latency measured against the Gate 1 range |
| **Final** | Wk 10 | Target architecture and roadmap accepted by the steering committee; anything untested marked "not tested" |

| Honest unknown | How it is settled |
|---|---|
| **ERP and its change capture** | Sprint. Without change capture the ERP domain runs API polling or micro-batch, and Gate 1 shows its measured delay against the stated need |
| **Sandbox dataset and feed** | Requested before day 1. If none by day 3, the latency test is marked "not tested" and streaming stays a proposal |
| **Power BI connectivity** | Import refreshes on a schedule; DirectQuery freshness is bounded by query load, limits and cost. Measured per report in the sprint |
| **Where Composer code, CI/CD and access policies live** | Recorded in the sprint. Existing pipelines stay unless a test fails |

---

# Implementation plan: sprint, gate, then assessment

| Phase | Weeks | Person-days | Output |
|---|---|---|---|
| **0 · Scoping sprint** | 1–2 | 4 | Current-state sketch, freshness need and measured current freshness per domain, ERP change-capture check, **proposed milestones** |
| **Gate 1** | end wk 2 | – | Steering committee decides: **go, adjust or stop**. If stop, you pay for the sprint only. |
| **A · Current state and requirements** | 3–5 | 6 | Architecture baseline, requirements by domain, tiered freshness map |
| **B · Options and tool selection** | 5–8 | 7 | Options scored on cost per tier, risk, latency and effort; one tier test on one domain; recommendation |
| **C · Target architecture and roadmap** | 8–10 | 5 | Target architecture with a freshness tier per domain, sequenced roadmap, risks, one-page steering summary |

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
