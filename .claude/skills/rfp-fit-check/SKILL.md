---
name: rfp-fit-check
description: Decides bid / bid-with-conditions / no-bid for one Pitch Wars RFP, scoring capability fit against Recordly's profile and the roster, deliverability, buyer relationship and expected value after fees. Use before spending any fee on a new project, when a new project opens, when choosing which buyers to work on first, or when someone asks "is this RFP right for us".
allowed-tools: Read, Grep, Bash
---

# RFP fit check (bid / no-bid)

Every request costs money (feedback €1,000, proposal €3,500), and the team has only 3 reading slots at once and a clock. This skill decides **whether** to pursue a project and **how urgently**. It doesn't decide how to pitch (that's `rfp-trap-scan`).

## Inputs

- The buyer and open project from `GET /api/buyers`: bio, RFP, `stats`, `available_at`, the full `conversation` of every project (this includes teammates' requests)
- `GET /api/me`: `time_left_seconds`, fees, and `consultants` if present
- `recordly-profile.md` (this folder), `.claude/skills/price-check/evidence.md`

## Steps

1. **Hard gates.** If any one fails → **NO-BID** (or WAIT), stop:
   - No open project (`out_of_budget`) → NO-BID
   - `available_at` in the future (cooldown, e.g. 15 min after a lost proposal) → WAIT: report minutes remaining and "re-run after <available_at>"
   - Core of the work is "Not us (0)" in the profile
   - A mandatory requirement we can't meet truthfully (e.g. roster lacks the required role or availability; a required proprietary-platform track record; full-time on-site far from our offices if we can't staff it). If `/api/me` has no `consultants`, judge from `recordly-profile.md` and mark deliverability "unverified (no roster)"
   - **Rate floor:** the smallest credible scope × the role minimum (€920+/day) is clearly above the likely budget B → NO-BID
   - Less than ~10 minutes left on the clock and no proposal-ready deck
   - **Teammate active** (this is the single definition; other files refer to it): the **open** project's `status` field equals `"thinking"` (a deck is being read right now), or its latest conversation `at` is less than 3 minutes old (someone may be about to send the next version). Entries are stamped when the reply arrives, so `status` is the only live signal → WAIT and coordinate. Activity on closed projects never blocks.

2. **Score fit (0–3 each).** Quote evidence for each score.
   | Criterion | 3 | 0 |
   |---|---|---|
   | Capability | Core tier, stack we know | Not us |
   | Deliverability | Team size 1–4, roster/available, scope bounded | Needs a big crew or unavailable roles |
   | Requirement risk | Few traps, all answerable honestly | Contradictory or impossible demands we can't qualify |
   | Hidden-preference match | Bio's positive experiences and fears map to things we do (e.g. bio praises an AI assistant → we can show gen AI) | Bio wants something we can't credibly show |
   | Relationship | 3 = past win or praise · **2 = no history yet** · 1 = one loss or mixed replies | 0 = no-replies, "stop asking for reviews", penalties |
   | Commercial | Similar budget evidence ≥ €50k | Likely < €10k |

3. **Expected value.**
   - Budget estimate B: nearest known-price row in `price-check/evidence.md` (state which). No comparable row → use the project-type anchor in `price-check/SKILL.md` and mark B `(anchor)`. A price that drew a hard over-budget verdict is an upper bound on B.
   - Win probability P: start at 0.5 when the fit total ≥ 13/18; 0.35 at 9–12; 0.2 below 9. +0.1 for a past win with this buyer; −0.15 after a loss or a no-reply.
   - Expected cost C: **future** fees only (planned feedback rounds × €1,000 + €3,500). Fees already spent are sunk.
   - EV = P × B − C. **Follow-on bonus:** a win opens the buyer's next project, so add 0.3 × B × P unless the buyer is `out_of_budget`. Ignore `out_of_budget_message`: every buyer has one, and it's only shown once the budget runs out.

4. **Decide.**
   - Priority from EV alone: **A** ≥ €25k · **B** €10–25k · **C** €0–10k · **NO-BID** ≤ €0 (or any capability/deliverability score of 0).
   - Add **"+ conditions"** when any score is 1 or a trap needs a qualified answer. List exactly what the deck must say to stay honest (e.g. "Yes if: real-time for operational KPIs, daily for financial close").
   - Decision line format: `BID-A`, `BID-C + conditions`, `NO-BID`, `WAIT(<time>)`.
   - C-priority bids use reading slots only when no A/B work is waiting.

5. **VDE.** Run `vde-check`. If it says INCLUDE, recompute B and EV with the VDE price; the VDE can make a low-budget project viable above the rate floor.
6. **Plan the spend.** Number of feedback rounds (0–2) before proposing. Use 0 when there's strong price evidence and a high fit.

## Output

```
Fit: <buyer_id> · <project_id>
Decision: BID-A | BID-B | BID-C | BID-WITH-CONDITIONS | NO-BID | WAIT(<until>)
Gates: pass | failed: <which> ← "<evidence>"
Scores: capability=<n> deliverability=<n> req_risk=<n> hidden_pref=<n> relationship=<n> commercial=<n> → <total>/18
EV: P=<p> × B=€<b> − C=€<c> (+ follow-on €<f>) = €<ev>   [B from: <evidence row>]
Conditions / honest qualifiers: - …
Spend plan: <n> feedback round(s) then proposal | proposal now | none
Biggest risk: <one line>
```

On NO-BID or WAIT, return only the `Fit`, `Decision`, `Gates` and `Spend plan` lines, plus `Re-run after: <time>` for WAIT.

## Example (real: Terveystalo's first project, scored as it should have been *before* any request, so relationship = 2 for no history)

```
Decision: BID-WITH-CONDITIONS
Scores: capability=3 deliverability=3 req_risk=2 hidden_pref=1 relationship=2 commercial=2 → 13/18
EV: P=0.5 × B=€60k − C=€5.5k (+ follow-on €9k) = €33.5k → priority A, with conditions
Conditions: - Bio praises a "digital appointment assistant" delivered by an external consultancy → the deck must show
              patient-facing conversational AI experience, or we lose on it.
              (We didn't; lost with price "good", project_fit "excellent".)
            - Productivity-gain sharing must be explicit (RFP firm requirement)
            - Finnish-language delivery (hint: "relying on English … friction")
```

## Do not

- Do not no-bid only because the price evidence is low; a win also opens the next project.
- Do not score capability from the RFP title alone. Read what the work actually is.
- Do not mark a requirement "met" if meeting it would mean claiming experience we don't have. That's an over-promise and a later penalty.
