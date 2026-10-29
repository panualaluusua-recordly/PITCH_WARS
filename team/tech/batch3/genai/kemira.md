Buyer: kemira | AI in scope: yes <- "prototype autonomous agent workflows connecting SAP S/4HANA, SAP Datasphere, and SAP Analytics Cloud within Microsoft Azure" and "an external partner glossed over edge-case constraints and overpromised autonomous resolution across enterprise SAP data"
Project: kemira-hands-on-agentic-ai-hackathon-for-an-internal-te (prototype event, not production)
Autonomy: proposes, human approves. Never automated: any write-back to S/4HANA or Datasphere, master-data changes, access changes, posting to a production channel, any answer for rows the user may not see.
Eval: edge-case set 40-60 cases seeded from one plant's Datasphere space (3-4 workflows x ~12 cases), labelled by Kemira data owners with our SAP architect as tie-break | metrics see section 3 | cadence: re-run on every prompt, model or tool change
Hosting: Kemira's own Azure subscription, EU region, model endpoint Kemira already approves (else the one IT approves), accessed behind a thin abstraction layer; Datasphere read-only, nothing leaves their tenant
Cost: unit cost per agent run measured during prep; per-team token cap; Azure budget alert
Known failure modes: see section 6
Left out on purpose: see section 7

## 1. AI scope and autonomy level
The RFP asks for agent workflows, so AI is in scope. The hackathon is a prototyping event, so the autonomy ceiling is "agent proposes, person approves". The buyer's own failure story is autonomy oversold plus edge cases glossed, so the deck must not use "autonomous resolution" as a claim. The candidate workflows in Ville's draft (DQ triage, KPI "why did it move" explainer, master-data anomaly queue) all fit a read-only, propose-only design. They are the draft's choice, not RFP asks: confirm in prep.

## 2. Human gate
- Agent proposes: a finding, an explanation, a queue entry or a question to a person. It writes only to a test channel.
- Approves: the named Kemira data owner of the affected plant/domain. Nothing is acted on until a person marks it accepted in the register.
- Never automated: SAP/Datasphere writes, master-data correction, authorisation changes, production bot, anything affecting dosing, ordering or financial postings.
- Escalate by default: missing/duplicate master data, unit or currency mismatch, stale data, conflicting sources, and any request the agent cannot ground in a certified view. It says so and hands to the data owner.
- Kill switch: removing the agent's service identity role (or one feature flag) stops all runs; written into the day-1 runbook. A hard per-run step and token limit stops a looping run.
- Audit: every run logs input, tool calls, answer, approver.

## 3. Eval plan
- Edge-case set: 40-60 cases (plan, confirm in prep). Sampled from one plant's Datasphere space: (a) real incidents the team remembers, (b) a random draw from certified views, (c) deliberately seeded faults (duplicate material, unit mismatch, late load, a plant the user may not see, ambiguous question). Labelled by Kemira data owners; each case has an expected outcome: resolve, escalate or refuse.
- Metrics. Targets are proposals; the numeric gate is agreed with Kemira after the first measurement on the seed agent, not fixed before:
  - Resolved-correctly rate on in-scope cases
  - Wrong-and-confident rate (the one we watch hardest; every miss is shown)
  - Escalation correctness: share of seeded faults escalated rather than answered
  - Access leaks: answers exposing rows outside the user's authorisation (tested explicitly with a restricted test user; any leak fails)
  - Stale-data disclosure: share of answers that state data age
- Regression: full set re-run on every prompt, model, tool or Datasphere-view change; diffed against the previous run; a worse wrong-and-confident rate blocks the change.
- Language: the RFP does not say which language users write. If Kemira staff query in Finnish, add ~10 Finnish questions to the set. Ask in the scoping call.
- Readout reports resolved, escalated and wrong with real numbers, including the misses.

## 4. Hosting and data
- Azure, EU region, in Kemira's subscription (P6). Model endpoint Kemira already approves, called through an abstraction layer so it can be swapped (P1).
- Agents read certified Datasphere views only; access inherited from SAP authorisations, row-level by plant. Sensitive fields masked before any model call. Logs stay in Kemira's tenant.
- Unknown until prep: which model endpoint exists in Kemira's tenant; if data access is late we use a masked extract and say so.

## 5. Cost model (token/compute cost only)
- Unit cost = (input + output tokens) x the approved model's price per token, per agent run, plus Datasphere query cost if metered. Not yet measured. Prep records tokens per run on the seed agent; the figure goes into the readout.
- Per-run token ceiling and per-team daily ceiling are set from that measurement. Azure Cost Management budget on the resource group with alerts at 50/80/100 %, key disabled at the cap. The deck already says "per-team cost cap agreed in prep": consistent.
- For a 2-day event the cap is per team (12-16 participants in 4 teams is an assumption in the draft).
- The go/no-go note reports cost per prototype and the extrapolated monthly cost if it ran continuously.

## 6. Known failure modes
- Confident wrong explanation of a KPI move -> every answer cites view, filter, data age and unit, so a reviewer can click through; counted in the register.
- Unit/currency or plant-scope mixup between S/4HANA and Datasphere -> agent refuses to compare and shows both values; a slip shows in the seeded set.
- Missing or duplicate master data treated as real -> flagged and escalated; misses show in escalation correctness.
- Stale data answered as current -> every answer states data age; a missing line is a defect.
- Permission leak -> tested with a restricted user; any leak fails the gate.
- Model or prompt change silently lowers quality -> regression run on every change.
- Prototype works on the seed plant, fails on another -> readout states "tested on one plant only".
- Agent loops or burns tokens -> step/token ceiling stops the run, logged.

## 7. Left out on purpose
Autonomous resolution, SAP write-back, production chat bot, new platform or licences, side projects (docs assistant, CSRD, which Rasmus disliked earlier), predictive/ML models, any accuracy figure before we have measured it.

## Ready slide text (paste)
Title: How we test the agents and keep people in control
- Agents read certified Datasphere views and propose. A named Kemira data owner approves. No write-back to SAP, no autonomous resolution.
- Every prototype is scored on a seeded edge-case set from one plant: resolved, escalated, wrong. The readout shows the real numbers, including the misses.
- The pass gate (for example share resolved correctly, wrong-and-confident rate, zero access leaks) is agreed with you after the first measurement on the seed agent, not fixed beforehand.
- Tests re-run on every prompt, model or tool change. A worse result blocks the change.
- Runs in your Azure subscription in an EU region, on the model endpoint you approve, behind a swappable layer. Nothing leaves your tenant.
- Token cost per run is measured in prep. Per-team cap, Azure budget alert and a kill switch.
