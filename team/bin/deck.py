"""Render a deck spec (JSON) to a 16:9 PDF plus a markdown copy.

Usage: python team/bin/deck.py spec.json out_basename
Writes out_basename.pdf and out_basename.md.

Spec: {"client": str, "title": str, "subtitle": str, "footer": str,
       "slides": [{"title": str, "bullets": [str], "diagram": {...}, "table": [[str]], "note": str}]}
diagram = {"columns": [{"title": str, "boxes": [str]}], "band": str, "height": int}: an architecture flow.
Bullets starting with "-- " are rendered as sub-bullets. **bold** is supported.
Theme: Recordly dark charcoal + lime by default (scored well on `recordly_style`); set "theme": "light" in the
spec for the old white + teal look.
"""
import json
import re
import sys

from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, TableStyle

W, H = 960, 540
THEMES = {
    "dark": dict(BG="#1b1b1b", INK="#d4d4d4", STRONG="#ffffff", ACCENT="#e3ff87", ON_ACCENT="#1b1b1b",
                 MUTED="#8a8a8a", RULE="#434343", PANEL="#262626", BOX="#1b1b1b", BAND="#2b3118"),
    "light": dict(BG="#ffffff", INK="#1b2430", STRONG="#1b2430", ACCENT="#0b6e4f", ON_ACCENT="#ffffff",
                  MUTED="#5b6675", RULE="#d7dde4", PANEL="#f2f6f4", BOX="#ffffff", BAND="#e8f3ee"),
}
T = {}


def set_theme(name):
    T.clear()
    T.update({k: HexColor(v) for k, v in THEMES[name].items()})

try:
    pdfmetrics.registerFont(TTFont("Sans", "C:/Windows/Fonts/segoeui.ttf"))
    pdfmetrics.registerFont(TTFont("Sans-Bold", "C:/Windows/Fonts/segoeuib.ttf"))
    from reportlab.pdfbase.pdfmetrics import registerFontFamily
    registerFontFamily("Sans", normal="Sans", bold="Sans-Bold", italic="Sans", boldItalic="Sans-Bold")
    F, FB = "Sans", "Sans-Bold"
except Exception:
    F, FB = "Helvetica", "Helvetica-Bold"


def md(s):
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)


def para(text, size, color=None, font=None, leading=None):
    color = color or T["INK"]
    st = ParagraphStyle("p", fontName=font or F, fontSize=size, leading=leading or size * 1.3, textColor=color)
    return Paragraph(md(text), st)


def draw(c, flow, x, y_top, w):
    _, h = flow.wrap(w, H)
    flow.drawOn(c, x, y_top - h)
    return y_top - h


def slide_frame(c, spec, n, total):
    c.setFillColor(T["BG"])
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(T["ACCENT"])
    c.rect(0, H - 8, W, 8, fill=1, stroke=0)
    c.setFont(F, 9)
    c.setFillColor(T["MUTED"])
    c.drawString(48, 22, spec.get("footer", "Recordly"))
    c.drawRightString(W - 48, 22, f"{n} / {total}")


def draw_diagram(c, d, y_top):
    """Left-to-right architecture flow: columns of boxes joined by arrows, optional band underneath.

    d = {"columns": [{"title": str, "boxes": [str]}], "band": str, "height": int}
    """
    cols = d["columns"]
    n = len(cols)
    gap = 26
    x0, width = 48, W - 96
    cw = (width - gap * (n - 1)) / n
    h = d.get("height", 190)
    top = y_top - 4
    for i, col in enumerate(cols):
        x = x0 + i * (cw + gap)
        c.setFillColor(T["PANEL"])
        c.setStrokeColor(T["RULE"])
        c.roundRect(x, top - h, cw, h, 6, fill=1, stroke=1)
        draw(c, para(col["title"], 11, T["ACCENT"], FB), x + 8, top - 6, cw - 16)
        boxes = col.get("boxes", [])
        bh = min(34, (h - 34 - 6 * len(boxes)) / max(len(boxes), 1))
        by = top - 30
        for b in boxes:
            c.setFillColor(T["BOX"])
            c.setStrokeColor(T["ACCENT"])
            c.roundRect(x + 8, by - bh, cw - 16, bh, 4, fill=1, stroke=1)
            p = para(b, 9.5, T["INK"], leading=11)
            _, ph = p.wrap(cw - 26, bh)
            p.drawOn(c, x + 13, by - bh / 2 - ph / 2)
            by -= bh + 6
        if i < n - 1:
            ax, ay = x + cw + 3, top - h / 2
            c.setStrokeColor(T["ACCENT"])
            c.setFillColor(T["ACCENT"])
            c.setLineWidth(2)
            c.line(ax, ay, ax + gap - 10, ay)
            path = c.beginPath()
            path.moveTo(ax + gap - 6, ay)
            path.lineTo(ax + gap - 13, ay + 5)
            path.lineTo(ax + gap - 13, ay - 5)
            path.close()
            c.drawPath(path, fill=1, stroke=0)
            c.setLineWidth(1)
    y = top - h - 6
    if d.get("band"):
        c.setFillColor(T["BAND"])
        c.rect(x0, y - 24, width, 22, fill=1, stroke=0)
        draw(c, para(d["band"], 10, T["INK"]), x0 + 8, y - 6, width - 16)
        y -= 30
    return y - 6


