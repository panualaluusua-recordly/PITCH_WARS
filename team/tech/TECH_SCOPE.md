# Tech & architecture: what we own in every offer

Source: all 36 open RFPs and buyer bios (2026-10-29), plus every buyer reply and review received so far
(13 buyers). Evidence is quoted. This is the brief for the tech/architecture agent organisation.

## 1. Our responsibility (and what is not ours)

**Ours (tech/architecture):**

| # | Responsibility | Why (evidence) |
| --- | --- | --- |
| T1 | **Target architecture on the buyer's own stack**, with a real diagram: sources → extraction → storage/model → serving/BI, where code and CI/CD live, where access control sits | Reviews: "an architectural diagram is conspicuously absent" (Aktia), "architecture diagrams are omitted" (Enfuce) → `explanatory_visuals` only *adequate*. Outokumpu: "glossy stock graphics … obscured basic data lineage" |
| T2 | **Technical answer to every hidden tech preference** (the "past problem" sentences, see §3) | About half of each review's `preferences` are tech; `project_fit` is the rating we move |
| T3 | **Trap handling**: unrealistic or risky asks get an honest technical answer | Fingrid praised the "transparent acknowledgement regarding lakehouse latency boundaries" |
| T4 | **Tech phase gates and the de-risking first step** (source probing, pilot slice, proof on their data) | Helsinki: "source-probing sprint… avoids deploying on quicksand"; Ponsse, Posti, Fingrid, Lähitapiola all objected to going full-scope before the data is known |
| T5 | **Technical risks & assumptions** (feeds `honest_unknowns`) | Aktia: "sidestep hard technical migration unknowns" → *weak*; Enfuce/Terveystalo risk tables → *strong* |
| T6 | **Requirement/compliance matrices** where the RFP demands them (Yes / Yes but not included / Yes if; numbered matrices; extraction per source) | Fingrid, Kela; Kela, Pirha, VR: "the supplier shall propose the extraction solution for all sources" |
| T7 | **Effort basis for the price** (work breakdown, the size of each phase); not the price itself | Price is the #1 reason for rejection; a smaller, phased technical scope is how price comes down without cutting rates |
| T8 | **Feedback mining on tech**: what tech choices were praised or punished → pattern library | Learning loop (§5) |

**Not ours:** final price and commercial terms, contract acceptance, team CVs and language commitments, storyline
and visual style. These belong to buyer-analyst, deck-writer, the price owner and the humans. We hand those owners
slides and inputs.

## 2. Engagement archetypes in the current RFPs

| Archetype | Buyers (open project) | What tech brings |
| --- | --- | --- |
| Architecture / tool assessment, readiness, roadmap | elisa, yliopiston-apteekki, veikkaus, enfuce (arch assessment), terveystalo (arch assessment), atria, kesko, lahitapiola, mandatum (AI Act governance) | Assessment method, scoring criteria, small scoping pilot first, use existing licences, concrete target-state options |
| Platform build / DW migration / reporting | fennia, oriola, city-of-helsinki (SME), helen, fingrid, ponsse, alko, tokmanni, vahterus | Architecture diagram, phased migration with a pilot slice, IaC templates, lineage/catalog, access model |
| Streaming / real-time | posti, (fingrid, elisa as traps) | Latency tiers, blast radius (one hub first), chaos/failover tests |
| ML / MLOps / forecasting | alma-media, varma, upm, metsa-group, pirha, valio | Reusable MLOps template, proof on real data, buy-vs-build, human decision on predictions |
| GenAI / agents | aktia (ticket→MR agent), sanoma (backlog agent), kemira (agentic hackathon), oulun-energia (RAG) | Human-in-the-loop by design, evals on edge cases, EU-hosted models, cost caps |
| FinOps | kela, savings-banks-group | Tagging/resource register, extraction of cost data, guardrails, no unvetted tools |
| Staffing (tech profile matters) | outokumpu, valmet, vr-group, s-group, upm | Concrete first-30-days technical plan, the specialist's stack fit |

## 3. Recurring tech preferences (our pattern library seeds)

Each row is a pattern the architect applies whenever the trigger appears.

