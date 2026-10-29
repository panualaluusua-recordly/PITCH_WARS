# Tech slides for City of Helsinki · SME reporting platform: rationale

Spec: `team/tech/slides/city-of-helsinki.json` (deck.py format, copy at `work/specs/city-of-helsinki-tech.json`,
preview `work/tech/city-of-helsinki-preview.pdf`). Analysis: `work/tech/city-of-helsinki.md`.

**No extra slides.** Kari wants fewer than 5 slides ("razor-thin technical briefing"; won review: "leans against"
seven slides). In deck v4, the architecture diagram replaces the slide 2 table, and the gates go into the slide 3
plan table. The deck stays at 4 slides.

| Element | Pattern | Evidence |
| --- | --- | --- |
| Diagram: extract → model → serve → find, each step with "Done when" | T1, P7 | RFP: "unify enterprise records from SAP S/4HANA Cloud and its current data setup ... a BI tool running in a public cloud" |
| Released CDS views / OData, no custom ABAP | P7 | Bio: "migrating core workflows to SAP S/4HANA Cloud" (clean core) |
| Reuse conventions from the earlier squad work | P6 | Reply: "you already know your way around our infrastructure" (tech-critic fix 2) |
| Row-level security per unit plus an access test per unit before go-live | P5 | Self-service across units; tech-critic fix 3 |
| Catalog: owner, Finnish description, refresh, lineage | P15 | Won earlier on it: "how anyone will actually locate and make sense of all these pipeline outputs" |
| Access band: City-issued read-only accounts, repos and tenant, no copy outside, access removed at close | P6, compliance | `work/compliance/city-of-helsinki.md` |
| Week-1 access + NDA before extraction; week-2 gate with pass/fail | P3 | "legacy pipeline quirks crop up constantly once you start touching raw tables"; praised "source-probing sprint" |
| KPIs ranked at the gate, lowest-ranked move out first | P4 | "an unyielding lump total feels far too rigid when discovery shifts the work" |

The diagram names only products the RFP or bio names. Everything else is "your current data setup", "your BI tool"
or "your catalog", confirmed in week 1.

**Left out on purpose:** AI features, new platforms or licences, streaming, Data Vault, VDE (there is no Snowflake + dbt), and
benchmark automation metrics (we have no real figures).
