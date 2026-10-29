#!/usr/bin/env bash
# Commit and push shared files. Defaults to the whole team/ folder.
# usage: push.sh "<message>" [paths...]
source "$(dirname "$0")/common.sh"
msg="${1:-update}"; shift || true
paths=("$@"); [ ${#paths[@]} -eq 0 ] && paths=(team)
git add -- "${paths[@]}"
git diff --cached --quiet || git commit -qm "$msg ($ME)"
for attempt in 1 2 3 4; do
  if git pull --rebase --autostash -q && git push -q; then echo "pushed"; exit 0; fi
  sleep 2
done
echo "push failed, check git status" >&2
exit 1
