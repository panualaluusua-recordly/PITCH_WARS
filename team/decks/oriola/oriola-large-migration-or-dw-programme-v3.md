# Data warehouse migration to Azure, proven on your own supply chain tables first
_Oriola Oyj: Recordly proposal | Pharmaceutical wholesale and distribution, Espoo_

## 2. We migrate your DW to Azure in 9 months for €168,000, and prove velocity in 8 weeks first
- **Phase 1 (8 weeks, €38,000 fixed):** migrate real supply chain tables (orders, stock, deliveries) end to end and publish measured velocity: tables per week, defects, reconciliation rate
- **Then decide:** phases 2-3 go ahead only if the measured velocity holds; no multi-year lock-in
- **One standard, no one-off scripts:** a metadata-driven ingestion framework for every SAP S/4HANA and wholesale interface, same pattern in every warehouse environment
- **Reliable reporting:** reconciled Gold layer feeding your BI tool, with automated data tests
- **Team:** 3 of 4 named consultants to be confirmed in writing at signature; replacement on request accepted
- **Total €168,000** (phase 1 €38k + phase 2 €86k + phase 3 €44k)

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

## 5. A proposed team, 3 of 4 confirmed in writing at signature, working side by side with your engineers
- **Reference 1:** Finnish wholesale distributor, SAP ECC → Azure lakehouse, 300 tables in 7 months
- **Reference 2:** Nordic healthcare logistics company, legacy SQL Server DW → Azure Databricks with automated reconciliation
- **Replacement:** you may request any consultant's replacement; equal seniority within 10 working days, 2-week overlap at our cost
- Pairing with your engineers from phase 1; workshops, runbooks and documentation in Finnish
- Written update every second week and a monthly steering; decisions logged, no extra status meetings
- You may recruit our consultants after 12 months, with no fee
| Name | Role | Allocation | Certifications | Available |
| --- | --- | --- | --- | --- |
| Antti Koskinen | Lead architect | 60% | Azure Solutions Architect Expert, Databricks DE Professional | At signature |
| Mikko Laine | SAP data engineer | 100% | SAP Certified Associate, Databricks DE Professional | At signature |
| Riikka Salo | Data engineer | 100% | Azure Data Engineer Associate | At signature |
| Ville Nieminen | BI / test engineer | 50% from month 3 | Power BI Data Analyst Associate | Month 3 |

## 6. €168,000 total, paid per accepted milestone, with clear assumptions
- **Licensing:** no Recordly or third-party licences; Azure and BI licences billed to Oriola directly
- **Contract:** your standard terms accepted; you may stop after any gate and pay only accepted phases
- **Risks / assumptions:** up to 250 source tables; undocumented legacy logic is the main risk, measured in phase 1 and re-priced at the gate if needed
- No overage without your written approval; hours reported weekly in your own tool
- Effort basis: phase 1 ≈ 75 person-days; phases 2-3 sized from measured velocity at the gate
| Phase | Price | Payment |
| --- | --- | --- |
| 1 Velocity pilot (fixed) | €38,000 | On gate acceptance |
| 2 Core migration (capped) | €86,000 | Monthly, on velocity report |
| 3 Cut-over + handover (fixed) | €44,000 | On business sign-off |
| **Total** | **€168,000** (VAT 0%) | 30 days net |
