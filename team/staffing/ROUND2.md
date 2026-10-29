# Staffing round 2 - active portfolio support

Source snapshot: upstream `fc133b8`, 2026-10-29. Reviewer: Rauno / Codex. No requests sent to the game.

## Ownership and scope

Ville owns Kemira, S-group, UPM, VR Group and Valmet. This pass does not create versions or change roster rows for those buyers. Earlier staffing options for them are historical alternatives; Ville's sent versions and buyer outcomes supersede them. Comments only for the Prio A owners.

Current staffing pass: Kela, LahiTapiola, Alma Media, Enfuce, Ponsse and Savings Banks Group. Overall offer ownership is unchanged. A staffing review is not human approval or permission to submit.

## New review drafts

| Buyer | Staffing version | Effort / rate basis, 8 h per day | Price | Material change |
| --- | --- | --- | --- | --- |
| Kela | v3 | FinOps lead architect 12 + DE 12 + security/audit advisor 2 = 26 days, EUR 920/day | EUR 23,920 | Unsupported public-sector experience and availability changed to role requirements; actual consultants and references pending. |
| LahiTapiola | v3 | AI architect 10 x EUR 960 + DE 6 x EUR 920 + AI engineer 2 x EUR 960 | EUR 17,040 | Includes the previously omitted EUR 5/h AI premium on the strategy architect's AI assessment work. |
| Alma Media | v3 | MLOps lead 20 x EUR 960 + DE 20 x EUR 920 = 40 days | EUR 37,600 | Lean pair retained; start at signature is a target requiring resource verification, not a guaranteed mobilisation claim. |
| Enfuce | v2 | Architect 12 + Snowflake DE 10 = 22 days at EUR 920/day | EUR 20,240 | Candidate experience, certificates and availability are requirements rather than unsupported assertions. |
| Ponsse | v3 | DE 13 x EUR 920 + DA 7 x EUR 1,000 + architect 2 x EUR 920 = 22 days | EUR 20,800 | Smaller scope: three KPIs, two feeds, one reporting unit, six elapsed weeks. Assessment EUR 6,600; gated dashboard EUR 14,200. |
| Savings Banks Group | v4 | Definition 14 + Delivery 26 + ongoing 9 = 49 days at EUR 920/day | EUR 45,080 | Advisor effort moved to 2 days in each build phase, within the roster's 10% peak cap. No named resource commitment; optional VDE architecture must be separately funded. |

All totals exclude VAT. Other commercial inclusions remain as described in the draft. Architect and other-role base rates are proposed commercial rates unless separately confirmed; Rauno's mandatory DE/DA/AI rules are preserved. The shared price-check also sets EUR 115/h for other roles, which these variants meet.

## Ponsse: scope reduction, not a rate reduction

The buyer rejected the earlier bloated rollout and called the prior price flat-out above budget (prior sent price is unknown). The v2 draft was EUR 30,320 for 32 days. The new v3 is **EUR 20,800 for 22 days**, about 31% lower, with a correspondingly smaller deliverable: three agreed KPIs and two feeds for one reporting unit. No group-wide rollout, additional sites, sales reporting or expanded KPI catalogue is implied.

- Phase 0, two weeks: DE 4 + DA 2 + architect 1 = 7 days; EUR 3,680 + EUR 2,000 + EUR 920 = **EUR 6,600**.
- Gate: confirm feed feasibility and ledger definitions. Customer can stop and pays only the assessment.
- Phase 1, four weeks: DE 9 + DA 5 + architect 1 = 15 days; EUR 8,280 + EUR 5,000 + EUR 920 = **EUR 14,200**.
- Rates remain DE EUR 115/h, DA EUR 125/h, architect EUR 115/h. Technical owner must confirm that the smaller pilot is credible after profiling; no unchanged full-scope promise accompanies the lower price.

## Savings Banks: peak capacity correction

The original v2 priced 3 DORA-advisor days in four Definition weeks. At 20 planning workdays that is **15%**, above the roster's 10% reservation. The new draft uses:

| Phase | Lead days | DE days | Advisor days | Total | Advisor allocation |
| --- | --- | --- | --- | --- | --- |
| Definition, 4 weeks | 6 | 6 | 2 | 14 | 10% |
| Delivery, 8 weeks | 10 | 14 | 2 | 26 | 5% |
| Ongoing, 3 months | 6 | 3 | 0 | 9 | 0% |
| Total | 22 | 23 | 4 | 49 | |

The rebalancing preserves role totals and EUR 45,080. It is a proposed distribution, not evidence that the advisor can complete the compliance scope in those windows. Confirm it with the qualified advisor. Client approval gates remain in place.

## Resource evidence gate

The current public player guide was read directly from `/agents.md`. It says `GET /api/me` may provide `consultants` and `consultants_valid_until`; availability can change. A static repository roster does not replace that live evidence.

The team token is held by Rauno and is not stored in GitHub. Rauno reported saving it, but `.env` is not present in this checkout; the file location in the other session is pending. No live consultant identity or availability has yet been verified. Continue role-only work meanwhile; do not register a new team or commit credentials.

Before a named commitment: check live roster and validity time, actual role/language/certification evidence, date overlaps, absences and approved start. Do not invent a name or treat an old `offer` row as a verified booking.


## Verification

All six PDFs rendered and visually checked page by page (39 slides total); no renderer overflow marker. Prices above reconcile to role days at the stated 8-hour rates. These are staffing drafts for the existing offer owners, not submissions or verified consultant bookings.

Savings Banks Group v4 incorporates the concurrently published technical v3 safeguards (attribution rules, three-month baseline, alert-only rollout, non-production suspend limits, least-privilege access and two-day replacement cap), then adds the staffing corrections above. Technical v3 is preserved unchanged.
