Buyer: sanoma | Project: sanoma-analytics-backlog-agent
Stack: "a public cloud" (company_cloud_vendor), "its current data setup hosted on a public cloud" (RFP), "modernizing reporting pipelines on a public cloud" (bio), chat tool "a chat tool" (unnamed). NOT Snowflake, NOT dbt, NOT named in any source.
Unknown: cloud vendor; warehouse (Snowflake / BigQuery / Redshift / Databricks / Synapse); transformation tool (dbt or not); Git host (RFP says "merge requests" = GitLab wording; our VDE uses GitHub PRs); ticket system; chat tool; CI/CD; dev/test environments and whether prod data can be cloned or masked; PII in subscriber analytics data; share of backlog that is routine; ticket quality; existing conventions/tests.

## Triggers (architecture-patterns scan)
- P2 Human gate ← "autonomously draft merge requests for our engineers to review and validate" and "promised zero defects only to fail on basic edge cases" and "keeping human oversight central to our data pipeline" (high)
- P13 Proof on their data ← "test feasibility and align on developer workflows" in a "two-day collaborative hackathon", "fail on basic edge cases" (high; edge-case set on their real tickets plus baseline and numeric gate)
- P6 Code in client tenant ← "Earlier pilots handed over as finished black boxes struggled with internal adoption because our staff had no role in building them" (high; conventions, prompts, agent code in their repo, they co-author)
- P4 Small blast radius ← "pilot", "kicking off ... with a two-day collaborative hackathon" (medium; pilot slice of tickets, stop after hackathon is possible)
- P8 Cost guardrails ← not in RFP; consumption-based LLM/warehouse credits on agent runs (low; add a budget and alert as a guardrail, only if stack confirmed)
- P3 Data foundation first (light) ← "integrated with its current data setup" with no stack named (low-medium; day-1 probing of stack, repo, access instead of full Phase 0)
- P1 EU sovereignty: NOT triggered (no sovereignty language). Do not add.
- P7 Use what they own: weak trigger only ("current data setup"); say we work with their existing repo, CI and tools, no new BI tools (low)
- P5 Access: not stated; subscriber analytics data likely holds personal data (bio "centralized subscriber analytics"), so agent dev environment should run on non-prod or masked data (low)

## Hard constraints
- Humans review every merge request ("for our engineers to review and validate"; "human oversight central")
- Start with "a two-day collaborative hackathon alongside our core analytics team"
- Integrate with "current data setup hosted on a public cloud" (no new platform)
- Staff must have a role in building ("our staff had no role in building them")
- Deck content: "technical solution, the delivery team, the implementation plan, and the pricing model", "concise"
- Scope is "routine internal analytics requests" / "repetitive tasks", not all requests

## Traps and honest answers
- "Zero defects" / "autonomously" wording → no defect-free claim; agent drafts, person merges; every failure visible; weekly rejected-PR count. (Draft does this.)
- "Determine the necessary data model changes" from a free-text ticket → this is the hard part. Honest answer: agent handles only tickets that meet a defined routine class; unclear or new-domain tickets are routed back with questions. Share of routine tickets is unknown until the hackathon sample.
- "Public cloud" with unknown stack → do not assume Snowflake+dbt. Honest answer: state the VDE pattern runs in Snowflake + dbt; on other stacks the hackathon decides whether the pattern ports or we stop. Do not present the stack as given.
- "Black box" adoption failure → code, prompts, conventions, eval set in their repo, co-written; their engineers can change the agent's rules without us.
- Integrated agent with "autonomous" access → no production credentials; agent works only in dev/sandbox schemas, reads metadata and code, branch protection stops direct pushes.
- Edge cases → collect during hackathon into a versioned edge-case list that becomes a regression test set for the agent.

## Praised/punished before
- Aktia (ticket to MR agent), lost: "sidestep hard technical migration unknowns" was weak; scope fence and ML extras punished (patterns.md anti-patterns: "ML/AI extras outside scope (Aktia lost)"). Lesson: no AI extras beyond the agent, name unknowns.
- Terveystalo, P2 praised (patterns.md: "terveystalo (praised)"); P13 numeric gate "40% gate" won preference.
- Kemira (won): P13 working prototypes on their data, no overpromised autonomy ("kemira (won)" in P5/P7 rows).
- Oriola v1 (focus5-review): "Hard gate metrics fixed before any measurement" marked down. Apply: state pilot acceptance numbers as proposed targets after baseline.
- Outokumpu v2: naming tools the buyer never mentioned as their stack was marked down. Directly relevant to Snowflake/dbt assumption.
- No Sanoma replies yet (conversation empty, 0 feedback rounds).

