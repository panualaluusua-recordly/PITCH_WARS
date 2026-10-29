# Tech analysis: terveystalo | terveystalo-analytics-engineer-for-6-months

Buyer: terveystalo | Project: terveystalo-analytics-engineer-for-6-months (analysis only; earlier two projects lost)
Stack: "Databricks" (bio: "steered the rollout of Databricks across operational units"), "a public cloud" (vendor unnamed), "an ERP system", "a BI tool" (unnamed), "a chat tool"
Unknown: cloud vendor; ERP product and interface type (API, files, DB views; "data flows connecting to an ERP system", direction unclear); BI tool and semantic layer; Unity Catalog / workspace layout / medallion status; orchestration; CI/CD and repo host; IaC; what "all operational data sources" are (count, owners, clinical vs non-clinical); existing models and naming standards; data quality tooling; environments and whether non-patient or synthetic data exists for dev; split between external and internal developers; who reviews and merges.

## Technical asks (quotes)
- "develop scalable data pipelines and data models in Databricks to serve reporting in a BI tool and data flows connecting to an ERP system"
- "must propose an end-to-end data extraction solution covering all operational data sources"
- "recommended technical approach, project phases, consultant CVs" (staffing-style: one analytics engineer embedded in the "central Data & Analytics function in Helsinki", "six-month engagement")

## Triggers
- P3 Data foundation first <- "covering all operational data sources" (sources unnamed, feasibility unknown) (high)
- P4 Small blast radius <- "treating broad scoping wish-lists as rigid mandates" and "all operational data sources" (source waves, not all at once) (high)
- P7 Use what they own <- bio "rollout of Databricks"; earlier praise for "no new tools will be added besides Databricks inside our tenant" (high)
- P6 Code in client tenant + IaC <- bio "cautious continuity"; embedded consultant, work must live in their repos (medium)
- P12 Modelling fit <- "data models in Databricks to serve reporting" (staging/marts vs history; no DV named) (medium; do not push Data Vault, bio wants "rigid legacy reporting principles")
- P5 Access inherited <- healthcare data served to BI (Unity Catalog/RLS mirrored from source roles) (medium, inferred)
- P2 Human gate <- earlier RFP "unvetted logic into clinical reporting pipelines ... bypassed engineer inspection"; praised earlier. Applies as review-before-merge on pipeline changes, no AI agent needed here (medium)
- P1 EU sovereignty <- earlier reply "EU-only processing" met (low-medium; not in this RFP text; one line, EU region)
- P13 Proof on their data <- earlier "at least 40% measured time reduction" gate met; here use a first-source slice with acceptance checks (low)
- P15 Findability <- not asked; lineage and dictionary only as handover item (low)
- Not triggered: P8, P9, P10, P11, P14, P16.

## Hard constraints
- Location: Helsinki, central D&A function ("in Helsinki")
- Platform: Databricks on a public cloud; no new platforms (prior praise for no new tools)
- Duration: "six-month engagement"
- Finnish working language: earlier "all-native-Finnish delivery team, workshops, and documentation in Finnish" met; English "pointless friction" (documentation and pipeline comments in Finnish)
- Clinical data safety: earlier "non-patient data only"; dev on synthetic/anonymised data "not addressed" last time, marked down
- Deliverables: "at least two client references", "consultant CVs" (tech slide must be consistent with them)

