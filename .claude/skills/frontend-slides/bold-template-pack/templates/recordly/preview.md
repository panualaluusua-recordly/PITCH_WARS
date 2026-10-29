# Recordly Preview Card

Use this small file for title-slide previews only. For final deck generation, read the full design doc listed below.

## Files

- Full design doc: `bold-template-pack/templates/recordly/design.md`
- Preview card: `bold-template-pack/templates/recordly/preview.md`

## Selection Metadata

- Slug: `recordly`
- Tagline: Recordly's own house brand — Signal Lime as a single carrier on a film-grained ink ground, lime Montserrat Black headings at 0.70 line-height, square-cornered hairline structure.
- Mood: confident, precise, dark-mode-first, senior, plain-spoken
- Tone: data-native, editorial-minimal, a little cocky, never corporate-mystical
- Formality: medium-high
- Density: flexible (supports both low-density/speaker-led and high-density/reading-first — see `design.md` Content Density guidance in the parent skill)
- Scheme: dark (default); light and full-lime variants exist for rare emphasis/reference surfaces
- Best for: **This is the default house style for this kit.** Use it for any Recordly-branded deck — internal progress reviews, customer pitches, architecture walkthroughs, workshops — unless the user explicitly asks for a different aesthetic or an unbranded/generic look.
- Avoid for: Decks the user explicitly wants unbranded, or where they've asked for a specific non-Recordly aesthetic (e.g. a named competitor/brand pastiche, a purely experimental wildcard).

## Visual Snapshot

Film-grained ink (`#1B1B1B`) page, Montserrat Black 900 headline in Signal Lime (`#E3FF87`) at **0.70 line-height** across its own wrapped lines, with an off-white (`#EFEFEF`) Montserrat Light 300 lead line beneath it, one tier smaller. The heading is one colour — never split across a lime line and an off-white line. Greyscale photography only. No gradients, no shadows, square corners throughout. Uniform 96px margins, with the bottom band below y 979px left clear for the fixed furniture: a lime tab flush to the top-right edge, the wordmark bottom-left, and `THE BUSINESS DATA COMPANY` tracked out bottom-right.

This is Recordly's actual production brand, not an inspiration-board pastiche — every value is measured from the organization's own 2026 slide template (`2026_template.pptx`, 37 slides / 51 layouts), not inferred.

## Preview Ingredients

- Palette: ink #1B1B1B (with film grain); well #000000; lime #E3FF87; paper #EFEFEF; grey ramp #434343 / #666666 / #999999 / #B7B7B7
- Typography: See full design doc after selection.
- Signature move: Exactly one lime carrier per slide — though in this system a carrier may be a large fill (header band, pill, table header).
- Signature move: Montserrat Black 900 headings at 0.70 line-height — the tight heading block is the whole identity.
- Signature move: Lime Black heading + off-white Light lead line — hierarchy by size and weight drop, not by recolouring part of the heading.
- Signature move: Square corners and 2px hairlines everywhere; pill rows are the one rounded shape. Photography always greyscale.
- Signature move: ALL-CAPS eyebrows, chip labels and CTAs; no emoji; nothing below the y 979px furniture floor.

## Preview Rules

- Build exactly one title slide at 1920x1080 inside the fixed-stage model.
- Preserve the palette, type roles, 0.70 heading line-height, one-lime-carrier discipline, and voice rules (ALL-CAPS eyebrow, no emoji) described above.
- Include the film-grain overlay and the three furniture marks (lime tab, wordmark, tagline) — a preview without them doesn't read as Recordly.
- Use the user's real title/subtitle/context; do not copy demo slide content.
- The rendered preview must look like a real first slide, not a template-selection card.
- Never place internal workflow text on the slide: no `preview`, `generated from`, `preview.md`, `template`, `preset`, `style option`, `Option A/B/C`, file names, paths, or source-doc labels.
- Never place the template name or slug on the slide itself; mention it only in the chat message (call it "Recordly" / "the Recordly house style" when talking to the user).
- Never place user requirement notes such as desired vibe, audience, or internal-use labels on the slide unless the user explicitly wants those exact words in the deck.
- Use only real deck content for visible chrome: deck title, real section title, date, author, company, page number, or genuine content phrases from the user material.
- Never invent a figure, customer name, or quote for the preview — use a bracketed `[figure]` placeholder and flag it if the real number isn't known yet.
- Do not read `template.html` for preview generation — this template has no `template.html`; it is sourced from `design.md` and, for source-unit values, `reference/2026-slide-system.md` and `reference/2026-tokens.json`.
- Do not read other templates' `design.md` files.
- After the user picks this template for the full deck, read the full design doc before generating final slides.
