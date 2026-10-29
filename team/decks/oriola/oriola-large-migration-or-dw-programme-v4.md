# Data warehouse migration to Azure, proven on your own supply chain tables first
_Oriola Oyj: Draft staffing revision - candidate evidence, scope and rates require owner confirmation_

## 2. Nine-month capacity plan; commit to the eight-week pilot first
- **Phase 1: EUR 91,500 capacity fee:** 8 weeks, 2 DEs at 100% plus architect at 60%; 104 person-days. Validate access, source risk and velocity before later phases.
- **Then decide:** phases 2-3 go ahead only if the measured velocity holds; no multi-year lock-in
- **One standard, no one-off scripts:** a metadata-driven ingestion framework for every SAP S/4HANA and wholesale interface, same pattern in every warehouse environment
- **Reliable reporting:** reconciled Gold layer feeding your BI tool, with automated data tests
- **Team:** complementary role profiles; all candidates and dates require verification; replacement on request accepted
- **Draft programme estimate EUR 477,375**; phases 2-3 require scope and effort confirmation at the pilot gate. No blanket fixed-price promise for an unprofiled estate.

## 3. One metadata-driven pipeline pattern replaces hand-crafted wholesale scripts
- Adding a wholesale or warehouse interface = **one config row + tests**, not a new script. The same template runs in every warehouse environment.
- Built only in Oriola's Azure tenant and Git; no new licences. Azure consumption estimated €2,500–4,000/month, confirmed from the pilot's measured loads.
[Sources: SAP S/4HANA (CDS views, delta extraction), Warehouse & wholesale interfaces, Legacy DW (read-only during parallel run)] → [Ingest: one template: Azure Data Factory, metadata-driven, Config per interface in Git, Row-count & sum reconciliation] → [Azure lakehouse: ADLS Gen2: raw → curated → marts, SQL models in your Azure engine, version-controlled, Lineage + batch/lot traceability] → [Reporting: Semantic model in BI tool, Row-level access mirroring SAP roles, tested before go-live, Load monitoring & alerting]
(Parallel run: legacy stays read-only until reconciled totals match on consecutive loads; rollback = repoint BI to legacy · alerts with runbooks so incidents get fixed once)

_Week 1: probe SAP, interfaces and the legacy DW, inventory undocumented logic and confirm the ≤250-table assumption. Ingestion engine per interface type (Data Factory or alternative) chosen on measured throughput._

## 4. Three gated phases with measured velocity, not a big-bang programme
| Phase | Months | Deliverables | Gate / metric |
| --- | --- | --- | --- |
| 1 Velocity pilot | 1-2 | Framework v1, 15-20 supply chain tables migrated + reconciled, velocity report | Tables/week; targets confirmed after 2 weeks of measurement on 15-20 orders, stock and delivery tables (proposed: reconciliation ≥ 99.9%, ≥ 80% of interfaces config-only), no unrecovered load failure > 4 h: go/no-go |
| 2 Core migration | 3-7 | All wholesale + warehouse domains on the framework, BI repointed | Monthly velocity report vs. plan |
| 3 Cut-over + handover | 8-9 | Parallel run, legacy switch-off, runbooks, training | Business sign-off; your team operates |

## 5. Proposed role mix, allocations and verification before commitment
- **Replacement:** you may request any consultant's replacement; equal seniority within 10 working days, 2-week overlap at our cost
- Pairing with your engineers from phase 1; workshops, runbooks and documentation in Finnish
- Written update every second week and a monthly steering; decisions logged, no extra status meetings
- You may recruit our consultants after 12 months, with no fee
| Proposed role | Role | Allocation | Required certificates | Target start |
| --- | --- | --- | --- | --- |
| Lead architect | Lead architect | 60% | Azure Solutions Architect Expert, Databricks DE Professional | At signature |
| SAP data engineer | SAP data engineer | 100% | SAP Certified Associate, Databricks DE Professional | At signature |
| Data engineer | Data engineer | 100% | Azure Data Engineer Associate | At signature |
| BI / test engineer | BI / test engineer | 50% from month 3 | Power BI Data Analyst Associate | Month 3 |

_Draft role profiles: nominate consultants and verify CVs, certificates, languages, dates and actual availability before submission. No person is booked by this draft._

## 6. Pilot EUR 91,500; later phases are estimates subject to the gate
- DE EUR 115/h; BI/analytics EUR 125/h; proposed architect EUR 125/h (owner confirmation pending).
- 7.5 h/day: architect 60%, two DEs 100%, BI 50% from month 3. Eight weeks = 40 planning workdays; later months = 20 days each.
- Only the pilot is offered as a bounded capacity fee. Later scopes and prices are re-estimated from measured velocity; no overage without written agreement.
| Phase | Draft capacity fee | Role-days |
| --- | --- | --- |
| 1 Pilot: 8 weeks | EUR 91,500 | DE 80 + architect 24 = 104 |
| 2 Core: 5 planning months | EUR 275,625 estimate | DE 200 + architect 60 + BI 50 = 310 |
| 3 Handover: 2 planning months | EUR 110,250 estimate | DE 80 + architect 24 + BI 20 = 124 |
| Programme estimate | EUR 477,375 excl. VAT | 538 person-days |

_Excludes VAT, cloud, licences and travel. Exact working calendar and consultant availability pending. Verify any reference or credential before reintroducing it. Scope and risk allowance must be agreed before binding fixed-price delivery._

## 7. Staffing review and decision before submission
- Rauno / Codex staffing review: maximum two architects respected; complementary roles included; DE/DA floors and AI premium applied to the stated role scope.
- This revision replaces the lower draft price for the same capacity. If the buyer budget is lower, reduce scoped work or hours and re-estimate; do not discount below hourly minima.
- Candidate CVs, credentials, language skills, exact dates and actual availability remain unverified. Nominate and confirm before buyer submission.
- Final fixed-price deliverables, risk allowance and the proposed non-DE rates require offer-owner review. This is not a human approval or a request to send.
