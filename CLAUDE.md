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

1. Check `GET /api/me` for balance, fees and time left.
2. Read `GET /api/buyers`. For each open project, study the buyer's bio, the RFP and every earlier reply in the conversation.
3. Analyse what the buyer really wants, including what the RFP does not say (use the `buyer-analyst` agent).
4. Write a deck that answers the RFP and the buyer's priorities, and set a price (use the `price-check` skill). Render it to PDF.
5. Decide: send a feedback request to test the deck, or a proposal when you are confident. Change one thing at a time between feedback rounds so you can tell what the buyer reacted to.
6. Record the reply, update your notes and repeat. Keep an eye on the clock: an unsent proposal earns nothing.

## Team coordination (four players, one token)

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

- `.claude/agents/buyer-analyst.md`: analyses a buyer and their RFP before a deck is written.
- `.claude/skills/price-check/SKILL.md`: decides the price on a proposal.

Both are starting templates and team might delete them if they want. Improve them, and add more agents (for example a deck writer or a deck critic) and skills as the team's strategy develops.
