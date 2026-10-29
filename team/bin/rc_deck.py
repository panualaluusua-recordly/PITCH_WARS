"""Render a deck spec (team/bin/deck.py JSON format) as a Recordly 2026 frontend-slides HTML deck.

Usage: python team/bin/rc_deck.py spec.json out.html
Then:  bash .claude/skills/frontend-slides/scripts/export-pdf.sh out.html out.pdf --compact

Uses the frontend-slides skill's viewport-base.css and the Recordly template's recordly-base.css verbatim,
the knockout wordmark inline, and a fit-to-floor script so no slide overflows the 1920x1080 stage.
"""
import base64
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKILL = ROOT / ".claude/skills/frontend-slides"
RC = SKILL / "bold-template-pack/templates/recordly"


def md(s):
    """Escape text and turn **bold** into the paper-coloured emphasis used for key phrases."""
    s = html.escape(str(s))
    return re.sub(r"\*\*(.+?)\*\*", r'<strong class="em">\1</strong>', s)


def bullets(items):
    out = []
    for b in items:
        sub = b.startswith("-- ")
        out.append(f'<li class="{"sub" if sub else ""}">{md(b[3:] if sub else b)}</li>')
    return f'<ul class="rc-list rc-body bl">{"".join(out)}</ul>'


def table(rows):
    head = "".join(f"<th>{md(c)}</th>" for c in rows[0])
    body = "".join("<tr>" + "".join(f"<td>{md(c)}</td>" for c in r) + "</tr>" for r in rows[1:])
    return f'<table class="tb"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'


def diagram(d):
    cols = []
    for i, c in enumerate(d["columns"]):
        boxes = "".join(f'<div class="box">{md(b)}</div>' for b in c["boxes"])
        cols.append(f'<div class="col"><p class="rc-eyebrow ct">{md(c["title"])}</p>{boxes}</div>')
        if i < len(d["columns"]) - 1:
            cols.append('<div class="arrow">&rarr;</div>')
    band = f'<p class="band">{md(d["band"])}</p>' if d.get("band") else ""
    return f'<div class="dg">{"".join(cols)}</div>{band}'


def slide_html(spec, sl, n, total):
    parts = []
    if sl.get("bullets"):
        parts.append(bullets(sl["bullets"]))
    if sl.get("diagram"):
        parts.append(diagram(sl["diagram"]))
    if sl.get("table"):
        parts.append(table(sl["table"]))
    if sl.get("note"):
        parts.append(f'<p class="note">{md(sl["note"])}</p>')
    return f'''
<section class="slide rc-slide">
  <p class="rc-eyebrow eb">{md(spec.get("client", ""))}</p>
  <h2 class="rc-h3 tt">{md(sl.get("title", ""))}</h2>
  <div class="content">{"".join(parts)}</div>
  {furniture(n, total)}
</section>'''


WORDMARK = base64.b64encode((RC / "assets/logo/recordly-wordmark-knockout.png").read_bytes()).decode()


def furniture(n, total):
    return f'''<div class="rc-furniture"><div class="rc-furniture__tab"></div>
<img class="rc-furniture__wordmark" alt="Recordly" src="data:image/png;base64,{WORDMARK}">
<div class="rc-pagination">{n} / {total}</div><div class="rc-furniture__tagline">Data &amp; AI, delivered</div></div>'''


