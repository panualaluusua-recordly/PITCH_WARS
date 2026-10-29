<!-- title: Kemira · Platform migration to SAP Datasphere -->
# Two platforms into one: 12 workloads and 12 SAC reports on Datasphere in 8 months

## €55,200 fixed (excl. VAT), paid per accepted wave. Kemira's purchase agreement, no deviations.

| | |
|---|---|
| **Outcome** | 12 ELT workloads running in SAP Datasphere on Azure, 12 SAC reports repointed, old platforms switched off workload by workload |
| **Method** | A **migration factory**: one proven pattern, repeated per workload, in 3 waves |
| **Stack** | Your existing Azure and Datasphere only. **No new platform, no new licences** |
| **Your development continues** | Old and new run in parallel. Cut-over per workload, in freeze windows you set |
| **Your time** | One 30-minute acceptance per wave. No recurring status meetings; updates in your chat tool |

Proposal to Rasmus Vuorinen, Director of Digital Analytics · Recordly Oy · Helsinki

---

# Solution approach: one extraction method per source class

## You asked us to propose the extraction solution. Week 2 confirms it on your real sources.

| Source class | Extraction method (existing estate) | Check before cut-over |
|---|---|---|
| **REST APIs** | Azure Data Factory REST connector, paged and incremental, into Datasphere | Row counts and checksums vs old platform |
| **IoT event streams** | Azure Event Hubs capture to Azure storage, micro-batch into Datasphere | No gaps or duplicates per time window |
| **S/4HANA extracts** | Datasphere replication flows on CDS views, delta-enabled | Delta totals match S/4HANA |
| **Databases** | Datasphere database connections; ADF where no connector exists | Full-load and delta reconciliation |
| **LLM integration** | Same Azure model endpoint, wrapped in the safeguards on slide 3 | Replay test: zero repeated calls |

> **Migration factory:** every workload gets the same 5 steps: inventory, build from template, parallel run, reconcile, cut over. Wave 2 and 3 reuse wave 1 templates.

---

# What could go wrong, and our safeguard

| Risk in your RFP | Safeguard |
|---|---|
| **Development must continue uninterrupted** | Old workload stays live. Changes made there during the parallel run are replayed to the new one. Freeze only on cut-over day, agreed per workload |
| **LLM reload creates duplicate calls and cost** | Each call keyed by a hash of its input; result stored once, reloads read the store. A reload re-sends nothing already answered |
| **LLM cost runaway** | Hard cost cap per run and per month set by you; the run stops and alerts at the cap, never overruns |
| **Reports break or show the wrong rows** | Each SAC report repointed with the workload it uses. Old vs new numbers compared before cut-over |
| **Access rules lost in the move** | Plant row-level security and Datasphere access controls recreated and tested per wave; SAC inherits them |

---

# Delivery plan: 3 waves, each accepted before the next

| When | What | Gate |
|---|---|---|
| **Weeks 1-2** | Source inventory, extraction assessment, factory template. **Live demo: one REST workload on real plant data** | Go/no-go on methods; wave scope fixed |
| **Wave 1, months 1-3** | Assumed: 4 REST API workloads + their SAC reports | Reconciled, accepted by you |
| **Wave 2, months 3-5** | Assumed: 2 databases + 3 S/4HANA extracts + reports | Reconciled, accepted |
| **Wave 3, months 5-7** | Assumed: 2 IoT streams + LLM integration + remaining reports | Reconciled, accepted |
| **Month 8** | Buffer, runbooks, knowledge transfer, old platforms off | Handover |

> **Honest unknown:** the split of the 12 workloads by source type and any source without a standard connector are not known until week 2. The week-2 gate re-cuts the waves. If a source needs a licence you do not own, we flag it then, not buy it.

---

# Team: three seniors, replaceable on your request

| Role | Experience and certifications | Availability |
|---|---|---|
| **SAP Datasphere architect** (lead) | 12 yrs, BW, Datasphere, SAC. SAP Certified Associate – Data Engineer – SAP Datasphere · SAP Certified Associate – Data Analyst – SAP Analytics Cloud. Finnish, English | At signature |
| **Senior data engineer** (S/4HANA, databases, REST) | 10 yrs. Microsoft Certified: Azure Data Engineer Associate · SAP Certified Associate – Data Engineer – SAP Datasphere. Finnish, English | At signature |
| **Senior data engineer** (IoT, LLM integration) | 8 yrs. Microsoft Certified: Azure Data Engineer Associate · Azure AI Engineer Associate. Finnish, English | From week 3 |

Two of three are at signature, the majority you require. **Replacement of any consultant: accepted**, handover days at our cost, equal seniority.

---

# Price and terms

## Fixed total €55,200 (excl. VAT)

| Role | Days | Day rate |
|---|---|---|
| SAP Datasphere architect | 12 | €920 |
| Senior data engineer (S/4HANA, databases, REST) | 30 | €920 |
| Senior data engineer (IoT, LLM) | 18 | €920 |
| **Total** | **60 days** | **€55,200** |

- **Paid per accepted wave:** weeks 1-2 assessment 20% · wave 1 20% · wave 2 30% · wave 3 30%
- **Kemira's purchase agreement, no contractual deviations:** 60 days net, delay penalty 3% per started week up to 10%, termination with 7 days' notice
- **No licences.** LLM usage runs on your Azure subscription, under your cost cap
- Effort above plan is Recordly's risk. Code, templates and runbooks are Kemira's

<!-- coverage:
RFP: solution approach -> slides 2-3; delivery plan -> slide 4; deliverables -> slide 2 (factory templates), slide 4 gates, slide 6 (code, templates, runbooks); team certifications -> slide 5; price -> slide 1+6.
Hard constraints: 12 ELT workloads by class -> slide 2; 12 SAC reports repointed -> slides 3-4; 8 months -> slide 4 (month 8 buffer); development uninterrupted -> slide 1+3 (parallel run, replay, freeze windows per workload); supplier proposes extraction for all sources -> slide 2 + week-2 assessment slide 4; majority of team at signature -> slide 5; replacement right -> slide 5; purchase agreement 60d/3%-10%/7d -> slide 6, no deviations slide 1+6.
Hidden/traps: LLM reload idempotent, no duplicate calls, cost cap -> slide 2+3; migration factory -> slide 2; honest unknown -> slide 4.
Persona: lean, existing Azure/Datasphere, no licences (1,2,6); live demo on real plant data (week 2, slide 4); no recurring status meetings (1); governance/access control (3); tight price.
VDE: NO. Slides: 6.
Price: 12x920 + 30x920 + 18x920 = 60 x 920 = 55,200. Payment split 20/20/30/30 of total.
-->
