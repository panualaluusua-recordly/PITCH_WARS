Buyer: alko | Project: alko-master-data-quality-and-duplicate-cleanup
Stack: "an ERP system, its current data setup, and a BI tool operating on a public cloud" (RFP); bio: "connected an ERP system to a BI tool"; company_cloud_vendor: "a public cloud". No product, vendor or cloud is named.
Unknown: ERP product and version; "current data setup" (DW / lakehouse / flat extracts); BI tool; which public cloud; where item and supplier masters are mastered (ERP only, or also PIM/supplier portal); record volumes; existing duplicate rate and existing validation; ERP change process and whether merges can be written back or must go through ERP admins; Alko's repo/CI platform; the notification channel ("a chat tool" is the only hint); whether a Snowflake/dbt is in use (VDE check below).

## Triggers
- P3 <- "audit registries, eliminate redundant records" and bio "master data quality and duplicate cleanup" (confidence high). Phase 0 = audit and a go/no-go gate before cleanup.
- P2 <- "implement automated validation routines" + bio "reviewing every query parameter herself" (confidence medium). Automated rules, but every merge is proposed and approved by a person; no auto-merge. Not a literal AI trigger, but the same human-gate answer fits.
- P15 <- "audit registries" + "accurate item and supplier master data is critical for our operations across an ERP system, its current data setup, and a BI tool" (confidence medium). Rule book, data dictionary and a merge audit table are the findability deliverables.
- P6 <- bio "reviewing every query parameter herself" (confidence medium). Code and rules in Alko's repo, read access from day 1, so she can inspect it.
- P7 <- "operating on a public cloud" with no new tooling asked (confidence low). Build on what they have; no new licences.
- P4 <- bio "high-impact transformation" vs a fixed audit-first scope (confidence low). Item + supplier masters first, other masters only after the result.
- Not triggered: P1, P5, P8-P14, P16 (no sovereignty, freeze, latency, DV, streaming or edge text in the RFP).

## Hard constraints
- Deliverable list the deck must cover: "aims and background, recommended technical solution and deliverables, implementation plan and timeline, allocated team profiles including certifications and availability, and total pricing model, along with any formal contract deviations" (RFP; the technical part of this is "recommended technical solution and deliverables").
- Three technical outcomes: "audit registries, eliminate redundant records, and implement automated validation routines" (RFP).
- Scope is item and supplier master data: "accurate item and supplier master data" (RFP).
- Must work with the existing landscape: "ERP system, its current data setup, and a BI tool" (RFP). No new platform asked.
- Language of workshops and manuals is Finnish: "watched retail floor rollouts stall when project workshops and manuals were delivered in English" (bio). Applies to the rule book and runbooks too.
- Buyer inspects the logic: "Known for reviewing every query parameter herself" (bio).

## Traps
- "Automated" cleanup of records in the ERP -> Honest answer: automation is detection and validation; merge decisions are approved by a person and logged; nothing is deleted; every merge is reversible. Enfuce was won on exactly this ("deterministic rule-based matching with an audit table and reversible merges").
- "Eliminate redundant records" implies a duplicate rate and ERP write-back that nobody knows -> Honest answer: duplicate rate and write-back route are Phase 0 findings; scope of the cleanup is set at the gate after the audit (P3). Fingrid objected to going on while "ledger records and duplicate entries ... remain unaddressed".
- Fuzzy matching sold as a certainty -> Honest answer: exact keys (EAN/GTIN, Y-tunnus, IBAN) give confident candidates; similarity matches only go to a review queue; thresholds are agreed with her and tuned on a labelled sample from her own data.
- Product-domain false merges (same wine, different vintage or pack size) -> Honest answer: explicit never-merge rules, shown in the rule book.
- "High-impact transformation that stands out" -> Honest answer: show measurable before/after quality numbers from their own data, not a platform rebuild or AI extras. AI/ML is out of scope and was punished elsewhere (Aktia lost).
- Cloud/BI/ERP unknown -> Honest answer: say so, do not invent a stack. Any tool name that Alko did not state must be marked "proposed" or "if you use it".

