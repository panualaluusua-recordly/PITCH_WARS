Buyer: aktia | AI in scope: yes <- "implement an automated ticket-to-merge-request analytics developer agent ... translate analytics tickets into validated transformation code, tests, and pull requests" (project aktia-ticket-to-merge-request-developer-or-analytics-a)
Autonomy: proposes, human approves. Never automated: merging or approving its own work, schema-dependency changes without the data owner, production access, Temenos changes, change requests from chat.
Eval: edge-case set 40-60 closed Aktia tickets plus schema-dependency cases (their ticket history, labelled by Aktia analysts) | metrics see section 3, gate confirmed with Aktia after the first measurement | cadence: every prompt/model/convention change, weekly in operations
Hosting: Aktia's own cloud tenant, EU region, models served in tenant or by an EU provider named with an exit plan, behind an abstraction layer; no ticket text, code or data to external APIs
Cost: token/compute cost per ticket measured in Definition; monthly cap and alert; reported per approved PR
Known failure modes: see section 6
Left out on purpose: see section 7

## 1. AI scope
Asked for in the RFP, so in scope. Two RFP lines shape it: "an automated maintenance script that bypassed peer review and altered schema dependencies" and "exposure to foreign-headquartered AI API dependencies". The earlier loss on the data-warehouse project: "predictive modeling bells and whistles is precisely what sank this proposal". So the design is the minimum loop, ticket -> code -> tests -> PR -> human. No ML, anomaly detection or extras.

## 2. Human gate
- Agent proposes: transformation code, tests, and a PR with diff, test evidence and reasoning summary.
- Approves: a named Aktia reviewer. Changes touching schema dependencies are labelled and also need the data owner (two-person rule).
- Enforced technically, not by promise: branch protection, CODEOWNERS, an agent identity with no approve/merge right and no production credentials, no path for a script to alter schema outside a reviewed PR. This answers the post-mortem directly.
- Never automated: merge, deployment, schema-dependency alteration, Temenos Transact changes (read for reporting data only), production access, tickets from chat.
- Kill switch: Aktia can disable the agent's service identity or trigger at any time; in the operations runbook. The agent stops when stuck.
- Audit: an auditor agent logs actions and reasoning and reports deviations, exportable for supervisory review. Aktia compliance signs the control matrix; we do not certify.

## 3. Eval plan
- Edge-case set: 40-60 cases (plan; confirm after Definition). Sampled from Aktia's closed analytics tickets, stratified by type, plus every past change that affected schema dependencies, plus deliberately bad tickets (ambiguous, touching restricted data). Labelled by Aktia analysts, with the data owner for dependency cases.
- Metrics. The numeric gate is agreed with Aktia after the first measurement, not fixed now:
  - Share of PRs approved without rework
  - Dependency-change detection: share of dependency-altering changes correctly labelled (any miss reviewed individually)
  - Correct ask-back/refusal on ambiguous or out-of-scope tickets
  - Wrong-pass count: changes that passed tests but a reviewer rejected
  - Review minutes per PR and ticket lead time vs. a baseline measured in Definition
  - Bypass attempts: must be zero, tested by trying to push or merge as the agent identity
- Regression: replay the set on every prompt, model, convention or tool change and whenever the model provider or version changes; a failing gate blocks release. Results are kept as audit evidence.
- Language: the RFP asks for Finnish and Swedish capability and the buyer objected to English runbooks on the earlier project. Include Finnish and some Swedish tickets and business terms in the set; score ticket understanding and the language of PR comments. Runbooks and the control matrix in FI/SV. Ask which language tickets are written in.
- Quality of EU-hosted models is unmeasured. Definition runs the set on candidate hosting options and reports the comparison before scope is committed.

## 4. Hosting and data
- Aktia's tenant, EU region; all code, pipelines, CI/CD, logs and model calls inside their perimeter (the buyer objected to vendor-managed environments on the earlier project). P1, P6.
- Model access behind an abstraction layer. Definition delivers hosting options (in-tenant EU serving or a named EU provider), each with an exit plan; no foreign-HQ API dependency without Aktia's explicit approval. Do not name a model or provider yet.
- The VDE runs in the customer's own Snowflake only if they use Snowflake + dbt (unconfirmed; "current data setup"). Definition week 1 confirms.
- Data minimisation: tickets and code only; no customer personal data in prompts unless approved; masking rules agreed.
- DORA items (provider register, exit plan, incident handling) go into the control matrix; compliance-analyst owns the detail.

## 5. Cost model (token/compute cost only)
- Unit cost = tokens or credits per ticket attempt, including review-agent loops, retries and auditor logging. Not measured; the Definition run on the eval set gives the first figure, delivery refines it.
- In-tenant model serving adds a fixed endpoint cost instead of per-token cost. Definition compares per-token vs. fixed cost at the expected ticket volume.
- Monthly cap = expected tickets x measured cost x a stated safety factor (assumption). Alert at 50/80/100 %, hard stop at the cap, resource monitor on the agent's warehouse or endpoint, retry cap per ticket.
- Monthly report: cost per ticket, per approved PR, and spend vs. cap.

## 6. Known failure modes
- Passes tests, wrong business logic -> reviewer rejects; reasoning summary in the PR; counted as wrong-pass.
- Dependency impact missed -> label absent; second-reviewer sampling; every miss goes into the set and is reviewed with the data owner.
- EU-hosted model weaker on Finnish/Swedish banking terms -> visible in the FI/SV slice; reported in Definition.
- Reviewer fatigue or rubber-stamping -> review minutes and approve-without-rework trend flagged; sampled second review.
- Agent stuck or looping -> stops and writes what it tried; retry cap.
- Provider or model change shifts behaviour -> regression gate, pinned versions.
- Poor ticket quality -> ask-back rate rises; reported to Aktia as an input problem, not hidden.
- Control matrix mistaken for certification -> stated plainly: Aktia compliance signs off.

## 7. Left out on purpose
ML models, anomaly detection, predictive features, extra use cases, new BI tools, Temenos changes, any foreign-API dependency, any accuracy or savings claim for Aktia before measurement, autonomous merge or schema change.

## Ready slide text (paste)
Title: Human gate, evals and cost control for the agent
- The agent drafts code, tests and a pull request. A named Aktia reviewer approves; schema-dependency changes also need the data owner. The agent has no merge right, enforced by branch protection, not by promise.
- Kill switch: Aktia can disable the agent's identity at any time. It stops when stuck. An auditor agent logs every action for supervisors.
- Test set: 40-60 of your closed tickets, including past schema-dependency cases and deliberately unclear tickets, labelled by your analysts, in Finnish and Swedish where your tickets are.
- Measured: approved without rework, dependency changes correctly flagged, correct ask-back, review minutes vs. your baseline. Pass gate agreed with you after the first measurement.
- Replayed on every prompt, model or convention change and before any model provider switch. A worse result blocks the release.
- Runs in your tenant, EU region, model behind a swappable layer with an exit plan; no data to foreign APIs. Token cost per ticket measured in Definition; monthly cap and alert.
