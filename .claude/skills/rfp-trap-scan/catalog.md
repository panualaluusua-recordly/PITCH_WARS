# Pattern catalog: what buyer text means and how to answer it

Evidence tags: **[won]**, **[lost]**, **[hint]** = seen in our own replies. Untagged = inferred from RFP patterns; verify with feedback.

## Past-failure sentences → requirement

| Buyer says (RFP or bio) | Requirement for the deck |
|---|---|
| Workshops/manuals/decks in English stalled, foreign-language presentations | All workshops, docs, runbooks and training **fully in Finnish** (and Swedish if mentioned). Not "English with summaries" **[hint: Aktia]** |
| Sloppy Swedish translations | Native Swedish speaker on the team, Swedish deliverables reviewed by a native speaker |
| Sampling missed discrepancies | Full-population automated reconciliation on every load |
| Consultant substitutions caused friction | Named key persons, substitution only with buyer approval, overlap at our cost, penalty clause **[hint: Aktia liked]** |
| Sprawling consulting crews, junior-heavy delegations, coordination overhead | 2–3 senior people who do the work themselves |
| Immaculate decks hid whether models work on real data; glossy binders; stock graphics | Concrete worked example on their data, proof-of-value step, lineage diagrams, no hype **[hint: Kemira]** |
| Multi-year commitments without early proof; milestones locked before testing | Short discovery or pilot on real data with a go/no-go gate before the build **[won: Helsinki]** |
| Unvetted register/source pipes, integration gremlins | Probe every source first, then build only approved sources **[won: Helsinki]** |
| Partners took months to learn our domain (insurance, pensions, rail, Data Vault) | Domain experience named explicitly, using the buyer's own vocabulary |
| Black-box handovers, staff had no role in building | Co-build and pair programming from week 1, not a handover at the end **[won: Helsinki]** |
| AI pushed unvetted code / promised zero defects | Human review gate on every AI output, honest error rates, a pilot measuring quality |
| Billable hours stayed static while AI sped work up; productivity gains must be shared | Fixed price per deliverable, or explicit gain-sharing |
| Open billing drifted / timesheet disputes | Fixed monthly fee or hard cap |
| Bespoke algorithms when commercial packages existed | Buy-vs-build assessment; prefer mature packages |
| Sprawling transformation blueprints nobody asked for | Answer only the tender; no "while we're at it" |
| Engineers bogged down in edge cases (freak anomalies) | Explicit 80/20 scope: handle the common cases, log the rest |
| Surprise cloud bills (vector refresh, compute) | Cost caps, budgets and alerts, scheduled refresh with limits |
| Shadow stacks from standalone tools | Everything inside the central platform |
| Reliance on non-EU / single-origin cloud APIs, extraterritorial jurisdiction | EU-hosted options, EU data residency, exit plan |
| Default permissions exposed margins to floor staff | Role-based access and row-level security designed up front |
| Front-end browser telemetry under regulatory scrutiny | No client-side tracking; server-side data only |
| Untracked prototype ran for months | Model/asset inventory, registration and ownership |
| Large consultancies commuting from Helsinki | Local presence or regular on-site days near the buyer |
| Partners' private-retail-only background failed in the public sector | Public-sector references and understanding of public administration |
| Audit criticised premium rates without value | Modest day rates, value per euro made explicit |
| Commercial bids anchored to published figures | Show an independent bottom-up calculation (days × rate) |
| Untapped capacity in existing software commitments | Use existing licences first; no new tools |
| Satellite/constrained links | Edge filtering and compression, incremental loads |
| Ledger records / duplicates across ERP and lakehouse "remain unaddressed" before reporting deliverables | Phase 0 reconciliation and dedupe with a go/no-go gate before any reporting output **[hint: Fingrid]** |

## Traps

