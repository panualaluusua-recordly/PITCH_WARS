"""Copy every buyer reply from the game API into the repo, so nothing a teammate triggered stays unrecorded.

Usage: python team/bin/ingest_replies.py [buyers.json]
Reads work/buyers_now.json (or the path given); with --fetch it calls GET /api/buyers first (token from .env,
never printed). Read-only against the game: it sends nothing.

Writes:
- team/buyers/<buyer_id>.md: an auto section between <!-- replies:auto --> markers (replaced on every run; text
  outside the markers is never touched).
- team/evaluations/reply-signals.md: one row per reply with the price signal class, deck, price from the file name.
"""
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
START, END = "<!-- replies:auto -->", "<!-- /replies:auto -->"
HARD = re.compile(r"flatly|completely|entirely|non-starter|out of bounds|flat out|dramatic|drastic", re.I)
SOFT = re.compile(r"\babove\b|trim|inflated|quite high|a bit high|too high|over budget|exceeds", re.I)


def load_env():
    env = {}
    p = ROOT / ".env"
    if p.exists():
        for line in p.read_text(encoding="utf-8").splitlines():
            if "=" in line and not line.lstrip().startswith("#"):
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"')
    return env


def fetch(out):
    env = load_env()
    req = urllib.request.Request(env["PITCH_WARS_BASE_URL"] + "/api/buyers",
                                 headers={"authorization": "Bearer " + env["PITCH_WARS_TEAM_TOKEN"]})
    data = urllib.request.urlopen(req, timeout=30).read()
    out.parent.mkdir(exist_ok=True)
    out.write_bytes(data)


def price_signal(entry):
    text = entry.get("text") or ""
    if entry.get("kind") == "no_reply":
        return "no reply"
    if entry.get("kind") == "verdict":
        r = (entry.get("review") or {}).get("ratings", {})
        return f"verdict {entry.get('result')}, price {r.get('price', '?')}"
    if HARD.search(text) and re.search(r"budget|price|commercial|fee|total", text, re.I):
        return "over-hard"
    if SOFT.search(text) and re.search(r"budget|price|commercial|fee|total", text, re.I):
        return "over-soft"
    return "none"


def deck_price(deck):
    m = re.search(r"eur(\d+)", deck or "", re.I)
    return f"€{int(m.group(1)):,}" if m else "unknown"


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    src = Path(args[0]) if args else ROOT / "work" / "buyers_now.json"
    if "--fetch" in sys.argv:
        fetch(src)
    buyers = json.loads(src.read_text(encoding="utf-8"))["buyers"]
    rows = []
    for b in buyers:
        sections = []
        for p in b["projects"]:
            team_deck = None
            for c in p.get("conversation") or []:
                if c.get("from") == "team":
                    team_deck = c.get("deck")
                    continue
                sig = price_signal(c)
                rows.append((b["id"], p["id"], c.get("kind"), team_deck, sig))
                body = (c.get("text") or "").strip().replace("\n", " ")
                review = c.get("review")
                lines = [f"- {c.get('at', '')[:16]} · **{c.get('kind')}** · deck `{team_deck or '?'}` "
                         f"({deck_price(team_deck)}) · price signal: **{sig}**", f"  > {body}"]
                if review:
                    r = review.get("ratings", {})
                    lines.append("  ratings: " + ", ".join(f"{k} {v}" for k, v in r.items()))
                    for pref in review.get("preferences", []):
                        lines.append(f"  - [{pref.get('verdict')}] {pref.get('evidence', '')}")
                sections.append((p["id"], "\n".join(lines)))
        if not sections:
            continue
        block = [START, "## Buyer replies (auto, from the game API; do not edit inside the markers)", ""]
        cur = None
        for pid, text in sections:
            if pid != cur:
                block.append(f"### {pid}")
                cur = pid
            block.append(text)
        block.append(END)
        f = ROOT / "team" / "buyers" / f"{b['id']}.md"
        old = f.read_text(encoding="utf-8") if f.exists() else f"# {b['name']}, {b['company_name']}\n"
        new = "\n".join(block)
        if START in old and END in old:
            old = old[:old.index(START)].rstrip("\n") + "\n\n" + new + old[old.index(END) + len(END):]
        else:
            old = old.rstrip("\n") + "\n\n" + new + "\n"
        f.write_text(old, encoding="utf-8")
    out = ["# Reply signals (auto, `team/bin/ingest_replies.py`)", "",
           "| Buyer | Project | Kind | Deck price | Signal |", "| --- | --- | --- | --- | --- |"]
    for bid, pid, kind, deck, sig in rows:
        out.append(f"| {bid} | {pid[:48]} | {kind} | {deck_price(deck)} | {sig} |")
    (ROOT / "team" / "evaluations" / "reply-signals.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{len(rows)} replies from {len({r[0] for r in rows})} buyers")


if __name__ == "__main__":
    main()
