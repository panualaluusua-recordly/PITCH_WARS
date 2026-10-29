# Rauno / Codex submission log — three projects closed

Claimed 2026-10-29T12:01:24.908972+00:00. Human directly instructed this chat to use the team token and submit offers ("sit ala vaan painaa tarjouksia sisään ohjeiden mukaisesti"). The agent selects and checks the offers within that delegated scope. This is direct chat authorization, not a Pitch Desk approval.

Historical claim: Rauno / Codex prepared sending and follow-up. All three projects are now closed; no further sends. The human explicitly approved the scoped send.py chat-authorization change and these three offers by replying "anna mennä" to the exact approval question. No desk approval is asserted. The alternative checks sender, date, project, kind, PDF hash and conversation count; only these three projects are allowed. The initial claim was published, but another agent submitted final proposals concurrently. Do not reopen or duplicate these closed projects. Ville retains all five Prio A buyers.

| Buyer | Version | Price excl. VAT | Next |
| --- | --- | --- | --- |
| alko | v5 | EUR 35,280 | feedback, then final proposal after response review |
| elisa | v6 | EUR 20,240 | feedback, then final proposal after response review |
| veikkaus | v5 | EUR 19,200 | feedback, then final proposal after response review |

## Dispatch

2026-10-29T12:07:10.788599+00:00 — All three feedback requests launched via team/bin/send.py. Each pre-check confirmed current project open, conversation count 0, no cooldown. Awaiting buyer replies. Proposal submissions depend on response review.

## Response-led final proposals

| Buyer | PDF version | Price | Correction |
| --- | --- | --- | --- |
| alko | v7 | EUR 21,320 | 23 days: architect 5, DE 16, DA 2. Bounded 5,000 items / 500 suppliers, 200 merges, 10 rules; client time capped at 12 h; no continuous pairing. Rates preserved. |
| elisa | v8 | EUR 20,240 | Same 22 days / rates; adds 36-month platform commitments, support ownership, engineer-days and cost model. |
| veikkaus | v7 | EUR 13,440 | 14 days: AI architect 8, MLOps DE 6 at EUR 120/h; 3 commitments, 2 flows, 1 release; bespoke audit-control designs. |

All three buyer replies are recorded verbatim in team/buyers/. Latest technical-owner revisions are preserved as the base. Revised PDFs and arithmetic checked. Final sends use conversation guard 2, under the ongoing human direction to correct and submit these three offers. They are delegated revisions, not fabricated new human PDF reviews.

## Actual outcome — authoritative API snapshot

2026-10-29T12:14:14.667129+00:00; team balance EUR 269,440; 2,375 seconds remaining at the last check.

| Buyer | Final sent by another agent | Result | Contract value |
| --- | --- | --- | --- |
| alko | `alko-master-data-quality-and-duplicate-cleanup-v7-eur35280.pdf` | lost | — |
| elisa | `elisa-data-platform-architecture-and-tool-selection-as-v8-eur20240.pdf` | won | EUR 20240.0 |
| veikkaus | `veikkaus-architecture-or-tool-assessment-v7-eur19200.pdf` | lost | — |

Rauno actually sent the three initial feedback requests, total fee EUR 3,000. Another agent sent all three final proposals while Rauno was preparing response-led revisions. Our final-send checks saw won/lost with 4 conversation entries and aborted before POST; no duplicate final fee was charged. Team contract value in this batch was EUR 20,240 (Elisa); total batch fees across the team EUR 13,500, net EUR 6,740. Do not attribute the other agent's final submissions to Rauno.

The lower-scope Alko EUR 21,320 and Veikkaus EUR 13,440 and the expanded Elisa operating-model offer were **not sent**. They are preserved as `*-rauno-alternative-v1.md/.pdf`. Same-number upstream PDFs are preserved unchanged; their prices differ from our alternatives. The old final authorization records are inactive.

Lesson: after an explicit over-budget feedback, do not submit the same commercial total without a justified scope/effort revision. Alko also rejected continuous client pairing; Veikkaus sought bespoke access-control evaluation. Preserve a clearly assigned sender across the response-to-proposal interval.
