---
version: 2026.2
name: Recordly
description: "Recordly's own house design system, measured from the production 2026 slide template (2026_template.pptx — 37 slides, 51 layouts). Dark-mode-first (#1B1B1B, film-grain textured) with a single Signal Lime (#E3FF87) carrier per slide. Montserrat is the only face: Black 900 for every heading at 70% line-height, ExtraBold 800 for uppercase chip and diagram labels, Light 300 for lead lines, Regular 400 for body. Structure is square-cornered and 2px-hairline flat — no gradients, no drop shadows, no rounded cards. Photography is always greyscale. A heading is lime Black at 0.70 line-height, with an off-white Montserrat Light lead line beneath it at 1.0."

colors:
  ink: "#1B1B1B"
  well: "#000000"
  lime: "#E3FF87"
  paper: "#EFEFEF"
  grey-700: "#434343"
  grey-600: "#666666"
  grey-400: "#999999"
  grey-300: "#B7B7B7"
  divider: "#EEEEEE"
  tagline: "#737373"
  teal-visited: "#0097A7"

color-aliases:
  surface-page-dark: ink
  surface-well-dark: well
  surface-page-light: paper
  surface-page-lime: lime
  text-strong-dark: paper
  text-body-dark: grey-300
  text-muted-dark: grey-400
  text-on-lime: ink
  border-structural: grey-600
  border-accent: lime

typography:
  h1:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontWeight: 900
    fontSize: "clamp(96px, min(7.5vw, 13.3vh), 144px)"
    lineHeight: 0.7
    sourcePt: 54
  h1-lead:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontWeight: 900
    fontSize: "clamp(64px, min(5vw, 8.9vh), 96px)"
    lineHeight: 0.7
    sourcePt: 36
  h2:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontWeight: 900
    fontSize: "clamp(61px, min(4.7vw, 8.4vh), 91px)"
    lineHeight: 0.7
    sourcePt: 34
  h2-diagram:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontWeight: 900
    fontSize: "clamp(54px, min(4.2vw, 7.4vh), 80px)"
    lineHeight: 0.7
    sourcePt: 30
  h3:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontWeight: 900
    fontSize: "clamp(43px, min(3.3vw, 5.9vh), 64px)"
    lineHeight: 0.7
    sourcePt: 24
  h4:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontWeight: 900
    fontSize: "clamp(25px, min(1.95vw, 3.4vh), 37px)"
    lineHeight: 0.7
    sourcePt: 14
  h5:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontWeight: 900
    fontSize: "clamp(16px, min(1.25vw, 2.2vh), 24px)"
    lineHeight: 0.7
    sourcePt: 9
  ingress:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontWeight: 400
    fontSize: "clamp(39px, min(3.05vw, 5.4vh), 59px)"
    lineHeight: 1
    sourcePt: 22
  subtitle:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontWeight: 300
    fontSize: "clamp(36px, min(2.8vw, 4.9vh), 53px)"
    lineHeight: 1
    sourcePt: 20
  subtitle-cover:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontWeight: 300
    fontSize: "clamp(32px, min(2.5vw, 4.4vh), 48px)"
    lineHeight: 1
    sourcePt: 18
  body:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontWeight: 400
    fontSize: "clamp(29px, min(2.2vw, 4vh), 43px)"
    lineHeight: 1.35
    sourcePt: 16
  body-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontWeight: 400
    fontSize: "clamp(22px, min(1.65vw, 3vh), 32px)"
    lineHeight: 1.35
    sourcePt: 12
  body-xs:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontWeight: 400
    fontSize: "clamp(15px, min(1.1vw, 2vh), 21px)"
    lineHeight: 1.35
    sourcePt: 8
  chip-label:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontWeight: 800
    fontSize: "clamp(18px, min(1.4vw, 2.5vh), 27px)"
    lineHeight: 1
    textTransform: uppercase
    sourcePt: 10
  diagram-label:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontWeight: 800
    fontSize: "clamp(15px, min(1.1vw, 2vh), 21px)"
    lineHeight: 1
    textTransform: uppercase
    sourcePt: 8
  eyebrow:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontWeight: 800
    fontSize: "clamp(15px, min(1.1vw, 2vh), 21px)"
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
    sourcePt: 8
  tagline-chrome:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontWeight: 800
    fontSize: "clamp(10px, min(0.75vw, 1.35vh), 14px)"
    lineHeight: 1
    letterSpacing: 0.22em
    textTransform: uppercase

