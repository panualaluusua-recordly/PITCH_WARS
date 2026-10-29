---
name: recordly-deck
description: Writes a Pitch Wars pitch deck as Markdown in the Recordly 2026 style, renders it to PDF for the team desk. Use when writing, revising or rendering any deck for a buyer.
allowed-tools: Read, Write, Edit, Bash
---

# Recordly deck

Buyers score decks on: **client_understanding, storyline, honest_unknowns, concreteness, slide_clarity, explanatory_visuals, recordly_style.** This skill produces decks that score "strong" on all of them.

## Inputs

- `rfp-trap-scan` output for the buyer (required; run it first if it's missing)
- The price and presentation from `price-check` (required)
- Earlier deck versions in `work/decks/<buyer_id>/` and `reply-reader` diagnoses

## Steps

1. Copy the structure of `example-won-helsinki.md` (won, presentation rated "excellent").
2. Write `work/decks/<buyer_id>/<project_id>-v<N>.md`. Never overwrite a version that has been sent.
3. Slide plan (default 5–7 slides; respect the slide target):
   1. **Cover:** the outcome in the buyer's words, plus the price and contract stance in the subtitle
   2. **Solution:** how it works, built on their named stack, and what is explicitly out of scope
   3. **Hidden requirements answered:** one row per past failure → our safeguard
   4. **Plan:** a table with phases, go/no-go gate, Q1 freeze or other constraints, knowledge transfer from week 1
   5. **Team:** a table with role, years, exact certifications, languages and availability at signature
   6. **Price and terms:** one fixed total, person-days × day rate (role minimum: DE €920, AI DE €960, DA €1,000 per day), payment terms, licences, "No contractual deviations", accepted clauses
   7. If the brief says `VDE: INCLUDE`: show the VDE inside the team and plan slides (not as a separate sales slide). Say which tasks it takes (runs 24/7), that a senior architect sets the architecture, conventions and examples it builds on and reviews its work, that a person approves every change, that it runs in their Snowflake on their AI credits, and the fixed term at €9,000/month. Use one real result from `.claude/skills/vde-check/vde-facts.md`.
   8. Optional statement slide: one sentence and the price
4. Cover **every section the RFP asks for**, using its wording in headings.
5. Every claim needs a number, a name or a mechanism. Include one honest unknown with how we'll resolve it (e.g. "source quality unknown until week 2; the gate decides").
6. Render: `python3 .claude/skills/recordly-deck/render.py <file.md>` (Recordly dark/lime theme, Montserrat; needs Chrome). This theme scored recordly_style "strong"; the white/teal look scored "weak". Check that the PDF exists and the slide count is right.
7. Before sending, get a verdict from the `deck-critic` agent.
8. **Send only through the team desk flow:** post the version with the `pitch-desk` skill. A human approves it on the Wolves Pitch Desk, and the named sender runs `team/bin/send.py`. Put the price in the PDF filename (`…-eur<price>.pdf`) so the price shows in the game's conversation history.

## Markdown format

- First line: `<!-- title: <Company> · <Short project> -->`. Slides are separated by `---`.
- One `# H1` per slide, an optional `## lead line`, then tables, bullets or `> callout`.
- Columns: `:::cols` / `:::cols3`, separated by `:::col`, closed with `:::`.
- Statement slide: first line `<!-- statement -->`.
- Max about 120 words per slide. The renderer shrinks text that overflows, but small text hurts slide_clarity.

## Do not

- Do not add AI/ML features, extra use cases or new tools that neither the RFP nor the bio asks for (cost us Aktia). Do show AI the bio clearly hopes for (missing it cost us Terveystalo).
- Do not leave docs and training in English for buyers who flagged language issues.
- Do not list several € subtotals that could be added up into a bigger "total".
- Do not invent personal names for consultants. Use roles with real certification names.
- Do not send from this skill. Sending is gated by the desk approval and `team/bin/send.py`.
