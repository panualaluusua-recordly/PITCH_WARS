# Sanoma – Valtteri Salmela (Director of Data and AI Strategy)
- Bio: defends headcount, political climber, wants visible wins. RFP: backlog agent pilot, public cloud (stack unconfirmed), past black-box pilots failed on adoption, past vendors promised zero defects, 2-day co-build hackathon first, concise deck.

## 2026-10-29 · v1 draft, sanoma-analytics-backlog-agent (NOT sent)
- File: work/decks/sanoma/sanoma-analytics-backlog-agent-v1.md/.pdf, 6 slides.
- Price €51,120 = 26 human days (Hackathon: architect 3 + DE 2 + AI eng 2 = €6,520; setup/pilot: architect 8 + DE 8 + AI eng 3 = €17,600) + VDE 3 × €9,000 = €27,000.
- Bets: (1) hackathon first, staff co-build, conventions and code in their repo = no black box; (2) failure-handling table, no zero-defects promise, weekly rejected-PR count; (3) agent supports engineers, does not replace them (headcount sensitivity); stop after hackathon pays €6,520 only.
- Unknowns on deck: stack (VDE needs Snowflake + dbt, confirmed day 1), share of backlog that is routine.
- Price risk: no budget evidence; pilot anchor €10–15k suggests this could be over budget. Fallback: hackathon + 1 month of human work only, or VDE 3 months is the main cost driver.

<!-- replies:auto -->
## Buyer replies (auto, from the game API; do not edit inside the markers)

### sanoma-analytics-backlog-agent
- 2026-10-29T12:10 · **verdict** · deck `sanoma-analytics-backlog-agent-v7-eur54440.pdf` (€54,440) · price signal: **verdict lost, price over budget**
  > While the technical governance and collaborative hackathon framing align well with our platform modernization agenda, the overall commercial exposure across your phased fee structure sits entirely outside the fiscal envelope I have cleared for this initiative.
  ratings: price over budget, buyer_fit weak, project_fit excellent, presentation excellent
  - [leans against] Slide 6 calculates fees from day rates and a recurring monthly retainer rather than passing AI delivery efficiencies into cost reductions.
  - [partly met] Slide 5 lists Finnish language capabilities across all three delivery resources, though written deliverable language is not specified.
  - [leans against] Slide 2 and slide 5 lean on unnamed platform benchmarks and consultant profiles without citing media or publishing peer references.
  - [not addressed] The deck focuses strictly on analytics backlog automation and does not touch newsroom or editorial workflow integration.
  - [met] Slide 1 and slide 4 anchor the kickoff on an in-person, two-day co-build hackathon with our internal engineering team in Helsinki.
  - [met] Slide 2 explicitly enforces sandbox drafting with branch protection and mandates that only Sanoma engineers can merge to main.
  - [met] Slide 2 and slide 6 specify that the solution leverages Sanoma's own tenant compute and cloud credits without proprietary vendor licenses.
  - [met] Slide 3 and slide 4 openly address edge cases, reject zero-defect illusions, and establish clear technical stop gates.
<!-- /replies:auto -->
