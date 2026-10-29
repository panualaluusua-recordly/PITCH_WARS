# Sourced by the team/bin scripts: repo root, .env and player name.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
set -a; source .env; set +a
ME="${PITCH_WARS_PLAYER:-}"
if [ -z "$ME" ]; then echo "Set PITCH_WARS_PLAYER=<your first name> in .env" >&2; exit 2; fi
# python3 on Windows can be the Microsoft Store stub, so test that it actually runs.
PY=""
for p in python3 python py; do
  if command -v "$p" >/dev/null 2>&1 && "$p" -c 1 >/dev/null 2>&1; then PY="$p"; break; fi
done
