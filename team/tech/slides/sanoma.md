# Tech & architecture slides for the Sanoma deck
_Sanoma: Two slides: they replace the solution slide and the human-oversight slide, not added on top_

## 2. The agent drafts in a sandbox; only your engineer can merge
- **Your stack, named after day 1.** The RFP says only "public cloud". If your warehouse is Snowflake with dbt, our running agent pattern deploys as is; otherwise the hackathon shows whether it ports, and you can stop.
- **Merge requests in your own tool.** Branch protection and required approval by your engineers: the agent has no merge right and no production credentials. Any engineer can pause it.
- **Not a black box.** Conventions, examples, prompts and the test set live in your repository; your engineers change the rules without us.
[Your backlog: Routine ticket (2-3 classes agreed at the hackathon), Unclear ticket: questions back on the ticket, No changes from chat] → [Agent in a dev sandbox: Reads ticket, code and model metadata, Plans which models change, Writes change and tests on non-prod or masked data] → [Checks: Review agent: SQL and your conventions, Your CI tests + edge-case regression set, Retry cap, then stops and writes what it tried] → [Your engineer: Merge request: diff, tests, reasoning, Approves or rejects, Only a person merges to main]
(In your repository and cloud tenant: branch protection, no agent merge right, no production credentials, run log and cost cap per ticket, pause switch)

## 3. Technical gates: you decide at each one, on numbers from your own tickets
| Gate | When | Pass criterion |
| --- | --- | --- |
| Access ready | Before hackathon day 1 | Repository and merge-request access, a dev schema, 5-8 sample tickets; masking rules agreed if ticket or data samples hold personal data |
| Hackathon go/no-go | Week 1, day 2 | Feasibility note: stack fit, routine share of the sample, edge cases found, access gaps, baseline lead time. Sanoma decides |
| Setup gate | End of week 3 | Agent scored on 30-50 of your closed tickets, incl. the ones that "always go wrong"; pass share agreed with you after the first run, not before |
| Pilot, weekly | Weeks 4-16 | Approved without rework, rejected and why, wrong passes, review minutes, lead time vs baseline. Any prompt, model or convention change replays the test set first |

_Technical unknowns, resolved on day 1: warehouse and transformation tool; Git and ticket host; share of the backlog that is routine; personal data in subscriber analytics. If the answer is "little routine work", we say so at the gate._
