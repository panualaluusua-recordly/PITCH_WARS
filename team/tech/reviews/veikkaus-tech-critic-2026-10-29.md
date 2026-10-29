# Tech critic: veikkaus v4 (2026-10-29)
Tech lens only. Sources: team/decks/veikkaus/veikkaus-architecture-or-tool-assessment-v4.md, team/tech/slides/veikkaus.md, team/tech/batch3/veikkaus.md, team/buyers/veikkaus.md, prior review in team/tech/reviews/ville-drafts-tech-review.md#veikkaus. Game API not called.

## Verdict: strong
The v4 deck answers all three RFP outcomes (technical debt, model deployment, target-state patterns). Its architecture matches the RFP's stack labels, and the traps are handled. The remaining gaps are small. Three of them can cost points in a sceptical two-hour interview.

## Top 3 tech fixes (most valuable first)

1. Slide "Technical methodology and deliverables": show one sample finding card.
   - Change: add a one-line card under the D1-D5 table, ready to paste: `Sample card: "Nightly player-reporting job, 14 of 90 runs failed, 3 manual restarts. Source: task log. Impact: late reports. Compliance: audit trail OK, lineage gap. Confidence: medium."`
   - Why: the interview line promises to "walk one finding card end to end", but no card appears anywhere in the deck.
   - Evidence: RFP two-hour interview; bio "demanding tangible proof over vendor promises".

2. Same slide, D4 row: pin option C and add a throughput baseline and a cost guardrail.
   - Change: replace "C re-platform pattern" with "C re-platform pattern, paper sketch only, no tool bake-off". Append: "Throughput scored on peak load and batch lag from your task logs. Run cost per option is a scoring input."
   - Why: "re-platform" next to "no new tools by default" reads as a contradiction. The spec's shrink path already defines C as a paper sketch.
   - Why: "high-throughput" carries 20 weight points but has no named measurement. The earlier review asked for this (its improvement #2).
   - Evidence: RFP "high-throughput data processing are paramount"; "substantial untapped capacity".

3. Same slide, D2 and D3 rows: add a localisation check and a rollback sample.
   - D2 addition: "Check: is localisation of player-facing report and model outputs a pipeline step? Reported as a finding, not a fix."
   - D3 addition: "rollback tested on one past deployment where history exists".
   - Why: the Swedish-translation problem is only answered as a deliverable-language promise. batch3 trap 7 says the technical angle is the pipeline step. The D3 rollback claim needs a named sample to survive questions.
   - Evidence: bio "sloppy Swedish translations"; RFP "streamline model deployment workflows".

## Missing technical answers
- No RFP technical ask is without a slide.
- Weakest answer: "how they fit together". The diagram shows a linear flow (platform -> AI -> BI/ERP), but BI normally reads from the data platform directly. The footer says "a scope map, not your confirmed architecture". Consider labelling arrows "data / models / reports" to avoid implying a confirmed topology.

## Already good
- Stack: only the RFP's own labels (cloud data platform, in-house AI platform, BI tool, ERP system). No vendor named; "Vendor-neutral: products confirmed in week 1".
- Diagram present, with D1-D4 evidence points per layer. The train -> register -> approve -> deploy -> monitor path shows where D3 lead time is measured. This closes the v1 "No architecture diagram" finding.
- Honest unknowns: products and licence terms, log exportability, under 6 months of deployment history shown as a range, no real-time promise (P10).
- Gates: week-1 access gate with a fallback (admins export logs, plan moves by the delay); week-4 evidence checkpoint with targets "confirmed with you after week 1"; compliance pass/fail; "changes proposed, never applied".
- Scope discipline: licence baseline first (P7); no new AI features, no build or migration; metadata and counts only with read-only accounts (P5); AI Act lens "we assess, not certify"; no gaming-law claim.
- Finding cards allow "evidence requested", so "no finding without evidence" holds when logs are missing.
- Shrink path exists in the spec (C as paper sketch, merged read-out).

## Out of scope here (other owners)
Vendor-specific certifications on the credentials slide belong to the staffing owner. They are already flagged in the earlier review.
