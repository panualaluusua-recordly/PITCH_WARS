# Staffing review and handoff - Rauno / Codex

Updated 2026-10-29. Staffing review completed for the five delivery modules currently in the repo, plus a new Valmet staffing module. Technical architecture remains with the tech owner. No game request was sent.

## Ready for the offer owners

Use the revised JSON/Markdown/PDF modules in `team/delivery/slides/` for UPM, VR, Metsa Group, Savings Banks Group and Vahterus. Use `team/staffing/valmet.json` for the Valmet staffing section. These are draft inputs for the deck writer, not complete approved offers.

The team tables now distinguish proposed candidates, required capabilities and target starts from verified credentials and availability. The roster is a proposal ledger, not evidence that a consultant exists or is available. Confirm CVs, language skills, certifications and calendar availability before submitting a deck with named commitments.

## Corrected effort and rate basis

Planning convention: **7.5 hours per person-day, 20 working days per planning month**. This is an estimate, not a verified working calendar. Actual holidays, absences, start/end dates and client working time must be checked before a binding fixed price. Amounts below exclude VAT, travel, licences and cloud consumption.

| Buyer | Effort by role | Staffing correction | Known rate-floor subtotal |
| --- | --- | --- | --- |
| Valmet | 6-week pilot: senior DE 30 days, analytics/QA 3 days | One DE + part-time analytics/QA, no dedicated architect; one mill only | 225 h x EUR 115 + 22.5 h x EUR 125 = **EUR 28,687.50** |
| UPM | AI engineer 120 days + architect 6 days = **126 days** | Includes the previously omitted 5% architect effort in the fixed-fee basis | AI engineering minimum: 900 h x EUR 120 = **EUR 108,000**, plus 45 architect hours |
| VR Group | Analytics engineer 120 days + architect 12 days = **132 days** | Analytics engineering budgeted conservatively at the DA floor | 900 h x EUR 125 = **EUR 112,500**, plus 90 architect hours |
| Metsa Group | DS 72 days + DE 44 days + architect 9 days = **125 days** | DE 60% pilot / 50% roll-out / 10% handover; DS 80%, architect 10% | DE: 330 h x EUR 115 = **EUR 37,950**, plus 540 DS hours and 67.5 architect hours |
| Savings Banks Group | Definition 15 lead + 8 DE + 2 advisor = 25 days; delivery 42 + 24 + 4 = 70; ongoing 1.5 + 1 + 0.5 = 3 days/month | Published allocations are caps; planned phase effort governs billing | Definition DE **EUR 6,900**; delivery DE **EUR 20,700**; ongoing DE **EUR 862.50/month**; lead/advisor still to price |
| Vahterus | Lead DE 72 days (Dec-May) + BI 40 days (Jan-May) = **112 days** | Replaces the inconsistent 70 + 35 day approximation; keeps 60% / 40% allocations | 540 h x EUR 115 + 300 h x EUR 125 = **EUR 99,600** |

**These subtotals are internal labour selling-price floors, not final fixed-price quotes.** Architect, DS, FinOps lead and regulatory-advisor base rates have not been supplied by Rauno. The price owner must price these roles explicitly. For every specialist whose work requires AI expertise, add EUR 5/h to the applicable base rate; UPM's AI engineer already includes it. Do not apply a universal DE rate to unrelated roles or silently make architect time free.

For a fixed price, sum all roles' hours x agreed selling rate, then add a documented risk allowance for the specific scope and any included expenses. Record acceptance criteria, exclusions, client dependencies and change control. Do not reduce an effective DE or DA rate below EUR 115/h or EUR 125/h through a package discount; AI floors are EUR 120/h and EUR 130/h respectively. No blanket contingency percentage has been approved.

## Shared roster and remaining checks

- Maximum two architects per offer. Reviewed delivery teams have zero or one. Valmet uses no dedicated architect.
- Complementary roles are included without adding unnecessary full-time specialists. Valmet's QA specialist is not yet nominated; client OT installation capacity is a dependency, not supplier capacity.
- The recorded shared allocations remain at or below 100% if all offers overlap: Antti 70%, Ville 90%, Tuomas 40%; others at most 100%. This arithmetic is **not verified availability**: dates, existing external work and absences remain unverified.
- Keep Outokumpu's corrected Teemu Hakala / Noora Lindqvist proposal. Do not restore Mikko Laine / Riikka Salo there; both are already proposed 100% for Oriola.
- Oriola: tech's 6-week estimate uses architect 50%, while the roster reserves 60%. Reconcile before quoting: 75 days at 50% architect, or 78 days at 60%, plus any later BI work. Do not choose silently.
- Tokmanni: scope says two people for eight weeks but roster lists engagement lead 40%, DE 100%, BI/security 80% (2.2 FTE). Price 88 days if those allocations cover all eight weeks, or reduce allocations in the offer and roster together. Later waves need separate estimates.
- Outokumpu: if priced as two full-time engineers plus a 10% engagement lead, count 252 days over six planning months or 504 over twelve; confirm duration. A mixed data/analytics role uses the DA floor when analytics scope applies.
- Varma: ML 100%, MLOps/platform 60%, architect 15% gives 210 days over six planning months. Price all three roles and apply AI premiums to specialists with AI requirements; confirm whether the platform role is DE or another rate class.

## Merge and submission handoff

1. Merge updated staffing modules into the offer owner's current deck; preserve their ownership.
2. Keep internal costing notes out of the buyer deck. Keep the candidate-verification caveat until evidence is available; do not remove it to imply confirmation.
3. Resolve missing rates, named-candidate evidence and exact project/date/scope checks before a fixed-price commitment or verified-availability claim.
4. Reconcile ownership with Wolves Pitch Desk when access is restored. Human approval and the existing sender workflow still apply.

No overall offer is marked approved or submission-ready by this staffing review. Ready status means the staffing edits are available for the offer owners to integrate.