spacing:
  margin: "96px"
  content-width: "1730px"
  y-eyebrow: "54px"
  h-eyebrow: "61px"
  y-title: "119px"
  h-title: "111px"
  y-body: "257px"
  h-body: "689px"
  y-floor: "979px"
  col-two: "826px"
  gutter-two: "77px"
  col-half: "902px"
  col-three: "561px"
  gutter-three: "19px"
  text-inset: "19px"
  hairline: "2px"
  radius-standard: "0"
  radius-pill: "9999px"

canvas:
  width: 1920px
  height: 1080px
  background: "{colors.ink}"
  texture: "fine film grain over {colors.ink}, rendering ≈ #242424 — never a flat fill"

components:
  eyebrow:
    background: "transparent"
    color: "{colors.grey-300}"
    letterSpacing: 0.1em
    textTransform: uppercase
    description: "Small uppercase section label sitting above the title at y 54px. Not lime, no pill, no fill — the source template's eyebrow is plain tracked-out type. If a slide needs a lime carrier, it goes to a component below, not here."
  title:
    color: "{colors.lime}"
    fontWeight: 900
    lineHeight: 0.7
    description: "The heading. Always lime, always Black 900, and always 0.70 line-height — which governs the gap between a heading's OWN wrapped lines, not the gap to anything else. A heading is one colour: do not split it across lime and off-white lines. NOTE: the source template's type-specimen slide shows a lime line above an off-white line at the same size ('THIS IS H1' / 'TITLE 54'); that is the specimen naming each style and its point size, not a headline treatment. Do not reproduce it as a design pattern."
  lead-line:
    fontWeight: 300
    color: "{colors.paper}"
    lineHeight: 1
    description: "Montserrat Light line sitting directly under a heading, one tier smaller (a 36 pt heading takes a 20 pt lead; a cover's 54 pt takes 18 pt). Off-white, never lime. This is the system's hierarchy device — a size-and-weight drop, not a colour change inside the heading."
  card:
    background: "{colors.well}"
    border: "{spacing.hairline} solid {colors.lime}"
    borderRadius: "0"
    size: "534px x 701px"
    description: "Flat square-cornered panel with a lime hairline outline and a PURE BLACK interior — one step darker than the page, so the card reads as a recessed well rather than a raised panel. Never {colors.ink}, never a shadow, never a radius."
  card-header:
    background: "{colors.lime}"
    color: "{colors.ink}"
    height: "83px"
    description: "Lime-filled band flush to the card's top edge, carrying a centred {typography.chip-label}. This band is the card grid's lime carrier — the three headers together count as one carrier, not three."
  chevron-process:
    size: "359px x 467px each, pitch 292px (67px overlap)"
    border: "{spacing.hairline} solid {colors.grey-600}"
    description: "Five chevrons brightening left to right: {colors.grey-700} → {colors.lime} → {colors.grey-600} → {colors.grey-300} → {colors.paper}. Position two is lime and is the slide's carrier. Move the lime to shift emphasis; never add a second lime step. Optional input block (467px x 365px, ink fill, grey-600 hairline) sits left of step one."
  pill-row:
    background: "{colors.lime}"
    borderRadius: "{spacing.radius-pill}"
    size: "1386px x 221px, pitch 267px"
    description: "The ONLY rounded component in the system, and the only place lime carries an icon. An ink disc (148px, inset 31px from the pill's top-left, not vertically centred) holds a 85px paper monoline icon. A {typography.diagram-label} row label sits to the left of the pill, outside it."
  table:
    description: "Lime header bands (65px tall) over grey-600 row bars (119px, pitch 127px). No cell borders, no zebra striping. Column 1 is the label column; an 88px gutter column at x 434px carries row numbers. Vertical dividers are {spacing.hairline} {colors.divider} with a small triangle marker. Max 7 rows."
  matrix-2x2:
    description: "Four 686px x 338px quadrants alternating {colors.grey-300} / {colors.grey-400} diagonally, each with an ink hairline. Axes are {spacing.hairline} {colors.paper} lines. This is the one component with NO lime at all — do not add a lime quadrant to give it an accent."
  icon-row:
    size: "115px icons, five across"
    description: "Five icons with a {typography.diagram-label} above and a {typography.body-xs} caption below. 40 icons ship in `assets/icons/`, named by subject, in two families: outline (single-weight monoline) and solid (filled with a grain texture matching the page ground). The source template's own icon row (layout 45) uses the five SOLID icons — eye, people-group, gauge, target, diamond — while the pill rows use outline icons inside the ink disc. Pick one family per row and stay in it; never mix. View `assets/icons/contact-sheet.png` to choose, and pull the real artwork rather than drawing stand-ins. Any addition matches the outline family's stroke weight and 115px box — never a third style, never duotone."
  photo:
    filter: "grayscale(1)"
    description: "Every image in the system is greyscale — measured saturation across all 86 source assets is 0.00–0.02, with no exceptions. Darken to 15–35% mean luminance when text sits over it, 50–65% when it doesn't. Framings: full bleed, half bleed from x 998px, or a framed 707px x 870px block at x 1106px / y 102px."
  placeholder-ph:
    background: "{colors.grey-700}"
    borderRadius: "0"
    description: "Flat grey block with a bottom-aligned {typography.body-xs} caption naming exactly what belongs there ('photograph: data engineer at a whiteboard'). Never draw or generate a stand-in image."
  furniture:
    description: "Three fixed marks reproduced on EVERY slide, matching the source template's baked-in master background: the lime tab (17px x 61px, flush to the top edge at x 1864px); the wordmark (138px x 13px at x 36px / y 1027px); and the tagline 'THE BUSINESS DATA COMPANY' in {typography.tagline-chrome} {colors.tagline}, right-aligned to x 1884px at y 1027px. This is why nothing else may sit below y 979px."
  pagination:
    position: "absolute, x 902px, y 1027px, width 115px, centred"
    color: "{colors.grey-400}"
    description: "Slide number, {typography.body-xs}, centred in the footer band between the wordmark and the tagline — the source template places it dead centre, not bottom-right."
