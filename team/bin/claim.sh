#!/usr/bin/env bash
# Claim a buyer for this player. The first claim that reaches the remote wins.
# usage: claim.sh <buyer_id> [note]
source "$(dirname "$0")/common.sh"
buyer="${1:?usage: claim.sh <buyer_id> [note]}"
note="${2:-}"
f="team/claims/$buyer.md"

for attempt in 1 2 3 4; do
  git pull --rebase --autostash -q
  if [ -f "$f" ]; then
    owner=$(sed -n 's/^owner: //p' "$f")
    if [ "$owner" = "$ME" ]; then echo "already yours: $buyer"; exit 0; fi
    if [ "$owner" != "unknown" ] && [ "$owner" != "released" ]; then
      echo "TAKEN by $owner: $buyer"; exit 1
    fi
  fi
  mkdir -p team/claims
  printf 'owner: %s\nsince: %s\nnote: %s\n' "$ME" "$(date -u +%FT%TZ)" "$note" > "$f"
  git add "$f"
  git commit -qm "claim $buyer ($ME)"
  if git push -q 2>/dev/null; then echo "CLAIMED $buyer"; exit 0; fi
  # Someone pushed first: drop our claim commit and check again.
  git reset -q --keep HEAD~1
done
echo "could not push claim for $buyer, run again" >&2
exit 1
