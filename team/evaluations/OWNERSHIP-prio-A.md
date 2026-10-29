# Prio A ownership: hands off

From 2026-10-29 ~10:45 UTC, **Ville owns kemira, s-group, upm, vr-group and valmet** (Prio A in `rfp-heatmap-2026-10-29.md`). Ville's agent reviews, submits and optimises them in the game, overriding the three-person sign-off for these five.

- Don't send requests to these buyers, don't post new versions, and don't change their roster rows.
- Valmet: Rauno's staffing review (`team/STAFFING_STATUS.md`) is welcome as a comment, but Ville decides and sends.
- Every send and reply is logged in `team/buyers/<buyer>.md`.

## Game log (Ville)
| Buyer | Sent | Price | Buyer reply (summary) | Next |
|---|---|---|---|---|
| kemira | v1 feedback | €12,200 | Liked: prior delivery, Azure/Datasphere only, live demo on real plant feeds. Disliked: static validation rule catalogs | v2 (adaptive baselines) sent as **proposal** |
| upm | v2 feedback | €107,400 | Over budget; wants a dedicated coordinator for delivery accountability | v3 €75,480 (VDE optional, Tuomas as coordinator) sent as feedback |
| vr-group | v2 feedback | €109,800 | Liked: Finnish native, rail domain. Flat-out over budget; rigid lump sum too inflexible | v3 capped at €73,600, monthly on actual days, adjustable, sent as feedback |
| s-group | v2 feedback | €55,200 | Liked: day-one start, Finnish, no fluff. Wants visible commercial impact (margin, checkout conversion), not just plumbing | v3 (commercial KPIs, result in week 4) sent as **proposal** |
| valmet | — | — | (applied UPM/VR lessons first) | v3 capped at €73,600 sent as feedback |

Savings Banks v2 (€45,080, human-led, VDE optional) is in `team/decks/savings-banks-group/` for the B-priority owners; it isn't Prio A.
| kemira | migration v1 fb | €55,200 | (pending) | new project kemira-platform-migration-two-warehouses |
| s-group | ticket→MR agent v1 fb | €42,880 | (pending) | new project after the win |
| upm | MLOps v1 fb | €56,960 | (after cooldown) | adds assistants and staff-time table, stage payments |
| vr-group | automation build v1 fb | €43,560 (incl. VDE 3 mo) | (after cooldown) | VDE: PRs only, human approves; fixed price vs billed boilerplate hours |
| valmet | exploration v1 fb | €24,480 | (after cooldown) | client time ≤ 4 h/week, demo on real data at week 3, explainable flags |

### Results after round 3 (12:08 UTC)
| Buyer · project | Price | Result | Why |
|---|---|---|---|
| kemira · platform migration | €55,200 | **WON** (price excellent) | lean, existing Azure/Datasphere, human-started LLM reloads |
| s-group · ticket→MR agent | €21,400 | **WON** | Azure-only, reuse existing blueprints, minimal developer drain |
| valmet · machine data exploration | €24,480 | **WON** (all excellent) | in Snowflake, plain-language flags, no techs pulled off shift, milestones |
| upm · MLOps | €56,960 max | LOST (price good) | missing: model confidence scoring + source lineage |
| vr-group · automation build | €18,400 cap | LOST (price fair) | budget very small even at €18k |
| s-group · AI/MCP hackathon | €9,400 | LOST (price excellent) | customer service AI not addressed |

Open now: kemira data platform phase 1 (fb pending), valmet 100-day roadmap €16,880, upm 100-day roadmap €16,920, vr-group data catalogue €10,120 cap, s-group lead data architect (drafting).
