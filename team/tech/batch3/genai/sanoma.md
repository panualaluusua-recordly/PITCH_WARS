Buyer: sanoma | AI in scope: yes <- "pilot an intelligent analytics backlog agent ... parse incoming backlog tickets, determine the necessary data model changes, and autonomously draft merge requests for our engineers to review and validate"
Autonomy: proposes, human approves. Never automated: merging, production access, deploying, answering ambiguous or new-domain tickets, taking change requests from chat.
Eval: edge-case set 30-50 closed tickets from their backlog history (their engineers' accepted solutions as references) | metrics see section 3, gate confirmed with Sanoma after the first measurement | cadence: every prompt/model/convention change, weekly in pilot
Hosting: their public cloud (stack unconfirmed; the VDE pattern needs Snowflake + dbt, confirmed hackathon day 1), model behind an abstraction layer, in their tenant, EU region
Cost: token/credit cost per ticket attempt measured in the hackathon; monthly cap and alert set from it
Known failure modes: see section 6
Left out on purpose: see section 7

## 1. AI scope and autonomy
The RFP asks for it in its own words, so AI is in scope. Two buyer failure stories drive the design: "Earlier pilots handed over as finished black boxes struggled with internal adoption because our staff had no role in building them" and "prior AI vendor demos that promised zero defects only to fail on basic edge cases". So: staff co-build, no accuracy or zero-defect claim, only "every defect is visible before it reaches the pipeline".
The RFP says "autonomously draft merge requests"; autonomy here ends at the draft. The RFP itself says engineers review and validate.

## 2. Human gate
- Agent proposes: a plan (which models change) and a draft merge request with tests, diff and reasoning summary. When the ticket is unclear it asks on the ticket instead of guessing.
- Approves: a Sanoma engineer on every MR. Branch protection and CODEOWNERS require human approval; the agent identity has no merge right and no production credentials.
- Never automated: merge, deploy, production data access, changes outside the repo workflow, tickets raised from chat.
- Stops when stuck and writes what it tried; the engineer takes over.
- Kill switch: disable the agent's service account or pause its trigger; documented in the hackathon workflow; any engineer can pause it.
- Adoption by design: conventions, "perfect examples", prompts and code live in Sanoma's repo, owned by their team; staff review the eval results weekly with us.

## 3. Eval plan
- Edge-case set: 30-50 tickets (plan; adjust after the hackathon). Sampled from Sanoma's closed backlog tickets, stratified by type (new column, join change, fix, ambiguous, cross-domain), plus 5-8 picked by the engineers as "the ones that always go wrong". Hackathon day 1: the team picks the first 5-8 real tickets; the full set is built in the setup weeks. Labelled by Sanoma engineers: the right change (their merged MR) and which tickets the agent should refuse.
- Metrics. Targets are confirmed with Sanoma after the first measurement, not before:
  - Share of MRs approved without rework
  - Rejected MRs with reason categories (the weekly count already promised)
  - Correct ask-back/refusal rate on ambiguous tickets
  - Wrong-pass count: changes that passed agent tests but an engineer rejected
  - Review minutes per MR and ticket-to-merge lead time vs. a baseline measured before the agent runs
- Regression: replay the set on every prompt, convention, model or tool change; a drop in approved-without-rework or any new wrong-pass blocks the change.
- Language: the RFP does not state ticket language. If tickets or column names are Finnish, include ~10 Finnish tickets and score understanding. Ask day 1.
- The week-16 report uses Sanoma's numbers. The "12 h by hand to 30 min" figure is a Recordly project result, not a Sanoma promise.

## 4. Hosting and data
Their public cloud, repo and tenant, EU region. The VDE runs in the customer's own Snowflake on their AI credits, only if they use Snowflake + dbt; otherwise we adapt the guardrails and re-agree scope at the hackathon gate. Model access behind an abstraction layer; nothing leaves the tenant (P1, P6). Ticket text may contain personal data: agree masking rules.

## 5. Cost model (token/compute cost only)
- Unit cost = tokens or credits per ticket attempt, including review-agent loops and retries. Not yet measured; the hackathon on 5-8 tickets gives the first figure. Retry and loop count capped per ticket.
- Monthly cap = expected ticket volume x measured cost per ticket x a stated safety factor (assumption). Alert at 50/80/100 %, hard stop at the cap. On Snowflake: a resource monitor on the agent's warehouse and credits.
- Weekly note shows cost per ticket and per approved MR, so cost per useful MR is visible.
- The deck says AI credits sit on their account, billed by their provider.

## 6. Known failure modes
- Passes tests, wrong in meaning (metric definition misread) -> engineer rejects; reasoning summary in the MR; counted in the weekly rejected report.
- Plausible change breaks a downstream dependency -> impact check listed in the MR; any miss is added to the edge-case set.
- Ambiguous ticket guessed -> agent should ask back; a guess shows in the ask-back metric.
- Little of the backlog is routine -> reported after the hackathon sample; we say so if the answer is "little".
- Engineers rubber-stamp -> review minutes per MR and rework rate would drop to near zero; flagged to Sanoma, second-reviewer sampling.
- Quality degrades after a model change -> regression run.
- Loops or cost balloon -> retry cap and spend alert.
- Adoption stalls anyway -> staff in the build, weekly session, engineers can stop the agent.

## 7. Left out on purpose
Autonomous merge, production access, any claim of defect-free output, any accuracy or time-saving promise for Sanoma before measurement, new BI tools, tickets outside routine analytics.

## Ready slide text (paste)
Title: How we test it and keep your engineers in control
- The agent drafts; a Sanoma engineer approves every merge request. It has no merge right and no production access. Anyone can pause it.
- No zero-defect claim. Every defect is made visible before it reaches your pipeline, with a weekly count of rejected MRs and why.
- Test set: 30-50 of your own closed tickets, including the ones that "always go wrong". Your engineers label the right answer.
- We measure approved without rework, rejected and why, correct ask-back on unclear tickets, review minutes and lead time vs. your baseline. The pass gate is agreed with you after the first measurement.
- Every prompt, model or convention change replays the set first. A worse result blocks the change.
- Runs in your tenant behind a swappable model layer. Cost per ticket is measured in the hackathon; monthly cap and alert follow from it.
