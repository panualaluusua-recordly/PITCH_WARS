# Team workflow: many agents, one token, human approval

Several players share one team token. Most run their own Claude Code; one uses ChatGPT. Their agents must not
pitch the same buyer twice or step on each other's sales, and no deck reaches a buyer without a human saying yes.
This page is the design. The agents and skills in `.claude/` implement it.

## Where things live

| What | Where | Who writes |
| --- | --- | --- |
| Offers, deck text, comments, approvals, game snapshot | **Wolves Pitch Desk** (claude.ai artifact, shared db): https://claude.ai/artifact/ThNoCmMvozghwtXXq7ALpF | agents via `ArtifactData`; humans via the page |
| Agent rules (short form) | desk `meta/protocol` | kept in sync with this page |
| What wins, prices seen so far | `team/PLAYBOOK.md` | anyone, via git |
| Deck renderer, sender | `team/bin/deck.py`, `team/bin/send.py` | via git |
| Agents, skills, guard hook | `.claude/` | via git |
| Private scratch (specs, previews, API dumps) | `work/` (git-ignored) | each player |

The game API stays the source of truth for buyer state (`open`, `thinking`, conversation). The desk adds what the
API does not know: who works a buyer, which deck version is under discussion, and who approved what.

## Offer lifecycle

One desk document per buyer, `offers/<buyer_id>`, for the buyer's currently open project.

```
draft ──> review ──(human presses Approve)──> approved ──(sender's agent sends)──> sent
            ^  ^                                  │                                 │
            │  └──── new version (voids approval) ┘                                 │
            └──────────── feedback reply ───────────────────────────────────────────┤
                                                                       won / lost <─┘   (parked = given up)
```

1. **Draft.** Any player's agent may open an offer for a buyer that has no desk offer and no owner. It posts the
   deck text (`deck_md`), price and version 1, and announces it in `comments`.
2. **Review and iterate.** Before the first send, the offer is open to everyone. Other players' agents review it
   (kind `review`, adversarial, one concrete change at a time). Any agent may post version N+1 with a comment saying
   what changed. Humans read and comment on the page.
3. **Approve.** Only a human, by pressing *Approve feedback* or *Approve proposal* on the page. The approval
   records the kind, the exact version, the price and **whose agent sends**. A new version voids it.
4. **Send.** Only the named sender's agent, only that version, only through `team/bin/send.py`. It then marks the
   offer `sent` and sets `owner` to its player.
5. **After the first send the buyer belongs to that player** (sales bonus): only the owner's agent revises, sends,
   or opens the buyer's next project. Others may still read and comment.
6. **Reply.** The owner's agent posts the buyer's reply verbatim (kind `buyer`). Feedback → back to `review`.
   Proposal → `won` or `lost`. If a next project opens, archive the old doc as `offers/<buyer_id>__<project_id>`
   and start a fresh offer with the same owner.

## Four-person sign-off: the last reviewer owns the submission

Team rule (2026-10-29, from Ville): **every offer is looked at by all four players: Rauno, Ville, Erika and Panu.**

- Each player (or their agent, on their behalf) records a sign-off in `team/signoffs/<buyer_id>.md`: one line with name, UTC time, offer version and verdict (`ok` or `fix: <one concrete change>`).
- **The last of the four to sign off becomes the offer's owner.** From then on they handle the whole customer process in the game: getting the human approval, submitting, reading the buyer's reply, running review and optimisation rounds (feedback versions), and the final proposal.
- Until all four have signed off, nobody submits the offer to the game.
- The owner still follows the hard guarantees below: a human Approve on the desk that names them as sender, and sending only with `team/bin/send.py`.
- A new version after the four sign-offs doesn't need four new sign-offs. The owner iterates, and teammates may still comment.

## Roles

| Role | Does | Never |
| --- | --- | --- |
| Human player | Chooses buyers, reads decks, comments, presses Approve | Shares the token |
| Player's agent (main session) | Orchestrates the subagents below for its player | Sends without an approval naming its player |
| `desk-scout` | Background status: free buyers, approvals waiting, comments to answer, conflicts | Writes offers |
| `buyer-analyst` | Reads bio, RFP and replies; lists explicit and hidden preferences | Writes decks |
| `deck-writer` | Spec → `deck.py` → posts a version to the desk | Approves or sends |
| `tech-analyst` | Tech triggers, constraints and traps → pattern ids (`architecture-patterns`) | Writes decks |
| `solution-architect` | Architecture slide with diagram, gates and risks slide, effort basis | Sets the price, sends |
| `deck-critic` | Clean-context review of any offer; tries to find why it would lose | Edits the deck |
| `tech-critic` | Clean-context attack on the deck's technical claims | Edits the deck |
| `feedback-miner` | Replies → quoted updates of playbook, pattern library, price evidence, trap catalog | Edits offers or the roster |
| ChatGPT teammate | Uses the page: reads, comments, approves; pastes decks into ChatGPT for analysis | — |

## Hard guarantees

- **Desk rule:** an agent sends only when `offers/<buyer_id>` has `state == approved`, `approval.send_by` equal to
  its player, and `approval.version == version`. Agents never write `approval` or `state: approved`.
- **Local guard (this repo):** `.claude/settings.json` makes every `python team/bin/send.py` call ask the human at
  the keyboard, and `.claude/hooks/guard-send.sh` blocks any other way of POSTing to `/api/requests`.
- **Optimistic writes:** every desk write to an existing document carries `if_version`; on a clash, re-read and redo.

The desk rule is a protocol, not access control: an agent writes the desk as its human. The local guard is what
makes a stray send impossible without someone at the keyboard.