## Traps -> honest answer
- "end-to-end data extraction solution covering all operational data sources" vs "treating broad scoping wish-lists as rigid mandates rather than interrogating whether every source was actually feasible or necessary" (the RFP contradicts itself on purpose) -> Do not promise all sources. Phase 0: source inventory, feasibility and necessity triage per source (owner, access, volume, refresh need, report that needs it), written go/no-go and a drop list; then extract in waves by value. One generic ingestion pattern in their tenant so each added source is configuration, not a bespoke pipeline. Name in/out sources after Phase 0, not before.
- One analytics engineer cannot build "all" sources, models and ERP flows in six months -> wave plan with the source count as a hypothesis, fixed at the Phase 0 gate.
- "data flows connecting to an ERP system", ERP and direction unknown -> assume read-side extraction first; any write-back to ERP is a separate decision with a sandbox; ERP documentation quality was an open question in the earlier deck.
- Clinical reporting correctness: earlier automation "quietly pushed unvetted logic into clinical reporting pipelines" -> pull request with named senior reviewer on every change, no direct prod deploy, tests and reconciliation counts against the legacy report before cut-over. No AI-generated-code claims.
- Dev data: earlier mark-down for no synthetic/anonymised data -> dev/test on masked or synthetic data in their tenant; prod only through their role model; whether masked data exists is a Phase 0 item.
- Drift from "analytics engineer" into AI/agents, re-platforming or Data Vault -> anti-pattern (side quests). No AI, no new tools.
- "scalable" with no figures -> volumes unknown; give throughput assumptions as Phase 0 measurements, not claims.
- Patient-facing conversational AI (bio: "digital appointment assistant") sank deal 1 as "conspicuously absent" -> not asked here; mention only as interface awareness (its data, if it lands in Databricks, is one candidate source). Low confidence.

## Praised / punished before
- P7 + P2 in terveystalo (deal 1, met): "no new tools will be added besides Databricks inside our tenant."; "branch protection requiring named senior engineer approval on every single pull request without auto-merges."
- P1 in terveystalo: "test environments with non-patient data only and EU-only processing."
- P13 in terveystalo: "firm gate requiring at least 40% measured time reduction." (met)
- Language: first feedback "relying on English for delivery and documentation introduces pointless friction"; later Finnish delivery and documentation met.
- Visuals: "relies on text cards rather than process diagrams" (adequate); deal 2 "visuaalisia arkkitehtuurikaavioita ei ole" (no architecture diagrams). A diagram is expected.
- Deal 2 punished: "ei mainita lainkaan synteettisen tai anonymisoidun datan hyödyntämistä kehityksessä" (no synthetic/anonymised data in dev); "ilman kevyttä aloitusauditoinnin vaihetta" (whole scope at once, no light start-audit phase) -> Phase 0 wanted; "viikoittaisina hands-on-tarkistuspisteinä" (weekly hands-on checkpoints) and "asynkronisen viestinnän" (asynchronous communication) preferred over two-weekly status reviews; split between external partner and internal development "ei sanota mitään" (not addressed) -> state who does what with their team.
- Deal 1 first feedback: "felt inconsistent and distinctly unfinished" -> tech slides must be internally consistent.
- Same-pattern wins (pattern status only): P3 at helsinki and enfuce; P7 at kemira.

## VDE
NO. Databricks, not Snowflake + dbt.

## Effort drivers
- Number of sources actually in scope after triage (dominant, unknown).
- ERP interface type, direction and documentation quality.
- Existing Databricks maturity (Unity Catalog, medallion layers, CI/CD) vs greenfield conventions.
- Reconciliation to legacy reporting before cut-over (clinical correctness); number of reports touched.
- Availability of masked/synthetic dev data; access approvals in a healthcare tenant.
- Finnish documentation and handover to the internal team.
- Single-engineer cadence: weekly hands-on checkpoints, asynchronous chat updates.

## Architecture slide must show
1. Left to right: sources (ERP, operational systems, "N unknown, triaged in Phase 0") -> one generic extraction pattern in their Databricks tenant -> their existing layers (bronze/silver/gold, confirm) -> BI semantic layer; ERP arrow marked read-first, write-back "decision at gate".
2. Source-triage funnel: inventoried -> feasible -> necessary -> built in waves, with a visible drop list.
3. Boundaries: inside client tenant, EU region, no new tools; dev on masked/synthetic data; prod via their access roles.
4. Control points: pull request with named senior reviewer, tests and row-count reconciliation to the legacy report, no auto-merge.
5. Phase gates: Phase 0 light audit and go/no-go, Wave 1, later waves, handover (Finnish docs, lineage and dictionary).
6. Unknowns table beside it: cloud vendor, ERP, BI tool, source list, orchestration, dev data, review owners; each with its Phase 0 action.
Diagram required; Finnish labels preferred.
