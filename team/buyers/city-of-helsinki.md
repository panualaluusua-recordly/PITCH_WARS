# City of Helsinki – Kari Voutilainen
- v1 €198k: over budget. Liked: standard agreement with no deviations. Disliked: committing to full register pipelines before the integration issues are isolated.
- v2 €138k + month-1 source-risk check with a go/no-go gate.
- v2 €138k: still "well above what we aimed for". Liked: source-probing sprint. Disliked: too many slides (wants a razor-thin briefing), knowledge sharing only at the end.
- v3 €84k, 6 slides, pairing from week 1.
- v3 €84k: NO price complaint. Liked pairing + Finnish runbooks. Concern: how to locate and understand pipeline outputs later (catalog/discoverability).
- v4 = v3 + data catalog/lineage slide → PROPOSAL at €84k.
- v4 PROPOSAL €84k: **WON**. Ratings price excellent, buyer_fit good, project_fit good, presentation excellent. Leans against: >5 slides (prefers <5). Not addressed: historical/benchmark pipeline automation metrics. Next project: city-of-helsinki-sme-reporting-platform
- SME v1 €61.1k feedback: flat out above budget. Welcomed us back (prior win counts). Disliked: rigid monolithic fixed sum; wants flexibility when discovery shifts work (e.g. fixed discovery + capped/phased build).

## 2026-10-29 · v2 draft: city-of-helsinki-sme-reporting-platform (NOT SENT)
- NOTE: v1 for this project was already sent (€61.1k, at €650/day, below floor), so this draft is **v2**: work/decks/city-of-helsinki/city-of-helsinki-sme-reporting-platform-v2.md/.pdf, 4 slides (answers "<5 slides").
- Price €43,440 maximum = 46 days (data engineer 30 × €920, data analyst BI 14 × €1,000, architect 2 × €920; avg €944/day). Structure: fixed discovery €10,440 (weeks 1-2, 11 days) + build capped at €33,000 (35 days, billed on actual days, never above cap). Firm 9 months, on site Tue+Thu.
- Bets: (1) fixed discovery + capped build answers the "monolithic lump sum" complaint, and the cut from €61.1k answers budget; (2) cover table maps each of his complaints and both mandatory criteria to an answer; days × rate rate card with no markup answers the council-scrutiny / agency-letterhead hint; (3) 4 slides, kept what he praised: standard agreement, pairing from week 1, Finnish docs, catalog/lineage, source gate, no AI.
- Open risks: true budget unknown (cap may still be over); "whole team on site Tue/Thu" implies analyst 2 d/week weeks 1-7 and engineer 3 d/week: confirm roster can do it; current data setup and BI tool unnamed (assumed Power BI certs); availability not backed by roster; historical automation metrics he lacked earlier are still not cited (no real figures available).

<!-- replies:auto -->
## Buyer replies (auto, from the game API; do not edit inside the markers)

### city-of-helsinki-two-person-data-engineering-squad-for-a-6-month-
- 2026-10-29T08:26 · **hints** · deck `city-of-helsinki-two-person-data-engineering-squad-for-a-6-month--v1.pdf` (unknown) · price signal: **over-hard**
  > First and foremost, the proposed price is flat out above our budget, which makes this a non-starter right out of the gate. I will give them credit for swallowing the City’s standard purchase agreement whole without sneaking in contract deviations, but locking the squad into full-scale register pipeline construction right from the start feels reckless when nobody has isolated the actual integration gremlins yet. Having spent years dragging our core workflows into SAP S/4HANA Cloud, I know precisely how fast unvetted municipal source pipes turn into an operational swamp, and dealing with these procurement overshoots makes me want to shut my laptop forever and go raise geese in peace.
- 2026-10-29T08:29 · **hints** · deck `city-of-helsinki-two-person-data-engineering-squad-for-a-6-month--v2.pdf` (unknown) · price signal: **over-soft**
  > Having survived our massive SAP enterprise overhaul a few years back, I know firsthand that messy municipal integrations will blow up in our faces if the pipelines are brittle, and battling city bureaucracy daily already makes me want to quit civilization to raise geese in peace. I will give them credit for front-loading the engagement with an initial source-probing sprint to validate registers before building production pipelines, which avoids deploying on quicksand. However, making me wade through a sprawling deck packed with far too many slides is pure overhead when a razor-thin technical briefing would cut through the noise much faster. Even worse, pushing internal knowledge sharing to a handover phase near the very end leaves our staff watching from the sidelines while external contractors build in a silo, ensuring we inherit technical debt we cannot maintain. Finally, their price sits well above what we aimed for, so they need to trim their figures down if they expect us to take this proposal seriously.
- 2026-10-29T08:31 · **hints** · deck `city-of-helsinki-two-person-data-engineering-squad-for-a-6-month--v3.pdf` (unknown) · price signal: **none**
  > Surviving our SAP migration taught me pure cynicism, but pairing directly with our internal developers and delivering native Finnish runbooks hits the architectural mark. I am still uneasy about how anyone will actually locate and make sense of all these pipeline outputs down the road, so polish that before municipal red tape drives me to raise geese.
- 2026-10-29T08:32 · **verdict** · deck `city-of-helsinki-two-person-data-engineering-squad-for-a-6-month--v4.pdf` (unknown) · price signal: **verdict won, price excellent**
  > No AI hype, no contract redlining, and a solid commitment to pair-program with our internal developers on clean pipeline architecture, which means my quiet goose farm will just have to wait.
  ratings: price excellent, buyer_fit good, project_fit good, presentation excellent
  - [met] Slide 6 accepts the City's standard purchase agreement as is with zero deviations and incorporates audit-ready lineage.
  - [met] Slide 2 and slide 3 commit to continuous Finnish-language runbooks and field-level Finnish business definitions.
  - [leans against] The technical briefing spans seven slides in total, exceeding the preferred ceiling of under five pages.
  - [met] Slide 3 focuses entirely on cataloguing, data dictionary, lineage, and naming conventions without speculative AI distractions.
  - [met] Slide 4 establishes pair programming from week one with City engineers leading later pipelines and taking over operations.
  - [met] Slide 6 commits to a fixed total of €84,000 for the six months with all overage risk explicitly sitting with Recordly.
  - [not addressed] The deck avoids AI hype but does not cite historical or benchmark pipeline automation metrics.
  - [met] Slide 2 and slide 4 mandate month one as a source-risk probing phase with a formal go/no-go decision gate.
### city-of-helsinki-sme-reporting-platform
- 2026-10-29T08:35 · **hints** · deck `city-of-helsinki-sme-reporting-platform-v1.pdf` (unknown) · price signal: **over-hard**
  > Look, you already know your way around our infrastructure and delivered solid work for us previously, so having your squad back on our municipal data setup is genuinely welcome. That said, municipal procurement red tape is already giving me a massive headache, and your proposal hits an immediate wall: the price is flat out above the budget. On top of that, locking the entire delivery into an inflexible, monolithic fixed sum makes me uneasy when dealing with enterprise municipal data; legacy pipeline quirks crop up constantly once you start touching raw tables, and committing to an unyielding lump total feels far too rigid when discovery shifts the work. Having dragged this city through our massive SAP cloud migration while council auditors breathed down my neck, I would honestly rather abandon civilization to raise geese in peace than try to justify these financials to the board.
<!-- /replies:auto -->
