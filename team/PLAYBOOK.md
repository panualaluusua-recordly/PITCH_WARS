# Deck playbook (from the first 4 buyers' replies and reviews)

## How buyers score a proposal

The proposal `review` rates `price`, `buyer_fit`, `project_fit`, `presentation`, and lists ~8 `preferences`
(about half from the buyer's bio, half hidden in the project) plus presentation criteria:
`client_understanding`, `storyline`, `honest_unknowns`, `concreteness`, `slide_clarity`.

**Every "past problem" sentence in the RFP or bio is a hidden preference.** Answer each one explicitly,
with a concrete mechanism, on a named slide. Examples seen:

| Signal in RFP / bio | What won |
| --- | --- |
| "messy integrations blew up", "unknown sources" | Month 1 = source-risk probing sprint with a formal go/no-go gate |
| knowledge left with contractors | Pair programming with internal staff from week 1; client engineers lead later work |
| foreign-language workshops stalled | All workshops, runbooks, documentation in Finnish (Swedish too where relevant) |
| hates status meetings / calendar load | No standing weekly status meetings; written bi-weekly updates + live dashboard |
| regulated / security | All code, pipelines, CI/CD inside the client's own cloud tenant and repos; no vendor-hosted envs |
| standard purchase agreement | Accept it as is, **zero deviations** (say so explicitly) |
| recruit consultants after 12 months | Accept explicitly, no fee |
| replacement of consultants / key-person friction | Accept; binding substitution terms (notice, equal seniority, overlap at our cost) |
| AI hype / overpromising | Stay strictly in requested scope; no speculative ML/AI extras (Aktia LOST on "ML anomaly detection bells and whistles") |
| existing stack | Build only on their current platform; no new licences |
| "too many slides" | Keep it short: **cover + 5 content slides max** (7 was marked down) |
| "too certain / idealized" | An explicit risks & assumptions slide: what could derail it, what would change scope/price |
| rigid lump sum disliked (Helsinki SME) | Fixed-price discovery, then capped phases with change rules |

## Structure that scored "strong" on storyline

1. Cover
2. **Answer first**: what we deliver, timeline, total price, the 3 commitments that address their pain
3. Approach / architecture on their stack (concrete deliverables D1..Dn)
4. Plan: phases with gates, pairing/handover, Finnish docs
5. Team: named people, role, % allocation, certifications, availability from date
6. Price breakdown by phase + commercial terms (accept their contract terms) + risks/assumptions

Action titles (titles that state the point), not topic titles.

## Price

Price is the total the buyer reads in the deck. "above budget" in feedback = a hard no; cut ~25-35%.
Calibration so far (both rated price **excellent** and won):
- Kemira, 100-day data & AI roadmap: **€16,500**
- City of Helsinki, 2 data engineers x 6 months: **€84,000** fixed
Most first decks were "above budget", so buyers' budgets are modest.

## Etiquette

- Feedback max ~2 per project. Enfuce after 5 feedbacks: "Stop asking for reviews".
- Re-sending the same deck for feedback wastes money.
- `no_reply` happens and the fee is lost.
