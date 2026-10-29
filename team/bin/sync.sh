#!/usr/bin/env bash
# Pull the shared repo and print the buyer board: API status next to the claim owner.
source "$(dirname "$0")/common.sh"
git pull --rebase --autostash -q || echo "(git pull failed, board may be stale)" >&2
auth="authorization: Bearer $PITCH_WARS_TEAM_TOKEN"
curl -s "$PITCH_WARS_BASE_URL/api/me" -H "$auth" > "${TMPDIR:-/tmp}/pw_me.json"
curl -s "$PITCH_WARS_BASE_URL/api/buyers" -H "$auth" > "${TMPDIR:-/tmp}/pw_buyers.json"
"$PY" - "${TMPDIR:-/tmp}/pw_me.json" "${TMPDIR:-/tmp}/pw_buyers.json" "$ME" <<'EOF'
import json, os, sys
me = json.load(open(sys.argv[1], encoding="utf-8"))
buyers = json.load(open(sys.argv[2], encoding="utf-8"))["buyers"]
player = sys.argv[3]
def owner(bid):
    p = f"team/claims/{bid}.md"
    if not os.path.exists(p):
        return ""
    for line in open(p, encoding="utf-8"):
        if line.startswith("owner: "):
            return line[7:].strip()
    return "?"
t = me.get("time_left_seconds", 0)
print(f"balance {me.get('money_eur')} EUR | time left {t//3600}h{(t%3600)//60:02d}m | fees {me.get('fees_eur')} | game_over {me.get('game_over')}")
print(f"{'buyer':24} {'status':10} {'msgs':>4} {'owner':12} project")
reading = 0
for b in buyers:
    open_p = next((p for p in b["projects"] if p["status"] in ("open", "thinking")), None)
    status = open_p["status"] if open_p else ("out" if b.get("out_of_budget") else "-")
    reading += status == "thinking"
    msgs = sum(len(p["conversation"]) for p in b["projects"])
    o = owner(b["id"])
    flag = ""
    if msgs and o in ("", "released"):
        flag = "  <- activity but unclaimed"
    if b.get("available_at"):
        flag += f"  cooldown until {b['available_at']}"
    mark = "*" if o == player else " "
    title = open_p["title"][:38] if open_p else ""
    print(f"{mark}{b['id']:23} {status:10} {msgs:>4} {o or '-':12} {title}{flag}")
print(f"decks in reading: {reading}/3   (* = yours)")
EOF
