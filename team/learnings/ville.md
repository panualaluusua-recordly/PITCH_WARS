# ville: learnings (Ville's Claude session, 2026-10-29)

Full detail and evidence: `.claude/skills/price-check/evidence.md` and `.claude/skills/rfp-trap-scan/catalog.md`.

## Results we caused
- **city-of-helsinki** squad: 4 rounds → **WON €84k** (price excellent). Keys: standard terms with zero deviations, a month-1 source-risk probe with a go/no-go gate, pairing from week 1, Finnish runbooks, a data catalog/lineage slide, ≤ 6 slides.
- **kemira** 100-day roadmap: €78k → 54k → 29k → 22k all "over budget" → **WON €16.5k**. Removing scope creep (docs assistant, CSRD) was also needed.
- **aktia** DW: €365k → 148k "over" → €95k no reply → **LOST at €88k** (price "good") because of an unrequested ML anomaly-detection add-on.
- Helsinki SME platform: €61.1k "flat out above budget"; disliked a "monolithic fixed sum". Next version: fixed discovery + capped phases.

## Rules that came out of it
1. Every past-failure sentence in an RFP or bio is a hidden requirement; everything the bio praises is a hidden preference (Terveystalo lost for missing the AI its bio praised).
2. No AI/ML add-ons unless the RFP or bio asks. Never claim experience on a buyer's proprietary platform.
3. Recordly dark/lime theme (`.claude/skills/recordly-deck/render.py`). The white/teal deck got recordly_style "weak".
4. Price: one clear total, days × rate, role minimums (DE €115/h, AI DE €120/h, DA €125/h). Fit the scope to the budget; don't cut the rate.
5. Max 3 feedback rounds (Aktia: no reply on the 4th; Enfuce: "stop asking for reviews").
6. Run `rfp-fit-check` (bid/no-bid with EV after fees) and `vde-check` before drafting.
