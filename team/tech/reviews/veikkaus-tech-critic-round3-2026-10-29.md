# Tech critic round 3: veikkaus v6 (2026-10-29)
Tech lens only. Sources: team/decks/veikkaus/veikkaus-architecture-or-tool-assessment-v6.md, work/buyers_now.json (veikkaus), round 2 review. Game API not called. No price, team, terms or storyline judged.

## Verdict: strong
All three RFP outcomes (debt, deployment, target-state patterns) have a deliverable and an evidence method. Stack uses only the RFP labels. Remaining gaps are small.

## Round 2 fixes landed
1. D3 rollback wording: YES ("traced on one past deployment from release records and runbook ... nothing executed by us").
2. D1 log window and sources: YES ("last 90 days of task logs", sources listed, "Each card cites log name and period").
3. Metadata-only compliance checks: YES (EVERY LAYER bar: access-grant lists, audit-log settings, catalog lineage).
4. Optional interface list in D1: NO (still not named).

## Top 3 new tech fixes
1. Slide "Technical methodology", D1 row: "how they fit together" has no named artefact. Add at the end of D1 evidence: "Interface list between the four layers: source, target, direction, schedule, owner, with failure points marked." | evidence: RFP "cloud data platform with an in-house AI platform, connected to a BI tool and an ERP system"
2. Same slide, diagram: "Operational source systems" and "ERP (feeds and receives)" are our guesses, not the buyer's words. Change the ERP label to "ERP system (interfaces confirmed in week 1)" and the sources label to "Operational source systems (to be confirmed)". | evidence: bio "legacy operational metrics onto a cloud data platform"; bio "proof over vendor promises"
3. Slide "Implementation plan", D4 / phase 3: scoring depends on peak load, but no fallback if peak or batch-lag data is thin. Add: "If under 90 days of load data exists, throughput is scored as a range and marked low confidence, and the option is not ranked on throughput alone." | evidence: RFP "high-throughput data processing are paramount"; bio "monitors task logs obsessively"

## Missing technical answers
- None without a slide. Minor: the team slide lists certifications from several named vendors while the deck says "vendor-neutral"; consider a one-line note "certifications show breadth; the assessment uses your products only" (wording check, not a tech blocker).

## Still good
- Week-1 access gate with fallback; week-4 evidence checkpoint; compliance pass/fail gate; AI Act "assess, not certify".
- Honest unknowns; no real-time promise; no new tools or AI features; sample finding card.
