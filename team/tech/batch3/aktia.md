# Tech analysis: aktia | project aktia-ticket-to-merge-request-developer-or-analytics-a

Buyer: aktia | Project: aktia-ticket-to-merge-request-developer-or-analytics-a
Stack: "our current data setup, a public cloud environment, and interfacing with Temenos Transact" (RFP); bio: "a public cloud", "a chat tool" (company_cloud_vendor / communication channel)
Unknown: cloud vendor; warehouse/transformation tool (Snowflake? dbt?); ticket system; Git host and CI; BI tool; whether branch protection/CODEOWNERS are available; which AI model hosting the regulator accepts; ticket volume and quality; whether Temenos-derived data in dev needs masking

## Triggers
- P2 <- "an automated maintenance script that bypassed peer review and altered schema dependencies" (high)
- P1 <- "scrutinized exposure to foreign-headquartered AI API dependencies" (high)
- P6 <- earlier Aktia reply: "leaving our pipelines and development workflows sitting inside vendor-managed environments while merely handing our team guest access leaves our operational perimeter far too exposed" (high; same buyer, still applies)
- P13 <- "concrete AI implementation case examples with measurable results" (medium: baseline on their tickets, numeric gate)
- P4 <- "ongoing operations" to be priced while the stack is unknown (medium: pilot of 2-3 ticket types, gate before run mode)
- P15 <- agent-written transformations need documentation/lineage visible to reviewers (low; no quote asks for it)
- P8 <- low; RFP silent on cost, only the draft mentions AI credits
- Not triggered: P3, P5, P7, P9, P10, P11, P12, P14, P16

## Hard constraints
- "strictly satisfy FIN-FSA, EBA, and DORA regulatory frameworks for AI governance and operational resilience"
- No unreviewed change path ("bypassed peer review and altered schema dependencies")
- No foreign-HQ AI API dependency exposure ("foreign-headquartered AI API dependencies")
- Everything in Aktia's perimeter (earlier review, [met]): "all code, pipelines, and CI/CD live strictly inside Aktia's cloud perimeter and repositories"
- Temenos read-only, no core changes (v5 review: "strictly read-only with no core changes")
- Scope fence, no ML extras: "predictive modeling bells and whistles is precisely what sank this proposal"
- Required deck contents: "supplier profile, financial standing, and any subcontractors; technical solution architecture and compliance posture; concrete AI implementation case examples with measurable results" (non-tech parts belong to other owners)

