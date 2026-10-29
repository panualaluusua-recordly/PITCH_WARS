# Virtual Data Engineer: facts we may claim

Source: Recordly Drive, "VDE-Snowflake-12_10_2026" and "Virtual Data Engineer" decks (Oct 2026). Claim nothing beyond this.

## What it is
- Recordly's approach to continuous data development and maintenance powered by AI agents.
- **Runs inside the customer's own Snowflake account** and uses the customer's Snowflake AI credits. Built on Snowflake and dbt, alongside Cortex Code.
- Not a single agent. It's a team with orchestration:
  - **Data Engineer agents:** analyse, plan and do maintenance and development work, resolve errors, spin up environments, migrate data. They run automatically or are triggered by a developer.
  - **Review agents:** SQL-specific, dbt-specific and general review. They run tests on every change and send work back for fixes.
  - **Auditor agents:** track logs and the agents' reasoning, keep an audit trail and report deviations.
- Uses Recordly's knowledge base: the expertise of our best specialists.

## How it works
- Questions: Slack → agent → answer in the thread
- Changes: GitHub issue → agent → pull request → **human approval**
- Reviews: GitHub PR → agent → comment → human approval
- Alerts: dbt failure → Slack → agent → root cause, PR or answer

## Guardrails
- It **can**: answer questions in Slack threads, open pull requests, investigate failed jobs.
- It **cannot**: approve or merge its own work, take change requests from Slack, keep running when stuck.
- **Every change goes through a person.**

## Example tasks
Profiling, data contracts, PII classification, schema drift, coding, testing and review, cost and performance optimisation, semantic modelling, catalog, API specification, data questions, reporting inconsistencies, data exports.

## Results from real projects
| Case | Result |
|---|---|
| Migration: Matillion + Redshift → dbt + Snowflake, jobs included | ~30 Snowflake credits per migrated table |
| Semi-complex pipeline: build, test, validate | 12 h by hand → 30 min |
| Power BI report rebuilt after a migration | Tens of seconds (with Cortex Code) |
| Business questions about pipelines or availability | Developer context switches per day: several → 0 |

## Best-fit signals
Migration underway or just finished · Snowflake + dbt · team is the bottleneck (many consultants, constant onboarding) · business wants answers directly · licence budget but no headcount.

## What it needs from humans
The VDE does the grunt SQL work from existing material. Humans provide the project structure, plan and data model, documentation and guidelines, work items and "perfect examples", and they review, guide and refine (source deck: "Value is created at different levels"). More VDE capacity means more need for architecture up front.

## Run mode
For continuous development, maintenance and monitoring, the VDE does the work 24/7 and the customer's own staff approve every change through pull requests. Recordly keeps light architect support (about 1 day/month).

## How we start
Pick 2–3 use cases → measure the baseline (lead time, review load, onboarding time) → deploy in their account → run for a **fixed 3-month term** → measure and scale.

## Commercials (team rule for Pitch Wars)
- **€9,000 per month, flat**, sold together with the human team, fixed term (minimum 3 months).
- Snowflake AI credit consumption is billed to the customer by Snowflake.