## Praised/punished before
- Rule-based matching, audit table, reversible merges in enfuce (won): "Slides 4 and 10 commit to deterministic rule-based matching with an audit table and reversible merges." (rated "partly met" for that preference: be explicit about the audit table, the merge/unmerge procedure and who approves).
- Dedup first in enfuce (won): "Tackling cardholder deduplication out of the gate is dead on after the identity trash that corrupted my tables".
- Source-probing/audit first in city-of-helsinki (won): "front-loading the engagement with an initial source-probing sprint to validate registers before building production pipelines, which avoids deploying on quicksand".
- Audit-lineage in city-of-helsinki (won): "audit-ready lineage".
- Data foundation before deliverables in fingrid (punished when skipped): "proceeding straight into automated reporting deliverables while our underlying ledger records and duplicate entries ... remain unaddressed leaves me uneasy".
- Full roadmap before the data is known in ponsse (punished): "committing to an entire implementation package from day zero rather than de-risking the data".
- Alko has no replies yet (conversation is empty), so there is no direct evidence on this buyer.

## VDE
VDE: NO. No Snowflake and dbt is named ("a public cloud", "current data setup"). The vde-check only applies to Snowflake + dbt; revisit if Phase 0 finds Snowflake.

## Effort drivers
- Audit size: the number of records and sources of item and supplier masters, and how much profiling needs ERP access (the largest unknown).
- Review-queue volume: the number of similarity matches that need her review; the labelled-sample tuning rounds scale with it.
- ERP write-back route: if merges go through ERP admins the effort is a hand-off list; if there is an API or load tool it needs testing and rollback.
- Number and complexity of validation rules (the deck says 10), and how they are run in Alko's environment (unknown until Phase 0).
- BI scorecard: depends on the BI tool and a place to store quality metrics.
- Finnish rule book, runbook and training material.
- Access lead time: repo and data read access on day 1 is the schedule risk.

## Notes for deck owner (Ville)
1. "Koodi Alkon repossa, lukuoikeus päivästä 1": the repo is not named in the RFP. Say "Alkon omassa repossa ja ympäristössä" and note we do not know the platform. Fine as is, but do not imply a repo already exists with a CI.
2. "10 automaattista sääntöä ajetaan joka latauksella": we do not know there is a load process. Reword to "ajetaan Alkon olemassa olevassa latauksessa tai ajastettuna, tarkennetaan vk 1" (unknown, Phase 0).
3. Slide 3 says "Sääntöpohjainen, ei koneoppimista" and that similarity thresholds like 0.85 / 0.9 are in rules. Similarity scores are themselves computed by a string metric (e.g. Jaro-Winkler or trigram), so name the metric as "ehdotus" and say thresholds are tuned on a labelled sample from Alko's data. The 0.85 and 0.9 are labelled "esimerkki"; keep that.
4. Missing: how a merge is undone. Reversibility is claimed ("kaikki palautettavissa") but not explained. Add one line: merge proposals and decisions stored in an audit table (who, when, rule, before/after values, survivor record), and an unmerge procedure. This is what enfuce rated "partly met" and what a reviewer of "every query parameter" will look for.
5. Missing: the survivorship rule (which record's attributes win in a merged record) and handling of references from other tables or the ERP (open orders, price lists, supplier contracts). A duplicate is not cleaned if downstream references still point at it. Mention as a Phase 0 question.
6. Missing: no architecture diagram. T1 and the reviews (Aktia, Enfuce: "architecture diagrams are omitted") say a diagram is scored. The stack is unknown, so draw it as a flow with unnamed boxes: sources (ERP item and supplier masters) -> audit and matching in Alko's environment -> review queue (approval) -> merge list to ERP change process -> validation on load -> quality metrics -> BI scorecard. Mark ERP/BI/cloud as "Alkon oma".
7. Missing: access and data protection. Supplier masters include IBAN, addresses and possibly sole-trader names; the work runs in Alko's environment under Alko's access model (P5-style: no copies out of their tenant). One line is enough; this is a gate question for Phase 0, not a compliance workstream.
8. Slide 5 team: "tiimi kattaa kolme suurta pilveä" is a claim about the team, not the technical design; the claims-auditor should confirm the certifications. Not my lane beyond that.
9. "Mikään sääntö ei aja ilman hänen hyväksyntäänsä" is good and matches P2. Keep, but make sure validation rules (read-only checks that raise alerts) are distinct from merges (which change data); only the latter need her approval, otherwise validation is blocked by approvals.
10. Gate 1 at week 2 is the correct de-risking step (P3, P4). Consider listing the Gate 1 decision inputs: duplicate rate by domain, share of exact-key vs fuzzy candidates, ERP write-back route confirmed, labelled sample accuracy. These are technical, so they are ours.
