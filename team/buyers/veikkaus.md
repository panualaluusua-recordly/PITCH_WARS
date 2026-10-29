# Veikkaus – Matias Lehtoranta (Development Manager, Data & Analytics)

## v1 draft (not sent)
- File: work/decks/veikkaus/veikkaus-architecture-or-tool-assessment-v1.md (6 slides). Price €18,400 = 20 person-days × €920 (anchor: Kemira €16.5k won / €22k "inflated"). No feedback or proposal sent yet.
- Bets: (1) evidence-based method, finding card with evidence per finding, sample shown at interview; (2) licence-utilisation baseline first, existing capacity before anything new, no new tools; (3) Finnish AND Swedish deliverables with native Swedish review + FI/SV/EN glossary.
- Also answered: compliance/governance lens, read-only access, no player data leaves; all 6 RFP sections in order; "No contractual deviations"; 2-hour interview prepared.
- Honest unknown on slide: platform vendors/licence terms not in RFP, settled by week-1 access checklist, week-4 checkpoint.
- To verify before sending: Swedish native-level speaker really on roster; certifications (Azure Solutions Architect Expert, Databricks DE Pro / ML Pro, SnowPro Core, Azure DE Associate, GCP Professional DE) are placeholders for roster; VDE = NO (advisory, not Snowflake).
- Fallback if over budget: 16 days × €920 = €14,720 (drop one option in D4, merge phases 3-4).

## Rauno / Codex feedback round 2026-10-29

Sent 5 (source version), kind feedback; fee EUR 1,000.

> The main issue here is commercial: the proposed price is clearly above our budget, and that cost overage is our primary concern before we can consider moving forward. On the technical side, I do appreciate that their methodology anchors the debt register directly in task log failure counts and run durations rather than subjective maturity frameworks. Still, relying on standard platform access toggles and out-of-the-box compliance configurations leaves me uneasy, especially since our past consolidation of legacy operational metrics onto the cloud data platform with our in-house AI platform proved that generic baseline settings leave far too many visibility gaps during regulatory audits.

Response-led final candidate: v7, EUR 13440.

## Final outcome observed by Rauno / Codex

2026-10-29T12:14:14.667129+00:00 — Another team agent submitted `veikkaus-architecture-or-tool-assessment-v7-eur19200.pdf` at 2026-10-29T12:10:15.543782+00:00. Result: **lost**. Rauno's subsequent final send aborted during pre-check (project already closed), before POST and with no additional fee.

> While the task-log evidence checks and deliverable breakdown are technically well-structured, the bottom-line commercial total on the pricing slide simply exceeds our available expenditure envelope.

```json
{
  "ratings": {
    "price": "over budget",
    "buyer_fit": "good",
    "project_fit": "good",
    "presentation": "excellent"
  },
  "preferences": [
    {
      "area": "buyer",
      "verdict": "partly met",
      "evidence": "Slides 2 and 4 apply a compliance and governance pass-fail gate to all findings and architectural options."
    },
    {
      "area": "buyer",
      "verdict": "met",
      "evidence": "Slides 1, 2, and 5 guarantee deliverables in Finnish and confirm Finnish language fluency across the team."
    },
    {
      "area": "buyer",
      "verdict": "met",
      "evidence": "Slide 2 commits to native Swedish review of all project deliverables and establishing a trilingual glossary in week 1."
    },
    {
      "area": "buyer",
      "verdict": "not addressed",
      "evidence": "Slide 3 reviews pipeline failure rates and lineage gaps without addressing managed SQL services versus custom orchestration."
    },
    {
      "area": "project",
      "verdict": "partly met",
      "evidence": "Slides 1 and 6 place the team at Recordly Oy in Helsinki and explicitly include Helsinki travel in the scope."
    },
    {
      "area": "project",
      "verdict": "met",
      "evidence": "Slide 2 establishes a licence-utilisation baseline first and explicitly rules out introducing net-new tools by default."
    },
    {
      "area": "project",
      "verdict": "not addressed",
      "evidence": "Slide 3 inspects access-grant lists and audit logs without evaluating bespoke access controls against default platform settings."
    },
    {
      "area": "project",
      "verdict": "met",
      "evidence": "Slide 5 lists specific cloud vendor badges including Azure Solutions Architect, Databricks Data Engineer, and SnowPro Core."
    }
  ],
  "presentation": [
    {
      "criterion": "client_understanding",
      "rating": "strong",
      "evidence": "Slide 2 mirrors our exact stack components, audit log requirements, and historical Swedish translation pain points."
    },
    {
      "criterion": "storyline",
      "rating": "strong",
      "evidence": "The narrative flows systematically from upfront scope and price to methodology, schedule checkpoints, and commercial terms."
    },
    {
      "criterion": "honest_unknowns",
      "rating": "strong",
      "evidence": "Slide 4 lists explicit open parameters including unverified software licence terms and missing export logs."
    },
    {
      "criterion": "concreteness",
      "rating": "strong",
      "evidence": "Slides 3 through 6 define concrete deliverable cards, exact task day counts, verified badges, and a fixed cost."
    },
    {
      "criterion": "slide_clarity",
      "rating": "strong",
      "evidence": "Every slide pairs a concise executive takeaway headline with clean, legible tabular data."
    },
    {
      "criterion": "explanatory_visuals",
      "rating": "strong",
      "evidence": "Slide 3 maps out our data flow into clear evaluation stages alongside structured tabular matrixes."
    },
    {
      "criterion": "recordly_style",
      "rating": "strong",
      "evidence": "The deck strictly adheres to the dark background, lime accent color, structured tables, and consistent footer branding."
    }
  ]
}
```
