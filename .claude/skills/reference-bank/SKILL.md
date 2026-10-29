---
name: reference-bank
description: Keeps a verified bank of Recordly customer cases and references and matches them to the references an RFP asks for, without inventing any. Use when an RFP or bio asks for references or case examples, when a deck contains an anonymised or placeholder reference, or before a deck is signed off.
allowed-tools: Read, Grep, Edit
---

# Reference bank

RFPs ask for references (Terveystalo, Kela, Yliopiston Apteekki and others). Ville's drafts carry placeholders
("2 references are anonymised placeholders"). Invented cases are an over-promise and a possible chargeback; real
cases the team forgot to use are lost points. This skill keeps one verified list in `references.md` (this folder).

## Inputs

- The RFP's reference ask (count, sector, size, platform, how recent).
- `references.md`: one row per case, with a `status` of `verified` (a human on the team confirmed it and what may
  be said), `anonymised-ok` (usable without the name) or `unverified` (never goes into a deck).
- `.claude/skills/rfp-fit-check/recordly-profile.md` ("Things we never claim").

## Steps

1. Read the RFP's ask. Pick the verified or anonymised-ok cases that match on platform, sector and size, most
   similar first. Write the wording allowed by the row (name or anonymised description, scope, outcome with its
   source).
2. If fewer cases match than the RFP asks for, say so in the deck honestly ("two anonymised references; contacts
   on request") and list the gap for the human. Do not fill it with an `unverified` row or a made-up case.
3. When a human confirms a new case, add it as a row with who confirmed it and when.
4. Report every placeholder reference found in a deck so a human can replace it.

## Output

```
Ask: <what the RFP wants> ← "<quote>"
Use: - <case id>: <wording to put in the deck> (status <verified|anonymised-ok>)
Gap: <missing references> → human to supply: <what is needed>
Placeholders in deck: - "<text>" (slide <n>)
```

## Do not

- Do not invent a customer, outcome, figure or contact person.
- Do not use `unverified` rows in a deck.
- Do not name a customer unless the row says the name may be used.
