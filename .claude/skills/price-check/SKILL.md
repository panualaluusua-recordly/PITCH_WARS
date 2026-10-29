---
name: price-check
description: Decides the euro total to put on a Pitch Wars deck, and how to present it, using the team's price evidence and the buyer's earlier replies. Use before any feedback or proposal deck is sent, when a reply mentions budget, or when someone asks "what should we charge".
allowed-tools: Read, Grep
---

# Price check

Budgets in this game are **far below real consulting rates** and vary by project, unrelated to effort.

## Rate floor (team rule, non-negotiable)

Minimum rates per role, at 8 h per person-day (team rules, Ville and Rauno):
| Role | Min €/h | Min €/day |
|---|---|---|
| Data engineer, architect, other roles | 115 | 920 |
| AI / ML data engineer | 120 | 960 |
| Data analyst | 125 | 1,000 |
| AI data analyst | 130 | 1,040 |
- No price may average below **€110/h overall**. In practice the role minimums above apply to every line.
- At most 2 architects per team. Names come only from the team roster (`team/delivery/ROSTER.md` in the team repo).
- To fit a low budget, **cut scope and person-days, never the rate**: fewer people, shorter duration, a discovery phase only, or a smaller first phase.
- If the smallest credible scope at the role minimum still exceeds the buyer's likely budget, don't bid (`rfp-fit-check` gate).

## Inputs

- The project type and scope (from `rfp-trap-scan` output)
- Earlier price verdicts for this buyer (from the `reply-reader` output or the conversation)
- `evidence.md` in this folder: every price we have tested and the verdict it got. **Read it every time.**

## Steps

1. **Anchor.** Find the closest project type in `evidence.md`. With no earlier signal for this buyer, start at the anchor in the table below.
2. **Adjust for this buyer.** "Over budget" / "flatly above" → cut at least 30%. "Completely above" / "dramatically" → cut 50%+. "Trim" / "inflated" (soft wording) → cut 20–25% and propose. No price complaint → keep the price, and send the proposal. Price rated "excellent" on a win → the budget had headroom; next time for the same buyer, try +10%.
3. **Check for a lost-proposal case.** If a proposal was lost with price "good" or "excellent", the price was not the problem. Don't cut it further.
4. **VDE line.** If `vde-check` says INCLUDE, price = human person-days × day rate + VDE months × €9,000 (flat). The floor applies to human days only; the VDE fee is not hours.
5. **Apply the rate floor.** Compute person-days for the proposed scope and check that price ≥ person-days × role minimum. If not, reduce the person-days (scope) until it holds. Never lower the rate.
6. **Present it.**
   - State **one fixed total** clearly on the summary slide and the price slide. Repeat it at most once more.
   - Show the breakdown as person-days × day rate (rate ≥ role minimum). The buyer must be able to see the days and the rate. Avoid percentages that hide the effort. Avoid several separate € subtotals that could be added up wrongly.
   - Payment terms, "no new licences", "VAT 0%".
   - If the buyer fears rigid lump sums (Helsinki SME hint), offer a **fixed discovery fee plus a capped build** instead of one monolithic sum.
7. Log the price, person-days, VDE months and the verdict in `evidence.md` after every reply.

## Starting anchors (update as evidence grows)

Budget evidence says what buyers will pay. The **max person-days** column says how much scope fits that budget at the €920/day floor. Scope the deck to that.

| Project type | Likely budget | Max person-days at €920 | Evidence |
|---|---|---|---|
| Squad / staff aug, 6 months | €84–94k | ~95–105 days (e.g. 1 FTE for ~5 months, not 2 people for 6) | Helsinki won €84k for 2 × 6 months (≈ €44/h, **below floor**, don't repeat); Enfuce won €93.6k |
| Roadmap / assessment, ~3 months | €16k | ~18 days (e.g. 1 senior, 2 days/week for 9 weeks) | Kemira won €16.5k for a 3-person, 12-week plan (**far below floor**) |
| Platform build / migration | ≤ €88k | ~100 days: a first phase or MVP, not the full programme | Aktia: €88k "good", €148k over |
| BI / reporting platform | < €61k | ~45–60 days | Helsinki SME: €61k over |
| Pilot / hackathon / PoC | €10–15k | 11–17 days | No evidence yet |

## Output

```
Price: €<total> = <person-days> × €<day rate ≥ role min> (avg €<n>/h) [+ VDE <m> × €9,000]
Presentation: <fixed total | discovery fixed + capped build | monthly fee × months>
Reason: <evidence used, quoting verdicts>
Confidence: low | medium | high
Next if over budget: €<lower price>
```

## Do not

- Do not offer a rate under the role minimum (DE €115/h, AI DE €120/h, DA €125/h), even if the buyer pushes. Shrink the scope instead.
- Do not promise full-scope delivery at a budget price. Every first attempt at full scope was over budget; fit the scope to the budget.
- Do not cut the price after a loss that the review attributes to something else.
- Do not change the price and the scope in the same feedback round unless the clock forces it. You won't know which change the buyer reacted to.
