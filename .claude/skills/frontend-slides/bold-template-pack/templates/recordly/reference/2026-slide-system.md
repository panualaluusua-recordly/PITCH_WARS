# Recordly 2026 — Slide Design System

Extracted from `2026_template.pptx` (37 slides, 51 layouts, updated 28.5.2026). Every value below was measured from the file, not inferred. Where the template contradicts itself, the conflict is flagged in [Known inconsistencies](#known-inconsistencies).

---

## 1. Canvas

| Property | Value |
|---|---|
| Aspect ratio | 16:9 |
| Dimensions | 10 × 5.625 in · 720 × 405 pt · 9144000 × 5143500 EMU |
| Origin | Google Slides export (PowerPoint-compatible) |
| Default background | Dark, textured |

Design at 10 × 5.625 in. If you rebuild in PowerPoint's 13.333 × 7.5 in canvas, multiply every measurement in this document by 1.333.

---

## 2. Colour

The palette lives in the theme as `Simple Light`. Eight roles, no gradients anywhere in the file.

| Token | Hex | Theme slot | Role |
|---|---|---|---|
| `ink` | `#1B1B1B` | dk1, accent2 | Default background; text on lime |
| `lime` | `#E3FF87` | dk2, accent1, hlink | Headings, active state, fills, rules |
| `paper` | `#EFEFEF` | lt1 | Primary text on dark; light-mode background |
| `grey-700` | `#434343` | accent3 | Earliest step in sequences |
| `grey-600` | `#666666` | accent4 | Hairline outlines, table row bars |
| `grey-400` | `#999999` | lt2, accent5 | Muted text, matrix fill |
| `grey-300` | `#B7B7B7` | accent6 | Body copy on dark, matrix fill |
| `teal` | `#0097A7` | folHlink | Visited links only — never as a brand colour |

Also present, undocumented in the theme: `#000000` (card interior fill), `#EEEEEE` (diagram divider lines), `#FFFFFF` (once).

### Distribution

Lime is an accent, not a background. Across the deck it carries roughly one element per slide: the heading, or one active step, or one header band. The 60/30/10 split in practice is ink / greys+paper / lime.

### Contrast

| Pairing | Ratio | Verdict |
|---|---|---|
| `paper` on `ink` | 15.0:1 | Any size |
| `lime` on `ink` | 15.5:1 | Any size |
| `grey-300` on `ink` | 8.6:1 | Any size |
| `grey-400` on `ink` | 6.1:1 | Any size |
| `ink` on `lime` | 15.5:1 | Any size — the standard lime-chip treatment |
| `grey-600` on `ink` | 3.0:1 | **Structure only.** Never body text. |

---

## 3. Backgrounds

Four modes. All are 1920 × 1080 PNGs applied as a full-bleed background fill, not shapes.

| Mode | Spec | Use |
|---|---|---|
| **Dark** (default) | `#1B1B1B` plus fine film-grain noise, rendering ≈ `#242424` | Everything, unless there's a reason |
| **Light** | `#EFEFEF` flat | Logo sheets, occasional inverted sections |
| **Lime** | `#E3FF87` flat | Rare emphasis dividers; one statement per deck at most |
| **Photo** | Greyscale image, darkened | Covers, section breaks, half-bleed panels |

The noise texture is what stops the dark mode reading as flat black. Keep it — don't substitute a plain `#1B1B1B` fill.

Photo backgrounds that carry text are darkened hard: measured mean luminance runs 37–90 out of 255 (≈ 15–35%). Photos with no text over them sit at 130–160. Match that when you place a new image, or the lime headline stops holding.

---

## 4. Typography

**Montserrat throughout**, in four weights. Helvetica Neue is the declared fallback, then Arial. All four weights are embedded in the file, so the deck travels.

| Weight | Where |
|---|---|
| Montserrat Black (900) | H1–H5, all slide titles |
| Montserrat ExtraBold (800) | Labels inside chips, cards, diagrams |
| Montserrat Light (300) | Subtitles, lead lines under titles |
| Montserrat (400) | Ingress, body copy |

### Scale

The template ships its own specimen (slide 35). These are the sanctioned sizes — don't invent intermediate ones.

| Style | Size | Weight | Colour | Line height |
|---|---|---|---|---|
| H1 | 54 pt | Black | lime | 70% |
| H2 | 34 pt | Black | lime | 70% |
| H3 | 24 pt | Black | lime | 70% |
| H4 | 14 pt | Black | lime | 70% |
| H5 | 9 pt | Black | lime | 70% |
| Ingress | 22 pt | Regular | lime | 100% |
| Subtitle / lead | 20 pt (18 pt on covers) | Light | paper or grey-300 | 100% |
| Body 01 | 16 pt | Regular | grey-300 | 100% |
| Body 02 | 12 pt | Regular | grey-300 | 100% |
| Body 03 | 8 pt | Regular | grey-300 | 100% |
| Chip / card label | 10 pt | ExtraBold | ink (on lime) | 100% |
| Diagram label | 8 pt | ExtraBold | ink or paper | 100% |

The **70% line height on headings** is the single most characteristic typographic move in this system. It governs the gap between a heading's *own* wrapped lines, which lock into a tight block; it does not apply to the space between a heading and the copy beneath it. Never loosen it.

### Heading + lead line

A heading is **one colour: lime**. Hierarchy comes from a size-and-weight drop to an off-white Montserrat Light lead line directly beneath it — 36 pt Black over 20 pt Light on the statement and framed-image layouts, 54 pt over 18 pt on covers.

The type-specimen slide (35) and the theme-reference layout (1) show a lime line above an off-white line at the same size:

```
THIS IS H1     ← lime  #E3FF87   the style's name
TITLE 54       ← paper #EFEFEF   the style's point size
```

That is the specimen labelling each style, **not a headline treatment.** Those two boxes carry no line-height override (so they sit at 100%), whereas every real title placeholder is set to 70%. Don't reproduce the two-colour pair as a design pattern.

### Body copy

- Bullet character `●` at 13 pt, indent `marL 0.5in / indent -0.34in`
- Nested levels: `○` then `■`
- Paragraph spacing: 0 before/after at level 1; 6 pt before at levels 2+
- Text box insets: 0.1 in (7.2 pt) on all four sides — Google's default, and it's why nominal gutters look wider than they measure

---

## 5. Grid

### Horizontal

| Element | Position | Width |
|---|---|---|
| Margin | 0.50 in both sides | — |
| Content column | x = 0.50 | 9.01 in |
| Two columns | x = 0.50 / 5.20 | 4.30 in each, 0.40 in gutter |
| Half split | x = 0.50 / 5.20 | 4.70 in each |
| Three columns | x = 0.50 / 3.54 / 6.58 | 2.92 in each, 0.10 in gutter (≈0.30 in visually, after insets) |
| Photo panel | x = 5.20 → 10.00 | full-bleed right half |
| Framed image | x = 5.76, y = 0.53 | 3.68 × 4.53 in |

### Vertical

| Element | y | Height |
|---|---|---|
| Eyebrow | 0.28 in | 0.32 in |
| Title | 0.62 in | 0.58 in |
| Body | 1.34 in | 3.59 in |
| Body ends | 4.93 in | — |
| Footer safe zone starts | 5.10 in | — |
| Slide number | 5.35 in (x = 4.70) | 0.23 in |

Nothing below **y = 5.10 in**. That band belongs to the baked-in furniture.

---

## 6. Furniture

Three fixed marks, baked into the background image on the master — not editable shapes, and not to be re-created per slide.

| Mark | Position | Size |
|---|---|---|
| Lime tab (rotated `ЯDLY`) | flush to top-right, x = 9.71 | 0.09 × 0.32 in |
| Wordmark | bottom-left, x = 0.19, y = 5.35 | 0.72 × 0.07 in |
| Tagline `THE BUSINESS DATA COMPANY` | bottom-right, right edge at 9.81, y = 5.35 | 1.57 in wide, ≈`#737373`, uppercase, wide tracking |

---

## 7. Logo

Wordmark: **ЯECOЯDLY** — first letter reversed, and the `R` inside `-RDLY` picked out in lime. Six variants ship in the file.

| Variant | Composition | Use |
|---|---|---|
| Ink box | ink block, paper letters, lime `Я` | On photography or busy backgrounds |
| Lime box | lime block, knockout letters | Emphasis, merchandise |
| Knockout | paper letters + lime `Я`, transparent | Dark backgrounds (the default) |
| Positive | ink letters + grey `Я`, transparent | Light backgrounds |
| `ЯDLY` tab | short lockup in ink box | Corner mark, favicon, small sizes |
| `Я` mark | single glyph in ink box | Avatar, 1:1 crops |

Clear space: at least the height of the wordmark on all sides. Never recolour the lime `Я` and never set the wordmark in Montserrat by hand — use the supplied artwork.

---

## 8. Components

Measured off the six component layouts. Line weight is **0.75 pt everywhere** and corners are **square everywhere**, except the pill rows, which are fully rounded.

### Cards (3-up)

| Part | Spec |
|---|---|
| Card | 2.78 × 3.65 in, fill `#000000`, 0.75 pt `lime` outline |
| Positions | x = 0.38 / 3.53 / 6.66, y = 1.36, gutter 0.37 in |
| Header band | 2.78 × 0.43 in, fill `lime`, flush to card top |
| Header label | 10 pt ExtraBold `ink`, centred |
| Body | 10 pt, centred, starting y = 2.81 |

The interior is `#000000`, not `ink` — slightly darker than the background, so the card reads as a recessed well rather than a raised panel. Keep it.

### Chevron process (5 steps)

| Part | Spec |
|---|---|
| Chevron | 1.87 × 2.43 in, y = 2.23, pitch 1.52 in (0.35 in overlap) |
| Positions | x = 1.76 / 3.27 / 4.79 / 6.31 / 7.83 |
| Fill sequence | `#434343` → `lime` → `#666666` → `#B7B7B7` → `#EFEFEF` |
| Outline | 0.75 pt `#666666` |
| Input block | offpage-connector 2.43 × 1.90 in at x = 0.12, fill `ink`, 0.75 pt `#666666` |
| Leader lines | 0.75 pt `#EFEFEF` |
| Labels | 8 pt ExtraBold |

Position 2 is lime — the sequence brightens left to right, and lime marks the active step. Move the lime, don't add a second one.

### Pill rows

| Part | Spec |
|---|---|
| Pill | 7.22 × 1.15 in, fully rounded, fill `lime`, no outline |
| Positions | x = 2.06, y = 1.27 / 2.66 / 4.05 (pitch 1.39 in) |
| Icon disc | 0.77 in circle, fill `ink`, inset 0.16 in from pill's top-left |
| Icon | 0.44 in, paper monoline, centred in disc |
| Row label | x = 0.14, w = 1.79 in, left of the pill |

### Table

| Part | Spec |
|---|---|
| Header bands | 0.34 in tall, fill `lime`; x/w = 0.38/1.63, 2.27/4.22, 6.74/2.96 |
| Header label | 10 pt ExtraBold `ink` |
| Row bars | 0.59–0.65 in tall, fill `#666666`, pitch 0.66 in |
| Row number gutter | 0.46 in wide at x = 2.26 |
| Column divider | 0.75 pt `#EEEEEE` vertical line with a small triangle marker |

### 2×2 matrix

| Part | Spec |
|---|---|
| Quadrant | 3.57 × 1.76 in, 0.75 pt `ink` outline |
| Positions | x = 2.06 / 5.64, y = 1.36 / 3.13 |
| Fills | `#B7B7B7` and `#999999`, alternating diagonally |
| Axes | 0.75 pt `#EFEFEF`; vertical at x = 1.96, horizontal at y = 4.97 |
| Axis labels | 8 pt ExtraBold, outside the frame |

### Icon row

Five icons at y = 2.66, x = 0.91 / 2.64 / 4.60 / 6.43 / 8.32, each ≈0.60–0.83 × 0.60 in, with labels above and below at y = 1.83 and 3.69.

### Icons

43 icons ship on the icon sheet: monoline, single-weight stroke, paper on dark, drawn to a ~0.6 in box. Add to the set in the same style rather than mixing in filled or duotone icons.

---

## 9. Photography

| Rule | Spec |
|---|---|
| Colour | Greyscale. Measured saturation across every image: 0.00–0.02. No exceptions in the file. |
| Subject | People at work — real colleagues, candid, mid-task. No stock gestures, no isolated objects. |
| Resolution | 1920 × 1080 minimum for full-bleed |
| Darkening (text over) | To 15–35% mean luminance |
| Darkening (no text) | 50–65% mean luminance |
| Framing | Full-bleed, half-bleed panel (x = 5.20 → 10.00), or framed placeholder 3.68 × 4.53 in |

Branded clothing appears in most shots. That's the motif doing work — favour images where the wordmark is legible somewhere in frame.

---

## 10. Layout patterns

The 51 layouts collapse into 11 patterns. Names below are usable; the file's own names (`CUSTOM_6_1_1_4_2_1_1_1_1_1_2`) are auto-generated noise.

| Pattern | Layouts | Structure |
|---|---|---|
| **Cover** | 2, 3, 15, 19, 20 | Photo or flat bg; centred title (lime, y 2.12, w 6.96) + 18 pt Light subtitle |
| **Statement** | 23, 24 | One title, 54 pt, y 2.12, w 7.04 |
| **Statement, offset** | 25, 26 | Title shifted right (x 3.94, w 5.57) to clear a photo subject on the left |
| **Statement, two-line** | 27, 28 | 36 pt Black title + 20 pt Light line, full width, y 1.53 / 2.81 |
| **Photo + text** | 10–14 (photo left), 16–18 (photo right), 35, 36 | Half-bleed image, text in the opposite half |
| **Text + framed image** | 21 | 36 pt title + 20 pt lead in left half, 3.68 × 4.53 in image right |
| **Content, full width** | 29, 30, 34 | Eyebrow + title + body across 9.01 in |
| **Content, two column** | 31, 32 | 4.30 in columns; L31 gives each its own title |
| **Content, three column** | 33 | 2.92 in columns, 14 pt titles, 16 pt body |
| **Diagram** | 44 (chevron), 45 (icon row), 46 (cards), 47 (pills), 48 (table), 49 (matrix) | Title + prebuilt graphic + labelled placeholders |
| **Reference** | 1 (type specimen), 42 (icons), 50, 51 (logo sheet), 40, 41 (lockups), 43 (blank) | Not for presenting — brand reference pages |

Title size varies by pattern, and it's deliberate: 54 pt for statements, 36 pt where a lead line follows, 34 pt for standard content, 30 pt on diagram slides, 24 pt in two columns, 14 pt in three.

---

## 11. Rules

**Do**

- One lime element per slide. Heading, or active step, or header band — pick one.
- Keep 70% line height across every heading's own wrapped lines.
- Left-align body copy and lists. Centre only cover titles and chip labels.
- Respect the 0.50 in margin and the 5.10 in floor.
- Hold every rule and outline at 0.75 pt.
- Keep photography greyscale and darken it to match the text over it.
- Use the type scale as given: 54 / 34 / 24 / 22 / 20 / 16 / 14 / 12 / 10 / 9 / 8.

**Don't**

- Don't tint lime, add a second accent, or introduce `#0097A7` as a brand colour.
- Don't round rectangle corners. Square everywhere; pills are the one exception and they're fully rounded.
- Don't set `#666666` as body text on dark — it's a 3.0:1 structural grey.
- Don't rebuild the logo, tagline, or corner tab as shapes. They're on the master.
- Don't set headings in anything but Montserrat Black.
- Don't drop the background noise for a flat fill.
- Don't put content in the bottom 0.5 in.

---

## Known inconsistencies

Worth fixing if this template gets a 2027 revision:

1. **Two left margins.** The `CUSTOM_*` layouts sit at x = 0.495 in; the `BLANK_*` diagram layouts sit at x = 0.38 in. Content slides and diagram slides are misaligned by 0.11 in. Standardise on 0.50 in.
2. **Eyebrow drifts.** The eyebrow placeholder sits at y = 0.28 on content layouts but 0.01–0.24 on the diagram layouts.
3. **Heading weight split.** The type specimen slide uses Montserrat Black for H2–H5; the reference layout uses Montserrat ExtraBold for the same styles. Pick one — Black is dominant in real use.
4. **Stray values.** `#E46962` (a coral) appears once in layout 3, and Manrope is declared once in layout 48 on an empty run. Neither belongs to the system; both are leftovers.
5. **Auto-generated layout names.** All 51 are named `CUSTOM_*` or `BLANK_*` with numeric suffixes, so nobody can pick a layout from the menu. Rename them to the patterns in section 10.
6. **Theme font mismatch.** The theme's major/minor fonts are still Arial while every real style overrides to Montserrat. Set the theme fonts to Montserrat so new text boxes start on-brand.
7. **Unused reference layouts** (40, 41, 50, 51, 1, 42) sit in the same list as presentation layouts. Move them to the end or into a separate brand file.
