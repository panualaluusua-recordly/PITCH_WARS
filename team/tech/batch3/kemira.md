Buyer: kemira | Project: kemira-hands-on-agentic-ai-hackathon-for-an-internal-te
Stack: "SAP S/4HANA, SAP Datasphere, and SAP Analytics Cloud within Microsoft Azure", "coordinating via a chat tool" (bio: company_cloud_vendor "Microsoft Azure"; channel "a chat tool", product unnamed)
Unknown: Azure model endpoint/service and region approved by Kemira; how agents reach Datasphere (OData / SQL / views exposed to which identity); whether Datasphere data access controls apply per user or a service identity; chat product (Teams is an assumption, RFP does not name it); repo host ("your repo"); sandbox data (one plant space vs masked extract); participant count and skill level; lead time to approve Azure resources; where run logs are stored; what the earlier pilot actually stalled on technically.

Triggers:
- P2 ← "struggled after an external partner glossed over edge-case constraints and overpromised autonomous resolution across enterprise SAP data" (high)
- P5 ← prior win: "Directs that Azure AI outputs and SAC access inherit role-based permissions from SAP authorisations" and "downstream access governance still feels a bit too loose" (high)
- P13 ← "reviewing candidate use cases through static slides makes me distinctly uneasy"; "[leans against] ... a slide deck ... rather than a live demo on our water treatment data" (high); RFP wants "hands-on ... prototype" (medium)
- P7 ← "no new platforms or licences"; "shiny new software licenses we do not need" (high)
- P8 ← "fiercely safeguarding resources" (bio) plus model usage on their Azure subscription (low-medium; cost cap is our addition, not asked)
- P3 ← "messy, day-to-day water treatment flows" and edge cases in SAP data (medium; as a light data-access/quality check in prep, not a phase 0 programme)
- P4 ← prototype scope: one plant's Datasphere space first (medium, own design)
- P1 ← none in RFP or bio (not triggered; do not add)
- P9, P10, P11, P12 ← none found

Hard constraints:
- Platform: SAP S/4HANA + Datasphere + SAC on Azure ("within Microsoft Azure"); no new platforms or licences ("no new platforms or licences" earlier review)
- Deliverables: "comprehensive slide deck covering ... proposed technical approach and deliverables, implementation plan, team credentials and availability, and total pricing"
- Agents are "autonomous agent workflows" in the ask, but the buyer's history demands honest limits ("overpromised autonomous resolution")
- Access: SAP authorisations must carry through to anything the agent shows (Kemira v4: "downstream access governance still feels a bit too loose")
- Location: global function, event in Helsinki ("function in Helsinki")
- Contract items (standard agreement, 12-month hire right) are not ours; noted only so tech does not contradict them

Traps:
- "Autonomous agent workflows" prototyping vs the earlier failure → honest answer: agents read governed data and propose; person approves; no write-back to SAP; measured edge-case results reported with misses. (P2, T3)
- "Connecting S/4HANA, Datasphere and SAC" invites a wide integration → read certified Datasphere views and SAC KPIs only; direct S/4HANA connection out of scope.
- "Prototype across enterprise SAP data" → one plant's space first, scale only after test results (P4).
- Production chat bot hidden in "coordinating via a chat tool" → test channel only; production bot needs their IT approval.
- Hackathon outputs mistaken for products → each prototype gets a go/no-go note; code cleaned in their repo, not production hardened.
- Unknown sources/data access → honest: masked extract fallback, said on the day.
- Side quests (docs assistant, CSRD) punished earlier ("side quests like text assistants for product documentation") → keep workflows to SAP/Datasphere/SAC analytics.

