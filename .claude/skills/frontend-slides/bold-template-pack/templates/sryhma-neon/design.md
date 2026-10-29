---
version: alpha
name: S-ryhmä Neon
description: A Finnish cooperative-retail operations system built on two greens — the heritage S-green (#00aa46) that carries structure on light surfaces, and a neon sibling (#00f062) that behaves like emitted light on near-black ink. Display type runs Space Grotesk; Archivo handles body and chrome; every numeral is JetBrains Mono with tabular figures. Light slides are white cards on a near-white ground with hairline borders; dark slides are ink surfaces carrying a hairline scan grid and neon glow. The aesthetic borrows from retail operations dashboards, warehouse floor terminals, and realtime monitoring screens — data-forward, calm at rest, with one glowing element per surface doing all the emphasis work. Built for boardroom readability at distance and for decks that alternate between narrative and dense operational data.

colors:
  bg: "#f7faf8"
  surface: "#ffffff"
  surface-sunken: "#eff4f1"
  primary: "#00aa46"
  primary-hover: "#00913b"
  neon: "#00f062"
  ink: "#050907"
  ink-card: "#17211d"
  ink-raised: "#1f2b26"
  ink-border: "#2b3831"
  text: "#131816"
  text-muted: "#5f6b64"
  text-light: "#7f8c85"
  text-inverse: "#f2f7f4"
  text-muted-inverse: "#8d9b94"
  text-light-inverse: "#5e6d66"
  border: "#e2e9e5"
  border-brand: "#00aa46"
  brand-soft: "rgba(0, 170, 70, 0.10)"
  positive: "#00913b"
  negative: "#d3352b"
  cyan: "#00e0ff"
  violet: "#8b5cff"
  amber: "#ffb020"
  magenta: "#ff2d78"

typography:
  h1:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 700
    fontSize: 114px
    lineHeight: 1.02
    letterSpacing: -0.035em
    color: "{colors.text}"
  h2:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 700
    fontSize: 72px
    lineHeight: 1.05
    letterSpacing: -0.03em
    color: "{colors.text}"
  h3:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 600
    fontSize: 42px
    lineHeight: 1.15
    letterSpacing: -0.02em
    color: "{colors.text}"
  eyebrow:
    fontFamily: "'Archivo', sans-serif"
    fontWeight: 600
    fontSize: 21px
    lineHeight: 1.1
    letterSpacing: 0.14em
    textTransform: uppercase
    color: "{colors.primary}"
  lede:
    fontFamily: "'Archivo', sans-serif"
    fontWeight: 400
    fontSize: 33px
    lineHeight: 1.4
    color: "{colors.text-muted}"
  body:
    fontFamily: "'Archivo', sans-serif"
    fontWeight: 400
    fontSize: 27px
    lineHeight: 1.45
    color: "{colors.text-muted}"
  body-sm:
    fontFamily: "'Archivo', sans-serif"
    fontWeight: 400
    fontSize: 23px
    lineHeight: 1.45
    color: "{colors.text-muted}"
  metric-hero:
    fontFamily: "'JetBrains Mono', monospace"
    fontWeight: 500
    fontSize: 84px
    lineHeight: 1
    letterSpacing: -0.03em
    fontVariantNumeric: tabular-nums
    color: "{colors.text}"
  metric-value:
    fontFamily: "'JetBrains Mono', monospace"
    fontWeight: 500
    fontSize: 69px
    lineHeight: 1
    letterSpacing: -0.03em
    fontVariantNumeric: tabular-nums
    color: "{colors.text}"
  metric-label:
    fontFamily: "'Archivo', sans-serif"
    fontWeight: 600
    fontSize: 19px
    lineHeight: 1.2
    letterSpacing: 0.14em
    textTransform: uppercase
    color: "{colors.text-muted}"
  metric-delta:
    fontFamily: "'JetBrains Mono', monospace"
    fontWeight: 400
    fontSize: 23px
    lineHeight: 1.3
    fontVariantNumeric: tabular-nums
    color: "{colors.positive}"
  section-number:
    fontFamily: "'JetBrains Mono', monospace"
    fontWeight: 500
    fontSize: 180px
    lineHeight: 1
    color: "{colors.neon}"
    textShadow: "0 0 60px rgba(0, 240, 98, 0.45)"
  step-label:
    fontFamily: "'JetBrains Mono', monospace"
    fontWeight: 500
    fontSize: 23px
    lineHeight: 1
    letterSpacing: 0.1em
    color: "{colors.neon}"
  card-index:
    fontFamily: "'JetBrains Mono', monospace"
    fontWeight: 500
    fontSize: 21px
    lineHeight: 1
    letterSpacing: 0.1em
    color: "{colors.text-light}"
  blockquote:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 600
    fontSize: 78px
    lineHeight: 1.18
    letterSpacing: -0.03em
    color: "{colors.text}"
  cite-name:
    fontFamily: "'Archivo', sans-serif"
    fontWeight: 600
    fontSize: 27px
    lineHeight: 1.2
    color: "{colors.text}"
  cite-role:
    fontFamily: "'Archivo', sans-serif"
    fontWeight: 400
    fontSize: 23px
    lineHeight: 1.3
    color: "{colors.text-muted}"
  chart-value:
    fontFamily: "'JetBrains Mono', monospace"
    fontWeight: 500
    fontSize: 30px
    lineHeight: 1
    fontVariantNumeric: tabular-nums
  chart-label:
    fontFamily: "'Archivo', sans-serif"
    fontWeight: 400
    fontSize: 24px
    lineHeight: 1.2
    color: "{colors.text-muted}"
  footer:
    fontFamily: "'Archivo', sans-serif"
    fontWeight: 400
    fontSize: 21px
    lineHeight: 1.3
    color: "{colors.text-light}"
  counter:
    fontFamily: "'JetBrains Mono', monospace"
    fontWeight: 400
    fontSize: 21px
    lineHeight: 1.3
    fontVariantNumeric: tabular-nums
    color: "{colors.text-light}"

spacing:
  pad-slide-x: 132px
  pad-slide-y: 108px
  pad-footer-bottom: 66px
  pad-card-lg: 48px
  pad-card-md: 45px
  pad-card-sm: 42px
  gap-grid-lg: 84px
  gap-grid-md: 36px
  gap-chart-bars: 42px
  gap-eyebrow-h2: 21px
  gap-h2-content: 84px
  gap-quote-cite: 72px
  logo-height-cover: 78px
  logo-height-closing: 66px
  accent-rule-width: 180px
  accent-rule-height: 3px

canvas:
  width: 1920px
  height: 1080px
  background: "{colors.bg}"
  model: fixed-stage

radii:
  pill: 999px
  card-lg: 14px
  card-md: 10px
  card-sm: 6px
  bar: "12px 12px 3px 3px"
  circle: 50%

effects:
  shadow-card: "0 1px 2px rgba(9, 16, 13, 0.06)"
  shadow-raised: "0 6px 16px rgba(9, 16, 13, 0.09), 0 2px 4px rgba(9, 16, 13, 0.05)"
  glow-brand: "0 0 20px rgba(0, 240, 98, 0.30), 0 2px 8px rgba(0, 240, 98, 0.20)"
  glow-live: "0 0 12px rgba(0, 240, 98, 0.55)"
  ambient-light: "radial-gradient(120% 90% at 12% 0%, rgba(0,240,98,0.10) 0%, rgba(0,224,255,0.06) 42%, rgba(255,255,255,0) 72%)"
  ambient-dark: "radial-gradient(120% 90% at 12% 0%, rgba(0,240,98,0.16) 0%, rgba(0,224,255,0.10) 40%, rgba(5,9,7,0) 70%)"
  grid-fine: "repeating-linear-gradient(0deg, rgba(0,240,98,0.05) 0 1px, transparent 1px 24px), repeating-linear-gradient(90deg, rgba(0,240,98,0.05) 0 1px, transparent 1px 24px)"
  ease-out: "cubic-bezier(0.16, 1, 0.3, 1)"
  ease-standard: "cubic-bezier(0.2, 0, 0.1, 1)"
  dur-fast: 140ms
  dur-base: 220ms
  dur-slow: 400ms
  dur-ambient: 18s
  stagger-step: 45ms

components:
  card-light:
    background: "{colors.surface}"
    border: "1px solid {colors.border}"
    borderRadius: 14px
    padding: 45px
    boxShadow: "{effects.shadow-card}"
    description: "Primary content card on light surfaces. White fill, hairline neutral border, soft 14px radius, near-invisible shadow. Never a colored left-border accent, never a tinted fill."
  card-focal:
    background: "{colors.surface}"
    border: "2px solid {colors.border-brand}"
    borderRadius: 14px
    padding: 48px
    boxShadow: "{effects.glow-brand}"
    description: "The one emphasized card per surface. Same white fill, but a 2px S-green border and the neon glow shadow. Exactly one per slide — a second focal card cancels the first."
  card-ink:
    background: "{colors.ink-card}"
    border: "1px solid {colors.ink-border}"
    borderRadius: 14px
    padding: 45px
    description: "Content card on dark surfaces. Ink fill, hairline ink border, no shadow — depth on dark comes from surface value, not shadow."
  ambient-field:
    background: "{effects.ambient-light}"
    animation: "drift 18s cubic-bezier(0.45,0,0.55,1) infinite alternate"
    description: "A slow drifting green-cyan radial wash filling the whole surface behind content. At most one per slide, and only on cover, quote and closing surfaces. Use {effects.ambient-dark} on ink surfaces."
  scan-grid:
    background: "{effects.grid-fine}"
    opacity: 0.5
    description: "A 24px hairline lattice at 5% neon opacity, filling the surface behind content. Reserved for dark operational and data surfaces — never on a cover or a quote."
  accent-rule:
    width: 180px
    height: 3px
    background: "{colors.neon}"
    boxShadow: "{effects.glow-live}"
    description: "A short glowing neon rule under an oversized section number. Used only on section-divider surfaces."
  live-dot:
    width: 12px
    height: 12px
    borderRadius: 50%
    background: "{colors.neon}"
    boxShadow: "{effects.glow-live}"
    description: "A glowing dot preceding a realtime-data label. Only ever used when the figures shown are genuinely live; never decorative."
  metric-card:
    background: "{colors.surface}"
    border: "1px solid {colors.border}"
    borderRadius: 14px
    padding: 42px
    description: "KPI cell: uppercase tracked label, then a large tabular-mono value, then a mono delta line. Promote the single most important cell to {components.card-focal}."
  bar-accent:
    background: "{colors.neon}"
    borderRadius: "12px 12px 3px 3px"
    boxShadow: "{effects.glow-brand}"
    description: "The highlighted bar in a chart on an ink surface. Exactly one bar per chart is neon; the rest are {components.bar-neutral}."
  bar-neutral:
    background: "{colors.ink-raised}"
    border: "1px solid {colors.ink-border}"
    borderRadius: "12px 12px 3px 3px"
    description: "Non-highlighted chart bars on ink. Grow from the baseline with transform-origin bottom, staggered 60ms apart."
  bar-accent-light:
    background: "{colors.primary}"
    borderRadius: "12px 12px 3px 3px"
    description: "The highlighted bar when the chart sits on a light surface. Heritage green, no glow — glow needs an ink ground to read."
  avatar-initials:
    width: 66px
    height: 66px
    borderRadius: 50%
    background: "{colors.brand-soft}"
    color: "{colors.primary}"
    description: "Circular initials badge beside a quote attribution. Soft green tint, green initials, weight 700."
  footer-bar:
    position: "absolute left {spacing.pad-slide-x} right {spacing.pad-slide-x} bottom {spacing.pad-footer-bottom}"
    description: "Slide footer: organisation name on the left in {typography.footer}, page counter on the right in {typography.counter}. Present on data and content slides; omitted on cover, section-divider, quote and closing surfaces."
  logo-lockup:
    description: "Raster PNG lockups only — sok-logo-full.png on light grounds, sok-logo-full-white.png on ink. Never redraw, recolor, rotate or reconstruct the S-mark, and never place a glow behind it."
---

## Frontend Slides Fixed-Stage Policy

When this design system is used by the `frontend-slides` skill, generate the final deck as a **fixed 1920×1080 stage** that scales uniformly to the browser viewport. The deck preserves a 16:9 slide canvas on every screen, including phones; it may letterbox or pillarbox, but it must not reflow slide content for mobile.

Every dimension in this document is already expressed in 1920×1080 stage pixels — there are no `vw`, `vh`, `clamp()` or `rem` values to translate. Use them literally.

Use `deck-stage.js` or an equivalent inline stage scaler for final output: render each slide at 1920×1080, scale the whole stage with one transform, and verify rendered screenshots for both text overflow and panel overlap.

## Overview

S-ryhmä Neon is a **retail-operations presentation system**. It was built for decks that alternate between narrative (what changed, who it helps) and dense operational data (availability percentages, waste, pick times, sales by chain) without the two halves looking like different decks.

Its foundational premise is **two greens with different jobs**. The heritage **S-green** (`{colors.primary}` — `#00aa46`) is the structural brand green: it works on white, it carries eyebrows, focal borders and light-surface chart bars, and it never glows. The **neon green** (`{colors.neon}` — `#00f062`) is emitted light: it only appears on ink surfaces or as a glow, and it marks exactly one thing per slide — the section number, the highlighted bar, the live-data dot, the focal card. Confusing the two is the fastest way to break the system: neon type on white is illegible, and heritage green with a glow behind it looks like a rendering error.

The system runs on **two grounds, not one**. Light surfaces (`{colors.bg}` — a near-white `#f7faf8`) carry narrative, KPI grids and quotes. Ink surfaces (`{colors.ink}` — a near-black `#050907`) carry section dividers, charts and the closing. The alternation is the deck's rhythm: roughly every third surface is ink, and an ink surface always signals either "new chapter" or "this is the data".

Type is three faces in **strictly non-overlapping roles**. **Space Grotesk** (600–700) is display only — h1, h2, h3, and the blockquote. **Archivo** (400–600) is body and chrome — ledes, paragraphs, eyebrows, labels, footers. **JetBrains Mono** (400–500, tabular figures) is every numeral without exception — metric values, deltas, section numbers, quarter labels, chart values, page counters. A percentage set in Archivo is wrong even when it is 23px in a footnote; the mono numerals are what make the deck read as operational rather than promotional.

Depth is **hairline, not shadowed**. Light cards are white with a 1px `{colors.border}` hairline and a shadow so soft it registers as a seam. Ink cards have a 1px `{colors.ink-border}` hairline and no shadow at all. The only strong depth signal in the system is the neon glow, and it is rationed to one element per surface.

**Density philosophy: generous narrative, dense data.** A narrative surface holds an eyebrow, one h2, and three to four cards or a single lede. A data surface holds four metric cells or a six-bar chart. Both breathe at 132px side padding. The system reads as credible when numbers are specific (97,4 % — not "over 97 %") and thin when they are rounded into vagueness.

**Key Characteristics:**
- Two grounds: near-white `{colors.bg}` for narrative, near-black `{colors.ink}` for dividers, charts and closing.
- Two greens: heritage `{colors.primary}` for structure, `{colors.neon}` for emission — never interchanged.
- Space Grotesk (display) + Archivo (body/chrome) + JetBrains Mono (every numeral).
- Exactly one glowing element per surface.
- Eyebrows are uppercase Archivo 600 at 0.14em tracking in heritage green.
- Cards are white (or ink) with hairline borders — never tinted fills, never colored left-border accents.
- Two atmospherics: the 18s drifting ambient field (cover, quote, closing) and the hairline scan grid (ink data surfaces). Never both on one slide.
- Motion is a reveal, not a transition: content emerges with opacity + 10px lift + blur-out, staggered 45ms.
- Logos are supplied raster PNGs; the S-mark is never redrawn.

## Colors

### Palette

- **Bg** (`{colors.bg}` — `#f7faf8`): The light ground. A near-white with a faint cool-green cast that keeps white cards visible against it. Never pure white as the ground, never gray.
- **Surface** (`{colors.surface}` — `#ffffff`): Card fill on light surfaces. Pure white, so cards read as lifted off the ground without a shadow.
- **Primary** (`{colors.primary}` — `#00aa46`): Heritage S-green. Eyebrows, focal card borders, light-surface chart bars, positive figures on light grounds, avatar initials. Passes contrast on white; use it whenever green must be *read* rather than *seen*.
- **Neon** (`{colors.neon}` — `#00f062`): Emitted light. Section numbers, accent rules, live dots, highlighted bars on ink, quarter labels, and every glow. **Only on ink grounds, never as text on white.**
- **Ink** (`{colors.ink}` — `#050907`): The dark ground. Near-black with a green undertone.
- **Ink-card / Ink-raised / Ink-border** (`#17211d` / `#1f2b26` / `#2b3831`): The three steps of dark surface value — card fill, raised element (neutral chart bars), hairline border.
- **Text** (`{colors.text}` — `#131816`): Headlines and primary content on light grounds.
- **Text-muted** (`{colors.text-muted}` — `#5f6b64`): Ledes, body paragraphs, chart labels.
- **Text-light** (`{colors.text-light}` — `#7f8c85`): Footers, page counters, card index numerals.
- **Text-inverse / muted / light** (`#f2f7f4` / `#8d9b94` / `#5e6d66`): The same three-step ladder on ink grounds.
- **Border** (`{colors.border}` — `#e2e9e5`): Hairline neutral border on light cards. Not green — green borders are reserved for focal cards.
- **Brand-soft** (`{colors.brand-soft}`): Heritage green at 10%. The only tinted fill in the system, used for the avatar-initials badge.
- **Positive / Negative** (`#00913b` / `#d3352b`): Directional change figures only, inline, always in mono. Never fills, never borders.
- **Cyan / Violet / Amber / Magenta** (`#00e0ff` / `#8b5cff` / `#ffb020` / `#ff2d78`): Data-series colors for multi-series charts only, used strictly in that order after green. Never as decoration, never as a second brand accent.

### Defaults

- **Default ground**: `{colors.bg}`. Switch to `{colors.ink}` only for section dividers, chart surfaces and the closing.
- **Default headline color**: `{colors.text}` on light, `{colors.text-inverse}` on ink. Headlines are never green.
- **Default body color**: `{colors.text-muted}` on light, `{colors.text-muted-inverse}` on ink.
- **Default eyebrow color**: `{colors.primary}` on light, `{colors.neon}` on ink. Always uppercase, always 0.14em tracking.
- **Default card**: `{components.card-light}` on light, `{components.card-ink}` on ink.
- **Default numeral color**: `{colors.text}` / `{colors.text-inverse}` — numerals get their emphasis from size and the mono face, not from color. Color a numeral only when it is a directional change (positive/negative) or a section number (neon).
- **Default chart bar**: `{components.bar-neutral}`, with exactly one `{components.bar-accent}`.

There is **no second brand accent**. Cyan, violet, amber and magenta exist for multi-series charts and nowhere else. Categorical differentiation in every other context is done by position, size or label.

## Typography

### Font Family Stack

**Space Grotesk** (Google Fonts, 600–700) — display only. h1 (114px cover/closing), h2 (72px section headline), h3 (42px card title), blockquote (78px). Its slightly technical geometry is what keeps the deck from reading as a generic corporate template.

**Archivo** (Google Fonts, 400–600) — body and chrome. Ledes (33px), body (27px), small body (23px), eyebrows (21px uppercase), metric labels (19px uppercase), footers (21px). High x-height, holds up at distance.

**JetBrains Mono** (Google Fonts, 400–500) — every numeral, always with `font-variant-numeric: tabular-nums`. Metric heroes (84px), metric values (69px), section numbers (180px), deltas (23px), chart values (30px), quarter labels (23px), page counters (21px).

The boundaries are hard. Space Grotesk in a paragraph reads as a landing page; Archivo on a metric value loses the tabular alignment that makes columns of figures scan; a numeral in Archivo anywhere breaks the operational register the whole system is built on.

### Typography Scale

| Token | Size | Family | Weight | Use |
|---|---|---|---|---|
| `{typography.h1}` | 114px | Space Grotesk | 700 | Cover and closing title |
| `{typography.h2}` | 72px | Space Grotesk | 700 | Section headline on every content slide |
| `{typography.h3}` | 42px | Space Grotesk | 600 | Card title inside a content card |
| `{typography.eyebrow}` | 21px | Archivo | 600 | Uppercase 0.14em eyebrow above the h2 |
| `{typography.lede}` | 33px | Archivo | 400 | Cover subtitle / opening paragraph |
| `{typography.body}` | 27px | Archivo | 400 | Card body and standard paragraph |
| `{typography.body-sm}` | 23px | Archivo | 400 | Secondary body, cite role line |
| `{typography.metric-hero}` | 84px | JetBrains Mono | 500 | Single dominant figure in a three-up |
| `{typography.metric-value}` | 69px | JetBrains Mono | 500 | KPI value in a four-up grid |
| `{typography.metric-label}` | 19px | Archivo | 600 | Uppercase 0.14em KPI label |
| `{typography.metric-delta}` | 23px | JetBrains Mono | 400 | Change line under a KPI value |
| `{typography.section-number}` | 180px | JetBrains Mono | 500 | Oversized neon number on a section divider |
| `{typography.step-label}` | 23px | JetBrains Mono | 500 | Quarter / phase label on a roadmap |
| `{typography.card-index}` | 21px | JetBrains Mono | 500 | 01 / 02 / 03 index inside a content card |
| `{typography.blockquote}` | 78px | Space Grotesk | 600 | Quote body |
| `{typography.cite-name}` | 27px | Archivo | 600 | Quote attribution name |
| `{typography.cite-role}` | 23px | Archivo | 400 | Quote attribution role and location |
| `{typography.chart-value}` | 30px | JetBrains Mono | 500 | Value above a chart bar |
| `{typography.chart-label}` | 24px | Archivo | 400 | Category label under a chart bar |
| `{typography.footer}` | 21px | Archivo | 400 | Organisation name in the slide footer |
| `{typography.counter}` | 21px | JetBrains Mono | 400 | Page counter in the slide footer |

### Defaults

- **Cover / closing title**: `{typography.h1}`, max-width 1350px. Never more than four lines.
- **Section headline**: `{typography.h2}` — every content slide has exactly one.
- **Card title**: `{typography.h3}`.
- **Eyebrow**: `{typography.eyebrow}` — 21px Archivo 600, uppercase, 0.14em, green. Every content slide opens with one.
- **Body**: `{typography.body}` at 27px. Below 23px, text stops being readable from the back of a room; the system has no smaller body size.
- **Any numeral**: the mono ladder. Pick by role, not by taste: 84px for a dominant three-up figure, 69px in a four-up KPI grid, 30px on a chart bar, 23px for deltas and labels.

### Signature Treatments

Non-optional whenever the element type appears:

- **Every eyebrow is uppercase Archivo 600 at 0.14em tracking**, in `{colors.primary}` on light and `{colors.neon}` on ink. The wide tracking is the signal; without it the eyebrow reads as a stray label.
- **Every headline carries negative tracking** — `-0.035em` at h1, `-0.03em` at h2, `-0.02em` at h3. Untracked Space Grotesk display looks unset.
- **Every headline is text-colored, never green.** Green is the accent, not the voice.
- **Every numeral is JetBrains Mono with tabular figures.** No exceptions, at any size.
- **Every metric label is uppercase Archivo 600 at 0.14em, muted** — it sits *above* its value, never below.
- **Every slide except cover, divider, quote and closing carries the footer bar**: organisation left, page counter right.
- **Exactly one glowing element per slide.** Count them before shipping a surface.

### Typography Principles

The voice contrast is **near-black display ↔ green tracked eyebrows ↔ muted gray body ↔ mono numerals**. Italic and underline are never used. Emphasis is available in three moves only: change weight within the display ladder, shift color from muted to text, or set the thing in mono.

Numerals are the system's second voice. When a slide has a number worth saying out loud, that number should be the largest element on the surface and it should be exact — `97,4 %`, `-14 min`, `4,21 M€`. Finnish decks use a space as the thousands separator and a comma as the decimal (`184 320 €`); keep the source locale's convention rather than converting.

## Layout

### Canvas System

Fixed 1920×1080 stage. Slide padding is uniform: **132px left and right, 108px top and bottom**, with the footer bar pinned at **66px from the bottom** inside that padding. Content columns therefore run 1656px wide.

Slides are absolutely positioned within the stage and cross-fade on change over `{effects.dur-base}`. Nothing slides horizontally — the deck's motion vocabulary is emergence, not travel.

### Padding and Gap Scale

| Token | Value | Use |
|---|---|---|
| `{spacing.pad-slide-x}` | 132px | Slide horizontal padding |
| `{spacing.pad-slide-y}` | 108px | Slide vertical padding |
| `{spacing.pad-footer-bottom}` | 66px | Footer bar distance from the bottom edge |
| `{spacing.pad-card-lg}` | 48px | Focal card and three-up card padding |
| `{spacing.pad-card-md}` | 45px | Standard content card padding |
| `{spacing.pad-card-sm}` | 42px | KPI cell padding in a four-up grid |
| `{spacing.gap-grid-lg}` | 84px | Gap between roadmap columns |
| `{spacing.gap-grid-md}` | 36px | Gap between cards in a three- or four-up grid |
| `{spacing.gap-chart-bars}` | 42px | Gap between chart bars |
| `{spacing.gap-eyebrow-h2}` | 21px | Eyebrow to headline |
| `{spacing.gap-h2-content}` | 84px | Headline to the content region |
| `{spacing.gap-quote-cite}` | 72px | Quote body to attribution |

### Surface Types

Seven surface types cover the system. Each has a fixed structure; vary the content, not the skeleton.

**Cover** — light ground with the ambient field. Logo lockup top-left (78px tall), then a large vertical gap, then eyebrow → h1 (max-width 1350px) → lede (max-width 960px). Footer carries the organisation and the date. No slide-header, no page counter.

**Content (three-up)** — eyebrow → h2 → a row of three `{components.card-light}`, each with a mono index (`01`), an h3 title and body. Promote the first card to `{components.card-focal}` when one option is the recommendation.

**Data (three-up hero)** — eyebrow → h2 → three cards, each a `{typography.metric-hero}` figure over a 27px descriptive line. Use when three numbers carry the argument.

**KPI grid (four-up)** — eyebrow → h2 → four `{components.metric-card}` cells, each label → value → delta. Exactly one cell is `{components.card-focal}`. Footer present.

**Section divider** — ink ground with the scan grid. Oversized neon `{typography.section-number}`, then `{components.accent-rule}`, then h1 in inverse text, then a muted inverse lede. No footer, no page counter.

**Chart (ink)** — ink ground with the scan grid. Live-dot + neon eyebrow → h2 in inverse text → a row of bars, each: mono value above, bar, category label below. Exactly one bar is `{components.bar-accent}`. Bars grow from the baseline with `transform-origin: bottom`, staggered 60ms.

**Quote** — light ground with the ambient field. `{typography.blockquote}` at max-width 1410px using proper curly quotation marks, then 72px gap, then `{components.avatar-initials}` + name + role. No eyebrow, no footer.

**Closing** — ink ground with the ambient field (dark variant). White logo lockup (66px), then h1, then a row of three roadmap columns: neon `{typography.step-label}` over a 30px inverse line, max-width 345px each, 84px apart.

### Persistent Chrome

The footer bar is the only persistent chrome: organisation name left, page counter right, both at 21px, pinned 66px from the bottom between the slide's side padding. It appears on content, data and KPI surfaces and is deliberately absent from cover, divider, quote and closing — those surfaces are meant to feel like full stops.

There are no nav arrows, no progress bar and no keyboard hint baked into the slides; navigation chrome belongs to the stage, not the design.

## Depth and Elevation

### Hairline Cards (Primary Depth Mechanism)

Light cards are pure white on a near-white ground with a 1px `{colors.border}` hairline and `{effects.shadow-card}` — a shadow at 6% opacity that functions as a seam rather than a lift. Ink cards use a 1px `{colors.ink-border}` hairline and no shadow whatsoever; on dark grounds, depth comes from surface value (`{colors.ink}` → `{colors.ink-card}` → `{colors.ink-raised}`).

### Glow as the Only Strong Elevation

`{effects.glow-brand}` and `{effects.glow-live}` are the system's only assertive depth signal, and they are rationed: **one glowing element per surface**. That element is whichever of these the slide is actually about — the focal card, the highlighted bar, the section rule, the live-data dot. Two glows on one surface makes both read as decoration.

Glow requires an ink ground or a green element to attach to. A glow behind a white card on a white ground disappears; a glow behind the logo is forbidden outright.

### No Tinted Fills

Unlike tint-based systems, cards here are never filled with a translucent brand color. The one exception is `{components.avatar-initials}` at 10% green. Tinting a card to signal importance is the wrong move — promote it to `{components.card-focal}` instead.

### Atmospherics

Two, and never together on one slide:
- **Ambient field** — an 18s drifting green-cyan radial wash on cover, quote and closing surfaces. It reads as light in the room, not as a gradient background.
- **Scan grid** — a 24px hairline lattice at 5% neon opacity on ink data and divider surfaces. It reads as a monitoring screen.

## Shapes and Treatment

### Border Radius

- **`{radii.card-lg}` = 14px** — all content, metric and ink cards.
- **`{radii.card-md}` = 10px** — small inline blocks.
- **`{radii.card-sm}` = 6px** — chips and tight chrome.
- **`{radii.bar}` = 12px 12px 3px 3px** — chart bars: rounded at the top, nearly square where they meet the baseline.
- **`{radii.pill}` = 999px** — chips and tags.
- **`{radii.circle}` = 50%** — avatars, live dots.

Radii are tighter than a consumer-retail system on purpose: this is operational software rendered at presentation scale, and 14px cards read as precise where 24px would read as friendly.

### Border Weights

- **1px `{colors.border}`** (light) / **1px `{colors.ink-border}`** (ink) — the universal hairline.
- **2px `{colors.border-brand}`** — focal cards only.
- **3px `{colors.neon}`** — the section-divider accent rule only.

Borders are opaque, not translucent. The system's quietness comes from the border being nearly the same value as the ground, not from lowering its opacity.

### Decorative Element Types

**Card, light** (`{components.card-light}`) — white, hairline, 14px, 45px padding. The workhorse.

**Card, focal** (`{components.card-focal}`) — white, 2px green border, neon glow. One per surface.

**Card, ink** (`{components.card-ink}`) — ink fill, hairline ink border, no shadow.

**Section number** (`{typography.section-number}`) — a 180px mono numeral in neon with a 60px green text-shadow. The single largest element in the deck.

**Accent rule** (`{components.accent-rule}`) — 180×3px glowing neon bar, sitting between the section number and its headline.

**Live dot** (`{components.live-dot}`) — a 12px glowing neon circle preceding a realtime label. Only when the data is genuinely live.

**Chart bars** (`{components.bar-accent}` / `{components.bar-neutral}`) — one neon, the rest ink-raised. Value above in mono, label below in Archivo.

**Avatar initials** (`{components.avatar-initials}`) — 66px circle, 10% green fill, green initials at weight 700.

**Ambient field** (`{components.ambient-field}`) — the drifting wash. Cover, quote, closing.

**Scan grid** (`{components.scan-grid}`) — the hairline lattice. Ink data and divider surfaces.

**Logo lockup** (`{components.logo-lockup}`) — supplied PNGs, green on light and white on ink, at 78px (cover) or 66px (closing).

## Do's and Don'ts

### Do

- Alternate grounds deliberately: light for narrative, ink for dividers, charts and the closing. Roughly every third surface should be ink.
- Keep the two greens in their lanes — heritage `{colors.primary}` for anything that must be read on white, neon `{colors.neon}` for anything that emits on ink.
- Set every numeral in JetBrains Mono with tabular figures, at every size.
- Open every content slide with the tracked uppercase eyebrow, then exactly one h2.
- Ration the glow to one element per surface, and make it the thing the slide is about.
- Use exact figures with the source locale's number formatting (`97,4 %`, `184 320 €`, `4,21 M€`).
- Give charts one neon bar and let the rest sit in `{colors.ink-raised}`.
- Let content emerge: opacity 0→1, 10px lift, 6px blur out, 400ms `{effects.ease-out}`, staggered 45ms across a list.
- Use the supplied PNG logo lockups, green on light and white on ink.
- Keep atmospherics apart — ambient field on cover/quote/closing, scan grid on ink data surfaces, never both.

### Don't

- Don't put neon green type on a light ground. It fails contrast and reads as a glitch.
- Don't glow more than one element per slide, and never glow the logo.
- Don't set a headline in green. Headlines are near-black on light, near-white on ink.
- Don't set any numeral in Archivo or Space Grotesk.
- Don't fill a card with a tinted brand color to signal importance — promote it to `{components.card-focal}`.
- Don't add a colored left-border accent to a card. That pattern does not exist here.
- Don't introduce a third accent hue. Cyan, violet, amber and magenta belong to multi-series charts only.
- Don't put the ambient field and the scan grid on the same surface.
- Don't round numbers into vagueness. "Nearly 98 %" is weaker than `97,4 %` in this system.
- Don't add nav arrows, progress bars or keyboard hints to the slide surfaces — that chrome belongs to the stage.
- Don't redraw, recolor or reconstruct the S-mark.

## Motion

Motion is functional and layered in three speeds.

- **Reveal** (`{effects.dur-slow}` 400ms, `{effects.ease-out}`): content emerges — opacity 0→1, `translateY(10px)`→0, `blur(6px)`→0. Lists stagger at `{effects.stagger-step}` 45ms per item.
- **Chart growth** (400ms, `{effects.ease-out}`): bars scale from `transform-origin: bottom`, staggered 60ms; sparkline strokes draw themselves via dash-offset.
- **Slide change** (`{effects.dur-base}` 220ms): cross-fade only, no horizontal travel.
- **Ambient** (`{effects.dur-ambient}` 18s, alternating): the background field drifts and scales slightly. Live dots pulse on a 2.4s cycle.

No bounces, no springs, no parallax, no letter-by-letter typing. Everything respects `prefers-reduced-motion`.

## Responsive Behavior

The system is a fixed 1920×1080 stage scaled with a single transform. There is no responsive behavior by design: no `clamp()`, no media queries, no reflow. On narrow viewports the stage letterboxes.

All dimensions in this document are literal stage pixels. If a surface overflows, cut content or drop to the next size in the ladder — do not scale a slide's contents independently of the stage.

### Print Behavior

Each slide prints as one landscape page at stage size. Freeze ambient and reveal animations to their end state before printing; the scan grid, glow and ambient field all render in print. Ink surfaces print as intended dark pages — check the target printer before committing to a deck that is one-third ink.

### Presenter Behavior

Navigation, thumbnails, speaker notes and PDF export are provided by `deck-stage.js`; slides carry a `data-label` and `data-speaker-notes` attribute each and no navigation markup of their own.

## CJK & International Content

The deck is Finnish-first, and the system is built for Finnish, Swedish and English. For CJK content, swap the Latin stack and apply the universal adjustments below.

### Recommended Chinese Pairing

| Role | Latin (default) | Chinese counterpart |
|---|---|---|
| h1 / h2 / h3 / blockquote | Space Grotesk 600–700 (negative tracking) | 思源黑体 Noto Sans SC 700 (0 tracking) |
| Body / lede / eyebrow / labels | Archivo 400–600 (uppercase on eyebrows) | 思源黑体 Noto Sans SC 400–500 (no transform) |
| Every numeral | JetBrains Mono 400–500 tabular | JetBrains Mono, unchanged |

### Loading

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```

### Universal CJK Adjustments

- **Line-height**: increase ~15–25%. Body 1.7–1.8 (up from 1.45), display 1.15–1.25 (up from 1.02–1.05).
- **Letter-spacing**: 0 on every CJK run. The −0.03em display tracking overlaps CJK strokes; the +0.14em eyebrow tracking reads as gappy on square glyphs.
- **Text transform**: no `uppercase` on CJK — the eyebrow and metric-label tokens must drop it.
- **Punctuation**: full-width Chinese punctuation （，。：；！？「」）.
- **No trailing 。 on display headlines.**
- **盘古之白**: an ASCII space between every CJK character and adjacent Latin character or digit — `2026 Q2 门店运营`, not `2026Q2门店运营`.
- **Keep numerals in JetBrains Mono.** Operational figures stay Latin Arabic digits by convention, and the mono face is the system's identity — do not let a CJK face pick them up.

### Aesthetic Notes for This System

The identity here is grounds, greens and mono numerals — none of it depends on Latin type, so it transfers cleanly. The one real loss is the eyebrow: uppercase + 0.14em tracking is its whole signal, and CJK drops both. Compensate by pairing every CJK eyebrow with `{components.accent-rule}` (shortened to 90px on light surfaces, in heritage green) so the chrome still reads as chrome.

### Known CJK Gap

- **No CDN Chinese face carries Space Grotesk's technical geometry.** 思源黑体 reads as more institutional; the deck will feel slightly more official and less operational-modern.
- **The eyebrow signal weakens** and needs the accent-rule compensation described above.
- **Long CJK headlines break the 114px h1 budget faster than Latin.** Drop the cover title to 96px for CJK rather than letting it run to five lines.

## Iteration Guide

1. Decide the ground first. Narrative → light. Chapter break, chart or closing → ink. If more than half the deck is ink, the alternation has stopped meaning anything.
2. Open every content surface with the tracked uppercase eyebrow, then exactly one h2 at 72px.
3. Choose the surface type from the seven in **Layout** before writing content into it, and keep its skeleton.
4. Set every numeral in JetBrains Mono, sized by role from the mono ladder.
5. Pick the one thing the slide is about and give it the glow — focal card, accent bar, section rule or live dot. Nothing else glows.
6. Cards are white (or ink) with hairlines. If a card needs more weight, promote it to `{components.card-focal}`; never tint it.
7. Charts get one neon bar; everything else is `{colors.ink-raised}`.
8. Add the footer bar to content, data and KPI surfaces. Leave cover, divider, quote and closing bare.
9. Reveal content rather than transitioning it: opacity + 10px lift + blur-out, 45ms stagger.
10. If a surface feels sparse, add a real number or a real quote — not a second accent color, a heavier border or a decorative shape.

## Known Gaps

- **Fonts load from Google Fonts** with no self-hosted fallback. Where Google Fonts are blocked, the deck falls back to system sans and loses the mono numeral identity entirely — the most damaging failure mode in this system.
- **The licensed S-ryhmä brand typeface was never supplied.** Space Grotesk, Archivo and JetBrains Mono are flagged substitutions; if the real family arrives, swap the three `fontFamily` stacks and nothing else changes.
- **No icon set ships with this pack.** Lucide (2px stroke outline) is the substitution used by the parent design system; load it from CDN if a surface needs icons.
- **The ink surfaces are expensive to print** and can look muddy on office laser printers. For print-first decks, consider limiting ink to the section dividers.
- **The one-glow-per-surface rule is not enforceable in code** — it needs a human check per slide.
- **Multi-series charts are weakly supported.** The `{colors.cyan}`/`{colors.violet}`/`{colors.amber}`/`{colors.magenta}` sequence exists but has not been tuned for accessibility against ink at small sizes.
- **The ambient field is a CSS animation on a pseudo-element**; capturing it in a static screenshot freezes it at an arbitrary frame, so exported PNGs of cover and quote surfaces vary slightly between runs.
- **The 180px section number can collide with a long headline** on section dividers when the headline runs past three lines. Shorten the headline; the number does not scale.
- **No table component is defined.** Operational decks often want one; until it exists, use a KPI grid or a chart instead of improvising a table.
- **Logos are raster PNGs**, not vectors. At 78px on a 1920 stage they are adequate; above ~200px they soften.
