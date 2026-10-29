---
name: architecture-patterns
description: Maps a Pitch Wars RFP's and bio's tech triggers to Recordly's pattern library (P1–P16) and turns them into an architecture slide with a diagram plus a tech gates and risks slide. Use whenever a deck needs its architecture or technical answers, when a new project opens, or when a reply or review praised or punished a tech choice.
allowed-tools: Read, Grep, Write, Bash
---

# Architecture patterns

Our lens is tech and architecture. Reviews mark `project_fit` and `explanatory_visuals` down when the deck lacks a
diagram or skips a technical "past problem". This skill makes the answer systematic. The library is `patterns.md`
in this folder: **read it every time**.

## Inputs

- `rfp-trap-scan` output for the buyer (or the RFP, bio and replies if it is missing)
- `patterns.md`, `team/tech/TECH_SCOPE.md` (what is ours and what is not)
- `vde-check` verdict, if any (it changes the architecture only on Snowflake + dbt)

## Steps

1. **Trigger scan.** For every trigger phrase in `patterns.md`, find it in the RFP or bio. Record the quote and the
   pattern id. A tech sentence that matches no pattern is a candidate new pattern: list it for `feedback-miner`.
2. **Stack.** Name the buyer's own stack from the RFP and bio. Everything in the diagram runs on it: no new
   platform or licence unless the RFP asks (P7). If the stack is unknown, say so and make Phase 0 find out (P3).
3. **Architecture slide.** Action title that states the point. A `diagram` (deck.py format: columns sources →
   extraction → storage/model → serving, plus a band for where code, CI/CD and access control live). Max 12 boxes,
   real product names from their stack, no stock graphics. 3 bullets: the mechanism for each top trigger.
4. **Gates and risks slide.** The de-risking first step with a numeric go/no-go gate (P3, P4, P13), the freeze
   windows (P9), and 3–4 honest technical unknowns with how each is resolved. This feeds `honest_unknowns`.
5. **Effort basis.** Person-days per phase for the price owner (T7). Never a price.
6. **Scope fence.** List what the patterns tempt us to add and we leave out. AI/ML is out unless the RFP or bio asks.
7. Write `work/tech/<buyer_id>.md` (analysis) and `work/specs/<buyer_id>-tech.json` (the two slide objects).

## Output

```
Buyer: <id> · Stack: <their stack> ← "<quote>"
Triggers: - P<n> ← "<quote>" → <our answer in one line>
Candidate new patterns: - <tech sentence> (no match)
Slides: work/specs/<buyer_id>-tech.json (architecture + diagram, gates and risks)
Effort basis: phase 0 <d> days, phase 1 <d> days …
Left out on purpose: - …
```

## Status rules (learning loop)

A pattern in `patterns.md` is `candidate` until two independent buyers confirm it with a review quote, then `rule`.
One refutation marks it `conditional` with the quote. `feedback-miner` is the only role that edits the library, and
only with a quote from a real reply.

## Do not

- Do not invent a stack or product the buyer does not use. Do not claim experience on their proprietary platform.
- Do not add AI/ML or streaming because the pattern exists; the RFP or bio must trigger it.
- Do not output more than two slides. The deck-writer fits them into the cover + 5 limit.
