# Tech critic: savings-banks-group, deck v2 (2026-10-29)
Scope: technical content only. No price, names, terms, storyline or style. Game API not called.
Sources: deck v2 .md, team/tech/slides/savings-banks-group.md/.json, RFP and bio from work/buyers_now.json.
No team/buyers/savings-banks-group.md exists. There are no buyer replies yet.

## Verdict: adequate (close to strong)
Every technical ask in the RFP has a slide. The stack matches what the buyer stated: Snowflake on Azure,
Power BI and Temenos. The non-European AI toolchain trap is handled honestly. Three method gaps remain.
A sceptical, process-first architect would probe each of them.

## Top 3 tech fixes, most valuable first

1. Slide 3 (and phase row in slide 2): say how cost is attributed to a bank, and how it is validated.
   Evidence: "establish the central Snowflake and Power BI reporting stack across member banks";
   deck: "Unknown until the baseline: how much cost can be attributed to a bank automatically".
   Problem: shared warehouses, serverless features and Power BI capacity do not split cleanly per bank.
   An unknown with no method reads as a risk.
   Change, replace the third bullet with:
   "Attribution: query and role tags where warehouses are per bank; usage-based allocation where shared. Remainder goes to a
   visible 'unallocated' line. Definition reports the unallocated % and you approve the allocation rules."
   Add to the Definition gate: "Baseline = at least 3 months of usage, read-only roles, signed off by you."

2. Slide 4 (Budgets, monitors row) and slide 2 (Delivery): make guardrails safe for production reporting.
   Evidence: "Cautious, he prioritizes process adherence over innovation"; deck: "Resource monitors", "Auto-suspend".
   Problem: a resource monitor that suspends a warehouse can stop member-bank reporting. Nothing says this is controlled.
   Change, add under the table:
   "Guardrails go live in two steps: alert-only for 2 weeks, then enforce. Hard suspend is used only on non-production
   warehouses. Every change is code in your repo, reviewed by your change board, and has a rollback."
   Also add one line on access needed: "Read-only access to Snowflake account usage, Azure Cost Reader and Power BI capacity
   metrics in Definition. Write access only in Delivery, on approved changes."

3. Slides 2, 3 and 4: define what "pipelines tied to non-European AI toolchains" means, and the boundary of the fix.
   Evidence: "compliance exposure when examining operational pipelines tied to proprietary non-European AI toolchains".
   Problem: slide 4 lists the inventory, but not how it is found or what happens next. Slide 4 also says "Out of scope:
   re-platforming" while slide 3 promises "replaced or documented with an exit plan". Replacement could be large.
   Change, replace the slide 3 first bullet's second sentence with:
   "Inventory method: scan Snowflake external functions, integrations, tasks and query history, plus Azure app
   registrations and egress. Each finding is classed as remove, replace or exit plan. Replacement of a pipeline
   larger than 2 days is scoped as a change request after Definition."
   Also state that the inventory record feeds the DORA register-of-information entries.

## Minor notes
- Slide 5: the Snowflake AI services limit is stated honestly and is conditional on board approval. Keep it.
  The Snowflake model-hosting region needs a one-line check in Definition. The deck already says "confirmed in Definition".
- Slide 3: the diagram label for Power BI "capacity metrics" assumes a capacity SKU. Add "or Premium Per User" only
  if confirmed in Definition. The deck does not claim this today, so it is an optional note.
- Slide 4: "Savings measured against the baseline" needs a normaliser (credits per workload unit, not raw credits),
  or growth will hide savings. One phrase in the Delivery gate is enough.

## Already good
- The stack is the buyer's own. No new tools or licences. The deck says so on slides 3, 4 and 5.
- P10 honesty: no savings percentage quoted, "Honest unknown" box, VDE results labelled "None of these is a FinOps saving figure".
- Phases have gates. The buyer can stop after Definition, which suits the cautious bio and the restructuring.
- The mapping table that re-points costs when banks integrate answers the restructuring hint directly.
- The AI agent boundary is clear: agents open pull requests, never approve or merge, and keep an audit trail.
- The VDE option sits outside the total, and the human-led path is the default.
- Out-of-scope list is explicit (Temenos feeds, re-platforming) and the change board path is on slide 4.
- The architecture diagram follows sources, model, guardrails, reporting, with the "as code" and "reviewed" arrow labels.

## Missing technical answers
None missing outright. Attribution method, guardrail rollout safety and toolchain inventory method are thin (fixes 1 to 3).