## VDE
VDE: MENTION as the technical basis, conditional INCLUDE only if Snowflake + dbt is confirmed
Stack: unconfirmed ← "a public cloud" (stack gate of vde-check: other or unknown platform = do not offer as a running product).
VDE takes (if Snowflake+dbt): model changes and tests from existing patterns, PR review by SQL/dbt/general agents, failed-job root cause.
Buyer signal: + backlog pain ("sit in the backlog for weeks"), agent pilot, co-build; - "zero defects" burn (offer only with human approval as headline, which the draft does).
Technical note for pricing owner (no figures): the VDE needs setup-month architect work for conventions and examples (vde-check step 4) and ongoing review days; the draft's architect days cover setup. Price is not my lane.
Must say: person approves every change; runs in your Snowflake on your AI credits; fixed term. The draft says these.

## Effort drivers
- Stack match: Snowflake+dbt means deploy pattern as is; other stack means porting or a different build (biggest swing, unknown until day 1).
- Quality of existing repo: conventions, tests, naming, documentation; no conventions means more architect setup.
- Routine share of backlog and ticket quality: smaller share means smaller pilot value, not more work.
- Environment access lead time: dev/sandbox schema, CI hooks, Git permissions, masked data (often the real critical path before hackathon).
- Number of ticket classes the agent covers in pilot (keep 2-3).
- Review load on their engineers (measured: review minutes per PR).

## Notes for deck owner (Ville)
1. Stack is asserted too firmly. Slide 2 says "our proven pattern runs inside your own Snowflake with dbt, on your AI credits" and slide 6 says "AI credits on your Snowflake account", while the RFP names no vendor. Rephrase as a conditional ("if your warehouse is Snowflake with dbt, ...; otherwise the hackathon tells us whether the pattern fits, and you can stop") and add a stack-fit check to hackathon day 1 output. Avoid pricing the VDE as if Snowflake were given. (Outokumpu anti-pattern: naming tools not in their RFP.)
2. Git vocabulary: RFP says "merge requests"; the draft says "pull request". Use "merge request (pull request)" or their term, and do not assume GitHub/Slack (the VDE facts use GitHub issues and Slack; RFP says only "a chat tool", Git host unknown). Tickets-only intake is good and fits "Changes: ... not from Slack".
3. Missing P2 hardening that a data-engineer reader will look for: branch protection or CODEOWNERS so the agent cannot merge or push to main, a kill switch / retry limit ("Agent is stuck" row exists; add max attempts), no production credentials.
4. Missing environment and data safety: agent works in dev/sandbox on masked or non-prod data (subscriber analytics probably holds personal data; low confidence), read access to code and metadata only. Add to Phase 2 and as a hackathon-prep dependency (access ready before day 1).
5. Missing baseline: the "Measured in the pilot" line has metrics but no baseline or numeric acceptance gate (P13). Say the hackathon sample sets the baseline (current ticket lead time, rework rate) and targets are agreed with Sanoma after that, not fixed now (Oriola lesson).
6. Edge-case handling: say the edge-case list becomes a versioned regression set in their repo, and that every rejected MR feeds it. This directly answers "fail on basic edge cases".
7. Define "routine": name the ticket classes the pilot covers (for example add a column, new metric/model from an existing source, test addition; examples to confirm with them) and the fence ("ambiguous or new-domain requests" already out of scope). Keep to 2-3 classes.
8. Hackathon realism: "5–8 real tickets" in 2 days is fine, but the output "feasibility note" should list stack fit, routine share, edge cases found, and access gaps. Specify what must be ready before day 1 (repo access, dev environment, sample tickets).
9. "12 h by hand to 30 min" is in vde-facts as "Semi-complex pipeline: build, test, validate"; fine, but label it as a Recordly case on a Snowflake+dbt project, not a promise on Sanoma tickets. Draft wording "Real result (Recordly projects)" is acceptable; avoid implying 24x on their backlog.
10. Cost guardrail (P8, low): if Snowflake, add a credit budget and alert for agent runs, reported weekly. Optional; only if it fits slide space.
11. Claim check: "An auditor agent logs every step" matches vde-facts (Auditor agents). "Review agents ... SQL, dbt and general" matches. "Only a person merges" matches ("cannot approve or merge its own work").
12. Do not add AI/ML extras, new BI tools or EU-hosting claims (no trigger).
