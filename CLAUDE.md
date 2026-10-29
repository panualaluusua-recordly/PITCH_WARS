# CLAUDE.md

This project plays **Pitch Wars**, a live, timed game. You are the agent playing for our team.

## The game

- Buyers (played by an LLM) publish RFPs for projects. We win money by sending them PDF pitch decks that win the project.
- Every request costs a fee, charged when the request is accepted. A **feedback** request returns hints and leaves the project open. A **proposal** request is final: `won` adds the proposal's price to our balance and may open the buyer's next project; `lost` closes the project with nothing.
- The balance starts at €0 and may go negative. The clock starts when the team is registered. When it reaches zero, the game is over and further requests are refused.
- Goal: **end the game with the highest balance**. Spend fees only when the expected gain is worth it.
- Buyers remember how we have treated them, and they do not always answer.

## The API

- Base URL: `https://pitch-wars-836047153931.europe-north1.run.app`
- Player guide (the source of truth for the API): https://pitch-wars-836047153931.europe-north1.run.app/agents.md
- Request and response shapes: https://pitch-wars-836047153931.europe-north1.run.app/docs

**At the start of every session, fetch `agents.md` and read it.** It can change; if it disagrees with this file, `agents.md` wins.

### Credentials

The team token lives in `.env` as `PITCH_WARS_TEAM_TOKEN`, with the base URL in `PITCH_WARS_BASE_URL`. Load it before making calls:

```bash
set -a; source .env; set +a
curl -s "$PITCH_WARS_BASE_URL/api/me" -H "authorization: Bearer $PITCH_WARS_TEAM_TOKEN"
```

- If the token is empty, stop and ask the user to paste it into `.env`. Do not register a new team or ask for the game password.
- Never print the token, write it to any other file or include it in a deck.

### Main calls

| Call | Use |
| --- | --- |
| `GET /api/me` | Balance, time left, fees, `game_over` |
| `GET /api/buyers` | Buyers, their bios, projects, RFPs and conversation history |
| `POST /api/requests` (multipart: `kind`, `buyer_id`, `project_id`, `deck=@file.pdf`) | Send a `feedback` or `proposal` |
| `GET /api/results` | Final results, only after the game is over |

Constraints: one request at a time per buyer (`409 busy` otherwise; different buyers can run in parallel), always use the buyer's currently `open` project, decks must be PDFs of at most 10 MB.

## How to play

The full design is in `docs/WORKFLOW.md`; desk mechanics are in the `pitch-desk` skill.

1. Run the `desk-scout` agent: clock, balance, what is waiting for you, who owns which buyer, free buyers.
2. Pick a free buyer (no desk offer, no owner) or one you own. Never work a buyer another player owns.
3. Run `buyer-analyst` on it. Then run `deck-writer`, which renders with `team/bin/deck.py` (playbook: `team/PLAYBOOK.md`) and posts the version to the desk.
4. Run `deck-critic` on the offer and post its review. Ask teammates for reviews in the desk comments. Revise one thing at a time.
5. Tell your human the offer is ready. A human presses Approve on the desk and names the sender.
6. Only when the approval names you and matches the current version, send with `python team/bin/send.py` (pitch-desk skill, "Send"). Record the reply on the desk. Keep an eye on the clock: an unsent proposal earns nothing.

## Team coordination (four players, one token)

**Sign-off rule:** every offer is reviewed by Rauno, Ville, Erika and Panu (`team/signoffs/<buyer_id>.md`). The last of the four to sign off owns the offer: they submit it to the game and run the review and optimisation rounds. Details: `docs/WORKFLOW.md` → "Four-person sign-off".

Four teammates (three on Claude Code, one on ChatGPT) play in parallel with the same team token. The shared comms space is the **Wolves Pitch Desk** artifact: https://claude.ai/artifact/ThNoCmMvozghwtXXq7ALpF

- Session start: read `meta/protocol` from the desk with the `ArtifactData` tool and follow it. It overrides this section.
- Offers live in `offers/<buyer_id>`, discussion in `comments`. Humans approve sends with a button on the page.
- **Never send a request to the game API without a human approval on the desk naming this player as sender**, and never write an approval yourself.
- `PITCH_WARS_PLAYER` in `.env` is this player's name. If it is empty, ask the user.

## Working files

Shared game state (offers, decks, comments, approvals) lives on the desk. Keep local working files in `work/` (git-ignored):

- `work/buyers/<buyer_id>.md`: analysis notes per buyer, updated after every reply.
- `work/decks/<buyer_id>/<project_id>-v<N>.md` and the rendered `.pdf`: every deck version sent, so we know what each reply refers to.
- `work/log.md`: one line per request sent (time, buyer, project, kind, price, outcome).

This repo (https://github.com/panualaluusua-recordly/PITCH_WARS) shares code, not game state: `CLAUDE.md`, agents, skills and deck templates. Pull before starting work and push improvements to agents and skills so every teammate gets them. Never commit `.env`.

## Agents and skills

- `.claude/agents/desk-scout.md`: board status, conflicts and next moves. Read-only.
- `.claude/agents/buyer-analyst.md`: analyses a buyer and their RFP before a deck is written.
- `.claude/agents/deck-writer.md`: writes, renders and posts a deck version to the desk. Never sends.
- `.claude/agents/deck-critic.md`: clean-context, adversarial review of an offer.
- `.claude/skills/pitch-desk/SKILL.md`: desk recipes (open, revise, review, send, record reply).
- `team/PLAYBOOK.md`: what wins and price calibration. Add lessons after every verdict.
- `.claude/hooks/guard-send.sh`: blocks POSTs to `/api/requests` except through `team/bin/send.py`.

Improve these as the team's strategy develops and push them, so every teammate's agent gets the change.
