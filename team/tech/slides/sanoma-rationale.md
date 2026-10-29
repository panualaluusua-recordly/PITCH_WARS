# Sanoma tech slides: rationale

Spec: `team/tech/slides/sanoma.json` (preview `sanoma.pdf`, slide text `sanoma.md`, both from `team/bin/deck.py`).
Inputs: `work/tech/sanoma.md`, `work/genai/sanoma.md`, tech-critic review (sanoma v1), deck v2/v3.

## Patterns applied
- **P2 Human gate** ("autonomously draft merge requests for our engineers to review and validate"; "promised zero defects"): branch protection and required approval, agent has no merge right or production credentials, retry cap, pause switch.
- **P13 Proof on their data** ("fail on basic edge cases"): 30-50 closed tickets as test set, baseline at the hackathon, pass share agreed after the first run (Oriola lesson: no gate numbers fixed before measurement).
- **P6 Code in client tenant** ("black boxes ... staff had no role in building them"): conventions, prompts, test set in their repo.
- **P4 Small blast radius**: hackathon go/no-go, 2-3 ticket classes.
- **P3 light / stack unknown**: tools named only after day 1; Snowflake + dbt stated as a condition, not as their stack (Outokumpu anti-pattern).
- **P5 light**: dev sandbox on non-prod or masked data; masking rules before day 1 (low confidence that subscriber data holds PII).
- **P8 light**: cost cap per ticket in the band only; measured in the hackathon (genai cost model).

## Left out on purpose
EU-sovereignty claims (no trigger), new BI tools, ML/AI extras, autonomous merge, any accuracy or time-saving promise for Sanoma, GitHub/Slack/Snowflake as given facts.

## Where the slides go
Slide 1 replaces deck slide 2 (Proposed technical solution). Slide 2 is folded into the deck's existing slides
rather than added: the gate rows go into the plan table's Gate column, the unknowns line goes on the human-oversight
slide. Deck stays at cover + 5.

## Effort basis (not a price)
Unchanged from the v2 day counts: hackathon 7 person-days, setup and pilot human work 19, run review 3.
Tech note: access prep before day 1 is Sanoma-side work; if the stack is not Snowflake + dbt, the setup days do not
cover a port and the scope is re-agreed at the hackathon gate.
