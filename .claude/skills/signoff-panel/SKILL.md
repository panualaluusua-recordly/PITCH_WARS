---
name: signoff-panel
description: Runs the full pre-sign-off review of one Pitch Wars offer version (claims, tech, deck critique, rate floor, roster, language) in parallel and produces a draft sign-off line for team/signoffs/<buyer_id>.md. Use before any player or agent records a sign-off, and when the last sign-off decides who owns the offer.
allowed-tools: Read, Grep, Glob, Bash, Agent
---

# Sign-off panel

The rule: Panu, Rauno and Ville each sign off every offer; the last one owns submission. A sign-off should mean
something, so it is backed by the same checks every time. This skill runs them in parallel from the main session
(sub-agents cannot start other sub-agents).

## Inputs

- Buyer id and version (deck at `team/decks/<buyer_id>/<project_id>-v<N>.md` or the desk offer's `deck_md`).
- Existing `team/signoffs/<buyer_id>.md`.

## Steps

1. Start these agents in one message, each with the deck text, version, price and buyer id:
   `claims-auditor`, `tech-critic`, `deck-critic`. Add `compliance-analyst` for regulated buyers (finance,
   insurance, health, public sector) and `language-editor` when the buyer wrote in Finnish or Swedish.
2. Check yourself, from files: price ≥ person-days × role minimum (`price-check`), one total, roster rows exist and
   stay ≤ 100% (`team/delivery/ROSTER.md`), no `placeholder` or `TBD` text in the deck, the PDF exists and its page
   count matches the slide plan, file name carries `eur<price>`.
3. Merge into one verdict. Any `contradicted` claim, floor breach or over-booked person is `fix:`. A single
   concrete change goes in the line; the rest goes in the report.
4. Draft the line, in the format of `team/signoffs/README.md`:
   `| <player> | <UTC time> | v<N> | ok | fix: <one concrete change> |`.

## Output

```
Offer: <buyer_id> v<N> €<price>
Panel: claims <verdict> | tech <verdict> | critic <verdict> | floor <ok|breach> | roster <ok|conflict> | placeholders <n>
Blocking: - <finding> ← "<quote>"
Draft sign-off line: | <player> | <time> | v<N> | <ok | fix: …> |
Signed so far: <players> → this sign-off would make <player> the owner | not the last
```

## Do not

- Do not append the line yourself unless the player tells you to; a sign-off is their statement.
- Do not decide who owns the offer; report whether this sign-off would be the last.
- Do not send or approve anything.
- Stay in your lane: report rule breaches as facts with their source; do not take positions on the price level,
  storyline or contract terms. Say so in every sub-agent brief.
