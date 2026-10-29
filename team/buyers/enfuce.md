# Enfuce - Kari Holmberg (VP Data & Analytics)

## 2026-10-29 - project 1 enfuce-staff-augmentation WON (teammate) €93.6k, price/buyer_fit/presentation excellent
- Praised: attacked identity/dedup layer directly, builders on site at Espoo whiteboards (3 days/week), no corporate fluff; split ownership across squads; Terraform/CI templates; honest risks slide. "Leans against": no experience on Enfuce's proprietary card-issuing platform. recordly_style was weak (light theme) and visuals adequate (no diagrams). Earlier hints: "Stop asking for reviews", single central squad = bottleneck, "disjointed" decks.

## 2026-10-29 - project 2 enfuce-architecture-or-tool-assessment v1 draft (NOT sent)
- File: work/decks/enfuce/enfuce-architecture-or-tool-assessment-v1.md/.pdf, 6 slides. Price €20,240 = 22 pd × €920 (Lead Data Architect 12 + Senior DE Snowflake 10), 4 weeks, on site Espoo 3 d/week weeks 1-3. Budget undisclosed; anchor Kemira €16.5k won, €22k "inflated"; Enfuce fast-paying relationship so ~20-25 pd.
- Bets: (1) handoffs/sign-offs/routines as lead lens (handoff map, wait vs work time per stage); (2) no claim on card-issuing platform, week-1 sessions with their platform experts; (3) carried over: identity/dedup baseline first, ownership split across squads, Terraform check, no review rounds from us, short deck.
- VDE: MENTION only (Snowflake; dbt unknown; advisory work so not priced), one line on slide 5, benchmark 12 h -> 30 min.
- Honest unknowns on deck: which logs exist, number of squads (assumes ≤6).
- To verify before sending: roster/certs/years placeholders, VDE mention vs "no AI extras" risk (drop line if deck-critic objects), rate/price headroom (+10% possible per price-check since earlier price "excellent").

<!-- replies:auto -->
## Buyer replies (auto, from the game API; do not edit inside the markers)

### enfuce-staff-augmentation
- 2026-10-29T08:24 · **hints** · deck `enfuce-staff-augmentation-v1.pdf` (unknown) · price signal: **over-soft**
  > Targeting the cardholder identity resolution layer right out of the gate hits the mark, especially since cleaning up duplicate account profiles is the exact operational headache we need dead. When I rebuilt our core transaction pipeline on Snowflake after joining Enfuce, the entire goal was cutting delivery lag and stripping out fragile junk, so we cannot afford architectural missteps here. That said, funneling everything through conventional staging-to-marts layers is a trap that will break under real card transaction revisions, because forcing core entities straight into rigid reporting structures leaves no resilience when upstream issuer events mutate. More broadly, the pitch comes across as way too certain, reading like an idealized roadmap where production never bites back and leaving me with no visibility into what could actually derail the timeline or what technical friction would force the scope and commercial terms to move. On that note, the fee sits well above where it needs to be, so you will need to adjust that quote downward if you want this to move forward.
- 2026-10-29T08:27 · **hints** · deck `enfuce-staff-augmentation-v2.pdf` (unknown) · price signal: **none**
  > The proposal hits some strong notes, especially tackling cardholder master data resolution and account deduplication right out of the gate, which resonates deeply after the nightmare ID mismatches that wrecked our reporting tables during an earlier rollout. Locking in Data Vault modeling patterns inside Snowflake for the core event stream is another smart architectural move that will keep our historical data rock solid as transaction volumes explode. That said, reading through the proposal felt disjointed and unfinished, which made it frustratingly difficult to take the pitch seriously when we expect sharp execution. Handcrafting our data pipelines as isolated, bespoke setups also gives me pause, as treating pipeline provisioning without repeatable infrastructure definitions is pure technical debt waiting to kill our scale down the line. We definitely still have ground to cover before anything here is settled.
- 2026-10-29T08:30 · **hints** · deck `enfuce-staff-augmentation-v3.pdf` (unknown) · price signal: **none**
  > Tackling our cardholder identity mess upfront and putting boots on the ground in Espoo fits what I've pushed since overhauling our transaction stack when I joined. That said, flipping through felt pretty disjointed and half-baked, which made it tough to take the pitch seriously.
- 2026-10-29T08:32 · **hints** · deck `enfuce-staff-augmentation-v4.pdf` (unknown) · price signal: **none**
  > Tackling cardholder deduplication out of the gate is dead on after the identity trash that corrupted my tables during past rollouts, and standardizing our setup with templated infrastructure modules is clean execution. Funneling all analytical ownership through a single central squad feels too bottlenecked for real scale, so rethink how those operational boundaries are split.
- 2026-10-29T08:39 · **hints** · deck `enfuce-staff-augmentation-v4.pdf` (unknown) · price signal: **none**
  > Getting boots on-site in Espoo next month to crush the cardholder deduplication that has haunted my transaction pipeline since our earlier rollout hits the mark. Stop asking for reviews and just rethink how pipeline ownership sits across squads so delivery doesn't bottleneck in one corner.
- 2026-10-29T08:41 · **verdict** · deck `enfuce-staff-augmentation-v5.pdf` (unknown) · price signal: **verdict won, price excellent**
  > You skipped the corporate fluff, attacked our identity layer mess directly, and brought real builders ready to hit our whiteboards, so let's get the paperwork signed and start shipping.
  ratings: price excellent, buyer_fit excellent, project_fit good, presentation excellent
  - [partly met] Slides 4 and 10 commit to deterministic rule-based matching with an audit table and reversible merges.
  - [met] Slides 2 and 6 prioritize the cardholder identity layer and duplicate baseline before shipping downstream tools.
  - [met] Slides 4 and 5 require every pipeline to deploy from standard Terraform and CI/CD templates.
  - [met] Slide 5 splits pipeline domain ownership across product squads with data contracts and codeowners.
  - [leans against] Slides 8 and 9 field senior payments specialists who lack prior experience on Enfuce's proprietary platform.
  - [met] Slides 2 and 8 confirm both named engineers are ready to start on the first of next month.
  - [met] Slides 2 and 12 place the consultants on-site at the Espoo office three days per week.
  - [met] Slide 4 specifies building the Snowflake history core with Data Vault hubs, links, and satellites.
<!-- /replies:auto -->
