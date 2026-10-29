# Price evidence log

Append one row per reply that says anything about price, **only when the deck price is known**. Key: buyer + project + kind + price, never duplicated. Newest last.
Teammates' prices: decks sent with `send.sh` carry the price in the uploaded filename (`…-eur84000.pdf`), visible in each conversation entry's `deck` field.

| Buyer | Project type | Price sent | Kind | Verdict (quote) |
|---|---|---|---|---|
| city-of-helsinki | 2-person squad, 6 months | €198,000 | feedback | "flat out above our budget" |
| city-of-helsinki | 2-person squad, 6 months | €138,000 | feedback | "well above what we aimed for" |
| city-of-helsinki | 2-person squad, 6 months | €84,000 | feedback | no price complaint |
| city-of-helsinki | 2-person squad, 6 months | €84,000 | proposal | **WON**, price "excellent" |
| kemira | 100-day roadmap, 12 weeks | €78,000 | feedback | "flatly above our budget" |
| kemira | 100-day roadmap, 12 weeks | €54,000 | feedback | "flatly above our budget" |
| kemira | 100-day roadmap, 12 weeks | €29,000 | feedback | "entirely above our budget" |
| kemira | 100-day roadmap, 12 weeks | €22,000 | feedback | "trim that inflated price tag so I can finally approve" |
| kemira | 100-day roadmap, 12 weeks | €16,500 | proposal | **WON**, price "excellent" |
| aktia | DW consolidation, 11 months, regulated bank | €365,000 | feedback | "completely above our budget", "dramatically realign" |
| aktia | DW consolidation, 11 months, regulated bank | €148,000 | feedback | "flatly above our budget" |
| aktia | DW consolidation, 11 months, regulated bank | €95,000 | feedback | no reply |
| aktia | DW consolidation, 11 months, regulated bank | €88,000 | proposal | LOST, price "good" (lost on an ML add-on) |
| city-of-helsinki | SME reporting platform, 4 months | €61,100 | feedback | "flat out above the budget"; also disliked "monolithic fixed sum" |
| enfuce | staff aug: 1 senior FT + part-time dev, 6 months | €93,600 | proposal | **WON** (teammate), price "excellent" after 5 feedback rounds |

## Verdicts with unknown price (context only, not usable for anchors)

| Buyer | Project type | Price sent | Kind | Verdict (quote) |
|---|---|---|---|---|
| terveystalo | agent-accelerated migration pilot | unknown (v2) | feedback | "seems quite high, though it might still be within budget" (over-soft) |
| terveystalo | agent-accelerated migration pilot | unknown | proposal | LOST (teammate), price "good"; lost on missing patient-facing AI |
| fingrid | finance/margin reporting automation (Databricks+D365), scope small | unknown (teammate v1) | feedback | "plainly above our approved budget", "cannot advance an engagement that exceeds our authorized expenditure limits" |
| kemira | agentic AI hackathon, 13 pd | €12,200 | proposal | **WON**, price "excellent" (all four ratings excellent) |
| s-group | 1 FTE × 3 months call-off, 60 pd × €920 | €55,200 | proposal | **WON**, price "excellent" |
| upm | 1 ML engineer ~50% × 6 months + coordinator | €107,400 → €75,480 → €68,800 | fb, fb, proposal | over budget → "quite high, might be within outer bounds" → LOST, price "good" (hidden preference: chatbots/conversational tooling) |
| vr-group | analytics engineer ~60% × 6 months | €109,800 → €73,600 cap | fb, proposal | "flat-out above budget" → no reply → LOST, price "fair" |
| valmet | senior DE ~60% × 6 months | €73,600 cap | fb (no reply), proposal | LOST, price "fair" (wanted client staff time capped at half a day a week, Q1 freeze, EU jurisdiction) |