| Pattern | Trigger in RFP/bio | Seen in | Our standard answer |
| --- | --- | --- | --- |
| **P1 EU sovereignty** | "foreign-headquartered AI API", "single-origin offshore cloud APIs", "non-European AI toolchains", "extraterritorial jurisdiction" | aktia, lahitapiola, savings-banks, valmet, terveystalo (EU-only praised) | EU-region processing, model access behind an abstraction layer, EU/open-weight fallback, documented exit plan, no data leaves tenant |
| **P2 Human gate on automation** | script/PR "bypassed peer review", "overpromised autonomous", "zero defects" demos, automated maintenance/claims decisions | aktia, terveystalo (praised), sanoma, kemira, pirha, lahitapiola | Agent proposes, human merges: branch protection, CODEOWNERS, no auto-merge, eval set of edge cases, kill switch; models advise, people decide |
| **P3 Data foundation first** | unknown or messy sources, duplicates, discrepancies | helsinki (won), fingrid, lahitapiola, ponsse, alko, enfuce (won) | Phase 0: profile and reconcile sources, a risk report and a go/no-go gate before building features |
| **P4 Small blast radius** | "entire operation right away", multi-year commitments | posti, oriola, kesko, ponsse, elisa | Pilot slice (one hub, one domain, N jobs), measured velocity, then scale |
| **P5 Access inherited, not reinvented** | leaked margins via default permissions, RLS before deployment | alma-media, kemira (won), tokmanni, yliopiston-apteekki | Mirror the source/role permissions (SAP auth, RLS, Unity Catalog), test access before go-live |
| **P6 Code in client tenant + IaC** | vendor-managed environments, hand-crafted one-off scripts, isolated deployment scripts | aktia, enfuce (won: Terraform templates), oriola, varma, upm | Everything in the client's repos and cloud; Terraform/CI templates; one reusable pattern, no bespoke pipelines |
| **P7 Use what they own** | mature commercial packages exist, untapped licence capacity, no new licences | metsa-group, veikkaus, kemira (won), terveystalo | Buy-vs-build check, exploit existing licences, zero new tools by default |
| **P8 Cost guardrails** | billing spikes from vector refresh, open billing drift, FinOps | oulun-energia, upm, kela, savings-banks | Budgets + alerts, capped refresh schedules, cost per use case reported |
| **P9 Respect freezes** | no production changes in Q1 | vahterus, vr-group, oulun-energia | Plan cut-overs outside the freeze; build and test in Q1, deploy after |
| **P10 Honest latency** | "real-time access to all data, no batch" | elisa, fingrid (praised) | Latency tiers: streaming where it pays, micro-batch elsewhere; cost of each tier |
| **P11 Binding prior design** | earlier vendor's blueprints are binding | fennia, helen (praised), valio | Implement as designed; log deviations as change requests, never redesign |
| **P12 Modelling fit** | Data Vault, data mesh, staging→marts | enfuce (won: DV hubs/links/sats; domain ownership), fennia, vr-group, fingrid | Data Vault for volatile history, domain ownership with data contracts, no single central bottleneck |
| **P13 Proof on their data** | decks hid whether models work, static slides, hypothetical efficiencies | alma-media, kemira, terveystalo (won pref: 40% gate), oriola, tokmanni | Proof of value on their tables with a baseline and a numeric gate |
| **P14 Edge/bandwidth** | satellite links saturated by raw telemetry | valmet | Aggregate/compress at the edge, push summaries, backfill off-peak |
| **P15 Findability** | "how will anyone find these pipeline outputs" | helsinki (won) | Catalog, data dictionary, lineage, naming conventions as deliverables |
| **P16 Resilience testing** | "no platform hiccup halts parcel tracking" | posti (praised chaos testing) | Failure-injection tests, replay, DLQ, SLOs as acceptance gates |

**Anti-patterns that lost or were marked down:** ML/AI extras outside scope (Aktia lost); side quests beyond
the asked scope (Kemira hint); rigid staging→marts for mutating events (Enfuce); full-scope day one (Ponsse,
Posti); autonomous triggers in critical operations (Pirha); late onboarding/mobilisation (Alma, Helen).

## 4. Per-buyer tech hooks (open projects)

