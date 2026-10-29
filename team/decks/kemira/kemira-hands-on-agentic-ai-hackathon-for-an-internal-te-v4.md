<!-- title: Kemira · Agentic AI Hackathon -->
# Agentic AI hackathon: working prototypes, honest limits

## Two days on your SAP, Datasphere, SAC and Azure. €12,280 fixed. No contract deviations.

| | |
|---|---|
| **Background** | An earlier pilot stalled when edge cases were glossed over and autonomy was oversold |
| **Aim** | 3–4 agent prototypes your people build, tested on **real Datasphere data**, each with a written edge-case register |
| **Our stance** | Agents read governed data and **propose**; a person approves. No autonomous write-back to SAP |
| **Your time** | A 45-minute scoping call and a 45-minute readout. No recurring status meetings |

Proposal to Rasmus Vuorinen, Director of Digital Analytics · Recordly Oy · Helsinki

---

# Technical approach and deliverables

## Agents read your governed SAP data and propose; a person decides. Nothing new to license.

<div markdown="0" style="display:grid;grid-template-columns:1fr 40px 1fr 40px 1fr 40px 1fr;gap:0;align-items:stretch;font-size:0.72em;line-height:1.25;margin:0.2em 0 0.5em 0">
<div style="border:2px solid #434343;border-radius:10px;padding:14px;background:#232323"><div style="color:#E3FF87;font-weight:800;text-transform:uppercase;letter-spacing:0.05em;font-size:0.8em;margin-bottom:10px">Your SAP data, read-only</div><div style="border:2px solid #E3FF87;border-radius:8px;padding:10px;margin-bottom:10px">Certified <b style="color:#fff">Datasphere views</b>, one plant's space first (S/4HANA material, plant, batch)</div><div style="border:2px solid #E3FF87;border-radius:8px;padding:10px">SAC KPIs</div></div>
<div style="display:flex;align-items:center;justify-content:center;color:#E3FF87;font-size:1.6em;font-weight:800">&rarr;</div>
<div style="border:2px solid #434343;border-radius:10px;padding:14px;background:#232323"><div style="color:#E3FF87;font-weight:800;text-transform:uppercase;letter-spacing:0.05em;font-size:0.8em;margin-bottom:10px">Access layer, your Azure</div><div style="border:2px solid #E3FF87;border-radius:8px;padding:10px;margin-bottom:10px">Runs <b style="color:#fff">as the signed-in user</b>: no shared service account</div><div style="border:2px solid #E3FF87;border-radius:8px;padding:10px;margin-bottom:10px">Short read-only tool list you review in prep</div><div style="border:2px solid #E3FF87;border-radius:8px;padding:10px">Masks the fields your data owner lists</div></div>
<div style="display:flex;align-items:center;justify-content:center;color:#E3FF87;font-size:1.6em;font-weight:800">&rarr;</div>
<div style="border:2px solid #434343;border-radius:10px;padding:14px;background:#232323"><div style="color:#E3FF87;font-weight:800;text-transform:uppercase;letter-spacing:0.05em;font-size:0.8em;margin-bottom:10px">Agent, your Azure subscription</div><div style="border:2px solid #E3FF87;border-radius:8px;padding:10px;margin-bottom:10px">Model endpoint you approve</div><div style="border:2px solid #E3FF87;border-radius:8px;padding:10px;margin-bottom:10px">Step and token cap per run</div><div style="border:2px solid #E3FF87;border-radius:8px;padding:10px">Field text treated as data, not instructions</div></div>
<div style="display:flex;align-items:center;justify-content:center;color:#E3FF87;font-size:1.6em;font-weight:800">&rarr;</div>
<div style="border:2px solid #434343;border-radius:10px;padding:14px;background:#232323"><div style="color:#E3FF87;font-weight:800;text-transform:uppercase;letter-spacing:0.05em;font-size:0.8em;margin-bottom:10px">People decide</div><div style="border:2px solid #E3FF87;border-radius:8px;padding:10px;margin-bottom:10px">Proposal in a <b style="color:#fff">test channel</b> of your chat tool</div><div style="border:2px solid #E3FF87;border-radius:8px;padding:10px;margin-bottom:10px">Data owner: Approve / Reject, logged</div><div style="border:2px solid #E3FF87;border-radius:8px;padding:10px"><b style="color:#fff">Nothing written to SAP</b></div></div>
</div>
<div markdown="0" style="background:#2B3118;border-radius:8px;padding:10px 16px;font-size:0.7em;margin-bottom:0.6em">Run log (input, tool calls, answer, approver) in your Azure tenant · code in your repo · no new platform, no new licences · production bot needs your IT approval: out of scope</div>

**Candidate workflows** (chosen with you in prep): data-quality triage on Datasphere rules · KPI "why did it move" explainer · master-data anomaly queue

**Deliverables:** D1 seeded sandbox agent · D2 3–4 hackathon prototypes in your repo (sandbox data, not for production use) · D3 edge-case register per prototype · D4 go/no-go note per prototype

---

# Edge cases and limits, stated up front

## No promise of autonomous resolution. We measure it and report the misses.

