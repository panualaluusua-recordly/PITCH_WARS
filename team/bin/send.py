"""Send a feedback or proposal deck and print the reply.

Usage: python team/bin/send.py <feedback|proposal> <buyer_id> <project_id> <deck.pdf> [expected_msgs]
With expected_msgs, aborts if the project's conversation length differs (another player is active).
Re-checks that the project is open (not thinking) first; retries on too_many_requests / conflict.
Reads the token from .env; never prints it.
"""
import json
import subprocess
import sys
import time


def env():
    vals = {}
    for line in open(".env", encoding="utf-8"):
        line = line.strip()
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            vals[k] = v.strip().strip('"').strip("'")
    return vals


E = env()
BASE, TOKEN = E["PITCH_WARS_BASE_URL"], E["PITCH_WARS_TEAM_TOKEN"]


def curl(args):
    out = subprocess.run(["curl", "-s", "-H", f"authorization: Bearer {TOKEN}", *args],
                         capture_output=True, text=True, encoding="utf-8").stdout
    try:
        return json.loads(out)
    except Exception:
        return {"error": "bad_json", "raw": out[:500]}


def project_state(buyer_id, project_id):
    for b in curl([f"{BASE}/api/buyers"])["buyers"]:
        if b["id"] == buyer_id:
            for p in b["projects"]:
                if p["id"] == project_id:
                    return p["status"], len(p["conversation"]), b.get("available_at")
    return None, 0, None


def main():
    kind, buyer, project, deck = sys.argv[1:5]
    expected = int(sys.argv[5]) if len(sys.argv) > 5 else None
    status, n, avail = project_state(buyer, project)
    print(f"pre-check: status={status} msgs={n} available_at={avail}", flush=True)
    if status != "open":
        sys.exit(f"ABORT: project status is {status}")
    if expected is not None and n != expected:
        sys.exit(f"ABORT: conversation has {n} messages, expected {expected}; someone else may be working this buyer")
    for attempt in range(40):
        r = curl(["-X", "POST", f"{BASE}/api/requests", "-F", f"kind={kind}", "-F", f"buyer_id={buyer}",
                  "-F", f"project_id={project}", "-F", f"deck=@{deck};type=application/pdf", "--max-time", "300"])
        err = r.get("error")
        if err in ("too_many_requests", "conflict"):
            print(f"{err}, retrying...", flush=True)
            time.sleep(20)
            continue
        if err == "llm_failed":
            print("llm_failed (refunded), retrying...", flush=True)
            time.sleep(5)
            continue
        print(json.dumps(r, ensure_ascii=False, indent=1))
        return
    print("gave up after retries")


main()
