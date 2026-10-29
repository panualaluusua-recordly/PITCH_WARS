---
name: reply-reader
description: Turns a Pitch Wars buyer reply (feedback hints or a proposal verdict with its review) into a structured diagnosis and ONE next action. Use right after any request returns, when reading a buyer's conversation history, or when deciding between another feedback round and a proposal.
allowed-tools: Read, Write, Edit, Grep
---

# Reply reader

Buyer replies mix persona flavour ("I'd rather raise geese") with real signals. This skill separates them and decides the next move.

## Inputs

- The reply JSON (saved next to the deck as `*-feedback-reply.json` or `*-proposal-reply.json`), or the buyer's `conversation` from `GET /api/buyers`
- The deck version it refers to (`work/decks/<buyer>/<project>-vN.md`). For a teammate's reply there is no local deck: use the `deck` name from the conversation entry, write the price as `unknown`, and skip the evidence row.
- `work/buyers/<buyer_id>.md`

## Steps

1. **Price signal.** Quote the exact words. Classify as `over-hard` (flatly, completely, entirely, non-starter), `over-soft` (trim, inflated, a bit high), `none` (price not mentioned), or `ok`.
2. **Liked.** List what they credited. **These must stay unchanged in the next version.**
3. **Disliked.** List each complaint, rewritten as a concrete change ("too many slides" → "cut to ≤5 slides").
4. **Ignore the flavour.** Personal-life remarks are persona colour, not requests.
5. **For a proposal verdict**, read the `review` too: every rating that isn't excellent/good, every preference that's `leans against`, `partly met` or `not addressed`, and every presentation criterion below `strong`. A buyer's `next_project_id` means a new RFP: run `rfp-trap-scan` on it.
6. **Decide the next action:**
   - `no_reply: true` → the buyer may be tired of us. Don't send another feedback round; propose with the best version, or move on.
   - Price `none`/`ok` and at most one small complaint → fix it and **send a proposal**.
   - Price over → apply `price-check`; one more feedback round only if it's the first or second round.
   - Already 3 feedback rounds → propose, don't ask again.
   - A presentation criterion below strong (e.g. `recordly_style: weak`) → list it under Fix; it costs points on every future deck.
7. Append the diagnosis to `work/buyers/<buyer_id>.md`, add a row to `.claude/skills/price-check/evidence.md` when price was mentioned, and add any lesson that generalises to `.claude/skills/rfp-trap-scan/catalog.md`.

## Output

```
Reply to: <deck file> (<kind>, €<price>)
Price signal: <class> ← "<quote>"
Keep: - …
Fix: - <concrete change> ← "<quote>"
Review gaps (proposals): - …
Next action: <feedback vN+1 | proposal vN+1 | move on> because <reason>
The one change to make: <single change>   (a price change plus ONE content change may be bundled when the buyer explicitly asked for both and ≤1 feedback round is left)
```

## Example (real)

```
Reply to: city-of-helsinki-...-v2.pdf (feedback, €138,000)
Price signal: over-hard ← "price sits well above what we aimed for"
Keep: - month-1 source-probing sprint ("avoids deploying on quicksand")
Fix: - cut to ≤6 slides ← "sprawling deck packed with far too many slides"
     - pairing from week 1 ← "knowledge sharing to a handover phase near the very end"
Next action: feedback v3 at €84k (price-check: cut ≥30%)
Outcome: v3 had no price complaint; v4 won at €84k.
```

## Do not

- Do not treat "not rated yet" or a missing price remark as a price problem.
- Do not throw away what the buyer praised when fixing complaints.
- Do not send a fourth feedback round to the same project.
