# Aktia – Camilla Engblom
- v1 (€486k) not sent; repriced to v2 €365k before sending (Def 45k / Delivery 272k / Handover 48k).
- v2 €365k: "completely above budget", "dramatically realign". Liked: written updates instead of status syncs. Disliked: English runbooks/blueprints with only brief local summaries. Wants full Finnish/Swedish docs.
- v3 €148k: flatly above budget. Liked key-person substitution terms. Disliked: code/pipelines in vendor-managed environments with guest access. Wants everything in Aktia's perimeter.
- v4 €95k stated once (percent split), all code in Aktia tenant.
- v4 €95k feedback: NO REPLY (fee lost). Possibly fatigue after 4 feedback rounds.
- v5 €88k → PROPOSAL
- v5 PROPOSAL €88k: LOST. price good, project_fit fair. Reason: ML anomaly detection / predictive 'bells and whistles' sank it. Wants IP buy-out clauses explicit. Next: aktia-ticket-to-merge-request-developer-or-analytics-a

## 2026-10-29 · v1 draft, aktia-ticket-to-merge-request-developer-or-analytics-a (NOT sent)
- File: work/decks/aktia/aktia-ticket-to-merge-request-developer-or-analytics-a-v1.md/.pdf, 7 slides.
- Price €60,440 = 36 human days (Definition: architect 5 + AI eng 3 = €7,480; Delivery: architect 8 + DE 12 + AI eng 5 = €23,200; Ops: architect 3 d + VDE 3 × €9,000 = €29,760).
- Bets: (1) agent cannot merge own work, named Aktia reviewer = answers the review-bypass post-mortem; (2) EU/in-tenant model hosting options, no external APIs, exit plan = answers foreign-HQ AI dependency; (3) strict scope fence (no ML/anomaly add-ons, no Temenos changes) + FI/SV docs + key-person terms and written updates kept.
- Honest unknowns on deck: stack not stated (VDE pattern is Snowflake + dbt; Definition week 1 confirms; stop after Definition), EU-model quality, ticket quality.
- To verify before sending: supplier financial standing wording, team years/certs, Swedish native reviewer.

<!-- replies:auto -->
## Buyer replies (auto, from the game API; do not edit inside the markers)

### aktia-data-warehouse-consolidation
- 2026-10-29T08:28 · **hints** · deck `aktia-data-warehouse-consolidation-v2.pdf` (unknown) · price signal: **over-hard**
  > While I appreciate that Recordly took my crusade against calendar-clogging status syncs to heart by leaning into written updates, we have an immediate commercial showstopper: their proposed price is completely above our budget. Years ago when I rebuilt our wealth analytics unit around Temenos Transact, I learned to appreciate ambitious architecture, but expecting Aktia to bankroll an engagement that sails entirely past what we can spend feels more like subsidizing a tech startup than contracting a delivery partner. Beyond that financial gulf, leaving our primary runbooks and architectural blueprints in English with only brief local summaries leaves me uneasy, as forcing our operational staff to parse foreign technical phrasing introduces needless friction during supervisory audits. Unless they can dramatically realign their commercial terms with what we can actually finance, this conversation will be remarkably brief.
- 2026-10-29T08:31 · **hints** · deck `aktia-data-warehouse-consolidation-v3.pdf` (unknown) · price signal: **over-hard**
  > Our primary roadblock here is commercial: the total price is flatly above our budget, which brings this conversation to an abrupt halt unless Recordly is willing to get realistic about their commercial terms.   I will give them credit for their key-person substitution terms, however; putting binding replacement penalties and talent commitments directly into the contract is a refreshing bit of accountability that protects us from standard consultancy games. Ever since I arrived at Aktia to overhaul our Temenos reporting, my corporate survival instinct has depended on keeping our core architecture airtight. To that end, leaving our pipelines and development workflows sitting inside vendor-managed environments while merely handing our team guest access leaves our operational perimeter far too exposed for a regulated bank. They will need to bring their pricing under our ceiling and clean up where that code actually lives before we entertain taking this any further.
- 2026-10-29T08:32 · **no_reply** · deck `aktia-data-warehouse-consolidation-v4.pdf` (unknown) · price signal: **no reply**
  > No reply.
- 2026-10-29T08:35 · **verdict** · deck `aktia-data-warehouse-consolidation-v5.pdf` (unknown) · price signal: **verdict lost, price good**
  > Layering machine learning anomaly detectors and predictive capabilities over read-only extraction feeds might look cutting-edge in a pitch deck, but indulging in predictive modeling bells and whistles is precisely what sank this proposal.
  ratings: price good, buyer_fit good, project_fit fair, presentation good
  - [partly met] Slide 5 and 6 insist on full audit trails and FIN-FSA traceability, keeping an ML anomaly detector tethered to human sign-off.
  - [met] Slide 8 and 9 mandate all deliverables, runbooks, and workshops in Finnish and Swedish as the default standard.
  - [partly met] Slide 3 and 7 outlaw standing weekly status syncs in favor of bi-weekly written updates and live dashboards.
  - [partly met] Slide 11 showcases internal document checking and balance anomaly detection rather than speculative customer-facing AI gimmicks.
  - [leans against] Slide 4 insists Temenos extraction remains strictly read-only with no core changes, opting for ML anomaly detection on slide 5.
  - [partly met] Slide 10 details binding staffing substitution terms and financial penalties, though explicit IP buy-out clauses remain implicit.
  - [met] Slide 4 and 6 dictate that all code, pipelines, and CI/CD live strictly inside Aktia's cloud perimeter and repositories.
  - [met] Slide 2 and 5 replace spot-checking with automated full-population reconciliation across every historical account balance.
### aktia-ticket-to-merge-request-developer-or-analytics-a
- 2026-10-29T12:02 · **verdict** · deck `aktia-ticket-to-merge-request-developer-or-analytics-a-v6-eur61080.pdf` (€61,080) · price signal: **verdict lost, price over budget**
  > While your operational controls look considerably sharper than in your previous bid, your commercial expectations are still orbiting a reality far beyond what this department is prepared to underwrite.
  ratings: price over budget, buyer_fit excellent, project_fit good, presentation excellent
  - [met] Audit logs are append-only in our log store, each PR includes reasoning, and controls map directly to FIN-FSA, EBA, and DORA.
  - [met] All three named engineers speak Finnish and runbooks, control matrices, and training are explicitly delivered in Finnish and Swedish.
  - [partly met] They kill off status meetings in favor of bi-weekly written updates, though they fail to specify delivering them via our internal chat tool.
  - [met] The entire scope is targeted squarely at internal analytics engineer developer productivity and pull request workflows.
  - [met] Hard branch protections ensure only human reviewers can merge, while the agent is strictly sandboxed from committing to production.
  - [met] Slide 4 explicitly evaluates an EU-headquartered provider and tenant-hosted open-weight models against hyperscalers with exit testing.
  - [against] The architecture provisions dedicated agent identities with a kill switch rather than inheriting individual developer credentials.
  - [met] Staffing consists exclusively of three senior specialists with no junior consulting pyramid or subcontractors.
<!-- /replies:auto -->
