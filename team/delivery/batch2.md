# Delivery input: second batch (VR Group, UPM, Metsä Group, Savings Banks Group, Vahterus)

Source: RFPs and bios only (2026-10-29). No feedback requested yet. Pattern ids (D1..D8, DP1..DP10) refer to
`DELIVERY_SCOPE.md`. Every name comes from `ROSTER.md`.

Ready-made slides: `team/delivery/slides/<buyer>.json` (+ `.pdf` preview), two slides each in `deck.py` format:
1. **Team and availability**
2. **Delivery plan and governance**

The deck-writer copies both into the buyer's spec after the tech slides. Drop internal costing notes from buyer-facing slides, but retain the candidate-verification caveat until supporting evidence is recorded. Current staffing calculations and rate rules are in `team/staffing/REVIEW.md`; the summary below reflects the corrected effort.

| Buyer | Delivery hooks (evidence) | Our answer | Effort basis |
| --- | --- | --- | --- |
| **vr-group**, analytics engineer 6 mo | "no production changes during Q1" (DP2); bio: railway concepts lost "across foreign-led workshops" (DP8); asks for "team profiles and certifications, delivery plan" | Proposed Jari Lehtonen 100%, target 1 Dec; Finnish and platform certificates required, evidence pending; production changes in Dec and from Apr only | 1 FTE x 6 mo ≈ 120 pd + 12 pd review |
| **upm**, FDE 6 mo | "billing drifted past initial department estimates" (DP3); recruit after 12 months, no fee (DP5); standard terms, deviations as tracked changes (DP4); bio: pipeline "collapsed during a critical quarterly close" | Proposed Henna Kallio 100%, target 1 Dec, evidence pending; fixed monthly fee, weekly hours in UPM's system, no releases around quarter close, zero deviations | 120 pd AI engineer + 6 pd architect = 126 pd |
| **metsa-group**, forecasting | "verified availability and relevant technical certifications" (DP1); "document any formal contract deviations" (DP4); "anchor tightly to published figures rather than … independent delivery calculations" (D8); shortlist presentation; bio: stalled on "every freak kiln anomaly" | Proposed DS + DE core team, supported by 10% architect; target 23 Nov, evidence pending; bottom-up 125 person-days in 3 gated phases; anomalies flagged, not modelled | 125 pd |
| **savings-banks-group**, FinOps | "FIN-FSA, EBA, and DORA" (DP9); "Finnish- and Swedish-speaking" member banks, "language capabilities", "financial sector experience" (DP8); pricing "partitioned into definition, delivery, and ongoing phases"; bio: "prioritizes process adherence" (DP7) | Bilingual banking FinOps team; DORA third-party terms accepted; three phases matching their partition; changes via their change board | 25 pd + 70 pd + 3 pd/month |
| **vahterus**, legacy modernisation | "no production changes take place during Q1" (DP2); bio: "ROI-obsessed… monitors every code commit" (DP10); "concise presentation deck"; Uusikaupunki | Small team, lead on site 2 days/week; ROI ledger linking commits to € benefit; build in Q1, go live in April | 112 pd (72 lead DE + 40 BI) |

## Hand-offs

- **Price owner:** use the corrected role-by-phase effort and minimum-rate basis in `team/staffing/REVIEW.md`. Confirm all role rates, candidate evidence and exact working calendars before quoting.
- **Tech role:** extraction "for all sources" (VR), buy-vs-build (Metsä), EU-only tooling (Savings Banks) are tech items.
  Our slides only promise delivery terms.
- **Roster:** the recorded Outokumpu duplicate allocations were corrected upstream with Teemu Hakala and Noora Lindqvist. The ledger has no recorded allocation sum above 100%, but real availability, credentials and exact booking periods remain unverified. Treat all candidates as draft profiles.
