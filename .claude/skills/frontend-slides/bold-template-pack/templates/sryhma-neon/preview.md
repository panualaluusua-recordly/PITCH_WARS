# S-ryhmä Neon Preview Card

Use this small file for title-slide previews only. For final deck generation, read the full design doc listed below.

## Files

- Full design doc: `template-pack/templates/sryhma-neon/design.md`
- Preview card: `template-pack/templates/sryhma-neon/preview.md`
- Logo assets: `template-pack/templates/sryhma-neon/assets/`

## Selection Metadata

- Slug: `sryhma-neon`
- Tagline: Near-white operations canvas with heritage S-green structure and neon-green emission on near-black ink.
- Mood: operational, precise, modern, quietly technical
- Tone: factual, calm, data-forward, unhyped
- Formality: medium-high
- Density: medium-high
- Scheme: light with recurring dark surfaces
- Best for: Retail and store-operations reviews, supply-chain and inventory updates, realtime dashboard walkthroughs, rollout and pilot readouts, internal product reviews for operational software, cooperative and chain-steering briefings. Strong whenever exact numbers carry the argument.
- Avoid for: Consumer marketing, campaign and brand launches, anything warm, playful or appetite-led — the mono numerals and ink surfaces will read as a monitoring screen rather than an invitation.

## Visual Snapshot

A Finnish cooperative-retail operations system built on two greens — the heritage S-green (#00aa46) that carries structure on light surfaces, and a neon sibling (#00f062) that behaves like emitted light on near-black ink. Display type runs Space Grotesk; Archivo handles body and chrome; every numeral is JetBrains Mono with tabular figures. Light slides are white cards on a near-white ground with hairline borders; dark slides are ink surfaces carrying a hairline scan grid and neon glow.

The deck's rhythm is the alternation of grounds: narrative and KPI surfaces sit on near-white, while section dividers, charts and the closing drop to ink. Depth is hairline rather than shadowed, and the neon glow is rationed to exactly one element per surface — the focal card, the highlighted bar, the section rule, or the live-data dot. The aesthetic borrows from retail operations dashboards, warehouse floor terminals and realtime monitoring screens: data-forward, calm at rest, and precise about numbers.

## Preview Ingredients

- Palette: bg #F7FAF8; surface #FFFFFF; primary #00AA46; neon #00F062; ink #050907; ink-card #17211D; text #131816; text-muted #5F6B64; positive #00913B; negative #D3352B
- Typography: See full design doc after selection.
- Signature move: Two greens with different jobs — heritage #00AA46 reads on white, neon #00F062 only emits on ink.
- Signature move: Every numeral is JetBrains Mono with tabular figures, at every size.
- Signature move: Exactly one glowing element per surface.
- Signature move: Uppercase Archivo eyebrows at 0.14em tracking in green, above a single 72px Space Grotesk headline.
- Signature move: Cards are white or ink with hairline borders — never tinted fills, never colored left-border accents.
- Signature move: Two atmospherics that never co-occur — an 18s drifting ambient wash on cover/quote/closing, a hairline scan grid on ink data surfaces.

## International / CJK Preview Note

- If the preview uses Chinese or other CJK text, keep CJK letter-spacing at 0, loosen line-height, and avoid uppercase transforms on CJK runs.
- Keep numerals in JetBrains Mono even in CJK builds — the mono figures are the system's identity.
- Use the full `design.md` CJK section after selection for exact font pairings and script-specific adjustments.

## Preview Rules

- Build exactly one title slide at 1920x1080 inside the fixed-stage model.
- The title surface is the light ground with the ambient field, the logo lockup top-left, then eyebrow → h1 → lede.
- Preserve the palette, type roles, surface rhythm, and decorative vocabulary described above.
- Use the user's real title/subtitle/context; do not copy demo slide content.
- The rendered preview must look like a real first slide, not a template-selection card.
- Never place internal workflow text on the slide: no `preview`, `generated from`, `preview.md`, `template`, `preset`, `style option`, `Option A/B/C`, file names, paths, or source-doc labels.
- Never place the template name or slug on the slide itself; mention it only in the chat message.
- Never place user requirement notes such as desired vibe, audience, or internal-use labels on the slide unless the user explicitly wants those exact words in the deck.
- Use only real deck content for visible chrome: deck title, real section title, date, author, company, page number, or genuine content phrases from the user material.
- Only use the SOK logo lockups when the deck genuinely belongs to SOK or S-ryhmä; otherwise leave the logo slot empty.
- Do not read `template.html` for preview generation.
- Do not read other templates' `design.md` files.
- After the user picks this template for the full deck, read the full design doc before generating final slides.