## Traps
- "Agent" implies autonomy -> agent proposes, a named Aktia reviewer merges; no auto-merge; no change requests from chat; it stops when stuck.
- "Foreign-HQ AI API" is not solved by "EU region": a US-HQ hosted model service is still foreign-HQ -> list model-hosting options with the residual exposure of each (open-weight model in Aktia's own cloud tenant, EU-HQ provider, hyperscaler EU region), make the choice an Aktia compliance decision in Definition, keep a model abstraction layer and exit path.
- Agent touching Temenos or production -> the agent never connects to Temenos or production; it works on the extracted analytics layer in a dev environment (masked or sampled data where needed); production deploy only through Aktia's merge pipeline.
- Schema-dependency changes (the post-mortem) -> protected paths (CODEOWNERS): any change touching schema dependencies also needs the data owner; the agent has no rights to alter schemas outside a PR pipeline.
- Ticket text is untrusted input (vague tickets, prompt injection) -> start with 2-3 ticket types, unclear tickets go back with questions, agent permissions limited so the worst case is a bad PR a person rejects.
- Ongoing operations with unknown stack -> run mode is conditional on the Definition gate and pilot numbers.
- ML-flavoured additions (anomaly detection, prediction, auto-triage) -> out of scope; the only AI is the ticket-to-PR agent the RFP asks for.
- Recordly case results are not Aktia's -> baseline on Aktia's tickets in Definition before any promise.

## Praised/punished before
- P6 in aktia: "leaving our pipelines and development workflows sitting inside vendor-managed environments ... far too exposed" (punished); later "[met] ... all code, pipelines, and CI/CD live strictly inside Aktia's cloud perimeter and repositories" (praised)
- ML extras in aktia: "indulging in predictive modeling bells and whistles is precisely what sank this proposal" (punished)
- Unknowns in aktia: honest_unknowns weak, "sidestep hard technical migration unknowns and failure risks" (punished: name failure risks, not only gates)
- Diagram in aktia/enfuce: "architectural diagram is conspicuously absent" (punished, per TECH_SCOPE T1); v1 has one
- P1 and P2 in terveystalo: EU-only and human gate praised (patterns.md, no fresh quote read); kemira/sanoma/lahitapiola: no verdict yet

## VDE: INCLUDE-RUN (conditional on stack confirmation)
Stack: unknown, "our current data setup, a public cloud environment" (no Snowflake/dbt named). vde-check stack gate: do not offer as a running product on other stacks, so conditional. Work gate passes (ticket -> code/tests/PR; run phase >= 3 months). Buyer gate: plus = agent pilot, written-update culture; minus = unvetted-code incident (human approval is the headline, OK) and the ML-extras punishment (the RFP itself asks for the agent). Price math is not mine. Caveat: note 1 below.

## Effort drivers
- Stack match: Snowflake+dbt = deployment; anything else = the agent is a new build (swings Delivery most)
- Model-hosting decision and its acceptability to the supervisor (largest unknown, possible blocker)
- Conventions, "perfect examples", architect time (vde-check: setup 8-10 architect days, then 2-3 per month)
- Number and variety of pilot ticket types (2-3 keeps it small), ticket quality
- Branch protection, CODEOWNERS, audit-log integration in Aktia's Git/CI
- DORA/FIN-FSA control mapping (Aktia compliance signs off)

## Notes for deck owner (Ville)
1. VDE vs "no external APIs" conflict. vde-facts: the VDE "runs inside the customer's own Snowflake account and uses the customer's Snowflake AI credits ... alongside Cortex Code". Slide 4 says models are "served in your own tenant in an EU region, no ticket text, code or data to external APIs". If Aktia runs Snowflake, Cortex models are served by Snowflake (US-HQ), possibly third-party models: exactly the "foreign-headquartered AI API" exposure. Do not claim "no external APIs" on the Snowflake route unless confirmed. Reword to options with residual exposure, decided with Aktia compliance, with exit path. Slide 3 ("model calls stay in Aktia's tenant") and slide 7 ("AI credits ... billed by Snowflake") should be reconciled.
2. "If it is not Snowflake + dbt, we adapt the same guardrails to your stack" over-claims; vde-check: do not offer as if it runs there today. Say plainly that on another stack the agent is a new build, scope and the run-mode term are re-agreed at the gate.
3. Slide 3 "Temenos Transact is read for reporting data only": safer that the agent has no connection to Temenos or production, only the analytics layer in dev. The agent is a code writer, not an extractor.
4. Effort basis: v1 has architect 5 d + 8 d; ongoing 1 d/month. The 1 d/month matches vde-facts run mode, but during the pilot PR review and guidance is 2-3 d/month. Check that the pilot review load is covered.
5. Missing failure risks (last review: honest_unknowns weak). Add a short risk table: plausible-but-wrong PR and review fatigue/rubber-stamping, prompt injection via ticket text, flaky tests giving false green, model or provider change/drift, agent stuck loops (stops by design), model hosting not accepted by supervisor, ticket system without API or webhook.
6. The post-mortem is about bypassed review: state that the required reviewer is a person other than the ticket requester, CODEOWNERS on schema-dependency paths, and that reviewer load is measured in the baseline (already a Definition metric).
7. Ticket system, Git host and chat tool are unnamed (bio: "a chat tool"); keep generic but add "integrations confirmed week 1" to Definition. Chat is answers only, changes only from tickets (already said).
8. Case examples match vde-facts. But "~30 Snowflake credits per migrated table" is a Matillion+Redshift migration case, not a ticket-to-PR cost; do not let it read as cost per ticket.
9. Auditor agent: say where logs live (Aktia's own log store, retention agreed with compliance for DORA).
10. Keep the scope fence; nothing ML in v1, good. Optional one line: docs/lineage for agent-written models (P15, low).
