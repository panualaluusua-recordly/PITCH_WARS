# Virtual Data Engineer (VDE) offer variants (Ville)

**Status: drafts for review. Nothing sent to the game.** Each needs a desk offer, a deck-critic review and a human approval.

## What the VDE is (source: Recordly Drive deck "VDE-Snowflake-12_10_2026")
Recordly's team of AI agents (data engineer, review and auditor agents). It **runs inside the customer's Snowflake account** on their Snowflake AI credits and works from Slack, GitHub and dbt alerts. It opens PRs only; **a person approves every change**. Facts we may claim: `.claude/skills/vde-check/vde-facts.md`.

**Commercial rule:** €9,000/month flat, fixed term of at least 3 months, sold together with the human team. It takes ~70% of the simple work (runs 24/7) but needs **more senior architecture time** (8–10 days of setup + 2–3 days/month). Run mode: for continuous dev, maintenance or monitoring, the customer's staff approve the changes and Recordly keeps ~1 day/month.

## Variants

These use names from `team/delivery/ROSTER.md` and the role rates from `team/STAFFING_STATUS.md` (DE €115/h → €920/day, AI DE €120/h → €960/day).

| Buyer | Offer owner / other work | VDE variant | Price | vs human-only basis (batch2) |
|---|---|---|---|---|
| **upm** | delivery slides `team/delivery/slides/upm` | Henna Kallio 60% (78 pd × €960) + Tuomas Rantanen 6 pd + VDE months 4–6 | **€107,640** (6 × €17,940) | 120 pd × €960 = €115,200: **cheaper** |
| **vr-group** | delivery slides `team/delivery/slides/vr-group` | Jari Lehtonen 60% (78 pd × €920) + Tuomas 12 pd + VDE Feb–Apr (non-prod during the Q1 freeze) | **€109,800** (6 × €18,300) | 132 pd × €920 = €121,440: **cheaper** |
| **valmet** | **Rauno owns staffing** (`team/STAFFING_STATUS.md`) | Laura Heikkilä 60% (78 pd × €920) + Tuomas 6 pd + VDE months 4–6 | **€104,280** (6 × €17,380) | 120 pd × €920 = €110,400: **cheaper**. Rauno, use or ignore. |
| **savings-banks-group** | delivery slides `team/delivery/slides/savings-banks-group` | Johanna Berg / Markus Ek / Kaisa Virta: definition 8 pd + delivery 22 pd; **ongoing = VDE run mode** 3 months + 3 pd | **€57,360** | batch2 basis 25 + 70 pd + 3 pd/month is much larger. **Effort mismatch: price owner decides.** |

Files: `offers/<project>-vde-v1.md` (source) and `.pdf` (rendered in the Recordly dark/lime theme with `.claude/skills/recordly-deck/render.py`).

## If a variant is adopted
- Update `ROSTER.md`: Henna / Jari / Laura drop 100% → 60%, and Tuomas gains valmet 5% (his total goes 40% → 45%).
- Run `deck-critic`, post on the desk, and wait for a human Approve. Then use `send.py` as usual.

## Open risks for reviewers
- Savings Banks: their bio is wary of "proprietary non-European AI toolchains". The VDE runs on Snowflake's own AI services inside their account. Check that this wording doesn't over-claim.
- The certifications listed are copied from ROSTER.md. Don't add any that aren't there.
