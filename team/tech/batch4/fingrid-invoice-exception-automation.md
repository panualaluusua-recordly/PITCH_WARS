# Tech analysis: fingrid / fingrid-invoice-exception-automation (analysis only, no sends)

Buyer: fingrid | Project: fingrid-invoice-exception-automation
Stack: "Microsoft Dynamics 365 Finance & Supply Chain", "Databricks lakehouse with a data-mesh model on Microsoft Azure"; bio: "rollout of a Databricks lakehouse with a data-mesh model". The earlier project also named Power BI and Unity Catalog (from the v2 review, not in this RFP).
Unknown: the "two most common exception types" (which, volumes, current rules); how "meter changes" reach D365 (source of meter data, keys, owner domain); whether Databricks holds D365 data and in which mesh domain; whether resolution means write-back to D365 or only a queue/proposal; which D365 interface is allowed (OData/data entities, export, Dataverse link); existing Unity Catalog setup and monitoring tooling; duplicate/ledger quality (prior reply: "duplicate entries across Dynamics and the lakehouse remain unaddressed"); labelled history of past exceptions and resolutions; who owns data products in the billing domain; what "licensing costs" could arise (none expected on the owned stack).

## Technical asks (quoted)
- "automate detection, validation, and resolution logic on our Databricks lakehouse" -> rules/validation as code in Databricks, resolution logic per exception type.
- "initially targeting our two most common exception types" -> a narrow first slice, the two types fixed in Phase 0.
- "transparent data pipelines and reliable monitoring" -> lineage, run and quality monitoring, alerting, visible rules.
- "how business benefits and accuracy gains will be measured" -> baseline plus numeric gate on their data.
- "validates meter changes against our records in Microsoft Dynamics 365" -> reconciliation of meter-change events vs D365 master data.
- "hundreds of invoice discrepancies" each month -> low volume; scheduled batch is sufficient, streaming is not justified.
- "potential licensing costs" -> state what we need beyond owned licences (answer: none by default).

## Hidden tech preferences (bio and prior replies)
- "strict process compliance over unproven modernization" -> deterministic rules, documented procedure, no AI/ML extras (none asked; do not suggest).
- Prior reply: "maintaining strict control over data integrity was essential ... duplicate entries across Dynamics and the lakehouse remain unaddressed leaves me uneasy" -> data foundation first.
- Prior reply: "transparent acknowledgement regarding lakehouse latency boundaries ... aligns well with our architectural guidelines" -> honesty about limits is rewarded.
- Verdict met: "solutions build on existing D365, Databricks, and Power BI with no new licenses required"; "native Finnish language ... delivery team and all documentation".
- Verdict not addressed: "does not present AI acceleration figures"; "no mention of AI governance policies" -> if AI use in delivery is mentioned, state governance (human approval); do not add AI features.
- Verdict against: "omits a dedicated, named project manager" -> delivery-role gap; the plan and gates should show who owns each gate (roles only here).
- "rigidly keeping external consulting spend in check" -> small slice, existing tooling, effort visible per phase.

## Triggered patterns
- P3 Data foundation first <- "reconciles hundreds of invoice discrepancies", "validates meter changes against our records"; fingrid reply "duplicate entries ... remain unaddressed" (confidence high). Phase 0: profile the two exception types, match D365 vs lakehouse records, go/no-go gate.
- P12 Modelling fit <- "Databricks lakehouse with a data-mesh model" (high). Exception handling as a data product in the billing domain with a data contract; no central bottleneck.
- P7 Use what they own <- "Databricks lakehouse", "Microsoft Dynamics 365", prior "no new licenses required" (high). Delta tables, Workflows, Unity Catalog, Databricks SQL alerts, Power BI if needed; "potential licensing costs" answered as none new.
- P13 Proof on their data <- "how business benefits and accuracy gains will be measured" (high). Baseline from historical exceptions, precision/recall on a labelled sample, numeric gate.
- P4 Small blast radius <- "initially targeting our two most common exception types" (high). Two types, then expand.
- P2 Human gate on automation <- "resolution logic" plus "strict process compliance" (medium). Auto-resolve only rule-certain cases; the rest to a review queue; every action logged and reversible; kill switch. Matches Enfuce (won): "deterministic rule-based matching with an audit table and reversible merges".
- P15 Findability <- "transparent data pipelines" (medium). Catalog entries, Unity Catalog lineage, rule book as deliverable.
- P6 Code in client tenant + IaC <- "on our Databricks lakehouse" (medium). Repos and workspace theirs, asset bundles/Terraform, no vendor environment.
- P16 Resilience <- "reliable monitoring" (low-medium). Alerts on failed runs, replay of a run, quarantine for unparseable records, SLOs as acceptance.
- P5 Access inherited <- finance/billing data in D365 (low; not stated). Mirror D365 roles and Unity Catalog permissions.
- P8 Cost guardrails <- "rigidly keeping external consulting spend in check" (low). Job-cluster budgets and cost per run reported.
- P10 Honest latency: NOT triggered (no real-time ask). Say plainly that scheduled batch fits hundreds a month.
- P1, P9, P11, P14: no trigger.

