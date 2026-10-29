Buyer: veikkaus | Project: veikkaus-architecture-or-tool-assessment
Stack: "a cloud data platform with an in-house AI platform, connected to a BI tool and an ERP system on a public cloud" (RFP); bio: "company_cloud_vendor: a public cloud", "consolidation of legacy operational metrics onto a cloud data platform with an in-house AI platform"
Unknown: cloud vendor; which data platform (Snowflake/Databricks/other); what the "in-house AI platform" is and how models are trained/deployed; BI tool and ERP products; which "multi-year software commitments" hold the "substantial untapped capacity", terms and whether usage/admin logs are exportable; size/throughput of the pipelines ("high-throughput data processing"); whether Swedish matters inside the platform outputs (player reporting) or only in our deliverables; who approves access in a state-owned gaming operator and how long it takes. All are Phase 0 / week-1 work, not guesses.

Triggers:
- P7 <- "recent internal reviews highlighted substantial untapped capacity across our existing multi-year software commitments" (confidence high)
- P13 <- bio "privately demanding tangible proof over vendor promises"; "monitors task logs obsessively" (confidence high; applied as evidence per finding, measured on their logs)
- P15 <- "identify technical debt" + bio "player reporting pipelines" (lineage/inventory as part of D1/D2) (confidence medium)
- P5 <- "robust compliance, reliable governance" (access control/RLS in the target state and in our own read-only access) (confidence medium)
- P4 <- "Shortlisted vendors will participate in a two-hour interview", "prior to a final commercial evaluation round" (small, proven first step: licence baseline first) (confidence low)
- P10 <- "high-throughput data processing are paramount" (only if a target option proposes streaming; do not promise real-time) (confidence low)
- P6 <- "streamline model deployment workflows" (IaC/CI templates for model promotion as an option in D4, in their own repos) (confidence low)
- Not triggered: P1 (no sovereignty wording; do not add), P2 (no automation asked), P8, P9 (no freeze), P11, P12, P14, P16.

Hard constraints:
- Independent assessment of "our team's analytics architecture" ("We require an independent assessment") - independence of vendor, no licence sales
- Three outcomes: "identify technical debt, streamline model deployment workflows, and recommend target-state architectural patterns"
- Deck structure in order: "organizational background and aims, technical methodology and deliverables, implementation plan and timeline, proposed team credentials (including certifications and availability), detailed pricing, and any contract deviations"
- "Shortlisted vendors will participate in a two-hour interview" - technical content must survive a live walk-through
- Compliance/governance: "robust compliance, reliable governance" (state-owned gaming operator, 1,200 employees)

Traps:
- Hidden vendor assumption: certifications lists (Azure/Databricks/Snowflake/GCP) read as vendor bias for an unnamed platform -> list only what is on the roster, and state the assessment is vendor-neutral; platform stays an explicit unknown.
- "Untapped capacity" can invite recommending new tools -> baseline entitlement vs. actual use first; recommend existing capability; any new tool only as a named option with the reason existing capacity does not cover it.
- "High-throughput" is not a request for streaming -> score throughput in D4 with measured current volumes; no real-time promise.
- Access timing: read-only access "in week 1" assumes approvals that a regulated operator may not grant that fast -> keep the week-1 checklist, name fallback (exports/screenshots from their admins), say where it moves the schedule.
- Evidence depends on logs being kept -> honest answer already in draft (week-4 checkpoint); keep it.
- "Streamline model deployment" with an in-house AI platform we have not seen -> assess and measure lead time; do not propose building or replacing the platform; no AI/ML extras.
- Prior bad rollout was about "sloppy Swedish translations" -> that is mostly a language/process point; technical angle is whether localisation of player-facing report/model outputs is a pipeline step (check as a finding), not a promise to fix it.

Praised/punished before (no replies from veikkaus yet; same pattern buyers):
- P7 in kemira (won): "[met] Builds strictly on Kemira's existing SAP and Azure estate with no new platforms or licences."
- P7 in kemira: "Liked: no new licences, respects Datasphere/Azure. Disliked: side quests" -> stay inside the asked scope.
- Architecture assessment buyers (terveystalo, enfuce): review quotes "an architectural diagram is conspicuously absent" (Aktia), "architecture diagrams are omitted" (Enfuce) -> explanatory_visuals only adequate; terveystalo needs process diagrams ("Needs process diagrams", conservative proven patterns).
- Terveystalo carry-over: assessment should recommend "conservative, proven-pattern recommendations" (guess, low).

VDE: NO (advisory assessment, platform not Snowflake+dbt; no named Snowflake). Do not mention.

Effort drivers:
- Phase 1 size depends on how many "multi-year software commitments" exist and whether usage logs are exportable (days per commitment unknown).
- D2/D3 depend on number of pipelines and models and on log quality ("monitors task logs obsessively" suggests logs exist, medium confidence).
- D4 cost scales with number of options scored (2-3) and whether any option needs a throughput/compliance check.
- Access approval lead time and interviews with their team (about 2 h/week) bound the calendar, not the days.
- Cheapest levers: drop one D4 option, merge phases 3-4, sample the debt register (top-N pipelines) rather than full inventory.

Notes for deck owner (Ville):
1. No architecture diagram. T1 gap and the known explanatory_visuals penalty. Add one visual: assessment scope map (source -> cloud data platform -> in-house AI platform -> BI tool / ERP, with "where each lens (D1-D5) reads evidence" marked), clearly drawn as scope not as their confirmed architecture. Also a small model-deployment flow (train -> register -> approve -> deploy) showing where lead time is measured for D3. Use boxes labelled generically ("cloud data platform", "in-house AI platform") exactly as the RFP does.
2. Certifications are Azure/Databricks/Snowflake/GCP while the vendor is unnamed. Risk of looking vendor-leaning; fine if roster-true (already flagged), but add one line that the method is vendor-neutral and the stack is confirmed in week 1.
3. "Architecture map from configs and metadata" and "entitlement vs. usage ... from admin and usage logs" are claims about data we have not confirmed exist. Phrase as "from the admin/usage logs you have; gaps listed in week 1". The honest-unknown box covers part; tie D1 to it.
4. Compliance lens is stated but thin in the method table. Add, per finding card, the check list: access control, audit trail, lineage, player-data handling (slide 1 already lists them; D2/D3/D4 should repeat which are checked). Do not claim regulatory (gaming law) expertise beyond roster.
5. "High-throughput" is in the RFP but no deliverable measures it. Add to D1/D2: current volumes and job durations from task logs, so D4 throughput scoring has a baseline.
6. "No finding without evidence" is absolute; keep it but allow "confidence: low, evidence requested" cards so it does not fail when logs are missing.
7. Week-1 "read-only access in week 1" is a hard promise on their side; state it as a dependency with a fallback.
8. Do not claim the Swedish translation problem is technically fixed; it is a deliverable-language commitment (roster-dependent, flagged by you).
9. Wording check: "No new AI features" is good (no ML extras). Do not add GenAI/agent suggestions.
