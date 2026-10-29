---
name: vde-check
description: Decides whether Recordly's Virtual Data Engineer (VDE, AI agent team at a flat €9,000/month) fits a Pitch Wars project, what work it takes over from the human team, and how to price and pitch it honestly. Use for every RFP before pricing, when a buyer has Snowflake or dbt, a backlog/capacity problem, migrations, or asks how we use AI in delivery.
allowed-tools: Read, Grep
---

# VDE check

The VDE is a product: a team of AI agents that takes simple, repetitive data engineering work off human developers. It's sold **with** the human team at a **flat €9,000/month** for a fixed term. Facts and limits are in `vde-facts.md`. **Read it every time**, and never claim more than it says.

## Inputs

- `rfp-trap-scan` output (stack, scope, fears and hopes)
- `vde-facts.md` (this folder)

## Steps

1. **Stack gate.**
   - Snowflake **and** dbt → strong fit.
   - Snowflake without dbt → possible fit; say dbt adoption is part of the setup.
   - Other platforms (Databricks, BigQuery, Redshift, Azure-only, SAP) → **don't offer the VDE** as a running product. Mention it at most as "available for Snowflake + dbt" if the buyer asks how we use AI.
2. **Work gate.** List the RFP's work items and mark the ones the VDE can take: pipeline coding from existing patterns, tests and validation, PR review against agreed practices, failed-job root-cause analysis, schema drift, PII classification, data profiling, catalog and docs, migration grunt work, answering "where does this field come from" questions. It needs ongoing build or run work lasting **≥ 3 months**. Pure advisory, roadmap or assessment work → no VDE.
3. **Buyer gate.** Use the fears and hopes from the trap scan.
   - **Plus:** backlog or capacity pain, too many consultants, review bottleneck, migration underway, licence budget but no headcount, wants productivity gains shared, asks how we use AI internally, a co-build or agent pilot.
   - **Minus:** "no AI extras", AI-hype burns, unvetted code incidents (offer it only if human approval of every change is the headline), strict "no new tools" (it runs inside their Snowflake and uses their AI credits, so say exactly that).
4. **Offload math.** The VDE runs 24/7, so it takes most of the simple work. But it can only build well on a clear architecture, so **human architecture work goes up**.
   - VDE months = the build/run duration (minimum 3).
   - Split the human-only estimate into **simple work** (pipelines from patterns, tests, fixes, docs, migrations of similar objects) and **complex work** (design, unclear problems, stakeholder work).
   - The VDE takes **70% of the simple-work days** (range 60–80%; use 60% when the patterns are still unclear, 80% for repetitive migrations).
   - **Add senior architect days** so it can make good decisions while building:
     - Setup, month 1: **8–10 days** for architecture, data model, naming and dbt conventions, guidelines, well-specified work items and "perfect examples" for the agents
     - Ongoing: **2–3 days/month** for reviewing PRs, guiding the agents, refining conventions and handling escalations
   - New human days = complex days + 30% of the simple days + architect days.
   - New price = new human days × day rate (role minimum from `price-check`, ≥ €920) + VDE months × €9,000.
   - Offer the VDE only if the new price ≤ the old human-only price **or** the deck clearly delivers more for the same budget.
5. **Run mode (continuous work).** If the RFP has continuous development, maintenance, monitoring, hypercare or a run phase after delivery, the VDE can take it over:
   - It handles monitoring (dbt failure → root cause), small fixes and changes, and questions, 24/7.
   - **The customer's own staff approve every change** (PR approval), so no human Recordly developer is needed for day-to-day run work.
   - Recordly human time drops to about **1 day/month** of architect support for conventions, escalations and new skills.
   - Price for this phase: VDE months × €9,000 + those architect days. Offer it as the run model after hypercare, or as an option alongside an incumbent AMS partner (it supports them and doesn't replace them unless the RFP allows).
6. **Decide:** `INCLUDE`, `INCLUDE-RUN` (run phase only), `MENTION` (as an option or how we work, not priced) or `NO`.

## Output

```
VDE: INCLUDE | INCLUDE-RUN | MENTION | NO
Stack: <snowflake+dbt | snowflake | other> ← "<RFP quote>"
VDE takes: - <work item> (<days saved>)
Buyer signal: + … / − …
Days: simple <s> → VDE takes <0.7·s>; complex <c>; architect +<a> (setup <x> + <y>/month)
Price: human <d> days × €<rate> = €<a> + VDE <m> × €9,000 = €<b> → total €<a+b> (human-only would be €<c>)
Run phase: <m> months × €9,000 + <d> architect days; customer approves changes
Must say in deck: a person (the customer's staff in run mode) approves every change; runs in your Snowflake (AI credits on your account); fixed <m>-month term
```

## Do not

- Do not offer the VDE on non-Snowflake stacks as if it runs there today.
- Do not include the VDE without the architect days. Without clear architecture and conventions, it builds the wrong things faster.
- Do not claim the VDE replaces people or works unsupervised. Every change goes through a person.
- Do not hide the Snowflake AI credit consumption. It's on the buyer's account.
- Do not count the VDE fee as hours. The rate minimums (price-check) apply to human hours only.
- Do not add the VDE for a buyer who punished AI extras unless the RFP itself asks for AI-assisted delivery.
