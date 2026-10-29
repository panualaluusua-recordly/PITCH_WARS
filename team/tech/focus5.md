# Tech & architecture input: team focus buyers (Oriola, Tokmanni, Outokumpu, Varma, Valmet)

Source: RFPs and bios only (2026-10-29). We did not request any feedback. Pattern ids (P1..P16) refer to `TECH_SCOPE.md`.
Ready-made slides: `team/tech/slides/<buyer>.json` (+ `.pdf` preview). The deck-writer copies the two slide objects into
the buyer's spec after the answer-first slide. `deck.py` now renders the `diagram` field.

## Oriola: DW migration to Azure (P6, P4, P13)

- **Tech hooks:** "hand-crafted, one-off scripts across wholesale interfaces" → one metadata-driven ingestion template,
  config per interface. "Comprehensive multi-year commitments without early empirical velocity metrics on actual supply
  chain tables" → pilot with measured gates (velocity, reconciliation, template reuse, stability).
- **Bio (Teemu):** "meticulously oversees every technical detail", exhausted by fire-fighting → precise SAP terms (CDS
  views, delta extraction), monitoring + runbooks; "high-profile data wins" → pilot gives a visible early win.
- **Requested by RFP that touches tech:** licensing considerations → "Azure consumption only, no new per-user licences".
- **Pharma detail:** batch/lot traceability (GDP) in lineage.
- **Effort basis:** pilot 6 weeks ≈ architect 50% + 2 data engineers ≈ 75 person-days. Later waves are sized from
  measured velocity.
- **For the price owner:** the tech structure supports leading with the **firm pilot** and showing the later waves as
  "estimate, re-priced from pilot velocity". Which number leads is your call.

## Tokmanni: legacy application & reporting modernisation (P5, P13, P4, P7)

- **Tech hooks:** "default platform permissions inadvertently surfaced cross-departmental margin figures to general floor
  supervisors" → deny-by-default, row- and column-level security, access tests in CI. "ERP under active development" →
  integration layer with data contracts so ERP changes don't break reports.
- **Bio (Tarja):** "vendor pitches promising hypothetical time efficiencies failed to reduce actual store operating
  ledger lines" → every retired tool is tied to a ledger cost line with a baseline; "wary of complex technical risk,
  keep daily retail operations stable" → one app at a time, parallel run, rollback, no Q4 cut-overs.
- **Requested:** licence costs → none new unless a wave's business case nets a saving; certifications (not ours, but
  they must be real platform certs).
- **Effort basis:** wave 1 ≈ 8 weeks, 2 people; waves 2–3 ≈ 4 months, 2–3 people. FI/SE/DK data adds model work.

## Outokumpu: staff augmentation 6–12 months (P15, P6)

- **Tech hooks:** "spent hours dissecting glossy stock graphics … that completely obscured basic data lineage" → plain
  diagrams, Unity Catalog lineage as the review artefact. **Do not use decorative images anywhere in this deck.**
- **Bio (Tapio):** doctorate, 30 years of process manufacturing, led the Databricks+SAP migration → speak his stack
  (SAP MM/SD/PP/QM, bronze/silver/gold, Asset Bundles), "enterprise-scale impact" → reusable job templates.
  "Weary of corporate friction" → no standing status meetings, written monthly update.
- **Onboarding/transition plan** is requested: week 1 first merged PR, weeks 2–4 own backlog items, the last 4 weeks
  are a handover where their engineer leads.
- **Effort basis:** per the staffing offer; the extension keeps people and patterns (upsell argument).

## Varma: lab-to-production MLOps (P6, P2, P13)

- **Tech hooks:** "each introduced isolated deployment scripts and distinct configurations" → one golden path: repo
  template, config schema, CI/CD, registry, monitoring. "Alongside our newly hired internal data specialists" →
  use case 1 by us with pairing, 2 co-built, 3 built by them (handover proof).
- **Bio (Jaana):** "decks requiring mental translation of domestic earnings-related pension concepts" → use Finnish
  pension terms (työeläke, TyEL, eläkepäätös); "quick wins … to leadership" → use case 1 in production by month 2.
- **Risk we raise honestly:** models that touch individuals' pensions → human decision stays, explanations logged,
  EU AI Act classification per use case, pseudonymised training data.
- **Trap:** "~20 experiments" → don't promise to productionise all; triage the rest in month 5–6.
- **Effort basis:** 6 months ≈ ML engineer 100% + platform/MLOps engineer 50–60%.

## Valmet: senior data engineer, Snowflake (P14, P1)

- **Tech hooks:** "constrained satellite links where saturating wide-area bandwidth with raw mill telemetry caused severe
  operational delays" → edge aggregation, bandwidth cap, store-and-forward, off-peak backfill, one mill at a time.
  "Extraterritorial jurisdiction over centralized foreign hosting" → EU region, customer-managed keys, minimisation,
  Iceberg exit path, **with the limits stated openly** (Snowflake is US-headquartered).
- **Bio (Milla):** "executive visibility", "tight administrative ship" → a monthly KPI line (pipelines live, link usage,
  freshness) she can show upward.
- **Over-promise trap:** one engineer cannot install collectors at every mill. Scope = design + pilot at one mill;
  Valmet's site/OT staff install, we support.
- **Infor CloudSuite:** extraction via ION / Infor Data Lake APIs. Check API rate limits in week 1.
- **Certifications:** SnowPro Core + SnowPro Advanced: Data Engineer (heavily weighted). Must match a real consultant
  if the game publishes a roster.

## Cross-cutting notes for these five

- Each deck should carry **one architecture diagram** (all five slide sets have one), because reviews marked decks
  without one down on `explanatory_visuals`.
- Certifications named on our slides are placeholders until a consultant roster exists, so as not to over-promise.
- Visual theme (dark charcoal + lime is scored as `recordly_style`) belongs to the deck owners. `deck.py` is still light.

## Review findings to fix in the next versions (tech items, 2026-10-29)

From the clean-context `deck-critic` runs (full list with delivery items: `team/delivery/focus5-review.md`):

- **Oriola:** phrase the gate metrics (reconciliation ≥ 99.9%, ≥ 80% interfaces config-only) as targets agreed after
  the first pilot measurement, not fixed promises.
- **Outokumpu v2:** the bio confirms only Azure Databricks + SAP. Say "Unity Catalog lineage if enabled, otherwise
  documented lineage", drop Asset Bundles and the Power BI name, and say "your BI tool".
- **Varma:** replace "replaces twenty one-off deployment scripts" with the RFP's own framing (about twenty experiments,
  only a few in production). Add a leadership-facing quick-win metric (lead time from model to production).
- **Tokmanni:** the tech slides hold up. The deck is one slide over the limit, so merge slides 4 and 5 or move the
  deliverables line into the architecture slide.

**Done 2026-10-29 ~13:10 (tech-critic pass):** oriola v3, tokmanni v3, outokumpu v4 and varma v3 apply the
tech-only improvements: no unstated tools, measured gates, a week-1 technical probe, explicit unknowns, rollback and
parallel-run rules, and an honest lineage claim. Batch-2 tech slides were updated in place the same way
(`team/tech/batch2.md`).
