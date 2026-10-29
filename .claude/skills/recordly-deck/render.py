#!/usr/bin/env python3
"""Render a deck markdown file to a Recordly-styled PDF.

Usage: python3 work/render.py work/decks/<buyer>/<project>-vN.md
Slides are separated by a line containing only '---'.
The first slide is the cover. A slide whose first line is '<!-- statement -->'
renders as a lime statement slide.
"""
import base64, pathlib, re, subprocess, sys
import markdown

ROOT = pathlib.Path(__file__).resolve().parents[3]
LOGO = ROOT / ".claude/skills/frontend-slides/bold-template-pack/templates/recordly/assets/logo/recordly-wordmark-knockout.png"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

CSS = """
@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;800;900&display=swap");
@page { size: 1920px 1080px; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body { background: #1B1B1B; }
body { font-family: 'Montserrat','Helvetica Neue',Arial,sans-serif; color: #D4D4D4; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.slide { width: 1920px; height: 1080px; position: relative; overflow: hidden; background: #1B1B1B; page-break-after: always; break-after: page; }
.inner { position: absolute; left: 96px; right: 96px; top: 64px; bottom: 96px; overflow: hidden; }
.content { font-size: 30px; line-height: 1.38; }
.content h1 { font-weight: 900; color: #E3FF87; font-size: 72px; line-height: 0.95; letter-spacing: -0.01em; margin-bottom: 0.45em; }
.content h2 { font-weight: 300; color: #EFEFEF; font-size: 1.25em; line-height: 1.15; margin: 0 0 0.6em 0; }
.content h3 { font-weight: 800; color: #E3FF87; text-transform: uppercase; letter-spacing: 0.06em; font-size: 0.72em; margin: 0.7em 0 0.3em 0; }
.content p { margin: 0 0 0.55em 0; }
.content strong { color: #FFFFFF; font-weight: 800; }
.content em { color: #E3FF87; font-style: normal; }
.content ul, .content ol { margin: 0 0 0.6em 1.1em; }
.content li { margin: 0 0 0.28em 0; padding-left: 0.2em; }
.content li::marker { color: #E3FF87; }
.content table { border-collapse: collapse; width: 100%; margin: 0.3em 0 0.7em 0; font-size: 0.82em; }
.content th { text-align: left; font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em; font-size: 0.8em; color: #1B1B1B; background: #E3FF87; padding: 0.45em 0.6em; }
.content td { border-bottom: 2px solid #434343; padding: 0.42em 0.6em; vertical-align: top; }
.content td:first-child { color: #FFFFFF; font-weight: 600; }
.content blockquote { border-left: 6px solid #E3FF87; padding: 0.3em 0 0.3em 0.8em; margin: 0.4em 0 0.7em 0; color: #EFEFEF; font-weight: 300; font-size: 1.1em; }
.cols { display: grid; grid-template-columns: 1fr 1fr; gap: 64px; }
.cols3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 48px; }
.foot { position: absolute; left: 96px; right: 96px; bottom: 40px; display: flex; justify-content: space-between; align-items: center; font-size: 14px; font-weight: 800; letter-spacing: 0.22em; text-transform: uppercase; color: #737373; }
.foot img { height: 16px; }
.cover .inner { top: 260px; }
.cover .content h1 { font-size: 112px; line-height: 0.9; margin-bottom: 0.35em; }
.cover .content h2 { font-size: 46px; }
.cover .logo { position: absolute; left: 96px; top: 96px; height: 40px; }
.statement { background: #E3FF87; }
.statement .content, .statement .content strong { color: #1B1B1B; }
.statement .content h1 { color: #1B1B1B; font-size: 96px; }
.statement .content h2 { color: #1B1B1B; font-weight: 400; }
.statement .foot { color: #1B1B1B; }
.pn { color: #999; }
"""

FIT_JS = """
document.fonts.ready.then(() => {
  for (const inner of document.querySelectorAll('.inner')) {
    const c = inner.querySelector('.content');
    let size = parseFloat(getComputedStyle(c).fontSize);
    let h1 = c.querySelector('h1');
    let h1size = h1 ? parseFloat(getComputedStyle(h1).fontSize) : 0;
    let guard = 0;
    while ((c.scrollHeight > inner.clientHeight || c.scrollWidth > inner.clientWidth) && size > 15 && guard < 60) {
      size -= 1; c.style.fontSize = size + 'px';
      if (h1 && h1size > 48) { h1size -= 1.5; h1.style.fontSize = h1size + 'px'; }
      guard++;
    }
    if (c.scrollHeight > inner.clientHeight) { document.title = 'OVERFLOW'; console.log('OVERFLOW'); }
  }
  document.body.setAttribute('data-ready', '1');
});
"""


def slide_html(md_text, idx, total, logo_uri, title):
    kind = "cover" if idx == 0 else "normal"
    lines = md_text.strip().splitlines()
    if lines and lines[0].strip() == "<!-- statement -->":
        kind = "statement"
        md_text = "\n".join(lines[1:])
    # column blocks: ':::cols' ... ':::' and ':::col' separators
    def cols(m):
        cls = m.group(1)
        parts = re.split(r"^:::col\s*$", m.group(2), flags=re.M)
        inner = "".join(f"<div>{markdown.markdown(p, extensions=['tables'])}</div>" for p in parts if p.strip())
        return f'<div class="{cls}">{inner}</div>'
    html = re.sub(r"^:::(cols3|cols)\s*$(.*?)^:::\s*$", cols, md_text, flags=re.M | re.S)
    # render remaining markdown, leaving the column html intact
    html = markdown.markdown(html, extensions=["tables", "md_in_html"])
    logo = f'<img class="logo" src="{logo_uri}">' if kind == "cover" else ""
    foot = "" if kind == "cover" else f'<div class="foot"><img src="{logo_uri}"><span>{title}</span><span class="pn">{idx + 1} / {total}</span></div>'
    if kind == "statement":
        foot = f'<div class="foot"><span>Recordly</span><span>{title}</span><span>{idx + 1} / {total}</span></div>'
    return f'<section class="slide {kind}">{logo}<div class="inner"><div class="content">{html}</div></div>{foot}</section>'


def main(path):
    src = pathlib.Path(path).resolve()
    text = src.read_text()
    title = ""
    m = re.match(r"^<!--\s*title:\s*(.*?)\s*-->\s*\n", text)
    if m:
        title, text = m.group(1), text[m.end():]
    slides = [s for s in re.split(r"^---\s*$", text, flags=re.M) if s.strip()]
    logo_uri = "data:image/png;base64," + base64.b64encode(LOGO.read_bytes()).decode()
    body = "".join(slide_html(s, i, len(slides), logo_uri, title) for i, s in enumerate(slides))
    doc = f"<!doctype html><html><head><meta charset='utf-8'><title>deck</title><style>{CSS}</style></head><body>{body}<script>{FIT_JS}</script></body></html>"
    html_path = src.with_suffix(".html")
    html_path.write_text(doc)
    pdf_path = src.with_suffix(".pdf")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=8000",
                    "--run-all-compositor-stages-before-draw", f"--print-to-pdf={pdf_path}", html_path.as_uri()],
                   check=True, capture_output=True)
    print(f"{pdf_path} ({len(slides)} slides, {pdf_path.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    for p in sys.argv[1:]:
        main(p)
