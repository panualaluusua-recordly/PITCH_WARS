---
name: reply-ingest
description: Pulls every buyer reply from the game API into team/buyers/<id>.md and team/evaluations/reply-signals.md, so replies triggered by teammates are not lost, and then turns the new ones into price evidence and lessons. Use at session start, after any request returns, and before pricing or revising any offer.
allowed-tools: Read, Grep, Edit, Bash
---

# Reply ingest

Several players share one token, and replies to their requests land in the game, not in the repo. At the last run
17 buyers had replies and 12 of them were nowhere in the repo. Pricing and revising without them repeats mistakes.

## Steps

1. Run `python -X utf8 team/bin/ingest_replies.py --fetch`. It is read-only against the game, never prints the
   token, and rewrites only the auto section (between `<!-- replies:auto -->` markers) of each buyer note.
2. Read `team/evaluations/reply-signals.md`. For every buyer whose signal is `over-hard` or `over-soft` and who is
   not yet in `.claude/skills/price-check/evidence.md`, add a row to the "unknown price" table with the quote.
   The price stays `unknown` until the deck file name carries it (`…-eur<price>.pdf`); ask the player who sent it.
3. Run `reply-reader` on each reply new since the last run. Put the diagnosis under the markers, not inside them.
4. Hand lessons that generalise to `feedback-miner` (playbook, patterns, trap catalog).

## Output

```
Ingested: <n> replies from <m> buyers (<k> new)
Price signals not yet in evidence: <buyer: signal, quote>
Buyers with replies and no repo work: <list>
Next: <who should run reply-reader on which buyer>
```

## Do not

- Do not edit inside the markers; the next run overwrites them.
- Do not treat a price signal as an anchor when the price is unknown.
- Do not send anything; this skill only reads the game.
