# Tech & architecture slides for the Oriola deck
_Oriola Oyj: Two slides for deck-writer to insert after the answer-first slide_

## 2. One metadata-driven pipeline pattern replaces hand-crafted wholesale scripts
- Adding a wholesale or warehouse interface = **one config row + tests**, not a new script. The same template runs in every warehouse environment.
- Built only in Oriola's Azure tenant and Git; no new per-user licences, only Azure consumption (Data Factory, ADLS, Databricks DBUs).
[Sources: SAP S/4HANA (CDS views, delta extraction), Warehouse & wholesale interfaces, Legacy DW (read-only during parallel run)] → [Ingest: one template: Azure Data Factory, metadata-driven, Config per interface in Git, Row-count & sum reconciliation] → [Azure lakehouse: ADLS Gen2: raw → curated → marts, Databricks SQL models, version-controlled, Unity Catalog lineage + batch/lot traceability] → [Reporting: Semantic model in BI tool, Row-level access per business unit, Load monitoring & alerting]
(CI/CD from shared templates · alerts with runbooks so incidents get fixed once, not fire-fought every week)

_Decision point in the pilot: Data Factory vs Databricks ingestion per interface type, picked on measured throughput, not preference._

## 3. A 6-week pilot on real supply chain tables sets the velocity before any multi-year commitment
- **Technical unknowns we price in:** SAP extraction throughput and authorisations; undocumented logic in the legacy DW; length of the parallel run; GDP traceability of batch/lot data.
- Each later wave is sized from the pilot's measured velocity, so the price of the rest is evidence, not a guess.
| Gate metric | Measured on Oriola's own tables | Continue if |
| --- | --- | --- |
| Velocity | Tables migrated and reconciled per week (pilot scope: ~30 tables, 2 warehouse interfaces) | Forecast for full estate fits plan ±15% |
| Correctness | Row and value reconciliation against the legacy DW for stock, order and invoice measures | 100% on financial measures |
| Template reuse | Share of interfaces onboarded with config only, no custom code | ≥ 80% |
| Stability | Failed loads per week, time to recover | No unrecovered failure > 4 h |
