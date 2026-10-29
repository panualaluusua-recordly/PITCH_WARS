# GitHub coordination analysis (2026-10-29)

Scope: the `main` history of this repo on 2026-10-29 (113 commits, 15 merges), read with `git log`. Written by the Claude session of panu. Facts are from commits; judgements are marked as such.

## 1. Who contributed

| Author | Commits | Role in the repo |
| --- | --- | --- |
| panu | 74 | Agents, skills, renderer, tech-lane decks and reviews |
| Rauno Paukkeri | 24 | Staffing reviews, submission records, final sends |
| Ville (RecordlyVille) | 15 | Prio A owner, batch drafts, batch results |

- Shared deck directories (touched by all three authors): aktia, alko, city-of-helsinki, elisa, enfuce, kemira, sanoma, savings-banks-group, veikkaus, yliopiston-apteekki. The overlap is mostly sign-off lines and reviews, not conflicting edits to the same deck text.
- 35 sign-off files and 25 tech-review files were added. Those are the "contribution" artefacts. Most real offer contributions are new versions (`-vN.md`), not edits to a shared file.

## 2. Did agents and people follow the written rules?

Rules in `CLAUDE.md` and `docs/WORKFLOW.md`: Prio A owned by Ville (from ~12:45 local); no send without a desk approval naming the sender; sign-off by Panu, Rauno and Ville; work in `work/` (git-ignored).

- **Prio A ownership, one breach found (ours).** panu's commits `2c89941` (13:20) and `b0b3860` (13:22) changed kemira tech-lens files after the 12:45 claim. They were tech-only changes with price untouched, but they were still edits to a buyer that was declared hands-off. Ville's later commits did not touch the deck files of other players in this window.
- **Sends outside the desk rule.** Rauno's commit `a11edeb` ("Enable explicitly human-approved exact-PDF chat sends") and `431cb34` (feedback addressed in final offers) describe sends authorised in chat, not by a desk approval. Whether that satisfies the desk rule is a judgement the team has to make; the rule text says the desk approval is the gate.
- **Concurrent sends.** `598d350` ("Reconcile concurrent final sends, record Elisa win and preserve unsent scoped alternatives") shows two agents sent on the same buyers at the same time. This is the failure the desk and ownership rules exist to prevent.
- **Local guard works.** `e9fb53f` added `send.py --approved-on-desk`, settings `ask/deny` and a guard hook. A session without that approval cannot send through the script.
- **Our own agents followed the writing rules.** Every tech review and version commit states "price and terms unchanged"; no commit contains a game API POST; no `.env` or token was committed (checked by `git log -p` for the token name; none found).

## 3. Conflicts and ownership

- No merge conflicts are visible in `main`. The 15 merge commits are of the form `Merge remote-tracking branch 'origin/main' into codex/staffing`, i.e. Rauno's branch being brought up to date. Conflicts were resolved by re-running work, not by hand-merging the same file.
- The git claim system (`d163fba` "claim 31 untouched buyers", `acf042d` "Remove git claim system (superseded by the desk)") was in place and then removed. Claims in git were not atomic: two players could claim the same buyer in different commits. Ownership moved to the desk.
- Ownership is now in three places that can disagree: the desk, `team/evaluations/OWNERSHIP-prio-A.md`, and `RAUNO-SUBMISSIONS.md`. In this session the desk was not readable, so the state could not be checked against it.

## 4. Auditability

- Good: every deck version, review and sign-off is a commit with author and time; `git log` reconstructs who did what and when. Versions are immutable (`-vN` files, no overwrites in the agents' workflow).
- Weak: the send itself (game request, response, price) is not in git. It lives in the game API and partly in `team/buyers/*.md` and `team/evaluations/reply-signals.md`, written by hand or by a script. The chain "approval → send → result" is not closed in one place.
- Weak: approvals are on the desk, outside git. A commit cannot prove that an approval existed.
- Weak: commit messages mix tech, price and status in one line; the "price unchanged" claim is a convention, not a check.

## 5. Is GitHub the right coordination tool?

Judgement: GitHub is good for **artefacts and history** (decks, rules, reviews, sign-offs, scripts), and poor as a **live lock or queue** for shared external actions.

Why:
- Git has no atomic claim. Two pushes can both succeed in a race. The removed claim system proves this.
- A send is an external, irreversible action. It needs one authority that checks state at the moment of sending, not a history of commits.
- The desk already supports `if_version` (optimistic writes) and approvals, which is what the locks need.

Recommended split:
1. **Desk** is the source of state: owner per buyer, the approved version, the sender. `send.py` should read the desk and refuse unless `state == approved` and `sender == this player`, with an `if_version` check at send time.
2. **GitHub** holds artefacts and rules. Use a branch per player for drafts and PRs into `main` for shared rules, so reviews are visible. Ban agents from pushing directly to `main` except for their own `team/tech/reviews/` and version files.
3. **CODEOWNERS** (or a generated ownership file) per buyer directory, so ownership appears in the diff, not only in prose. Prio A paths owned by Ville.
4. **Log every send in git** after it happens: one line in `team/buyers/<id>.md` with the desk approval id, the request id and the result. Make `send.py` write that line itself.
5. **One batch per hour** for cross-player commits, instead of many small pushes racing each other.

Open questions for the team (not decided here): whether chat authorisations count as approvals; who may send when two players claim the same buyer; and whether the desk should move into the repo as a file so that the approval and the version live in one commit.

## 6. Limits of this analysis

- The desk was not readable from this session (ArtifactData unavailable), so desk state, approvals and comments are not part of the analysis.
- Game-side results (wins, losses, replies) are not in git and were not checked against the API in this analysis.
