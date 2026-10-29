# Team protocol: four Claude Code sessions, one team token

Four players run their own Claude Code sessions against the same team token. This repo is
the shared comms space. **Files are the messages**: nobody needs to chat to know who is doing what.

The game API is the source of truth for buyer state (conversations, `thinking`, fees).
This repo holds what the API does not know: **who owns a buyer, what we learned, what we sent.**

## Layout

| Path | Writer | What |
| --- | --- | --- |
| `team/claims/<buyer_id>.md` | the claimant | Lock: one buyer belongs to one player. |
| `team/buyers/<buyer_id>.md` | the claim owner | Buyer analysis, every reply received, next step. |
| `team/decks/<buyer_id>/<project_id>-v<N>.md` (+ `.pdf`) | the claim owner | Every deck version sent. |
| `team/log/<player>.md` | that player | One line per request: time, buyer, project, kind, price, outcome. |
| `team/learnings/<player>.md` | that player | Cross-buyer lessons: what wins, what loses, price signals. |
| `team/BOARD.md` | anyone (short edits) | Team-level decisions and strategy. |
| `.claude/agents/`, `.claude/skills/` | anyone, via commit | Shared agents and skills. |

Every file except `BOARD.md` has exactly one writer, so merges never conflict.

## Joining (once per player)

```bash
git -c core.longpaths=true clone <REPO_URL> PITCHWARS && cd PITCHWARS
git config core.longpaths true          # Windows: skill template paths are long
cp .env.example .env                    # paste the team token, set PITCH_WARS_PLAYER=<first name>
bash team/bin/sync.sh
```

## Rules for every agent

1. **Session start:** `bash team/bin/sync.sh`. It pulls the repo and shows the buyer board
   (API status + owner). Read `team/BOARD.md` and every file in `team/learnings/`.
2. **Before any request to a buyer:** `bash team/bin/claim.sh <buyer_id> "<short note>"`.
   - `CLAIMED` or `already yours` → go ahead.
   - `TAKEN by X` → do not send. Pick another buyer.
   - Never send to a buyer you have not claimed, even if its status is `open`.
3. **Re-check the API right before sending** (`thinking` = a request is already in flight).
   At most 3 decks are read at once across the team. On `too_many_requests`, wait and retry.
4. **After every reply:** update `team/buyers/<buyer_id>.md`, append to `team/log/<player>.md`,
   add any general lesson to `team/learnings/<player>.md`, then `bash team/bin/push.sh "<msg>"`.
5. **Done with a buyer** (no projects left, or you give up): `bash team/bin/release.sh <buyer_id>`.
6. **Pull often.** `sync.sh` is cheap; run it before choosing a new buyer.
7. Never commit `.env` or the token. Never write the token into any file.

Claims from before this repo existed are marked `owner: unknown`. The first player who claims one takes it over.
