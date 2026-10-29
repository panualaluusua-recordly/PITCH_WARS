<!-- title: Kemira · Agentic AI Hackathon -->
# Agentic AI hackathon: working prototypes, honest limits

## Two days on your SAP, Datasphere, SAC and Azure. €12,200 fixed. No contract deviations.

| | |
|---|---|
| **Background** | An earlier pilot stalled when edge cases were glossed over and autonomy was oversold |
| **Aim** | 3–4 agent prototypes your people build, tested on **real Datasphere data**, each with a written edge-case register |
| **Our stance** | Agents read governed data and **propose**; a person approves. No autonomous write-back to SAP |
| **Your time** | A 45-minute scoping call and a 45-minute readout. No recurring status meetings |

Proposal to Rasmus Vuorinen, Director of Digital Analytics · Recordly Oy · Helsinki

---

# Technical approach and deliverables

| Layer | How it works | Boundary |
|---|---|---|
| **Data** | Agents read **certified Datasphere views** (S/4HANA material, plant, batch) and SAC KPIs | Read-only. Access inherited from SAP authorisations, row-level by plant |
| **Agents** | Built in Kemira's Azure subscription with the model endpoint Kemira already approves | No new platform, no new licences |
| **Chat** | Agents post findings and questions to a test channel in your chat tool | Production bot needs your IT approval: out of scope |
| **Control** | Every run logged: input, tool calls, answer, who approved | Sensitive fields masked before any model sees them |

**Candidate workflows** (chosen with you in prep): data-quality triage on Datasphere rules · KPI "why did it move" explainer · master-data anomaly queue

**Deliverables:** D1 seeded sandbox agent · D2 3–4 working prototypes in your repo · D3 edge-case register per prototype · D4 go/no-go note per prototype

---

# Edge cases and limits, stated up front

## No promise of autonomous resolution. We measure it and report the misses.

| Edge case in SAP data | What the agent does |
|---|---|
| Missing or duplicate master data | Flags it, **escalates to a data owner** |
| Unit or currency mismatch between S/4HANA and Datasphere | Refuses to compare, shows both values |
| Rows the user may not see (plant authorisation) | Returns nothing for them and says why |
| Stale or late-loaded data | States data age before answering |
| Conflicting sources, ambiguous request | Asks a question, never guesses |

> Each prototype is scored on a **seeded edge-case test set**: cases resolved, escalated, and wrong. The readout shows the real numbers.

---

# Plan: a live agent on your data before the hackathon starts

| When | What | Result |
|---|---|---|
| **Prep, weeks 1–3** | Scoping call, pick workflows, read-only access to **one plant's Datasphere space**, build and test the seed agent | **Live demo on day 1, hour 1** |
| **Hackathon, 2 days on site in Helsinki** | 12–16 participants (assumed) in 4 teams. Day 1 build, day 2 edge-case testing and demos | 3–4 prototypes with test results |
| **Follow-up, week after** | Code cleanup in your repo, edge-case registers, 45-minute readout | Go/no-go per prototype |

> **Honest unknowns, closed in prep:** (1) model endpoint available in Kemira's Azure tenant, otherwise we use the one you approve; (2) data access granted before the event, otherwise a masked extract and we say so on the day; (3) final headcount and skill level.

---

# Team: three seniors, certified, dates agreed at signature

| Role | Experience and certifications | Days |
|---|---|---|
| **Senior AI / ML engineer** (lead facilitator) | 9 yrs, ML for manufacturing on Azure. Azure AI Engineer Associate · Azure Data Scientist Associate. Finnish, English | 6 |
| **Senior data engineer** (SAP, Datasphere) | 10 yrs, S/4HANA to Datasphere pipelines. SAP Certified Associate – Data Engineer – SAP Datasphere · Azure Data Engineer Associate. Finnish, English | 5 |
| **SAP data architect** (review) | 12 yrs, SAP BW, Datasphere, SAC. SAP Certified Associate – Data Analyst – SAP Analytics Cloud. Finnish, English | 2 |

Two facilitators on site both days. Any replacement is of equal seniority and agreed with Kemira first.

---

# Price and terms

## Fixed total €12,200 (excl. VAT)

| Role | Days | Day rate | Amount |
|---|---|---|---|
| Senior AI / ML engineer | 6 | €960 | €5,760 |
| Senior data engineer | 5 | €920 | €4,600 |
| SAP data architect | 2 | €920 | €1,840 |
| **Total** | **13** (prep 5, hackathon 5, follow-up 3) | | **€12,200** |

- **Fixed price:** effort above plan is Recordly's risk. Travel and on-site days in Helsinki included
- **No licences.** Model usage runs on Kemira's own Azure subscription, with a per-team cost cap agreed in prep
- **Kemira's standard purchase agreement: no deviations.** Kemira may hire deployed consultants after 12 months **without placement or transfer fees**: accepted in full
- Payment per Kemira's standard terms, invoiced after the readout is accepted. All code and results are Kemira's property

<!-- coverage:
RFP sections: background -> slide 1; aims and goals -> slide 1; technical approach and deliverables -> slide 2; implementation plan -> slide 4; team credentials and availability -> slide 5; total pricing -> slide 6.
Hard constraints: standard purchase agreement, no deviations -> slide 1 + 6; hire consultants after 12 months without placement/transfer fees -> accepted explicitly slide 6.
Hidden: earlier pilot glossed over edge-case constraints, overpromised autonomous resolution -> slide 3 (edge-case register, seeded test set, escalation) + slide 1 stance; no side quests -> candidate workflows limited to SAP/Datasphere/SAC analytics.
Persona: lean, no recurring status meetings (slide 1, 4), real data not slides (live seed agent day 1 hour 1, slide 4), governance/access control (slide 2, row-level inherited from SAP auth, masking, logs), no new licences (slide 2, 6), price small.
Honest unknowns: model endpoint, data access, headcount (slide 4).
VDE: NO (Azure/SAP stack, advisory/event). Slides: 6.
Price: 6 x 960 + 5 x 920 + 2 x 920 = 5,760 + 4,600 + 1,840 = 12,200; 13 days; avg EUR 938/day = EUR 117/h. Days: prep AI2 DE2 Arch1; hackathon AI2 DE2 Arch1; follow-up AI2 DE1.
-->