EXTRA_CSS = """
/* === DECK LAYOUT (Recordly 2026 on the fixed stage) === */
:root{--stage-bg:#1B1B1B; --slide-bg:#1B1B1B; --k:1}
.eb{position:absolute; left:96px; top:54px; width:1700px}
.tt{position:absolute; left:96px; top:110px; width:1700px}
.cv{position:absolute; left:96px; top:300px; width:1600px; display:flex; flex-direction:column; gap:56px}
.content{position:absolute; left:96px; right:96px; top:300px; bottom:110px; overflow:hidden;
  display:flex; flex-direction:column; gap:calc(26px*var(--k))}
.bl{font-size:calc(30px*var(--k)); padding-left:56px}
.bl > li{margin-bottom:calc(10px*var(--k))}
.bl > li::before{left:-40px; color:var(--rc-lime); font-size:.7em; top:.25em}
.bl > li.sub{margin-left:56px; color:var(--rc-grey-400)}
.em{color:var(--rc-paper); font-weight:800}
.tb{width:100%; border-collapse:collapse; font-size:calc(24px*var(--k)); line-height:1.25}
.tb th{background:var(--rc-lime); color:var(--rc-ink); font-weight:800; text-transform:uppercase;
  font-size:calc(19px*var(--k)); letter-spacing:.04em; text-align:left; padding:calc(14px*var(--k)) 18px}
.tb th .em{color:var(--rc-ink)}
.tb td{background:var(--rc-well); color:var(--rc-grey-300); padding:calc(12px*var(--k)) 18px;
  border-bottom:2px solid var(--rc-grey-600); vertical-align:top}
.tb tr td:first-child{color:var(--rc-paper); font-weight:800}
.dg{display:flex; align-items:stretch; gap:calc(14px*var(--k))}
.dg .col{flex:1; display:flex; flex-direction:column; gap:calc(10px*var(--k))}
.dg .ct{color:var(--rc-paper); font-size:calc(21px*var(--k)); margin-bottom:4px}
.dg .box{background:var(--rc-well); border:2px solid var(--rc-grey-600); color:var(--rc-grey-300);
  font-size:calc(23px*var(--k)); line-height:1.25; padding:calc(12px*var(--k)) 16px}
.dg .arrow{align-self:center; color:var(--rc-grey-400); font-size:calc(40px*var(--k)); font-weight:300}
.band{margin:0; border-left:6px solid var(--rc-grey-600); padding:6px 0 6px 20px; color:var(--rc-paper);
  font-size:calc(24px*var(--k)); line-height:1.3}
.note{margin:0; color:var(--rc-grey-400); font-size:calc(21px*var(--k)); line-height:1.35}
"""

JS = """
/* === STAGE SCALING + NAVIGATION === */
const stage=document.querySelector('.deck-stage'), slides=[...document.querySelectorAll('.slide')]; let cur=0;
function fit(){const s=Math.min(innerWidth/1920,innerHeight/1080);
  stage.style.transform=`translate(${(innerWidth-1920*s)/2}px,${(innerHeight-1080*s)/2}px) scale(${s})`;}
function show(i){cur=Math.max(0,Math.min(slides.length-1,i)); slides.forEach((s,j)=>s.classList.toggle('active',j===cur));}
addEventListener('resize',fit);
addEventListener('keydown',e=>{if(['ArrowRight',' ','PageDown'].includes(e.key))show(cur+1);
  if(['ArrowLeft','PageUp'].includes(e.key))show(cur-1);});
/* === FIT CONTENT ABOVE THE FLOOR: shrink type until nothing overflows === */
function fitContent(){slides.forEach(s=>{const c=s.querySelector('.content'); if(!c)return;
  const was=s.classList.contains('active'); s.classList.add('active'); let k=1;
  const t=s.querySelector('.tt'); const top=t.offsetTop+t.offsetHeight+40; c.style.top=Math.max(top,250)+'px';
  while(c.scrollHeight>c.clientHeight+1 && k>0.55){k-=0.04; c.style.setProperty('--k',k);}
  if(!was)s.classList.remove('active');});}
fit(); show(0); document.fonts.ready.then(fitContent);
"""


def build(spec):
    n = len(spec["slides"]) + 1
    cover = f'''
<section class="slide rc-slide cover">
  <p class="rc-eyebrow eb">{md(spec.get("client", ""))}</p>
  <div class="cv"><h1 class="rc-h1 rc-h1--lead">{md(spec.get("title", ""))}</h1>
  <p class="rc-lead rc-lead--cover">{md(spec.get("subtitle", ""))}</p></div>
  {furniture(1, n)}
</section>'''
    body = cover + "".join(slide_html(spec, sl, i + 2, n) for i, sl in enumerate(spec["slides"]))
    css = (SKILL / "viewport-base.css").read_text(encoding="utf-8") + (RC / "reference/recordly-base.css").read_text(encoding="utf-8") + EXTRA_CSS
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;800;900&display=swap">
<title>{html.escape(spec.get("client", ""))}: {html.escape(spec.get("title", ""))}</title>
<style>{css}</style></head>
<body><div class="deck-viewport"><div class="deck-stage">{body}</div></div><script>{JS}</script></body></html>'''


if __name__ == "__main__":
    spec = json.load(open(sys.argv[1], encoding="utf-8"))
    Path(sys.argv[2]).write_text(build(spec), encoding="utf-8")
    print("wrote", sys.argv[2])