| Edge case in SAP data | What the agent does |
|---|---|
| Missing or duplicate master data | Flags it, **escalates to a data owner** |
| Unit or currency mismatch between Datasphere views or SAC measures | Refuses to compare, shows both values |
| Rows the user may not see (plant authorisation) | Returns nothing for them; states that results are limited by the user's authorisation, without counts |
| Stale or late-loaded data | States data age before answering |
| Conflicting sources, ambiguous request | Asks a question, never guesses |
| Instruction-like text inside a master-data field | Treats it as data; the agent only has read-only tools |

> Each prototype is scored on a **seeded edge-case test set**, each case run 5 times: resolved, escalated, wrong. Go/no-go targets agreed in prep and confirmed after the first measurement, starting from zero wrong answers on authorisation cases.

---

# Plan: a live agent on your data before the hackathon starts

| When | What | Technical gate |
|---|---|---|
| **Prep, weeks 1–3** | Scoping call, pick workflows, read-only access to **one plant's Datasphere space**, your data owner lists fields to mask and labels the edge-case set, build and test the seed agent | Wk 2: a restricted test user sees zero rows outside its authorisation. Wk 3: seed agent's first measured run; targets agreed with you. Then: **live demo on day 1, hour 1** |
| **Hackathon, 2 days on site in Helsinki** | 12–16 participants (assumed) in 4 teams. Day 1 build, day 2 edge-case testing and demos | 3–4 prototypes; one counts as working when it meets the agreed targets on the seeded set, with zero access leaks; unmet items listed |
| **Follow-up, week after** | Code cleanup in your repo, edge-case registers, 45-minute readout | Go/no-go per prototype: real numbers incl. misses, token cost per run, "tested on one plant only" |

> **Honest unknowns, closed in prep:** (1) model endpoint and data access approved in time, otherwise the endpoint you approve and a masked extract, said on the day; (2) per-user identity into Datasphere, otherwise per-role test users; (3) final headcount and skill level. Tests re-run on every prompt, model or tool change; a per-team token cap and an Azure budget alert hold usage.

---

# Proposed team and role requirements

| Role | Required expertise and certifications | Days |
|---|---|---|
| **Senior AI / ML engineer** (lead facilitator) | ML for manufacturing on Azure. Azure AI Engineer Associate · Azure Data Scientist Associate. Finnish, English | 6 |
| **Senior data engineer** (SAP, Datasphere) | S/4HANA to Datasphere pipelines. SAP Certified Associate – Data Engineer – SAP Datasphere · Azure Data Engineer Associate. Finnish, English | 5 |
| **SAP data architect** (review) | SAP BW, Datasphere, SAC. SAP Certified Associate – Data Analyst – SAP Analytics Cloud. Finnish, English | 2 |

Two facilitators on site both days. Any replacement is of equal seniority and agreed with Kemira first.

---

# Price and terms

## Fixed total €12,280 (excl. VAT)

| Role | Days | Day rate | Amount |
|---|---|---|---|
| Senior AI / ML engineer | 6 | €960 | €5,760 |
| Senior data engineer | 5 | €920 | €4,600 |
| SAP / AI data architect | 2 | €960 | €1,920 |
| **Total** | **13** (prep 5, hackathon 5, follow-up 3) | | **€12,280** |

- **Fixed price:** effort above plan is Recordly's risk. Travel and on-site days in Helsinki included
- **No licences.** Model usage runs on Kemira's own Azure subscription, with a per-team cost cap agreed in prep
- **Kemira's standard purchase agreement: no deviations.** Kemira may hire deployed consultants after 12 months **without placement or transfer fees**: accepted in full
- Payment per Kemira's standard terms, invoiced after the readout is accepted. All code and results are Kemira's property


**Staffing review / Rauno:** role profiles are requirements, not verified people. Confirm CVs, certificates, languages and actual availability before submission. One day = 8 hours; DE minimum EUR 115/h, DA EUR 125/h, AI expertise adds EUR 5/h for the relevant specialist. Architect base EUR 115/h is proposed for owner confirmation, not a user-supplied minimum. At most two architects. Validate fixed scope and risk allowance before commitment.

SAP architecture includes AI workshop review: 2 days at EUR 120/h. Six AI engineer days, five DE days and two architect days remain 13 days.

<!-- coverage:
RFP sections: background -> slide 1; aims and goals -> slide 1; technical approach and deliverables -> slide 2; implementation plan -> slide 4; team credentials and availability -> slide 5; total pricing -> slide 6.
Hard constraints: standard purchase agreement, no deviations -> slide 1 + 6; hire consultants after 12 months without placement/transfer fees -> accepted explicitly slide 6.
Hidden: earlier pilot glossed over edge-case constraints, overpromised autonomous resolution -> slide 3 (edge-case register, seeded test set, escalation) + slide 1 stance; no side quests -> candidate workflows limited to SAP/Datasphere/SAC analytics.
Persona: lean, no recurring status meetings (slide 1, 4), real data not slides (live seed agent day 1 hour 1, slide 4), governance/access control (slide 2, row-level inherited from SAP auth, masking, logs), no new licences (slide 2, 6), price small.
Honest unknowns: model endpoint, data access, headcount (slide 4).
VDE: NO (Azure/SAP stack, advisory/event). Slides: 6.
Price: 6 x 960 + 5 x 920 + 2 x 920 = 5,760 + 4,600 + 1,840 = 12,200; 13 days; avg EUR 938/day = EUR 117/h. Days: prep AI2 DE2 Arch1; hackathon AI2 DE2 Arch1; follow-up AI2 DE1.
-->
