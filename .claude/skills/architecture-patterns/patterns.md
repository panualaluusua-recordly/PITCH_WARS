# Pattern library (P1–P16)

Single source of truth, moved from `team/tech/TECH_SCOPE.md` §3. All patterns below are `candidate` unless the "Seen
in" column shows a quoted confirmation; status rules (candidate → rule → conditional) are in `SKILL.md`.

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

