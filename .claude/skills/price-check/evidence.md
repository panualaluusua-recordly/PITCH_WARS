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
| aktia | ticket-to-merge agent, team productivity | €61,080 | proposal | LOST, price "over budget" ("commercial expectations ... far beyond what this department is prepared to underwrite") |
| alko | master data quality and duplicate cleanup | €35,280 | feedback | "total price ... above our budget"; over-soft, Finnish delivery praised |
| fingrid | finance and margin reporting, 21 person-days | €19,320 | proposal | LOST, price "excellent"; lost because team had no finance/business role |
| mandatum | AI Act readiness and governance | €24,840 | proposal | LOST, price "excellent"; lost because human oversight/automated-decision boundaries were missing |
| alko | master data quality and duplicate cleanup | €35,280 | proposal | LOST, price "over budget"; client-side continuous pairing also felt too demanding |
| elisa | data platform architecture assessment | €20,240 | proposal | **WON**, price "good" |
| fingrid | invoice exception automation | €19,720 | proposal | LOST, price "fair"; hours-saved metric did not match buyer's operational-return criteria |
| kemira | data platform phase 1 | €40,480 | proposal | LOST, price "excellent"; wanted a live demo on plant data rather than static slides |
| mandatum | legacy application and reporting modernisation | €25,240 | proposal | **WON**, price "excellent" |
| s-group | AI/MCP hackathon | €9,400 | proposal | LOST, price "excellent"; customer-service AI case omitted |
| s-group | ticket-to-merge agent | €21,400 | proposal | **WON**, price "good" |
| sanoma | analytics backlog agent | €54,440 | proposal | LOST, price "over budget" |
| terveystalo | analytics engineering support, 6 months | €15,640 | proposal | **WON**, price "excellent" |
| valmet | machine-data exploration | €24,480 | proposal | **WON**, price "excellent" |
| valmet | first 100 days data and AI roadmap | €16,880 | proposal | **WON**, price "excellent" |
| upm | MLOps prototype-to-production | €56,960 | proposal | LOST, price "good" |
| veikkaus | architecture and tool assessment | €19,200 | proposal | LOST, price "over budget" |
| vr-group | ingestion automation build | €18,400 | proposal | LOST, price "fair" |
| yliopiston-apteekki | data platform architecture assessment | €16,560 | proposal | LOST, price "good" |
| alma-media | prototype-to-production MLOps, 40 person-days | €37,600 | proposal | LOST, price "excellent" |
| atria | AI readiness assessment and roadmap | €16,760 | proposal | LOST, price "excellent" |
| city-of-helsinki | SME reporting platform, 46 person-days | €43,440 | proposal | LOST, price "fair" |
| elisa | operational and sensor data failure prediction | €16,960 | proposal | LOST, price "excellent" |
| enfuce | architecture and tool assessment, 22 person-days | €20,240 | proposal | LOST, price "over budget" |
| fennia | first data platform phase | €31,280 | proposal | LOST, price "excellent" |
| helen | semantic model and self-service setup, 28 person-days | €26,880 | proposal | LOST, price "fair" |
| kela | cloud data platform cost and FinOps cleanup | €23,920 | proposal | **WON**, price "excellent" |
| kesko | AI readiness assessment and roadmap | €16,760 | proposal | LOST, price "excellent" |
| lahitapiola | first 100 days data and AI roadmap | €17,040 | proposal | **WON**, price "good" |
| metsa-group | demand and inventory forecasting analytics, 46 person-days | €43,200 | proposal | LOST, price "fair" |
| outokumpu | staffing, 6–12 months | €37,875 | proposal | LOST, price "fair" |
| ponsse | SME CPQ reporting | €20,800 | proposal | LOST, price "excellent" |
| posti | streaming and event ingestion pipeline | €43,240 | proposal | **WON**, price "excellent" |
| savings-banks-group | cloud data platform cost and FinOps cleanup | €9,000 | proposal | LOST, price "over budget" |
| tokmanni | legacy application and reporting modernisation | €218,625 | proposal | LOST, price "over budget" |
| upm | first 100 days data and AI roadmap | €16,920 | proposal | **WON**, price "good" |
| varma | lab-to-production MLOps | €66,450 | proposal | LOST, price "fair" |
| valmet | first phase greenfield lakehouse platform | €33,120 | feedback | no price complaint |


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
| mandatum | AI Act readiness (probe, tiers €13.8k / €27.6k / €50.6k) | tiers | feedback | "full scope … sits firmly above our approved budget"; wants discovery-paced, not a rigid lump sum |
| fennia | platform phase 1 (probe, same tiers) | tiers | feedback | no price complaint ("close but not there yet"); worry: ramp-up on their core insurance system |
| posti | streaming pipeline (probe, same tiers) | tiers | feedback | no price complaint; wants hypercare / run support through peak season |
| vahterus | legacy reporting (probe, same tiers) | tiers | feedback | no price complaint; wants reporting inside the ERP (not a separate BI tool) and a deck in Finnish |
| terveystalo | arch assessment (probe, same tiers) | tiers | feedback | no reply |
| terveystalo | architecture assessment, 19 pd | €17,480 | proposal | LOST, price "over budget" ("well beyond"); budget < €17k |
| aktia | ticket-to-PR agent (VDE: 36 pd + 3 VDE months) | €61,080 | proposal | LOST, price "over budget" ("still orbiting a reality far beyond"); buyer_fit excellent, presentation excellent; disliked: dedicated agent identities instead of inheriting developer credentials |
| mandatum | legacy app & reporting modernisation, fixed discovery + capped phase, 27 pd | €25,240 | proposal | **WON**, price "excellent" |
| terveystalo | analytics engineer 6 months, part-time 17 pd | €15,640 | proposal | **WON**, price "excellent" |
| fingrid | invoice exception automation, ~21 pd | €19,720 | proposal | LOST, price "fair"; ROI defined as hours saved/task duration was rejected |
