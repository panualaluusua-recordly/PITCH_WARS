#!/usr/bin/env bash
# Give a claimed buyer back to the team.
# usage: release.sh <buyer_id> [reason]
source "$(dirname "$0")/common.sh"
buyer="${1:?usage: release.sh <buyer_id> [reason]}"
f="team/claims/$buyer.md"
git pull --rebase --autostash -q
printf 'owner: released\nsince: %s\nnote: released by %s. %s\n' "$(date -u +%FT%TZ)" "$ME" "${2:-}" > "$f"
bash team/bin/push.sh "release $buyer" "$f"
