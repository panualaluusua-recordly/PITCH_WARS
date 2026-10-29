# Kemira tech slides: rationale

Spec: `team/tech/slides/kemira.json` (deck.py preview: `kemira.pdf`). Deck version: `team/decks/kemira/...-v4.md` (built on the v3 that already had the tech-critic fixes).

Placement (no new slides, deck stays at 6): the architecture slide replaces the table on slide 2 "Technical approach and deliverables" (RFP heading kept); the gates & risks content goes into the plan slide (slide 4) as a "Technical gate" column plus the risks callout. Buyer earlier marked "[met] keeping architecture to a concise note", so we merged rather than added.

Patterns applied: P2 (read-only, propose, person approves; no SAP write-back), P5 (per-user identity so SAP plant authorisations apply; restricted test user gate), P7 (their Azure, Datasphere, SAC; no new licences), P13 (seed agent measured on real data before the event, live demo), P4 (one plant's space first), P8 (step/token cap per run, per-team cap, budget alert; no euro figures).

Fixes from work/tech/kemira.md "Notes for deck owner": #1 diagram added; #2 identity mechanism + per-role fallback stated as prep decision; #3 S/4HANA vs Datasphere contradiction removed; #4 restricted rows: "limited by authorisation, without counts"; #5 live demo made conditional on week-2/3 gates, masked-extract fallback; #6 masking: data owner lists fields, masking in access layer; #7 "sandbox data, not for production use"; #8 free-text instruction risk, ground-truth dependence, identity risk added; #9 targets after first measured run (kept); #10 no product names beyond RFP; #11 run log location stated.

Left out on purpose: direct S/4HANA connection, SAP write-back, production chat bot, autonomous resolution, new platforms/licences, named Azure AI products, euro-per-run cost figures, side quests (docs assistant, CSRD).

Effort basis: unchanged (prep 5, hackathon 5, follow-up 3 person-days per the deck). The new gates fit inside prep; the risk is data-owner labelling time on Kemira's side, not ours.
