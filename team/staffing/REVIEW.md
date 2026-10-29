# Staffing review and handoff - Rauno / Codex

## Ville's additional eight drafts (snapshot: upstream 82c98ea)

Staffing successors are ready in the same buyer folders; original versions remain for history. These use **8 hours/day**. They keep role profiles, mark credentials/languages/availability as requirements pending verification, and do not assign people merely because their names appear in the roster.

| Buyer | Staffing successor | Draft price | Staffing change |
| --- | --- | --- | --- |
| Aktia | v2 | EUR 61,080 | 36 days: AI architect 16, DE 12, AI engineer 8; architect premium included. Definition EUR 7,680, delivery EUR 23,520, run EUR 29,880. |
| Alko | v2 | EUR 35,280 unchanged | Architect 10, DE 24, DA 4 days; rate arithmetic passes. Unverified personal experience removed. |
| City of Helsinki | v3 | EUR 43,440 cap unchanged | DE 30, DA 14, architect 2 days; staffing provides team on-site coverage, not an impossible promise that every member attends all 20 on-site days. Four-slide target retained. |
| Elisa | v2 | EUR 20,240 unchanged | Architect 13, DE 9 days; rate arithmetic passes; confirmed-start claim removed. |
| Kemira | v2 | EUR 12,280 | AI engineer 6, DE 5, AI-review architect 2 days; architect AI premium included. |
| Sanoma | v2 | EUR 54,440 | 29 human days: AI architect 14 (hackathon 3 + setup 8 + run review 3), DE 10, AI engineer 5; 3-month VDE fee unchanged. |
| Veikkaus | v2 | EUR 19,200 | Architect 12 + MLOps DE 8 days at proposed AI rate EUR 120/h; the EUR 5/h premium covers AI-platform assessment expertise, not extra AI features. |
| Yliopiston Apteekki | v2 | EUR 16,560 unchanged | Architect 11, DE 7 days; 11 architect days across six weeks instead of promising 12. Unsupported references marked for verification. |

Architect base EUR 115/h in these drafts is a proposed rate, not a user-supplied company minimum. New roles are not booked. Scope, exact working calendar, candidate evidence and fixed-price risk assumptions still need confirmation. Technical owners retain platform-fit and compliance responsibilities. Staffing agent reviews are recorded in each buyer's sign-off file; no human approval was written.

## Latest complete offer revisions (snapshot: upstream 3eaabe2)

The newly arrived complete focus offers now have staffing-corrected successors. **Use these versions for further review; earlier prices for the same allocations are superseded.** They retain the technical owner's architecture. All are draft capacity prices, not verified-resource commitments or human approvals.

| Buyer | Latest staffing version | Draft price, excl. VAT | Calculation |
| --- | --- | --- | --- |
| Oriola | `team/decks/oriola/oriola-large-migration-or-dw-programme-v4` | Pilot EUR 91,500; full-programme estimate EUR 477,375 | Eight-week pilot: DE 80 days + architect 24 = 104 days. Nine-month estimate: DE 360, architect 108, BI 70 = 538 days. Later phases re-estimated at pilot gate. |
| Tokmanni | `team/decks/tokmanni/tokmanni-legacy-application-and-reporting-modernisation-v4` | EUR 218,625 | 22 planning weeks: lead 44, DE 110, BI 88 = 242 days. Explicit 2.2 FTE rather than an uncosted two-person approximation. |
| Outokumpu | `team/decks/outokumpu/outokumpu-staffing-6-12-months-v5` | EUR 227,250; EUR 37,875/month | DE 120, analytics 120, lead 12 = 252 days; free/as-needed lead support replaced with funded 10%. |
| Varma | `team/decks/varma/varma-lab-to-production-mlops-v4` | EUR 199,350; 3 x EUR 66,450 | AI ML 120, AI platform DE 72, AI architect 18 = 210 days; premiums included. |

These four use 7.5 hours/day and the stated working-day assumptions. Proposed non-DE bases: engagement lead and architect EUR 125/h; ML EUR 125/h, plus EUR 5/h when AI expertise is required. These bases are proposals for the offer owner, not new minima supplied by Rauno. DE/DA floors remain mandatory. Confirm actual calendars, credentials, availability, scope and risk allowance before committing. If a budget cannot support these allocations, reduce scope or effort and re-estimate rather than undercutting hourly minima.

The Oriola 50%/60% architect and Tokmanni two-person/2.2-FTE arithmetic issues noted in the earlier review below are **resolved in these new versions**. Old tech summaries remain historical inputs. The shared sign-off files record Rauno's agent review as changes requiring final owner confirmation, not approval to send.

Updated 2026-10-29. Staffing review completed for the five delivery modules currently in the repo, plus a new Valmet staffing module. Technical architecture remains with the tech owner. No game request was sent.

**Latest handoff:** four VDE offer drafts added by Ville were also reviewed and updated in place. Corrected totals and the separate 8-hour convention are in `team/delivery/pricing-floor-check.md`. UPM and Valmet are EUR 115,320 each, VR EUR 118,440, Savings Banks EUR 59,440 for a reduced one-bank pilot. Original lower totals are superseded. These are draft commercial proposals with candidate and base-rate confirmation still pending.

The Valmet six-week human pilot module below is an optional reduced-scope alternative, **not a replacement for the six-month RFP or a staffing addition to the VDE option**. Keep the six-month duration in the full offer. Select one variant with the offer owner; never add their allocations together or present a small pilot price as the full six-month price.

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
