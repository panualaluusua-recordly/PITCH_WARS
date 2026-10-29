# Tech & architecture slides for the Kemira hackathon deck
_Kemira Oyj: Two slides: architecture replaces the 'Technical approach' table; gates & risks replaces the plan slide_

## 2. Agents read your governed SAP data and propose; a person decides. Nothing new to license
- Read-only on **certified Datasphere views** and SAC KPIs, one plant's space first. S/4HANA is reached only through those views, never queried directly.
- Queries run **as the signed-in user** (no shared service account), so SAP plant authorisations apply unchanged. If Datasphere cannot take per-user identity in time, per-role test users: decided in prep week 1.
- Every proposal goes to a person with Approve/Reject in a **test channel** of your chat tool. Nothing is written to SAP. Removing the agent's role stops all runs.
[Your SAP data (read-only): Certified Datasphere views: one plant's space first, SAC KPIs] → [Access layer (your Azure): Runs as signed-in user or per-role test user, Short read-only tool list you review in prep, Masks the fields your data owner lists] → [Agent (your Azure subscription): Model endpoint you approve, Step and token cap per run, Field text treated as data, not instructions] → [People decide: Proposal in chat test channel, Data owner: Approve / Reject, Nothing written to SAP]
(Run log (input, tool calls, answer, approver) in your Azure tenant; code in your repo. No new platform, no new licences)

## 3. Every phase ends in a measured gate; misses are reported, not hidden
| When | Technical gate | Pass criterion |
| --- | --- | --- |
| Prep, week 2 | Access check | A restricted test user sees zero rows outside its plant authorisation; model endpoint reachable from your subscription |
| Prep, week 3 | Seed agent, first measured run | Edge-case set from one plant (labelled by your data owners), each case run 5 times: resolved, escalated, wrong. Targets agreed with you after this run, not before |
| Hackathon, day 2 | Prototype test | Counts as working when it meets the agreed targets on the seeded set; zero access leaks; unmet items listed |
| Follow-up | Go/no-go per prototype | Real numbers incl. misses, token cost per run, "tested on one plant only" |

_Technical risks, closed in prep: (1) access and model-endpoint approval lead time; fallback is a masked extract, said on the day; (2) per-user identity into Datasphere; fallback per-role test users; (3) free text in master data could carry instructions; agents only have read-only tools and treat it as data; (4) ground truth needs your data owners' time to label the set. Tests re-run on every prompt, model or tool change; a worse wrong-answer rate blocks the change. Per-team token cap and Azure budget alert._