Praised/punished before:
- P5/P7 in kemira (v5 won): "Builds strictly on Kemira's existing SAP and Azure estate with no new platforms or licences."
- P5 in kemira: "Directs that Azure AI outputs and SAC access inherit role-based permissions from SAP authorisations." (met)
- P5 partly: "Specifies row-level security by plant and region in SAC stories ..." (partly met)
- P13 in kemira: "Presents a slide deck outlining a future proof of value rather than a live demo on our water treatment data." (leans against)
- Anti-pattern in kemira: "side quests like text assistants for product documentation and broad corporate sustainability filings"
- Diagram evidence elsewhere: Aktia "an architectural diagram is conspicuously absent"; Enfuce "architecture diagrams are omitted"; kemira got "explanatory_visuals strong" with structured tables, so a diagram is a plus but tables are acceptable to this buyer.
- Same-pattern buyers (P2): Terveystalo praised human-gate design; Aktia lost on AI extras; Sanoma/Pirha pending, no replies used here.

VDE: NO (no Snowflake + dbt; SAP/Azure event work)

Effort drivers:
- Prep is the big one: read-only access to one plant's Datasphere space and a seed agent depend on access approval time (the unknown with the highest schedule risk); masked-extract fallback shrinks it.
- Hackathon size: participants 12-16 (assumed) in 4 teams; number of workflows built, 3-4.
- Seeded edge-case test set: its size and who labels truth (Kemira data owners) drives follow-up effort.
- Per-user access propagation to Datasphere (inherited authorisations) is harder than a service account; if not possible, fall back to test users per role.
- Cost scales with Azure model usage on their subscription, with a cap per team.
- Follow-up: code cleanup and edge-case registers per prototype.

## Notes for deck owner (Ville)
1. No architecture diagram (T1). Slide 2 is a table only. Add one box-and-arrow: Datasphere certified views / SAC KPIs -> read-only access layer (per-user authorisation) -> agent (Azure, their model endpoint) -> propose -> person approves -> chat test channel; run log alongside. Kemira scored tables "strong" last time, so it is optional, but it was the lowest-cost gap in other buyers' reviews.
2. Access claim is stronger than we know. "Access inherited from SAP authorisations, row-level by plant" holds only if the agent queries Datasphere with the user's identity (or per-role test users); a shared service account bypasses Datasphere data access controls. State the mechanism as a prep decision and list it under unknowns, otherwise the buyer who said access "feels a bit too loose" may find the gap.
3. Slide 3 row "Unit or currency mismatch between S/4HANA and Datasphere" contradicts slide 2 (agents read only Datasphere views, never S/4HANA). Reword to "between Datasphere views / SAC measures" or state that S/4HANA is not read directly.
4. "Rows the user may not see ... says why": saying why can reveal that restricted rows exist. Reword to "states that results are limited by the user's authorisation" without counts.
5. "Live demo on day 1, hour 1" depends on data access within weeks 1-3 plus an Azure model endpoint. Fallback exists in the unknowns line (masked extract), but slide 4's headline presents it as certain. Soften or mark conditional (confidence on access: unknown).
6. "Sensitive fields masked before any model sees them": say who defines the field list (Kemira data owner, in prep) and that masking runs in the read layer; otherwise it reads as unproven.
7. "Working prototypes" in two days by participants: honest label is hackathon prototypes on a sandbox with a go/no-go, not production. The deck says go/no-go already; add "sandbox data, no production use".
8. Missing tech risks list (T5): model endpoint lead time, access approval lead time, free-text fields in master data feeding the agent (content could carry instructions; treat field text as data, not commands), dependence on Kemira staff for ground truth in the edge-case set. Slide 4's three unknowns cover the first two only.
9. Edge-case scoring: "resolved, escalated, and wrong" is good. Do not fix pass thresholds before measuring; say "targets agreed after the first measured run" (anti-pattern from oriola v1).
10. Name only what the RFP names: the chat tool is correctly unnamed; "your chat tool" is fine. "Azure subscription" and "model endpoint Kemira already approves" are fine; do not name Azure OpenAI/Foundry/Copilot Studio unless the buyer does.
11. Run log: say where it is stored (their Azure subscription, their repo/storage), consistent with "all code and results are Kemira's property".
