# Ville's offer drafts: ready for review (nothing sent to the game)

Each needs sign-offs from rauno and panu (Erika is out sick) (`team/signoffs/<buyer>.md`). **The last of the three to sign off owns submission and optimisation.** All are rendered in the Recordly dark/lime theme with `.claude/skills/recordly-deck/render.py`. Team rows are **roles, not roster names yet**; add names from `team/delivery/ROSTER.md` before sending. Rates are at the team minimums (DE/architect €920/day, AI DE €960/day, DA €1,000/day).

| Buyer | Deck | Price | Person-days | Main bets | Open items before sending |
|---|---|---|---|---|---|
| kemira (we won before) | `team/decks/kemira/…hackathon…-v1` | €12,200 | 13 | Edge-case slide (answers past overpromise), read-only agents on certified Datasphere views, a person approves, seed agent demoed hour 1 | Azure model endpoint and data access unconfirmed; participant count assumed |
| city-of-helsinki (we won before) | `team/decks/city-of-helsinki/…sme…-v2` | €43,440 max | 46 | Fixed discovery €10,440 + capped build (he disliked a monolithic lump sum), 4 slides, on site Tue/Thu, prices firm 9 months | v1 at €61.1k was "flat out above budget"; budget still unknown |
| aktia | `team/decks/aktia/…ticket-to-merge-request…-v1` | €60,440 | 36 + VDE 3 mo | Agent can't merge its own work (answers their post-mortem), EU-tenant models, definition/delivery/ops split, no ML add-ons (lost last time on that) | Stack not confirmed Snowflake: gate in Definition; financial statements text is generic |
| sanoma | `team/decks/sanoma/…backlog-agent-v1` | €51,120 | 26 + VDE 3 mo | 2-day co-build hackathon first, "when it fails" table, no zero-defect promise | No budget evidence; fallback: hackathon + short human-only pilot ≈ €15–25k |
| alko | `team/decks/alko/…-v1` (in Finnish) | €35,280 | 38 | Everything in Finnish, actual matching rules shown, item + supplier masters only, quality scorecard | Price untested; fallback ≈ €26k (28 pd) |
| yliopiston-apteekki | `team/decks/yliopiston-apteekki/…-v1` (in Finnish) | €16,560 | 18 | No client-side tracking (knockout criterion), 6 weeks, plain-Finnish decision memo | 2 references are anonymised placeholders; match them to real cases |
| veikkaus | `team/decks/veikkaus/…-v1` | €18,400 | 20 | Evidence cards, licence utilisation first (no new tools), native-reviewed Finnish + Swedish | Needs a real Swedish speaker from the roster; fallback €14,720 |
| elisa | `team/decks/elisa/…-v1` | €20,240 | 22 | Paid 4-day scoping sprint + gate, honest "Yes if" on real-time, no timesheets, recruit-after-12-months accepted | 50% unused-day credit is our own commitment (keep or drop); fallback €16,560 |

VDE variants for upm, vr-group, valmet and savings-banks-group are in `team/vde/` (README there).

## Batch 2: remaining A/B buyers (takeovers and merges)

| Buyer | Deck | Price | Basis | Open items |
|---|---|---|---|---|
| upm | `team/decks/upm/…-v2` | €107,400 | Merge of panu's tech and delivery slides with the VDE variant: Henna 60% (78 pd × €960) + Tuomas 6 pd + VDE 3 mo | ROSTER says Henna 100%; update it if adopted. Part-time vs "embedded" may score lower |
| vr-group | `team/decks/vr-group/…-v2` | €109,800 | Merge: Jari 60% + Tuomas 12 pd + VDE Feb–Apr (non-prod in the Q1 freeze) | ROSTER says Jari 100%. dbt is unconfirmed, so the VDE months may need re-scoping |
| kela | `team/decks/kela/…-v2` | €23,920 | Takeover of v1 feedback (kept the security gate and tagging register): 26 pd × €920 | Requirement matrix rows are "assumed" |
| lahitapiola | `team/decks/lahitapiola/…-v2` | €16,640 | Takeover: data foundation baseline first (feedback), Finnish, on site in Espoo; 18 pd | EU-hosted AI endpoint claims need checking |
| alma-media | `team/decks/alma-media/…-v2` | €37,600 | Takeover: lean pair kept (praised), row-level access gate, proof on real data; 40 pd | v1 price unknown |
| enfuce | `team/decks/enfuce/…-v1` | €20,240 | New project after the win: handoff/sign-off bottlenecks first, no claim on their card platform, VDE only mentioned; 22 pd | Buyer said "stop asking for reviews": go straight to a proposal |
| s-group | `team/decks/s-group/…-v2` (in Finnish) | €55,200 | Takeover: v1 hint criticised English and the missing payroll-transition clause; 60 pd × €920 + rate card with tiers ≥ minimums | Finnish text check; tier discounts are our own proposal |
| ponsse | `team/decks/ponsse/…-v2` | €30,320 | Takeover: 2-week Phase 0 + gate, exec dashboard in 6 weeks (feedback: no massive rollout); 32 pd | v1 price unknown; fallback ≈ €21k |
