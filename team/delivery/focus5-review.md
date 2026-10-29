# Delivery-lens review of the focus offers (2026-10-29, ~12:15)

Four clean-context `deck-critic` runs on the Desk versions: oriola v1, tokmanni v1, outokumpu v2, varma v1. Valmet was
skipped because Rauno owns its staffing review (`team/STAFFING_STATUS.md`). Every verdict is **revise first**.

## Cross-cutting

| Issue | Seen in | Fix |
| --- | --- | --- |
| Names, certifications and availability stated as fact ("verified available", "At signing", "3 of 4 confirmed") | all four | Rauno's rule: mark as proposed, confirmed in writing at signature. All names are in `ROSTER.md`, and no one is double-booked. One critic said only Koskinen is listed for oriola; that was wrong. |
| Price far below the rate floors | all four | oriola ≈ €38/h, tokmanni ≈ €56/h, varma ≈ €57/h, outokumpu ≈ €48/h vs. DE €115/h. Decision needed: `pricing-floor-check.md` |
| No effort basis (person-days per role and phase), D8 | all four | Add a one-line basis to the price slide |
| Written governance cadence missing or thin, DP7 | oriola, tokmanni, outokumpu | "Written update every second week, monthly steering, decision log" |
| Recruitment clause missing, DP5 | all four | One line: "You may recruit our consultants after 12 months, no fee" |
| Billing control partial, DP3 | all four | "No overage without your written approval; hours reported weekly in your tool" |

## Per offer: the top delivery fix

- **oriola v1, €168k:** allocations imply about 583 person-days. Shrink the team or the scope, and add pairing with Oriola
  engineers from phase 1, Finnish-language delivery and a written-update cadence. The bio says Teemu is "exhausted by relentless fire-fighting".
- **tokmanni v1, €92k:** add a risks slide (Tarja is "wary of complex technical risk"), replacement and recruitment terms
  and the governance cadence. The RFP asks for "at least two client references", and the deck has two anonymous ones.
  It has cover + 6 content slides, one over the playbook limit.
- **outokumpu v2, €96k:** drop "both verified available"; do not name Unity Catalog, Asset Bundles or Power BI as if
  they were confirmed (the bio says only Azure Databricks + SAP); add continuous knowledge transfer, not just in the last 2 weeks.
- **varma v1, €95.2k:** add a quick-win benefit for leadership (the bio: "quick wins that showcase efficiency to
  leadership"); "replaces twenty one-off deployment scripts" overstates the RFP's "about twenty experiments".

## Our delivery slides

`team/delivery/slides/*` (batch 2) now say availability is planned and confirmed in writing at signature. The open
items above are for each offer's owner. Nothing has been sent to the game.
