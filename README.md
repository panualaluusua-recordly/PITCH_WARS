# Wolves of Wall Text: Pitch Wars

Our team's setup for Pitch Wars. Read `CLAUDE.md` for the game rules and how the agent plays.

- **Coordination:** the Wolves Pitch Desk, https://claude.ai/artifact/ThNoCmMvozghwtXXq7ALpF. Offers, decks, comments and send approvals live there. Agent rules are stored on the desk as `meta/protocol`.
- **This repo:** shared `CLAUDE.md`, agents (`.claude/agents/`), skills (`.claude/skills/`) and templates.

## Join (Claude Code)

```bash
winget install --id GitHub.cli -e      # macOS: brew install gh
gh auth login                          # GitHub.com, HTTPS, log in with a browser
gh auth setup-git
git -c core.longpaths=true clone https://github.com/panualaluusua-recordly/PITCH_WARS.git
cd PITCH_WARS && git config core.longpaths true
cp .env.example .env                   # paste the team token, set PITCH_WARS_PLAYER=<first name>
```

Then start Claude Code in the folder and say:

> Read the Wolves Pitch Desk protocol and join as `<first name>`.

## Join (ChatGPT)

Open the desk link in a browser while signed in to claude.ai. Read decks, post comments and press Approve there. Paste a deck into ChatGPT for analysis and post its answer as a comment.
