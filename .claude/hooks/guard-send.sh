#!/usr/bin/env bash
# PreToolUse guard for Bash: game requests go out only through team/bin/send.py, which
# .claude/settings.json makes ask the human first (see docs/WORKFLOW.md, "Hard guarantees").
input=$(cat)
if printf '%s' "$input" | grep -q 'api/requests' \
   && printf '%s' "$input" | grep -Eq -- '-X *POST|-F |--form|requests\.post|urlopen' \
   && ! printf '%s' "$input" | grep -q 'team/bin/send.py'; then
  echo "Blocked: send game requests only with 'python team/bin/send.py' after a human approved this version on the Wolves Pitch Desk (.claude/skills/pitch-desk)." >&2
  exit 2
fi
exit 0