## Hard constraints
- Platform: "Microsoft Azure", "Databricks lakehouse with a data-mesh model", "Microsoft Dynamics 365 Finance & Supply Chain": build only there.
- Scope: "initially targeting our two most common exception types".
- "transparent data pipelines and reliable monitoring": observability is an acceptance criterion.
- "at least two client references from comparable projects": only verified cases from reference-bank; no invention.
- "Shortlisted vendors will be invited to present": the technical walkthrough must stand on the slides.
- No freeze, region or security gate stated: unknown, ask.

## Traps and honest answers
- "automate ... resolution" read as full autonomy -> Auto-resolve only deterministic, rule-certain cases with audit table and reversal; ambiguous cases to a human queue. Auto-resolved share is measured, not promised.
- Building on unreconciled D365 vs lakehouse data (what she objected to before) -> Phase 0 audit of ledger/meter records and duplicates before any rule is automated; the gate sets scope.
- Write-back into D365 assumed -> Route unknown (data entities/OData, import journals, or proposals only). Default: proposals/queue first, write-back after the gate and with D365 owner approval; no direct database writes.
- "Two most common types" not named -> Phase 0 picks them from data (frequency and manual effort) with the billing team; do not guess types in the deck.
- Accuracy claims without a baseline -> Measure the current manual rate and time on a historical sample; agree the numeric gate in Phase 0; no invented number in the deck.
- Real-time reflex from the previous RFP -> Volume is hundreds per month; scheduled batch is right, justify it; do not promise real-time.
- Data-mesh conflict (our pipeline vs domain ownership) -> deliver as a data product with a contract and a named owner role in the billing domain; no central bottleneck.
- AI/ML or LLM matching as an extra -> not asked; excluded; rules first (Aktia lost on extras).
- "Potential licensing costs" -> no new licences on the owned stack; state any compute consumption as an estimate flagged unknown.
- Missing delivery governance role (verdict "against") -> show gate owners and a delivery-lead role on the plan slide; hand to the storyline owner.
- Meter data may come from outside D365 (metering system) -> source inventory in Phase 0; do not claim integration we have not seen.

## Praised/punished before
- P10 in fingrid: "transparent acknowledgement regarding lakehouse latency boundaries ... aligns well with our architectural guidelines".
- P3 in fingrid (punished when skipped): "proceeding straight into automated reporting deliverables while our underlying ledger records and duplicate entries ... remain unaddressed leaves me uneasy".
- P3 in fingrid (credited after fix): "Slide 4 establishes Phase 0 to match records and eliminate duplicates before any reporting build begins."
- P3 honesty in fingrid: "Slide 3 explicitly flags the unknown volume of ledger duplicates and sets a gating decision point."
- P7 in fingrid: "solutions build on existing D365, Databricks, and Power BI with no new licenses required."
- Visuals in fingrid: "Structured tables across slides 2 through 6 organize compliance, latency architecture, and pricing"; missing diagrams were punished at aktia and enfuce.
- P2 in enfuce (won): "deterministic rule-based matching with an audit table and reversible merges" (via team/tech/batch3/alko.md).

## VDE: NO
Stack gate: Databricks on Azure with D365, not Snowflake + dbt ("Other platforms ... Azure-only ... don't offer the VDE"). Two exception types and hundreds of items a month is also not 3+ months of ongoing build work. Mention only if the buyer asks how we use AI.

## Effort drivers
- Larger: unknown D365 interface and write-back route; quality of the meter-change source and duplicate level; rule count and edge cases per exception type; availability of labelled history for the baseline; access and approval cycles in a compliance-strict client; state of Unity Catalog and monitoring.
- Smaller: only two types; hundreds of records a month (no scale engineering); existing Databricks, no new tools; scheduled batch; review queue can be a Power BI or Databricks SQL view.
- Decision points: Phase 0 gate (data quality, chosen types), pilot gate (accuracy on their data), then expansion.

## What the architecture slide must show
1. Left to right: D365 F&SCM (invoices, meter master) and the meter-change source (unknown, dashed) -> ingestion into the existing Databricks lakehouse (domain tables, labelled "their workspace") -> detection and validation rules (versioned code) -> split: auto-resolve (rule-certain) / human review queue -> resolution back to D365 via an approved interface (route marked "Phase 0 decision") plus audit table.
2. Governance band: Unity Catalog lineage and permissions, data contract for the billing-domain data product, catalog entries.
3. Monitoring band: run status, data-quality checks, alerts, exception counts and accuracy KPI against baseline, in Power BI or Databricks SQL (owned tools only).
4. Cadence label: scheduled batch (hourly or daily), with one line on why not streaming for hundreds a month.
5. Gates on the diagram: Phase 0 audit gate; accuracy gate; human approval and kill switch. Unknowns shown as dashed boxes.
6. Footer: "no new licences; code and IaC in Fingrid repos and Azure tenant".
Gates/risks slide: D365 vs lakehouse reconciliation, write-back route, exception types, baseline, access approvals, change control in a compliance-strict process.
