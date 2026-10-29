Buyer: veikkaus | Project: veikkaus-architecture-or-tool-assessment
(Pricing out of scope. Evidence: RFP in work/buyers_now.json, draft team/decks/veikkaus/...-v1.md, team/buyers/veikkaus.md)

Regimes:
- Finnish Lotteries Act (arpajaislaki) licence regime, supervised by the National Police Board <- "Finland's state-owned gaming operator ... robust compliance, reliable governance" (implied). Responsible-gaming and AML (money laundering act) data likely in the landscape (implied).
- GDPR, player personal data <- "player reporting pipelines" (bio) (implied; draft only says "player-data handling")
- Swedish-language customer communication <- "sloppy Swedish translations drew player complaints" (named, bio)
- State-owned company information-security and procurement practice <- "any contract deviations" (implied, unconfirmed)
- EU AI Act <- "in-house AI platform", "streamline model deployment workflows" (implied; models touching player profiling or risk detection could matter; we assess, we do not build)
- NIS2: possible but unconfirmed; do not claim.

Supplier obligations -> our answer:
- Access to logs and metadata -> read-only, named Veikkaus-issued accounts, access list in week-1 checklist, revoked at close; no player-level data leaves Veikkaus' environment; findings carry counts and metadata only. slide 2, 5. Draft states the promise; add the mechanism.
- Confidentiality -> Veikkaus standard terms/NDA accepted (draft "no deviations"). Working material only in Veikkaus environment; delete working notes at close. Do not state where Recordly stores material unless verified.
- Personal data -> Veikkaus is controller, we process under their DPA if any is seen incidentally; no copy, no sample export.
- Compliance lens per finding (draft has a "compliance note"): access control, audit trail, lineage, retention/minimisation, plus AI Act lens: model inventory, risk class per in-house model, human oversight for player-affecting decisions, monitoring/drift. We assess; we do not certify Veikkaus. GAP: AI Act lens not in draft.
- Swedish deliverables with native review: draft; roster unverified.

Matrix (RFP's 6 sections; no numbered requirements):
- Organisational background and aims: Yes
- Methodology and deliverables: Yes
- Plan and timeline: Yes
- Team credentials incl. certifications, availability: Yes if roster confirms named certs and dates (verify)
- Detailed pricing: Yes (not commented here)
- Contract deviations: Yes, none listed
- Two-hour interview: Yes
- Independence (no vendor ties): Yes if no reseller/commission relationships (verify; profile says partner statuses unverified)
- Player data stays in environment: Yes
- Swedish deliverables: Yes if native Swedish reviewer on roster

Cannot promise (verify):
- Slide certs (Azure Solutions Architect Expert, Databricks DE Pro/ML Pro, SnowPro Core, Azure DE Associate, GCP DE) -> placeholders; roster only. Wording: "Certifications of the named consultants are listed at proposal; copies on request."
- Gaming-sector experience -> not in profile. Wording: "We have not assessed a gaming operator; we bring a regulated-sector method (finance, public sector) and pair with your compliance lead on the compliance lens."
- "governance in regulated sectors, 14 years" -> placeholder, verify.
- "takes no vendor commissions" -> verify partner agreements.
- ISO 27001 -> not held per profile; do not mention.
- "Swedish (native-level)" speaker -> verify.

Unsupported claims in draft: "No player-level data leaves your environment" is keepable only if all analysis runs on Veikkaus infrastructure; state that any AI-assisted analysis runs inside Veikkaus or on metadata only, and confirm our tooling does so. "Deliverables are Veikkaus' property": fine.

Gate before build: week-1 access and data-handling checklist (accounts, read-only scope, NDA/DPA signed, where working material lives). No log analysis before it passes. Week-4 checkpoint on evidence quality follows.

Slide additions: s2 row "Player data: Veikkaus is controller; metadata and counts only; named read-only accounts"; s3 add AI-governance lens (model inventory, risk class, oversight) to D3/D4; s5 replace placeholder certs with roster.