| Buyer | Key tech hooks (pattern ids) | Trap / honest answer |
| --- | --- | --- |
| aktia (ticket→MR agent) | P2, P1, P6, Temenos read-only | No foreign API dependency; agent never merges |
| alko (MDQ & duplicates) | P3, P15, validation rules | Automated validation, but merges reversible and reviewed |
| alma-media (MLOps) | P5 (RLS across Redshift+BigQuery before deploy), P13, P6, lean pair | Start immediately (late onboarding criticised) |
| atria (AI readiness) | P7, P13 | Finnish plant workshops (not tech) |
| city-of-helsinki (SME reporting) | P3, P15, SAP S/4HANA Cloud → BI | Pricing flexibility (phased) needs tech phase breakdown |
| elisa (arch & tool selection) | P10, P4 small scoping exercise first | "Real-time for all" → latency tiers |
| enfuce (arch assessment) | P12, handoffs/sign-off friction = process architecture, card platform | Assessment across all teams: scope the bottleneck analysis |
| fennia (platform phase 1) | P11, P12 (DV hubs/links), audit lineage to source | Binding blueprint: no redesign |
| fingrid (finance reporting) | P10, P3 (ledger dedupe first), data mesh | Compliance matrix Yes / Yes but / Yes if |
| helen (semantic model) | P11, P5 (Unity Catalog), start now | AMS incumbent runs ops → handover design |
| kela (FinOps) | P8, extraction for all sources, security questionnaire gate | Numbered requirement matrix |
| kemira (agentic hackathon) | P2, P13 (working prototypes on SAP data), edge cases | No overpromised autonomy |
| kesko (AI readiness) | P13, P4, Snowflake+dbt | Fast tangible validation, not a multi-year track |
| lahitapiola (100 days) | P1, P3, P2 (no automated claims decisions), avoid shadow stacks | Align with insurance-system renewal |
| mandatum (AI Act governance) | model inventory, risk classes, P2, handover to AMS | Discovery before locking scope |
| metsa-group (forecasting) | P7 (buy vs build), Databricks on SAP feeds, no edge-case gold plating | Independent effort estimate (don't anchor to published figures) |
| oriola (DW migration) | P6 (templates over scripts), P4 + P13 velocity metrics on real tables | Phase 1 firm, rest per measured velocity |
| oulun-energia (RAG) | P8 (vector refresh caps), P9 (Q1 freeze), Finnish language quality, P1 | Retrieval evals in Finnish |
| outokumpu (staffing) | P15 real lineage diagrams, Databricks+SAP | No glossy graphics |
| pirha (failure prediction) | P2 (advisory only), extraction for all sources, in-house ownership | Models assist, people decide |
| ponsse (CPQ reporting) | P3 assessment first, ledger↔machine reconciliation, D365 | End-to-end but phased |
| posti (streaming) | P4 (one hub first), P16, AWS+Azure → Databricks/Lakebase | Blast radius |
| s-group (panel) | AI-in-delivery evidence, rate card | Mostly commercial |
| sanoma (backlog agent) | P2, hackathon co-build, edge cases | No zero-defect promises |
| savings-banks-group (FinOps) | P1, P8, Snowflake on Azure, Temenos | DORA posture |
| terveystalo (arch assessment) | P7 licence implications, Databricks scalability | References |
| tokmanni (legacy modernisation) | P5 (margin visibility), P13 measurable ledger impact | ERP under development |
| upm (FDE) | P6 (no fragile bespoke), P8 capped billing, Snowflake+dbt+Databricks | — |
| vahterus (legacy modernisation) | P9 (no Q1 prod change), new ERP alignment | ROI per change |
| valio (failure prediction) | P11 binding design, sensor + ERP | — |
| valmet (senior DE) | P14 edge aggregation, P1, Infor → Snowflake | Certifications |
| varma (MLOps) | P6 reusable patterns, 3 use cases, handover to new hires | — |
| veikkaus (arch assessment) | P7 untapped licences, model deployment workflow | Independence |
| vr-group (analytics eng.) | P9, P12 (DV 2.0), extraction for all sources | — |
| yliopiston-apteekki (arch & tool selection) | browser telemetry sensitivity (privacy by design), licence impact | Quick, painless |

## 5. Agent organisation for the tech side (fits the team's existing agents)

The team already has `buyer-analyst` → `deck-writer` → `deck-critic`, plus `desk-scout`. We add tech specialists
that feed them. Our agents only read and write files and desk comments. They never send to the game.

| Role | Primitive | Input → output |
| --- | --- | --- |
| `tech-analyst` | sub-agent (read-only) | bio + RFP + replies → `work/tech/<buyer>.md`: tech requirements, triggered patterns (P-ids), traps, extraction/compliance matrix needs |
| `solution-architect` | main thread + skill `architecture-patterns` (this file §3 as the library) | tech analysis → 1–2 deck slides (architecture + diagram, tech gates/risks) as spec JSON for deck-writer |
| `architecture-diagram` | skill + deck.py support for an image/diagram per slide | architecture → simple box-and-arrow diagram rendered into the PDF |
| `tech-critic` | sub-agent, clean context | deck + RFP → tries to refute the tech claims: over-engineering, AI extras, missed triggers, unrealistic promises |
| `feedback-miner` | sub-agent (read-only) | all replies/reviews → proposed updates to §3 (new pattern, or a pattern confirmed or refuted), each with a quote |

Learning rule: a pattern becomes a rule after two independent buyers confirm it; one refutation marks it
"conditional". Track `project_fit` and `explanatory_visuals` per version as our KPI.

## 6. Cross-team findings to raise (not tech, but seen in the reviews)

- **`recordly_style` is scored.** Reviews expect the "dark charcoal canvas, electric lime accents". Decks
  rendered with `team/bin/deck.py` (white + teal) got *weak* (Enfuce, Terveystalo). The deck theme should
  change.
- `explanatory_visuals` rewards diagrams, which is our job (T1).
