<!-- title: Kemira · Data Platform Phase 1 -->
# Phase 1 of your data platform: S/4HANA in Datasphere, reported in SAC, that your own engineers can read

## €36,800 fixed (excl. VAT), paid per accepted milestone. Kemira's purchase agreement, no deviations.

| | |
|---|---|
| **Strategic goal** | One harmonised, governed data foundation for Kemira's operations, starting with the data that matters most |
| **Phase 1 outcome** | 3 S/4HANA domains (assumed: production and materials, plants, sales) flowing into SAP Datasphere on Azure, 3 SAC reports on top, in 14 weeks |
| **Our stance** | Your existing Azure, S/4HANA, Datasphere and SAC only. **No new platform, no new licences** |
| **What makes it different** | **Documentation is built with the pipeline, and your new engineers prove they can change it before we leave** |
| **Your time** | A 30-minute acceptance per milestone. No recurring status meetings; updates in your chat tool |

Proposal to Rasmus Vuorinen, Director of Digital Analytics · Recordly Oy · Helsinki

---

# Solution: S/4HANA to Datasphere to SAC, every step inspectable

## Built on what you already run. Phase 2 can extend the same pattern.

| Layer | How it works | What your engineers can see |
|---|---|---|
| **Source** | S/4HANA CDS views, delta-enabled | Source-to-target mapping sheet per view |
| **Ingest** | Datasphere replication flows. Azure Data Factory only where no standard connector exists | Flow definitions in your Datasphere space, named by one convention |
| **Model** | Layered Datasphere views: raw, harmonised, reporting. Business names, owners and descriptions on every object | Datasphere lineage view plus a one-page data dictionary |
| **Report** | 3 SAC stories on the reporting layer | Each KPI traced back to its source field |
| **Control** | Plant row-level security in Datasphere data access controls, inherited by SAC | Access matrix: who sees which plant, tested per milestone |
| **Quality** | **Adaptive checks**: expected ranges per plant are recalculated from recent data, instead of a static rule catalogue to maintain. Exceptions go to a named data owner | Check results in a Datasphere view |

> **Out of scope, on purpose:** new tools, AI features, additional domains, dashboards beyond the 3. These belong to Phase 2, if you want it.

---

# What went wrong before, and our safeguard

## Past handovers left new engineers unable to inspect or adjust pipelines. We design against that from week 1.

| Past failure | Safeguard |
|---|---|
| **No transparent documentation** | Docs are written as each pipeline is built, in **your** repository and Datasphere, not a PDF at the end. A milestone is not accepted without its docs |
| **New engineers could not inspect pipelines** | Your engineers join from week 1 and co-build one pipeline end to end. Lineage, naming convention and data dictionary make every object readable without us |
| **Could not adjust after consultants left** | **Handover test:** a Kemira engineer who did not build it changes a pipeline (adds a field, end to end to SAC) using only our docs. Final acceptance depends on it |
| **Knowledge sat in consultants' heads** | Recorded walkthrough per domain (20 min each), a runbook for failures and reloads, and a "how to add a source" guide |
| **Access rules unclear** | Access matrix delivered and tested per milestone; no report ships without it |

---

# Delivery approach and timeline: 14 weeks, 4 milestones

| When | What | Gate |
|---|---|---|
| **Weeks 1-3** | Source and access inventory, naming and documentation standard. **Live demo on real plant data: one S/4HANA view replicated into Datasphere and shown in SAC** | M1: go/no-go on the approach; domain scope fixed |
| **Weeks 4-8** | Domain 1 and 2 pipelines, adaptive checks, access controls, docs and walkthroughs | M2: reconciled to S/4HANA, accepted by you |
| **Weeks 9-12** | Domain 3, 3 SAC reports, access matrix tested | M3: reports accepted by business users |
| **Weeks 13-14** | Runbooks, handover test by your engineer, buffer | M4: final acceptance |

> **Honest unknowns:** which 3 domains and how many CDS views (we assume about 8-10 in total), whether S/4HANA extraction is already enabled for Datasphere, and the access granted to plant data. Weeks 1-3 settle all three; M1 re-cuts scope if needed. If something needs a licence you do not own, we flag it, we do not buy it.

---

# Core team: three seniors, replaceable on your request

| Role | Experience and certifications | Availability |
|---|---|---|
| **SAP Datasphere architect** (lead) | 12 yrs, BW, Datasphere, SAC. SAP Certified Associate – Data Engineer – SAP Datasphere · SAP Certified Associate – Data Analyst – SAP Analytics Cloud. Finnish, English | At signature |
| **Senior data engineer** (S/4HANA, Datasphere) | 10 yrs. Microsoft Certified: Azure Data Engineer Associate · SAP Certified Associate – Data Engineer – SAP Datasphere. Finnish, English | At signature |
| **Data engineer** (SAC, quality checks) | 6 yrs. Microsoft Certified: Azure Data Engineer Associate · SAP Certified Associate – Data Analyst – SAP Analytics Cloud. Finnish, English | From week 3 |

Two of three are at signature. **Replacement of any consultant: accepted**, handover days at our cost, equal seniority.

---

# Price and terms

## Fixed total €36,800 (excl. VAT)

| Role | Days | Day rate |
|---|---|---|
| SAP Datasphere architect | 10 | €920 |
| Senior data engineer (S/4HANA, Datasphere) | 20 | €920 |
| Data engineer (SAC, quality checks) | 10 | €920 |
| **Total** | **40 days** | **€36,800** |

- **Paid per accepted milestone:** M1 20% · M2 30% · M3 30% · M4 20%
- **Kemira's purchase agreement, no contractual deviations**
- **No licences.** Everything runs on your Azure, Datasphere and SAC
- Effort above plan is Recordly's risk. Code, documentation and runbooks are Kemira's

<!-- coverage:
RFP: solution -> slide 2; delivery approach and timeline -> slide 4; core team certifications and availability -> slide 5; total commercial pricing -> slides 1+6; strategic goals -> slide 1; deliverables -> slides 2 (artifacts), 3, 4 gates, 6 (code, docs, runbooks); contract deviations -> none, slides 1+6; interview presentation: concise slides.
Hidden: past failure (no transparent docs, new engineers cannot inspect/adjust) -> slide 3 five rows incl. handover test, co-build from week 1, docs in Kemira repo; SAP S/4HANA -> Datasphere -> SAC on Azure -> slide 2.
Persona: lean, existing stack, no licences (1,2,6); live demo on real plant data weeks 1-3 (4); no status meetings (1); governance/access (2,3); adaptive checks (2); LLM reloads not in scope (none requested; no AI); honest unknowns (4); VDE: NO. Slides: 6.
Price: (10+20+10) x 920 = 36,800. Split 20/30/30/20 = 7,360 / 11,040 / 11,040 / 7,360.
-->