---

## Frontend Slides Fixed-Stage Policy

The source system is a fixed **10 × 5.625 in / 720 × 405 pt** slide box that does not reflow. That maps onto the `frontend-slides` fixed-stage model exactly: generate a **1920×1080 stage** and treat every value in this file as already being at that scale. Two conversion factors, both exact, are worth keeping in mind when reading the source template directly:

- **Type:** 1920 / 720 pt = **×2.667**. A 54 pt title is 144 px; a 16 pt body is 43 px.
- **Geometry:** **192 px per inch**. A 0.5 in margin is 96 px; a 0.75 pt hairline is 2 px.

Every `fontSize` below carries its `sourcePt` so you can always get back to the original. The `clamp()` wrapper is stage-scaling give only — the design intent is the upper px value. Content never re-wraps or re-stacks for narrower screens; if a slide is at risk of overflow, split it, and never shrink type below the scale's floor.

## Overview

**Recordly is the organization this kit belongs to** — this is its actual house brand. Unlike every other template in this pack, which is an inspiration board, this one is a spec: every colour, size, and position below was measured from the production file `2026_template.pptx` (37 slides, 51 layouts, updated 28.5.2026), not inferred.

The system runs on **one face**. Montserrat does all four jobs: **Black 900** for every heading, **ExtraBold 800** for the uppercase chip/diagram/eyebrow vocabulary, **Light 300** for lead lines under a title, **Regular 400** for ingress and body. There is no second family and no mono face — figures use Montserrat with `font-variant-numeric: tabular-nums`.

The single most characteristic move in the system is **70% line-height on headings**. A heading that wraps to two or three lines locks into a tight block where the lines almost touch. It looks wrong until you see it against the rest of the brand, and it is non-negotiable — loosening it to a "safe" 1.1 is the fastest way to make a deck stop looking like Recordly. The 0.70 governs a heading's own wrapped lines only; the gap down to a lead line or body block is ordinary spacing, not 0.70.

Colour is dark-mode-first: **#1B1B1B with a fine film grain** (the noise is what keeps it from reading as flat black — reproduce it as an SVG `feTurbulence` overlay at ~5% opacity, never substitute a solid fill). Against that field sits exactly one saturated colour, **Signal Lime `#E3FF87`**, plus a five-step grey ramp and off-white `#EFEFEF` for text. Lime is a carrier, not a wash: one lime element per slide, though in this system a "lime element" is allowed to be a large fill — a card header band, a full-width pill, a table header row.

Structure is square and flat: **2px hairlines** (0.75 pt at source), **zero border radius** everywhere except the pill rows, which are fully rounded, and **zero shadows or gradients**. Photography is **always greyscale**.