def render(spec, out):
    set_theme(spec.get("theme", "dark"))
    c = canvas.Canvas(out + ".pdf", pagesize=(W, H))
    c.setTitle(spec["title"])
    total = len(spec["slides"]) + 1
    # cover
    slide_frame(c, spec, 1, total)
    c.setFillColor(T["ACCENT"])
    c.rect(48, 300, 6, 120, fill=1, stroke=0)
    y = draw(c, para(spec["client"], 16, T["MUTED"]), 70, 420, W - 140)
    y = draw(c, para(spec["title"], 34, T["ACCENT"], FB, 40), 70, y - 6, W - 140)
    draw(c, para(spec.get("subtitle", ""), 15, T["INK"]), 70, y - 14, W - 140)
    c.showPage()
    for i, s in enumerate(spec["slides"], start=2):
        slide_frame(c, spec, i, total)
        y = draw(c, para(s["title"], 24, T["ACCENT"], FB, 29), 48, H - 40, W - 96)
        c.setStrokeColor(T["RULE"])
        c.line(48, y - 10, W - 48, y - 10)
        y -= 24
        bullets = s.get("bullets", [])
        size = 15 if len(bullets) <= 6 else 13
        for b in bullets:
            if b.startswith("-- "):
                y = draw(c, para("– " + b[3:], size - 2, T["MUTED"]), 84, y, W - 140) - 4
            else:
                c.setFillColor(T["ACCENT"])
                c.circle(56, y - size * 0.55, 3, fill=1, stroke=0)
                y = draw(c, para(b, size), 68, y, W - 120) - 7
        if s.get("diagram"):
            y = draw_diagram(c, s["diagram"], y)
        if s.get("table"):
            rows = [[para(cell, 11, T["ON_ACCENT"] if r == 0 else T["INK"], FB if r == 0 else F) for cell in row] for r, row in enumerate(s["table"])]
            ncol = len(s["table"][0])
            widths = s.get("col_widths") or [(W - 96) / ncol] * ncol
            t = Table(rows, colWidths=widths)
            t.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), T["ACCENT"]),
                ("LINEBELOW", (0, 0), (-1, -1), 0.5, T["RULE"]),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]))
            _, th = t.wrap(W - 96, H)
            t.drawOn(c, 48, y - th - 4)
            y -= th + 12
        if s.get("note"):
            draw(c, para(s["note"], 11, T["MUTED"]), 48, max(y - 4, 70), W - 96)
        c.showPage()
    c.save()


def to_md(spec):
    lines = [f"# {spec['title']}", f"_{spec['client']}: {spec.get('subtitle', '')}_", ""]
    for i, s in enumerate(spec["slides"], start=2):
        lines += [f"## {i}. {s['title']}"]
        for b in s.get("bullets", []):
            lines.append(("  - " + b[3:]) if b.startswith("-- ") else ("- " + b))
        if s.get("diagram"):
            d = s["diagram"]
            lines.append(" → ".join(f"[{col['title']}: {', '.join(col.get('boxes', []))}]" for col in d["columns"]))
            if d.get("band"):
                lines.append(f"({d['band']})")
        for r, row in enumerate(s.get("table", []) or []):
            lines.append("| " + " | ".join(row) + " |")
            if r == 0:
                lines.append("|" + " --- |" * len(row))
        if s.get("note"):
            lines.append(f"\n_{s['note']}_")
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    spec = json.load(open(sys.argv[1], encoding="utf-8"))
    out = sys.argv[2]
    render(spec, out)
    open(out + ".md", "w", encoding="utf-8").write(to_md(spec))
    print("wrote", out + ".pdf")
