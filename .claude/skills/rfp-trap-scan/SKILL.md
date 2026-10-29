---
name: rfp-trap-scan
description: Scans a Pitch Wars buyer's bio, RFP and conversation for explicit asks, hidden requirements, traps and buyer preferences, and returns a requirement list a deck must answer. Use before writing or reviewing any deck, when a new project opens, or when someone asks "what does this buyer really want".
allowed-tools: Read, Grep, Bash
---

# RFP trap scan

Turns one buyer's texts into a checklist that the deck writer must answer and the deck critic can check. Buyers are LLM personas: **every concrete detail in the bio or RFP is planted on purpose** and is likely to be scored.

## Inputs

- The buyer object from `GET /api/buyers`: `bio`, `title`, `company_*` fields, the `open` project's `rfp`, and every earlier `conversation` entry (hints, verdicts, reviews), including **closed projects** of the same buyer.
- `work/buyers/<buyer_id>.md` if it exists.
- If the conversation has replies, run the `reply-reader` skill on them first.

## Steps

1. **Explicit asks.** List every section the RFP asks the deck to cover, in its order and with its words. Each becomes a deck heading.
2. **Hard constraints.** Pull every "must", "required", "mandatory" and every numeric condition (on-site days, references count, price validity, Q1 freeze, availability at signature).
3. **Past-failure sentences = hidden requirements; praised experiences = hidden preferences.** For each sentence about something that went wrong before (in the RFP *or* bio), write the opposite as a requirement. For each thing the bio praises or aspires to, show we can deliver it, inside scope. Use `catalog.md` to map common patterns.
4. **Traps.** Flag anything where the naive answer loses (see `catalog.md` → Traps): impossible demands, contract terms, binding blueprints from another vendor, "propose extraction for all sources", AI hype bait.
5. **Persona preferences.** From the bio: language, meeting tolerance, team size, risk appetite, ego (wants visible wins? quiet evenings?), what they despise (glossy decks, binders, status meetings).
6. **Scope fence.** Write one line on what is IN scope and list tempting add-ons that are OUT (extra AI, extra use cases, new platforms or licences).
7. **Standing requirements (every buyer, every time):** Recordly style (dark background, lime accents), at least one process or flow diagram/table, one consistent storyline, one clear total price.
8. **Format signals.** "concise", "preliminary", "technical briefing" mean 4–6 slides. "Comprehensive" means up to 9. A required compliance matrix adds 1–2 slides. Never more than 10. If the RFP refers to requirements it doesn't list, write assumed rows and label them "assumed".

## Output

```
Buyer: <id> · <name>, <title> · Project: <project_id>
Deck sections (RFP order): 1. … 2. …
Hard constraints: - … (quote)
Hidden requirements: - <requirement> ← "<quoted evidence>"
Traps: - <trap> → <how to answer>
Persona: language=<fi/sv/en>, team=<size>, tone=<…>, hates=<…>, wants=<…>
Scope fence: IN <…> | OUT <…>
Slide target: <n>
Price signals: <any budget words, earlier price verdicts>
```

Every line must quote its evidence. If something is a guess, mark it `(guess)`.

## Do not

- Do not summarise the RFP. Extract requirements.
- Do not skip bio details because they look like flavour. They are scoring criteria.
- Do not recommend AI or ML features unless the RFP asks for AI *in the solution* **or the bio shows the buyer wants it** (praises an AI assistant, "charting paths" to agents). Aktia was lost over an unrequested ML add-on; Terveystalo was lost for *missing* the conversational AI its bio praised. Read the bio for hopes as well as fears.
