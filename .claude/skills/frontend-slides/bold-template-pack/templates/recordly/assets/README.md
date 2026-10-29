# Recordly brand assets

Extracted from the production template `2026_template.pptx` (logo variants from
layouts 50/51, icon set from layout 42). These are the real artwork — do not
redraw the wordmark by setting Montserrat, and do not draw stand-in icons.

**Embed inline.** A generated deck must stay a single self-contained HTML file,
so convert whatever you use to a `data:` URI (or inline `<svg>`) rather than
referencing these paths.

## Logo — `logo/`

| File | Composition | Use |
|---|---|---|
| `recordly-wordmark-knockout.png` | Paper letters, lime `Я`, transparent | Dark backgrounds — **the default** |
| `recordly-wordmark-positive.png` | Ink letters, grey `Я`, transparent | Light backgrounds |
| `recordly-wordmark-inkbox.png` | Ink block, paper letters, lime `Я` | Over photography or busy fields |
| `recordly-wordmark-limebox.png` | Lime block, knockout letters | Emphasis, merchandise |
| `recordly-rdly-tab.png` | Short `ЯDLY` lockup in an ink box | Corner mark, small sizes |
| `recordly-mark.png` | Single `Я` glyph in an ink box | Avatar, 1:1 crops |

The wordmark is **ЯECOЯDLY** — first letter reversed, and the `R` inside `-RDLY`
picked out in lime. Clear space is one wordmark height on all sides. Never
recolour the lime `Я`.

Footer furniture uses the **knockout** variant at 138 × 13 px on the stage. Cover
and closer slides use a larger lockup instead of the small footer wordmark.

## Icons — `icons/`

40 icons, named by what they depict. **View `icons/contact-sheet.png`** to pick
one — it is a labelled grid of the whole set, so you never have to guess from a
filename.

Two families ship together, and the source template uses both:

- **Outline** — single-weight monoline: `rocket`, `brain-network`,
  `plug-connect`, `banknotes`, `process-list`, `scale-expand`, and most others.
- **Solid** — filled with a grain texture matching the page ground:
  `eye`, `people-group`, `gauge`, `target`, `diamond`.

The prebuilt icon-row layout (source L45) uses the five solid ones. The pill-row
layout uses outline icons inside the ink disc. Don't mix families within a
single row — pick one and stay in it.

Full inventory: `banknotes`, `brain-network`, `brick-wall`, `building`,
`camera`, `dashboard`, `diamond`, `diamond-outline`, `eye`, `factory-launch`,
`gauge`, `hand-magic`, `hands-sphere`, `head-analytics`, `head-question`,
`idea-gears`, `idea-structure`, `network-people`, `org-chart`, `people-group`,
`people-three`, `person-flag`, `person-suit`, `person-value`, `pipeline-gear`,
`plug-connect`, `presenter-chart`, `process-list`, `recycle`, `rocket`,
`scale-expand`, `smart-idea`, `strategy-path`, `system-monitor`, `table-grid`,
`target`, `team-group`, `team-idea`, `tools`, `trophy`.

If the deck needs an icon that isn't here, match the outline family's stroke
weight and box (115 px on the stage) rather than importing a third style.

## Photography

None ships here — the source template's 86 images are staff photography and stay
in the `.pptx`. Every one is greyscale (measured saturation 0.00–0.02). Use a
real greyscale asset, or a named `.rc-ph` placeholder that says exactly what
belongs there. Never generate a stand-in image.
