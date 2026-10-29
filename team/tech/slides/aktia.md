# Aktia tech slides: rationale

Buyer: aktia · Project: aktia-ticket-to-merge-request-developer-or-analytics-a
Spec: `team/tech/slides/aktia.json` (= `work/specs/aktia-tech.json`) · Preview: `team/tech/slides/aktia.pdf`
Deck: these slides are in `team/decks/aktia/aktia-ticket-to-merge-request-developer-or-analytics-a-v4.md` as slides 3 and 5
Inputs: `work/tech/aktia.md`, `work/compliance/aktia.md`, `work/genai/aktia.md`, `team/tech/reviews/ville-drafts-tech-review.md`

## Patterns applied
- **P2 human gate** <- "an automated maintenance script that bypassed peer review and altered schema dependencies".
  The agent identity has no approve, merge or admin rights. Aktia admins own branch protection and CODEOWNERS. Schema-dependency paths
  also need the data owner. The reviewer is never the requester. A week-1 bypass test checks all of this.
- **P1 EU sovereignty** <- "exposure to foreign-headquartered AI API dependencies". There are three hosting options, each with its
  **residual exposure** named. An EU region alone is not enough, because a US-HQ host or Snowflake Cortex is still a foreign-HQ provider. Aktia compliance chooses.
  The model sits behind one swappable interface and the exit is tested. We do not claim "no external APIs" because the Snowflake route cannot honour it.
- **P6 client tenant** <- earlier reply on "vendor-managed environments ... guest access". The deck says Aktia-issued identities, secrets
  in Aktia's vault, and everything in Aktia's repos and tenant.
- **P13 proof on their data / P4 small blast radius**: three gates (week 1 integrations, week 3 hosting + baseline, week 9 pilot).
  The targets are set after the first measurement, not fixed now.
- **P8 cost**: cost per ticket is measured in Definition and then capped (in the gate and in the note, not a new feature).

## Failure-risk table (answers "sidestep hard technical ... failure risks", honest_unknowns weak)
These risks are plausible-but-wrong PRs and reviewer fatigue, prompt injection through tickets, flaky tests, model or provider drift, no acceptable model, and stuck loops.

## Left out on purpose
ML, anomaly detection, auto-triage, extra use cases, new BI tools, any Temenos connection (the agent works only on the
analytics layer in dev), naming a specific model or provider, DORA contract clauses (contract terms are outside the tech lane).

## Effort basis (not a price; unchanged in the deck)
The deck has Definition 8 d, Delivery 25 d, Ops 3 d of architect time plus 3 months of the agent team. Note: during the pilot, PR review
and guidance usually take 2–3 architect days a month (vde-facts), against the "about 1 day per month" in run mode. Ville should check that the pilot review
load sits inside the Delivery days.
