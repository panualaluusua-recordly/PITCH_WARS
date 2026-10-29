# Tech critic round 2: veikkaus v5 (2026-10-29)
Tech lens only. Sources: team/decks/veikkaus/veikkaus-architecture-or-tool-assessment-v5.md, work/buyers_now.json (veikkaus), round 1 review veikkaus-tech-critic-2026-10-29.md. Game API not called. No price, team, terms or storyline judged.

## Verdict: strong
All three RFP outcomes (debt, model deployment, target-state patterns) have a deliverable. Stack uses only the RFP's own labels. Traps and gates are handled. Remaining gaps are one internal contradiction and two evidence-method gaps that a detail-oriented interviewer could probe.

## Round 1 fixes
1. Sample finding card under D1-D5 table: YES (slide "Technical methodology", "Sample finding card" line).
2. D4: option C as paper sketch, throughput baseline, run cost as scoring input: YES (D4 row, verbatim).
3. D2 localisation check and D3 rollback sample: YES (D2 "Check: is localisation..."; D3 "rollback tested on one past deployment").
Optional note on diagram arrows: YES (arrows labelled "data / models / reports (indicative)"; footer "a scope map, not your confirmed architecture").

## Top 3 new tech fixes
1. Slide "Technical methodology", D3 row: the rollback claim conflicts with "named read-only accounts" and "changes proposed, never applied".
   - Replace "rollback tested on one past deployment where history exists" with: "rollback traced on one past deployment from release records and runbook, walked through with your engineers; we execute nothing".
   - Evidence: RFP "streamline model deployment workflows"; deck's own "Named read-only accounts"; bio "demanding tangible proof".
2. Same slide, D1/D2 evidence column: name the log window and sources so the card numbers are reproducible.
   - Add: "Window: last 90 days of task logs (or all available). Sources: scheduler/task logs, admin and usage logs, access-grant export. Each card cites log name and period."
   - Evidence: bio "monitors task logs obsessively"; sample card "14 of 90 runs failed" has no stated window.
3. Same slide, compliance lens: say how lineage, audit trail and player-data handling are checked with metadata only.
   - Add to the "EVERY LAYER" bar or D2: "Compliance checks from configuration and metadata only: access-grant lists, audit-log settings, catalog lineage; no player-level rows read."
   - Evidence: RFP "robust compliance, reliable governance"; deck "no player-level data leaves your environment".

## Missing technical answers
- None without a slide. Weakest remaining: "how they fit together" is covered by D1 interfaces and the scope map, but the interface inventory is not named. Optional: in D1 add "interface list (source, direction, schedule) between the four layers".

## Still good
- Honest unknowns slide-level (products, log export, under 6 months history, no real-time promise).
- Week-1 access gate with fallback; week-4 evidence checkpoint; compliance pass/fail gate; AI Act "assess, not certify".
- No vendor tools introduced; no new AI features; licence baseline first.
