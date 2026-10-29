Buyer: city-of-helsinki | Project: city-of-helsinki-sme-reporting-platform
(Pricing out of scope. Evidence: RFP in work/buyers_now.json, draft team/decks/city-of-helsinki/...-v2.md, team/buyers/city-of-helsinki.md)

Regimes:
- Public procurement (hankintalaki 1397/2016): equal treatment, transparency <- "considerable council scrutiny regarding past digital engagements that carried heavy markups for global agency letterheads"; "transparent price breakdown" (named/implied)
- Mandatory criteria as exclusion tests <- "on site in Helsinki at least 2 days a week"; "firm and binding for 9 months from proposal submission" (named). A bid missing either can be rejected.
- Openness of Government Activities (julkisuuslaki): contract and bid become public; business secrets must be marked (implied)
- GDPR and Data Protection Act, municipal registers; SME records may include sole traders' personal data <- "enterprise records from SAP S/4HANA Cloud" (implied)
- Information Management Act (tiedonhallintalaki) and public-sector security practice (Julkri/VAHTI-style) (implied; no classification claimed)
- Contractor's Obligations Act (tilaajavastuulaki) documents (implied, standard in Finnish public contracts)
- EU AI Act: not triggered (draft excludes AI)
- City's standard purchase agreement <- replies: "swallowing the City's standard purchase agreement whole without sneaking in contract deviations" (named)

Supplier obligations -> our answer:
- Standard agreement accepted as published, no tracked changes (draft). Ok.
- Price binding 9 months from submission (draft s1, s4). Meets mandatory criterion.
- Transparent pricing: days x rate card (draft). "No markup" is true only if the rate card is the whole contract price list: say "rate card; no separate fees or surcharges" only if so.
- On site: whole team on site Tue and Thu; staff use City-issued access, comply with City security rules; laptops per City policy (verify).
- Data access -> read-only released CDS views/OData; City-issued accounts, least privilege, row-level security per unit in BI (draft s2). GAP: add City-side access logging, access removed at close, no production data copy outside the City tenant, build inside the City's cloud tenant in the City's chosen EU region.
- Personal data -> City is controller; we process under the City's terms/DPA; masked data in dev where possible.
- Subcontractors -> none; add one line (employees only, changes need City approval).
- Catalogue and lineage (draft step 4) supports traceability; do not call it "compliant".
- Public disclosure -> mark business secrets; assume the rate card is public.
- Finnish documents: draft.

Matrix (mandatory criteria and asks):
- On site >= 2 days/week: Yes if roster can cover Tue+Thu for all three (draft's own open risk)
- Prices firm 9 months: Yes
- Technical solution: Yes
- Implementation plan: Yes
- Team qualifications: Yes if roster and certs verified
- Transparent price breakdown: Yes
- Standard agreement: Yes
- Data stays in City environment: Yes
- Row-level security: Yes if the BI tool supports it (tool unnamed; Power BI, Looker, Tableau do; confirm week 1)
- Accessibility rules for public-facing dashboards: not included (internal reporting assumed)

Cannot promise (verify):
- Certs (Azure DE Associate, Databricks DE Pro, PL-300, Fabric Analytics Engineer, TOGAF 9) -> roster only; Databricks cert irrelevant to an unnamed stack, remove unless the City uses it.
- "11 yrs SAP S/4HANA Cloud extraction", "public-sector self-service" -> placeholders. Profile: SAP as a source is Solid, public sector credible. Verify named people.
- Tilaajavastuu/Vastuu Group status, insurance, tax debt certificate, any security clearance -> not in profile. Wording: "We supply the statutory contractor-obligation documents with the formal tender" only once verified.
- Historical automation benchmark metrics -> none; do not invent.
- ISO 27001 -> not held; do not mention.

Unsupported claims in draft:
1. "Whole team on site every Tue and Thu": ties to a mandatory criterion, not backed by roster. If untrue it risks exclusion or later breach. Safer: "at least 2 days a week on site, whole team in weeks 1-2".
2. "One rate card, no markup": see above.
3. Databricks cert for an unknown stack.
4. "No deviations" on SME-specific terms we have not seen: say "accepted as published".

Gate before build: week 1-2 discovery go/no-go exists (source probing). Add security precondition: City-issued access (SAP read roles, cloud tenant, security briefing and NDA signed) confirmed before any extraction runs.

Slide additions: keep to 4 slides (buyer wants <5). Add one row to the s2 table: "Access: City-issued, read-only, row-level security, no data copy outside City tenant", and one line on s3: "No subcontractors".
