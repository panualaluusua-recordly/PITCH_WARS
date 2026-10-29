Buyer: elisa | Project: elisa-data-platform-architecture-and-tool-selection-as
Stack: Google Cloud ("company_cloud_vendor": "Google Cloud"); "Google Cloud, BigQuery with Cloud Composer, Looker and Power BI, alongside an ERP system"; chat tool for communication
Unknown: which ERP and its change-capture options; real freshness need per domain; source systems/volumes (network, CRM, billing?); where Composer DAG code and CI/CD live; BigQuery access model (IAM, row/column policies); Looker vs Power BI split of use; current cost; what the "recent enterprise advisory initiative" produced and whether any blueprint binds us

Triggers:
- P10 <- "real-time access to all data is required, with no batch processing or delayed refreshes permitted across our target architecture" (high)
- P4 <- "milestones were locked in before testing team alignment on a small preliminary scoping exercise" (high)
- P7 <- "existing footprint centers on Google Cloud, BigQuery with Cloud Composer, Looker and Power BI" and a "tool selection" assessment (medium: no new licences by default; selection must score existing services first)
- P3 <- "alongside an ERP system" with no detail (low-medium: unknown source, Phase 0 probes it)
- P5 (low) <- two BI tools (Looker, Power BI) over BigQuery: access must be consistent in both. Not triggered by a quote; mention as a assessment criterion only
- P6 (low) <- "oversaw the migration toward BigQuery with Cloud Composer": assessment should record where code/IaC live; no build in scope
- Not triggered: P1 (no sovereignty quote), P2, P9 (no freeze), P11 (no binding blueprint; the stalled initiative is a process failure), P12, P13 (no model/proof ask), P8 (no cost-spike quote; cost per tier is part of P10), P14, P16.

Hard constraints:
- Real-time for all data, no batch ("no batch processing or delayed refreshes permitted across our target architecture")
- Stack is GCP: BigQuery, Cloud Composer, Looker, Power BI ("existing footprint centers on Google Cloud")
- Chat tool as channel ("company_communication_channel": "a chat tool"); strict procurement ("strictly adhering to procurement protocols")
- Deliverable is a proposal with "solution approach, team capabilities and availability, implementation plan, and pricing" (assessment, no build)
(12-month recruiting clause and meeting load are commercial/process, not ours.)

Traps:
- "Real-time everything, no batch" -> Honest answer: yes-if, by latency tier. Streaming (Pub/Sub -> BigQuery Storage Write API) for event data, CDC for ERP/transactional where the ERP supports it, micro-batch for joined models, daily batch for reconciled finance. Cost and failure surface of each tier stated. Note that the RFP says the requirement applies to the "target architecture", and a strict "no batch" is also physically impossible for reconciliations/period close. Never promise a tier before the source is tested.
- Locking milestones before scoping -> small scoping sprint first, with a go/adjust/stop gate (P4, T4).
- Unknown ERP -> Phase 0 source probing (P3); do not name an ERP or a CDC product (Datastream supports specific DB engines only; SAP/Oracle ERP may need other tooling). Say "depends on ERP".
- Tool selection could tempt new platform recommendations -> default is existing services (P7); a new tool only if a tested need is unmet. No AI/ML (neither RFP nor bio asks).
- Two BI tools: do not pick a winner without usage data; score on their licences and needs.

Praised/punished before:
- P10 in fingrid: "appreciate their transparent acknowledgement regarding lakehouse latency boundaries ... aligns well with our architectural guidelines" (praised honesty about latency)
- P4/scoping in city-of-helsinki: liked "source-probing sprint" (and "avoids deploying on quicksand" per TECH_SCOPE)
- Missing diagram punished: "an architectural diagram is conspicuously absent" (aktia), "architecture diagrams are omitted" (enfuce)
- Unknown-hiding punished: aktia "sidestep hard technical migration unknowns" -> weak

VDE: NO (BigQuery + Composer, not Snowflake + dbt; advisory engagement)

Effort drivers:
- Small: no build; existing stack; one ERP; scoping sprint (source probing + freshness need per domain) is the cheapest de-risking step.
- Big: number of data domains and sources to profile; ERP change capture investigation; scoring options across Looker and Power BI; target-architecture diagram plus roadmap; cost estimate per freshness tier.
- Effort basis (technical split only, not price): sprint = ERP probe + freshness interviews + current-state sketch (largest unknown); A = baseline and requirements per domain; B = options scored (latency, cost, risk, effort); C = target architecture diagram + roadmap + risks. Ville's 4/6/7/5 split is technically plausible; B is the most variable if domain count is high.

Slide suggestion (for solution-architect): diagram columns Sources (network/event, ERP, transactional) -> Extraction (Pub/Sub, CDC where supported, Composer batch) -> BigQuery (raw/curated/marts) -> Looker / Power BI; band: code repo + CI/CD for Composer DAGs, IAM and policy tags, cost monitoring. Mark ERP CDC box as "to be confirmed in sprint".

Candidate new patterns: none (the "stalled initiative" is P4).

Left out on purpose: AI/ML, new platforms, migration/build work, Data Vault, EU sovereignty, FinOps tooling.

## Notes for deck owner (Ville)
1. Diagram missing: the draft has tier tables but no architecture diagram. Reviews (Aktia, Enfuce) mark `explanatory_visuals` down for exactly this. Add one box-and-arrow diagram of the target tiers on BigQuery/Composer/Looker/Power BI.
2. Slide 3 says "Pub/Sub into BigQuery (Storage Write API)" and "CDC replication into BigQuery": these are our proposed mechanisms, not Elisa's stated stack. Label as "proposed" (anti-pattern: naming tools the buyer did not mention as their stack). Pub/Sub is not in the RFP.
3. "Looker on live BigQuery" is fine technically, but Power BI on BigQuery cannot be assumed live: Power BI's default import mode is scheduled refresh (DirectQuery is possible with limits). Under a "no delayed refreshes" requirement this is a real point; say Power BI connectivity mode is assessed in sprint, and state it as a risk.
4. Draft says "no AI or ML, no new platform ... unless the assessment shows an existing service cannot meet a tested need": good, keep.
5. "Micro-batch (5-15 min)" and "Streaming (seconds)" are illustrative numbers before any measurement. Phrase as "target ranges confirmed in the sprint" (Oriola anti-pattern: numeric gates before measurement).
6. Missing: access control/lineage as assessment criteria (IAM, policy tags, consistency across Looker and Power BI; where Composer DAG code lives); a cost-per-tier estimate deliverable (supports P10 "cost of each tier"); the assessment should also say what happens to existing Composer pipelines.
7. Certifications (Cloud Architect, Data Engineer, PL-300) and "14 years/9 years" experience: not tech lane, but the roster must verify them (claims-auditor).
8. Honest unknown on the slide covers ERP and freshness; add the unknown ERP identity itself and BI connectivity mode.
