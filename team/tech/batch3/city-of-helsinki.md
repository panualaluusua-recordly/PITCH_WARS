Buyer: city-of-helsinki | Project: city-of-helsinki-sme-reporting-platform
(Brief tech analysis by solution-architect, 2026-10-29. Sources: work/buyers_now.json RFP + bio + replies,
team/buyers/city-of-helsinki.md, work/compliance/city-of-helsinki.md, team/tech/reviews/ville-drafts-tech-review.md.)

Stack: SAP S/4HANA Cloud ("unify enterprise records from SAP S/4HANA Cloud and its current data setup");
"a BI tool running in a public cloud"; company_cloud_vendor "a public cloud"; bio "migrating core workflows to SAP
S/4HANA Cloud and modernizing municipal data assets".
Unknown: the "current data setup" (warehouse/lakehouse product), the BI tool, the cloud vendor, SAP extraction
route already in use (released CDS views / OData / existing integration), repo and CI/CD, catalog tool, how
access is managed per unit. All are Phase 0 (week 1) work, not guesses.

Triggers:
- P3 data foundation first <- "legacy pipeline quirks crop up constantly once you start touching raw tables" (high);
  praised before: "front-loading the engagement with an initial source-probing sprint ... avoids deploying on quicksand"
- P4 small blast radius / phased <- "committing to an unyielding lump total feels far too rigid when discovery
  shifts the work" (high; commercial answer exists, tech answer = KPIs ranked at the gate, lowest move out first)
- P15 findability <- earlier project: "uneasy about how anyone will actually locate and make sense of all these
  pipeline outputs" -> won with catalog/lineage (high)
- P5 access inherited <- "self-service analytics" across SME services units + council scrutiny (medium); RLS per unit
- P6 code in client tenant <- "pairing directly with our internal developers" praised; "inherit technical debt we
  cannot maintain" (high)
- P7 use what they own <- "its current data setup", "a BI tool" (no new platform asked) (high)
- Candidate new pattern: "council scrutiny ... heavy markups" is commercial, no tech pattern.

Hard constraints:
- On site in Helsinki >= 2 days a week ("must account for the following mandatory criteria") - not tech, flagged.
- Prices firm 9 months - not tech.
- Build on the City's SAP S/4HANA Cloud + current data setup + BI tool in a public cloud; no new licences.
- Compliance (work/compliance): City-issued read-only access, no data copy outside City tenant, access removed at
  close; gate before extraction: access + NDA + security briefing confirmed.

Traps:
- Unnamed stack -> do not name Azure/Databricks/Power BI as theirs; "confirmed in week 1".
- Legacy quirks -> gate with pass criteria (KPIs trace to raw tables, row counts reconcile, issues sized).
- SAP clean core -> released CDS views/OData, no custom ABAP in S/4HANA Cloud.

Praised/punished before (same buyer):
- Praised: standard agreement as is; source-probing sprint + go/no-go; pair programming from week 1; Finnish
  runbooks; catalog/lineage; no AI hype.
- Punished: full pipelines before integration issues isolated; >5 slides ("razor-thin technical briefing");
  knowledge sharing only at the end; monolithic fixed sum.
- Not addressed in won review: "does not cite historical or benchmark pipeline automation metrics"; honest_unknowns
  only adequate: "broader technical platform dependencies are lightly addressed".

VDE: NO (no Snowflake + dbt named).

Effort drivers: number of SME KPIs and SAP objects behind them; quirks found in raw tables; whether the earlier
squad's pipelines/conventions can be reused; BI tool RLS mechanics; catalog tool present or not.
Effort basis (existing v3 split, unchanged): discovery weeks 1-2 = 11 person-days; build + rollout weeks 3-10 =
35 person-days (cap). Not a price.