**Key characteristics:**
- `#1B1B1B` page with film-grain texture; light (`#EFEFEF`) and full-lime schemes exist for rare emphasis surfaces.
- One Signal Lime (`#E3FF87`) carrier per slide — a heading, one chevron step, one header band, or one pill stack.
- Montserrat only. Black 900 headings at **0.70 line-height**; ExtraBold 800 uppercase labels; Light 300 leads; Regular 400 body.
- Headings are lime and single-coloured; an off-white Montserrat Light lead line sits beneath, one tier smaller.
- Square corners, 2px hairlines, no shadows, no gradients. Pills are the one rounded thing.
- Greyscale photography, darkened to match whatever text sits on it.
- Baked-in furniture — lime corner tab, wordmark, tagline — on every slide; nothing below y 979px.
- No emoji, no invented figures/quotes/customer names, no drawn logos.

## Colors

### Palette (dark, default)

- **Ink** (`{colors.ink}` — `#1B1B1B`): page background, always with the grain overlay. Also the text colour on any lime surface.
- **Well** (`{colors.well}` — `#000000`): card interiors only. Deliberately darker than the page.
- **Signal Lime** (`{colors.lime}` — `#E3FF87`): headings, the active step in a sequence, card header bands, pill fills, table headers, hairline outlines on cards, links.
- **Paper** (`{colors.paper}` — `#EFEFEF`): lead lines and subtitles, axis lines, icons, the brightest step in a sequence.
- **Grey ramp**: `{colors.grey-700}` `#434343` (first step in a sequence, `.ph` fill) → `{colors.grey-600}` `#666666` (structural hairlines, table row bars — **never text**, it's 3.0:1) → `{colors.grey-400}` `#999999` (muted text, matrix fill) → `{colors.grey-300}` `#B7B7B7` (body copy on dark, matrix fill).
- **Divider** (`{colors.divider}` — `#EEEEEE`): diagram divider lines only.
- **Tagline** (`{colors.tagline}` — `#737373`): the footer tagline as it renders in the source. Chrome only.
- **Teal** (`{colors.teal-visited}` — `#0097A7`): visited-link colour inherited from the theme. **Never a brand colour** — do not put it on a slide.

### Alternate schemes

- **Light**: `{colors.paper}` `#EFEFEF` page, ink text, lime unchanged. Used in the source only for logo/reference sheets and occasional inverted sections.
- **Lime**: a full `#E3FF87` page with ink type. The source ships five of these layouts and uses none of them in the actual deck — treat it as at most one slide per deck, for a single hard emphasis beat.

Never mix schemes within one deck beyond that one sanctioned lime beat.

### Contrast (measured)

| Pairing | Ratio | Verdict |
|---|---|---|
| paper on ink | 15.0:1 | Any size |
| lime on ink | 15.5:1 | Any size |
| ink on lime | 15.5:1 | Any size — the standard chip treatment |
| grey-300 on ink | 8.6:1 | Any size |
| grey-400 on ink | 6.1:1 | Any size |
| grey-600 on ink | 3.0:1 | **Structure only. Never text.** |
| grey-700 on ink | 1.7:1 | Fills and sequence steps only |

### Defaults

- **Default surface**: `{colors.ink}` + grain.
- **Default heading colour**: `{colors.lime}`. This system differs from most — headings *are* the lime, rather than off-white with a lime accent word. Off-white belongs to the Light lead line beneath the heading, not to a second line of the heading itself.
- **Default body colour**: `{colors.grey-300}`.
- **Default border**: `{spacing.hairline}` solid — lime on cards, `{colors.grey-600}` on structural shapes.
- **One-carrier rule**: before finalising a slide, name the single element carrying the lime. "More than one" or "none" both mean fix it. A three-card grid's three header bands count as one carrier because they're one component.

## Typography

### Font Family Stack

**Montserrat** (Google Fonts, weights 300/400/800/900) is the entire system. Load exactly those four weights; the source template embeds Montserrat Light, Regular, ExtraBold and Black and nothing else that matters. Fallback chain is `'Helvetica Neue', Arial, sans-serif`, matching the source's own declared fallback.

There is **no second family and no monospace face**. For tabular figures use Montserrat 400 with `font-variant-numeric: tabular-nums`.

### Typography Scale

| Token | Source | Stage px | Weight | Line-height | Use |
|---|---|---|---|---|---|
| `{typography.h1}` | 54 pt | 144 | 900 | 0.70 | Statement slide, cover headline |
| `{typography.h1-lead}` | 36 pt | 96 | 900 | 0.70 | Title where a Light lead line follows |
| `{typography.h2}` | 34 pt | 91 | 900 | 0.70 | Standard content slide heading |
| `{typography.h2-diagram}` | 30 pt | 80 | 900 | 0.70 | Heading on a diagram slide |
| `{typography.h3}` | 24 pt | 64 | 900 | 0.70 | Column heading in a two-column layout |
| `{typography.h4}` | 14 pt | 37 | 900 | 0.70 | Column heading in a three-column layout |
| `{typography.h5}` | 9 pt | 24 | 900 | 0.70 | Smallest heading tier; rare |
| `{typography.ingress}` | 22 pt | 59 | 400 | 1.0 | Lime standfirst paragraph |
| `{typography.subtitle}` | 20 pt | 53 | 300 | 1.0 | Lead line under a title |
| `{typography.subtitle-cover}` | 18 pt | 48 | 300 | 1.0 | Cover-slide subtitle |
| `{typography.body}` | 16 pt | 43 | 400 | 1.35 | Default paragraph and list item |
| `{typography.body-sm}` | 12 pt | 32 | 400 | 1.35 | Card copy, dense columns |
| `{typography.body-xs}` | 8 pt | 21 | 400 | 1.35 | Captions, pagination, footnotes |
| `{typography.chip-label}` | 10 pt | 27 | 800 | 1.0 | Card header band, table header |
| `{typography.diagram-label}` | 8 pt | 21 | 800 | 1.0 | Chevron/pill/axis labels |
| `{typography.eyebrow}` | 8 pt | 21 | 800 | 1.0 | Section eyebrow above a title |
| `{typography.tagline-chrome}` | — | 14 | 800 | 1.0 | Footer tagline only |

Heading size is chosen **by layout, not by taste**: 144 px for statements, 96 px where a lead line follows, 91 px for standard content, 80 px on diagram slides, 64 px in two columns, 37 px in three. If a heading looks too heavy, change the layout or shorten the copy — never drop below Black 900.

### Defaults

- **Default heading token**: `{typography.h2}` on any ordinary content slide. `{typography.h1}` is for statement and cover slides only.
- **Default heading weight**: 900. Montserrat at 500/600/700 does not exist in this system.
- **Default label treatment**: ExtraBold 800, uppercase. Eyebrows carry 0.1em tracking; chip and diagram labels sit at default tracking.
- **Default line-height**: **0.70 on every heading**, 1.0 on ingress/subtitle/labels, 1.35 on body. The gap between a 0.70 heading and 1.35 body is the system's core rhythm.

### Signature Treatments

- **70% heading line-height.** The whole identity rests on this. Reproduce it literally on a heading's own wrapped lines, including where they nearly collide. Do not apply 0.70 to the space between a heading and the copy under it.
- **Lime headline + Light lead line.** The heading is lime Black; directly beneath it sits an off-white Montserrat Light line one tier down (36 pt → 20 pt, 34 pt → 20 pt) at 1.0 line-height. That size-and-weight drop is the hierarchy, not a colour split inside the heading.
- **A heading is one colour.** The specimen slide's lime-over-off-white pair is the specimen naming each style and its point size — not a headline treatment to copy.
- **Bullets are `●`, then `○`, then `■`**, at 13 pt source (35 px stage), indented 0.5 in (96 px) with a -0.34 in (-65 px) hanging indent.
- **ALL CAPS only on eyebrows, chip labels, diagram labels, table headers and CTAs.** Headings in the source are set in caps as content ('THIS IS H1'), so follow the user's own copy case for headings rather than force-uppercasing.

## Layout

### Canvas System

Fixed **1920×1080** stage, uniform **96px margin** on all four sides, one **1730px** content column. Three fixed rows, all measured from the source master:

| Row | y | Height |
|---|---|---|
| Eyebrow | 54px | 61px |
| Title | 119px | 111px |
| Body | 257px | 689px (ends 947px) |
| **Floor** | **979px** | Furniture band — nothing else goes here |

### Column Tracks

| Track | x | Width | Gutter |
|---|---|---|---|
| Content | 96 | 1730 | — |
| Two column | 96 / 998 | 826 | 77 |
| Half split | 96 / 998 | 902 | — |
| Three column | 96 / 680 / 1263 | 561 | 19 (≈57 visual, after insets) |
| Photo panel | 998 | 922, full bleed | — |
| Framed image | 1106 (y 102) | 707 × 870 | — |

Text blocks carry a **19px inset** on all four sides (0.1 in at source), which is why nominal gutters read wider than they measure.

### Persistent Chrome

The **furniture** (`{components.furniture}`) appears on every slide: lime tab top-right, wordmark bottom-left, tagline bottom-right. Pagination sits **centred** in the footer band at x 902px, not bottom-right. In the source these marks are baked into the master's background image; in a generated deck, reproduce them as a shared chrome layer so they're identical on every slide.

### The Closed Layout Set

Every slide must be one of these eleven surfaces, each mapped to the source layouts it came from. Do not invent a twelfth or hand-roll per-slide CSS outside this set.

1. **Cover** *(source L2, 3, 15, 19, 20)* — greyscale photo or flat ground; centred lime title (x 292px, y 407px, w 1337px) + `{typography.subtitle-cover}` lead. Wordmark lockup instead of the small footer wordmark.
2. **Statement** *(L23, 24)* — one line, `{typography.h1}`, x 96px / y 407px / w 1352px. Used when the point is the whole slide.
3. **Statement, offset** *(L25, 26)* — title shifted right to x 757px / w 1070px so a photo subject on the left stays visible.
4. **Statement, two-line** *(L27, 28)* — `{typography.h1-lead}` at y 294px + `{typography.subtitle}` at y 540px, both full width.
5. **Photo + text** *(L10–14, 16–18, 35, 36)* — half-bleed greyscale image on one side, eyebrow + title + body in the other 902px half. Photo left or photo right; alternate across a deck rather than repeating one side.
6. **Text + framed image** *(L21)* — `{typography.h1-lead}` + `{typography.subtitle}` in the left half, framed 707×870px image at x 1106px.
7. **Content, full width** *(L29, 30, 34)* — eyebrow + `{typography.h2}` + body across the full 1730px.
8. **Content, two column** *(L31, 32)* — 826px columns; L31's variant gives each column its own `{typography.h3}` heading.
9. **Content, three column** *(L33)* — 561px columns, `{typography.h4}` headings, `{typography.body}` copy.
10. **Diagram** *(L44 chevron, 45 icon row, 46 cards, 47 pills, 48 table, 49 matrix)* — `{typography.h2-diagram}` heading plus exactly one of the six prebuilt graphics. Pick the graphic that matches the content's actual shape: a sequence gets chevrons, parallel options get cards, capabilities get pills, comparison gets the table, positioning gets the matrix, categories get the icon row.
11. **Closer** *(L28, 50)* — final slide. Wordmark lockup, one closing line, no pagination. A full-lime ground is permitted here if the deck hasn't already spent its one lime beat.

## Depth and Elevation

### No Shadows, No Gradients

Zero `box-shadow`, zero `text-shadow`, zero decorative gradients. Two sanctioned exceptions:

1. The **film-grain overlay** on the page background — an SVG `feTurbulence` fractal-noise layer at ~5% opacity, desaturated. This is not decoration; without it the dark ground reads as flat black and the deck stops matching the source.
2. A **dark scrim over a full-bleed photo**, used solely to bring the image down to the 15–35% luminance band so text stays legible.

### Flat Square Structure

Depth comes from three flat tones — page (`#1B1B1B`), well (`#000000`), and lime — plus 2px hairlines. There is no elevation ladder beyond that. A card is *recessed*, not raised: its interior is darker than the page, which is the opposite of the usual card instinct and is the detail most often got wrong.

### Border Radius

**Zero on everything.** The pill rows are the single exception and they are fully rounded (`{spacing.radius-pill}`). There is no intermediate radius in this system — no 6px "softened card", no 4px chip. A rounded card is an immediate tell that the system wasn't followed.

## Shapes and Treatment

### Border Weights

2px is the universal hairline (0.75 pt at source, used for every rule, outline and divider in the file). Lime on cards, `{colors.grey-600}` on structural shapes and chevrons, `{colors.paper}` on axis and leader lines, `{colors.divider}` on table dividers. No double borders, no gradient borders, no single-side accent stripes.

### Decorative Element Types

**Two-tone title** — the primary lime carrier on most slides.

**Card with lime header band** — square black-interior panel, lime hairline, lime-filled header carrying a centred chip label.

**Chevron step** — one of five, with lime marking the active position.

**Pill row** — full-round lime bar with an inset ink icon disc. The only rounded shape in the system.

**Lime table header** — a filled band over grey row bars.

**Icon** — 115px box, from `assets/icons/`. Two families: outline (single stroke weight) and solid (grain-filled). One family per row.

**Placeholder (`.ph`)** — flat grey-700 block, square corners, bottom-aligned caption naming the missing asset. Never a drawn stand-in.

**Furniture** — lime tab, wordmark, tagline. Chrome, not content.

## Voice & Copy Rules

This system carries brand-voice rules alongside its visual rules — treat both as equally non-negotiable:

- **Person**: "we" for Recordly, "you"/"your" for the audience. Never third-person about Recordly in body copy.
- **Casing**: eyebrows, chip labels, diagram labels, table headers and CTAs are ALL CAPS. Body is sentence case. Follow the user's own case for headings. Never Title Case Every Word.
- **Emphasis**: the lime heading itself is the emphasis. Don't italicise or recolour single words inside it, and don't split it across two colours.
- **CTAs**: first-person, imperative, a little playful — "SHOW ME THE WAY", "I'M INTRIGUED" — not "Learn More" / "Get Started".
- **Length**: 1–3 sentences per section; a bullet is one line, two at most.
- **No emoji.** Anywhere, ever.
- **Vocabulary**: concrete and specific — a number, a system, a named failure, a stance. Avoid "synergy", "leverage" as a verb, journey-as-metaphor, "unlock potential" without a number, and any headline generic enough to sit unchanged on a competitor's deck.
- **Never invent** figures, customer names, or quotes. An unknown number becomes a bracketed `[figure]` placeholder that gets flagged to the user, not a made-up statistic.

## Do's and Don'ts

### Do

- Put the film grain on every dark surface — SVG fractal noise at ~5%, never a flat `#1B1B1B` fill.
- Set every heading in Montserrat Black 900, lime, sized by layout per the scale table, with **0.70 line-height across its own wrapped lines**.
- Pair a lime Black heading with an off-white Montserrat Light lead line beneath it, one tier smaller, at 1.0 line-height.
- Give every slide exactly one lime carrier and name it before moving on.
- Keep all four margins at 96px and leave everything below y 979px to the furniture.
- Hold every rule and outline at 2px, and every corner at zero radius except the pill rows.
- Fill card interiors with `#000000`, not `#1B1B1B`.
- Keep photography greyscale, darkened to 15–35% under text and 50–65% without.
- Reproduce the furniture — lime tab, wordmark, tagline — identically on every slide, with pagination centred.
- Match the diagram component to the content's real shape; a sequence gets chevrons, not cards.
- Use real logo and icon assets, embedded inline (inline `<svg>` or a `data:` URI) so the deck stays a single self-contained file.

### Don't

- Don't use `#DEFF16` or any other yellow — the accent is `#E3FF87`, and `#DEFF16` appears nowhere in the 2026 template.
- Don't set type in Archivo, Hanken Grotesk, Roboto Mono, or any face other than Montserrat.
- Don't loosen a heading's line-height toward 1.1 because 0.70 looks tight — it is meant to look tight. Equally, don't apply 0.70 to the gap between a heading and the copy beneath it; that collides.
- Don't round any corner except a pill row, and don't invent an intermediate radius.
- Don't set `#666666` as text — it's a 3.0:1 structural grey.
- Don't put `#0097A7` on a slide; it's an inherited visited-link value, not a brand colour.
- Don't add a drop shadow or a decorative gradient beyond the grain overlay and the photo scrim.
- Don't give a card a raised look, a coloured left rule, or an interior lighter than the page.
- Don't add a second lime element to a slide that already has one — including a lime quadrant on the matrix, which is deliberately lime-free.
- Don't split a heading across a lime line and an off-white line. That's the type specimen's labelling, not a brand pattern.
- Don't put content below y 979px, or shrink margins below 96px to fit more in.
- Don't colourise a photograph or use a duotone treatment.
- Don't use emoji, Title Case headings, or generic consultancy phrasing.
- Don't invent a customer name, quote, or statistic — mark the unknown and flag it.
- Don't invent a twelfth layout or write bespoke per-slide CSS outside the eleven named surfaces.

## Responsive Behavior

The source is a fixed 10 × 5.625 in box that crops rather than reflows. Carry that discipline over: the 1920×1080 stage scales as a whole (letterbox/pillarbox) and slide content never re-wraps or re-stacks for narrower screens. If content risks overflowing the padded box, split it into a second slide — never shrink type below the scale's floor values to force a fit.

### Scaling Behavior

- Headings scale 96 → 144px (h1) and 61 → 91px (h2); body scales 29 → 43px — all through the `clamp()` stage-scaling net, not as a mobile reflow mechanism.
- Margins, gutters, hairlines and the zero radius are fixed at their design values regardless of viewport.

### Presenter Behavior

Standard `frontend-slides` navigation: arrow keys / space to advance, swipe/tap where enabled. No template-specific chrome beyond the centred pagination number in the footer band.

## Iteration Guide

1. Any new deck stays in the dark scheme, with at most one lime-ground slide for a single emphasis beat.
2. Any new slide is one of the eleven named layouts. If none fits, re-shape the content — don't add a layout.
3. Any new slide gets exactly one lime carrier. Name it. Two means fix it; none means fix it.
4. Any new heading is Montserrat Black 900 in lime, sized by its layout, 0.70 across its own wrapped lines, with an off-white Light lead line beneath it where the layout calls for one.
5. Any new body or list copy is Montserrat 400 at 1.35, in `{colors.grey-300}`.
6. Any new label is Montserrat ExtraBold 800, uppercase, at 21 or 27px.
7. Any new number lands in a table's tabular-nums column or a diagram label — never a bulleted metric.
8. Any new panel is the card component (black interior, lime hairline, lime header band) — never a new bordered box.
9. Any new image is a real greyscale asset at the right luminance, or a named `.ph` placeholder.
10. Before shipping, check the grain is present, the floor is clear, every corner is square except the pills, no heading has drifted off 0.70, and no heading has been split into two colours.

## Provenance

Measured from `2026_template.pptx` and documented in this template's `reference/` folder:

- `reference/2026-slide-system.md` — the full written spec, including contrast maths, component dimensions in source inches, and the layout inventory.
- `reference/2026-tokens.json` — the same values machine-readable, in source units (inches and points) for anyone regenerating the PowerPoint template rather than a web deck.
- `reference/recordly-base.css` — this file's values as ready stage CSS: palette, type scale, grain overlay, furniture layer, and every component as a class. Copy it in after `viewport-base.css` rather than re-deriving the tokens by hand.
- `assets/` — the real brand artwork, extracted from the source file: `logo/` (six wordmark variants) and `icons/` (40 named icons plus a labelled contact sheet). See `assets/README.md`.

Where this file and those references disagree, the references win: they are in source units and this file is their ×2.667 / ×192 translation onto the 1920×1080 stage.

## Known Gaps

- **Fonts are now real, not substitutions.** The previous version of this template guessed Archivo + Hanken Grotesk + Roboto Mono. The source template embeds Montserrat Light/Regular/ExtraBold/Black, all four available on Google Fonts, so no substitution is needed. Helvetica Neue is the source's own declared fallback.
- **The lime differs from the Marp theme.** Recordly's older Marp deck theme uses Workman Yellow `#DEFF16` with a "never a fill" rule. The 2026 PowerPoint template uses `#E3FF87` and does use it as a large fill in named components. This file follows the 2026 template. If the two brand expressions need reconciling, that's a decision for the brand owner, not something to average.
- **No chart engine.** Tables, stats in tables, and the matrix are the only numeric surfaces. A bar or line chart has to be built ad hoc within the flat/square/2px/one-lime discipline — no gradients, no shadows on chart marks.
- **No CJK guidance.** The voice rules are English/Finnish only; Finnish product and event names stay untranslated inline.
- **Assets now ship with the template.** The six logo variants and 40 named icons are extracted into `assets/logo/` and `assets/icons/`, with a labelled `contact-sheet.png` for picking an icon. They still have to be inlined as `data:` URIs at generation time so the deck stays a single file — but no longer extracted from the `.pptx` first. Photography is the remaining external asset: the source's 86 staff images stay in the `.pptx`.
- **The source template has seven internal inconsistencies** (two different left margins, a drifting eyebrow y, a Black/ExtraBold split on the same styles, stray `#E46962` and Manrope declarations, auto-generated layout names, and theme fonts still set to Arial). This file resolves each in favour of the dominant usage; `reference/2026-slide-system.md` lists them all.