| Trap | Winning answer |
|---|---|
| "Real-time access to ALL data, no batch ever" | Don't promise it blindly. Answer "Yes if" / explain: streaming where it adds value, and where batch is the truth for finance. Respect the intent (freshness) honestly. **[hint: Fingrid praised the honest latency boundaries]** |
| Standard purchase agreement applies; deviations hurt scoring | "**No contractual deviations.**" **[won: Helsinki, praised]** |
| Right to recruit consultants after 12 months without fee | Accept explicitly |
| Right to require replacement of any consultant | Accept, with a replacement SLA |
| Majority of the team available at signature | State availability "confirmed from signature" for each role |
| Another vendor's blueprints are binding | Implement them as given; flag gaps as change requests, don't redesign |
| "Supplier shall propose the extraction solution for ALL sources" | Propose a pattern plus source-by-source assessment; don't promise blind coverage of unknown sources |
| No production changes in Q1 / winter peak | Plan shows a Q1 freeze, with go-lives before or after it |
| Security questionnaire before development | Plan includes it as a gate before build |
| Prices binding for 9 months | State it verbatim |
| References with contact persons (2–3, last 3 years) | Give the required number, comparable, dated; contacts provided to shortlisted bidders |
| Certifications "heavily weighted" | Name the exact vendor certifications per person, matched to their stack |
| Hackathon / co-build asked | Make it the first step of the plan |
| AI asked as "case examples" only, and the bio has no AI enthusiasm | Give cases, but keep the solution free of AI add-ons **[lost: Aktia]** |
| Bio praises an AI tool or consultancy success ("digital appointment assistant progressed smoothly") | Show matching experience (e.g. patient-facing conversational AI), even if the RFP doesn't ask **[lost: Terveystalo for omitting it]** |
| Buyer has a proprietary core platform (card issuing, insurance core) | Don't claim experience on it; show a ramp-up plan and pairing with their platform experts **[won but 'leans against': Enfuce]** |
| AMS partner takes over after hypercare | Continuous knowledge transfer with the AMS partner involved early |
| "Budget not disclosed, propose what is appropriate" | Still low. See `price-check`. |

## Hopes in bios → hidden preferences

| Bio says | Show in the deck |
|---|---|
| Watched autonomous agents go live, "charting paths" to multi-agent | A concrete, governed agent use case inside scope |
| Praises an outside consultancy that "shouldered delivery" | Turnkey delivery ownership, we carry the technical load |
| Dreams of a big exit / venture speed | Speed, measurable business impact |
| Steering toward permanent internal ownership | Enablement and handover from day 1 |

## Format complaints seen

- "disjointed", "unfinished", "half-baked" (Enfuce, Terveystalo: teammates' decks) → consistent structure, one storyline, no placeholder or uneven slides
- "too many slides" (Helsinki) → 5–7 slides
- "recordly_style: weak" (Terveystalo v3: white background, teal accents) → use the Recordly dark background with lime theme; also add process diagrams ("explanatory_visuals adequate": text cards only)
- "Stop asking for reviews" (Enfuce, after 5 feedback rounds) → propose by round 3

## Persona cues in bios

- "purged status meetings", "shut down laptop on time", "quiet evenings" → no recurring meetings, written updates, low demand on their time **[won: Kemira]**
- "guards architecture decisions" → options plus decision records; they decide
- "obsessed with ROI / bottom line" → numbers, payback and cost per outcome
- "career-driven, executive visibility" → quick visible wins and a leadership-ready result
- "process/compliance first, cautious" → standard terms, proven patterns, no experiments
- "cynical about contractors" → enablement, internal ownership, short engagement
- "reviews every query/commit" → transparency and access to everything we do

## Lessons from Prio A round (2026-10-29, Ville)
- **Buyers hold ~8 preferences, half of them NOT in the RFP or bio** (UPM: corporate chatbots/conversational tooling; VR: automated messaging with human-reviewed drafts, diagnostic bots, build-vs-buy for telemetry, tendering vs direct award; Valmet: working demos on real data, training format, industrial process modelling). A feedback round is the only way to surface them, so **don't propose after a no-reply**: VR and Valmet were lost that way.
- **Pairing from week 1 is not universal.** Valmet marked continuous co-building "against": cap client staff involvement (e.g. half a day a week) unless the buyer asks for co-build.
- **Stage/milestone payments beat calendar billing** (UPM, Valmet): pay per accepted stage.
- **Q1 change freezes apply even when the RFP doesn't say so** for industrial buyers (Valmet).
- **US-headquartered platforms** (Snowflake) count against buyers who flag jurisdiction; don't build the pitch on them there.
