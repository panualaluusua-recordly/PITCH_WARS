# Delivery input: second batch (VR Group, UPM, Metsä Group, Savings Banks Group, Vahterus)

Source: RFPs and bios only (2026-10-29). No feedback requested yet. Pattern ids (D1..D8, DP1..DP10) refer to
`DELIVERY_SCOPE.md`. Every name comes from `ROSTER.md`.

Ready-made slides: `team/delivery/slides/<buyer>.json` (+ `.pdf` preview), two slides each in `deck.py` format:
1. **Team and availability**
2. **Delivery plan and governance**

The deck-writer copies both into the buyer's spec after the tech slides and **drops the `note` field**, which holds
our effort basis for the price owner and must not reach the buyer.

| Buyer | Delivery hooks (evidence) | Our answer | Effort basis |
| --- | --- | --- | --- |
| **vr-group**, analytics engineer 6 mo | "no production changes during Q1" (DP2); bio: railway concepts lost "across foreign-led workshops" (DP8); asks for "team profiles and certifications, delivery plan" | Jari Lehtonen 100% from 1 Dec, Finnish-native, SnowPro Adv. DE + dbt + AWS; production changes in Dec and from Apr only | 1 FTE x 6 mo ≈ 120 pd + 12 pd review |
| **upm**, FDE 6 mo | "billing drifted past initial department estimates" (DP3); recruit after 12 months, no fee (DP5); standard terms, deviations as tracked changes (DP4); bio: pipeline "collapsed during a critical quarterly close" | Henna Kallio 100% from 1 Dec; fixed monthly fee, weekly hours in UPM's system, no releases around quarter close, zero deviations | 1 FTE x 6 mo ≈ 120 pd |
| **metsa-group**, forecasting | "verified availability and relevant technical certifications" (DP1); "document any formal contract deviations" (DP4); "anchor tightly to published figures rather than … independent delivery calculations" (D8); shortlist presentation; bio: stalled on "every freak kiln anomaly" | 2-person core team from 23 Nov who also present; bottom-up 125 person-days in 3 gated phases; anomalies flagged, not modelled | 125 pd |
| **savings-banks-group**, FinOps | "FIN-FSA, EBA, and DORA" (DP9); "Finnish- and Swedish-speaking" member banks, "language capabilities", "financial sector experience" (DP8); pricing "partitioned into definition, delivery, and ongoing phases"; bio: "prioritizes process adherence" (DP7) | Bilingual banking FinOps team; DORA third-party terms accepted; three phases matching their partition; changes via their change board | 25 pd + 70 pd + 3 pd/month |
| **vahterus**, legacy modernisation | "no production changes take place during Q1" (DP2); bio: "ROI-obsessed… monitors every code commit" (DP10); "concise presentation deck"; Uusikaupunki | Small team, lead on site 2 days/week; ROI ledger linking commits to € benefit; build in Q1, go live in April | ≈ 105 pd |

## Hand-offs

- **Price owner:** effort bases above. Our rates are not set here.
- **Tech role:** extraction "for all sources" (VR), buy-vs-build (Metsä), EU-only tooling (Savings Banks) are tech items.
  Our slides only promise delivery terms.
- **Roster:** our five teams add no conflicts. The existing conflict (Mikko Laine, Riikka Salo in oriola and outokumpu) is
  flagged in `ROSTER.md` for the focus-5 owner.
