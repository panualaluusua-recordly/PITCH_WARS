# Changelog

## 2026.2 — Recordly house brand wired to the measured design system

The `recordly` template is now backed end-to-end by the design system measured
from the production file `2026_template.pptx` (37 slides, 51 layouts, updated
28.5.2026), and every path the skill tells a generator to read now resolves.

### Fixed

- **`SKILL.md` Phase 3 pointed at five files that don't exist.** The Recordly
  generation instruction referenced `reference/voice.md`,
  `reference/layouts.md`, `../../../reference/tokens.md`,
  `../../../reference/layouts.md` and `.claude/assets/recordly-wordmark.svg`.
  A deck generated down that path hit dead ends and improvised. It now points at
  `reference/2026-slide-system.md`, `reference/2026-tokens.json`,
  `reference/recordly-base.css` and `assets/`.
- **Stale Marp-era rule.** "One-yellow-moment-per-slide" (Workman Yellow
  `#DEFF16`, the older Marp theme) replaced with the one-lime-carrier rule
  (`#E3FF87`), which is what the 2026 template actually does.
- **File-map table** row for Recordly replaced with the two directories that
  exist.
- **Chevron hairline.** A `border` on a `clip-path` element is clipped away,
  leaving a diagonal artifact. The stroke is now the parent's background with
  the fill as an inset pseudo-element clipped to the same shape.
- **Icon-row component was documented wrong.** `design.md` said "monoline
  single-weight paper icons … never filled or duotone". The source's own icon
  row (layout 45) uses five *solid*, grain-filled icons. The set has two
  families and the template uses both; that is now documented.
- **`.rc-pill` had no default width**, so a narrow pill silently rendered as a
  lozenge. Set to the source's 1386px.

### Added

- **`reference/recordly-base.css`** — the tokens as working 1920×1080 stage CSS:
  palette, type scale, grain overlay, furniture layer, and all components as
  classes. Copy in after `viewport-base.css` instead of re-deriving values. The
  three most-often-missed details (0.70 heading line-height, the film grain,
  `#000000` card interiors) are handled by class rather than by memory.
- **`assets/logo/`** — six wordmark variants extracted from the source file.
  `recordly-wordmark-knockout.png` is the default on dark.
- **`assets/icons/`** — 40 icons named by subject (`rocket`, `brain-network`,
  `gauge`, `target`…) plus a labelled `contact-sheet.png`, so an icon is chosen
  by looking rather than guessing from a filename.
- **`assets/README.md`** — manifest, clear-space rule, and the two icon
  families.
- Skill and plugin descriptions now name the Recordly house brand so it is
  discoverable as a trigger.

### Notes

- `reference/2026-slide-system.md` and `reference/2026-tokens.json` are
  canonical. `design.md` is their ×2.667 (type) / ×192 per inch (geometry)
  translation onto the stage; where they disagree, the references win.
- Photography remains the one external asset — the source's 86 staff images stay
  in the `.pptx`. Use a real greyscale asset or a named `.rc-ph` placeholder.
- The source template's seven internal inconsistencies (two left margins, a
  drifting eyebrow, a Black/ExtraBold split, stray `#E46962` and Manrope, auto
  generated layout names, Arial theme fonts) are resolved here in favour of
  dominant usage and listed in `reference/2026-slide-system.md`.
