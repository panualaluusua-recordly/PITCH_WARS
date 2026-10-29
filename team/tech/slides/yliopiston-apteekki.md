# Tech slides: yliopiston-apteekki (rationale)

Spec: `team/tech/slides/yliopiston-apteekki.json` (deck.py format; preview `work/tech/yliopiston-apteekki-preview.pdf`).
Used in deck `team/decks/yliopiston-apteekki/...-v4.md` as s3 (architecture) and s5 (gates and risks).

Inputs: `work/tech/yliopiston-apteekki.md`, `work/compliance/yliopiston-apteekki.md`,
`work/assessment/yliopiston-apteekki.md`, `team/tech/reviews/ville-drafts-tech-review.md`.

## Slide 1: architecture (current state = frame for options A/B/C)
- Vendor-neutral: the RFP names only "an ERP system, omnichannel operations, and a BI tool across a public cloud".
  No product names; ERP, cloud and EU/EEA location marked "vahvistetaan vk 1" (outokumpu anti-pattern).
- Knockout box highlighted in the Keruu column: no browser scripts, pixels or tags (bio: "hypersensitive to
  front-end browser telemetry").
- Server-side is *not* sold as compliant (compliance + tech analysis trap): bullet 1 says legal basis is for their DPO.
- Option A "current tidied" with the 0.5-point rule comes from the assessment design (P7, "keep current" is real).
- Where access control sits: reporting layer box "Pääsynhallinta ja lokitus arvioidaan joka vaihtoehdossa" (P5, low).
- Band: read-only access, current licences, no production change (P4, bio "quick, painless").

## Slide 2: gates and risks
- Four checkpoints with pass criteria; Gate 1 before scoring (T4, P3).
- Pilot ("pistokoe") on synthetic or anonymised data only, no customer or prescription-level data (compliance GAP).
- Existing tags reported as findings only, never removed. This deliberately rejects the tech-critic suggestion
  "merkitään poistettaviksi tai korvattaviksi" (ville-drafts-tech-review item 3): removal is outside the RFP and
  conflicts with "keep daily operations quietly moving".
- Unknowns: licence list wk 2 (cost is direction only without it), sample data wk 3 (fallback: document check,
  scores marked less certain). Stack unknowns stay in the s2 callout.
- Scope fence: no build, migration, tag removal, legal opinion or AI.

## Patterns
P7 (high), P3 (medium), P4 (medium), P1 (low, EU/EEA as criterion), P5 (low). Not used: everything else.

## Effort basis (not a price)
Unchanged from the deck: current state 4, criteria + Gate 1 3, options + pilot 6, recommendation 5 = 18 pd.
Shrink path (assessment design): pilot on two flows (-1), option C as sketch only (-2).
