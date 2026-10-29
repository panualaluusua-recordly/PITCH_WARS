# Tech-lens review of Ville's drafts (2026-10-29, ~13:25)

Eight clean-context `tech-critic` runs, technical content only. Price, names, terms and style are other owners'.
Slide numbers follow each deck's own slide order (cover = 0). Each fix is ready to paste and quotes its evidence.

| Buyer, version | Verdict | Biggest gap |
| --- | --- | --- |
| kemira v1 | strong | How SAP authorisations apply to the agent |
| aktia v1 | adequate | Agent permissions and a pilot gate threshold |
| alko v1 | adequate | No flow diagram; merge mechanics unspecified |
| city-of-helsinki v2 | adequate | Gate pass/fail criteria; reuse of our earlier work |
| elisa v1 | adequate | "Yes, if" on real-time is not honest enough (P10) |
| sanoma v1 | adequate | Names Snowflake + dbt, which the buyer never did |
| veikkaus v1 | adequate | No architecture diagram |
| yliopiston-apteekki v1 | adequate | No architecture diagram; no tag inventory |

## kemira v1: strong
1. s1: "Identity: the agent queries Datasphere on behalf of the signed-in user (no shared service account), so SAP plant authorisations apply unchanged." Evidence: earlier reply, "downstream access governance still feels a bit too loose".
2. s2: "Go/no-go thresholds agreed in prep: zero wrong answers on authorisation cases; wrong-answer and escalation rates reported per prototype; each test case is run 5 times." Evidence: "overpromised autonomous resolution".
3. s3: "A prototype counts as working when it passes the seeded set on real Datasphere data; unmet items are listed." Evidence: "reviewing candidate use cases through static slides makes me distinctly uneasy".
4. s1: "Proposals appear in the chat test channel with Approve/Reject; the decision is logged; nothing is written to SAP."
5. s1: "Agents call read-only Datasphere views through a short, listed set of tools that Kemira reviews in prep."

## aktia v1: adequate
1. s3: "The agent has read-only access to the repo and the dev schema only, no production credentials, and cannot push to protected branches. Schema-dependency changes are blocked without data-owner approval." Evidence: "automated maintenance script that bypassed peer review and altered schema dependencies".
2. s6: "Pilot gate: merged-without-rework rate, test pass rate and review minutes per PR beat the Definition baseline; targets set at the week-3 gate; a miss means stop or adjust."
3. s4: "Model hosting is decided at the gate on 20 of your tickets. If the EU-hosted model falls short, the scope narrows to simple tickets. No external API." Evidence: "exposure to foreign-headquartered AI API dependencies".
4. s3: label the stack "assumed, confirmed week 1". Drop the Snowflake-credits line (the RFP names no Snowflake). Show the review and auditor agents as one review-and-log step.
5. Missing: rollback for a bad merge and DORA incident logging, run cost per ticket with a cap, ticket and git platform named as assumptions, audit-log location and retention.

## alko v1: adequate
1. s2: flow diagram "ERP + nykyinen dataratkaisu → profilointi → sääntömoottori (Alkon repo) → tarkistusjono (Katariina hyväksyy) → ERP-muutosprosessi → BI-laatumittaristo". Evidence: "Known for reviewing every query parameter herself".
2. s2: "Yhdistämisessä pääietue valitaan sovitulla säännöllä; viitteet ohjataan uuteen avaimeen; vanha avain säilytetään ja palautus testataan pilotissa."
3. s3: "Portti 2 (vk 5): 200 yhdistämisen pilotti ennen koko erää. Portti 3: validointi 2 viikkoa varoitustilassa ennen estoja."
4. s2: "Virhe → varoitus ja rivi karanteeniin, ei latauksen pysäytystä. Samankaltaisuusmitta ja raja-arvot Katariinan hyväksymät."
5. s3: "Edellytykset: lukuoikeus tuote- ja toimittajadataan vk 1; tarkistusjonon koko arvioidaan vk 2."

## city-of-helsinki v2: adequate
1. Plan, Discovery row: "Gate passes when 3 priority SME KPIs trace to raw SAP and register tables, row counts reconcile, and open data-quality issues are listed with sizing. On fail: re-scope or stop." Evidence: "legacy pipeline quirks crop up constantly".
2. Solution, Extract row: "Reuse the pipelines, access and conventions we built in the earlier squad engagement; no new tooling." Evidence: "you already know your way around our infrastructure".
3. Solution, Serve row: "An access test per unit before go-live; SAP authorisations mirrored, not reinvented" (P5).
4. Replace vendor-specific certifications (Azure, Databricks, Power BI, Fabric) with "certified on the stack confirmed in week 1"; "all code and IaC in the City's repos and tenant". Evidence: "a BI tool running in a public cloud" (none named).
5. Build row: "KPIs ranked with the SME team at the gate; the lowest-ranked move out first." Evidence: "an unyielding lump total feels far too rigid".

## elisa v1: adequate
1. s2: "Literal real-time for all data is neither achievable nor safe; finance close reconciles daily. We propose freshness SLAs per domain, confirmed at Gate 1." Evidence: "real-time access to all data… no batch". The deck's own tiers include batch (P10).
2. s3: "Measured proof: a Pub/Sub → BigQuery → Looker test on one real feed, end-to-end latency in seconds, plus ERP CDC feasibility." Evidence: "milestones locked in before testing… a small preliminary scoping exercise".
3. s2: "Power BI: DirectQuery on BigQuery for the live tier; import refresh only for the daily tier." Power BI is in their stack without a mechanism.
4. s3: Phase B scoring adds streaming cost and quota per domain, Composer load, and query cost on live data.
5. s3: "Name the ERP and its CDC options; if none, API polling at 1–5 min, shown to the steering group."

## sanoma v1: adequate
1. s1: replace "runs inside your own Snowflake with dbt" with "Built on your stack, in your repository and merge-request tool; we name tools only after day 1 confirms them". Evidence: "current data setup hosted on a public cloud" (§7 anti-pattern). Use "merge request".
2. Human oversight: "Agent access: dev schema only, read-only on production metadata, no PII samples, a run-cost cap per ticket, all runs logged."
3. Human oversight: "An edge-case test set built from your past failed tickets at the hackathon; the agent is scored on it before each pilot phase." Evidence: "promised zero defects only to fail on basic edge cases".
4. s1: "12 h → 30 min on one pipeline in one Recordly project. Not a promise for your tickets; the pilot measures yours."
5. Plan: "The hackathon records the baseline lead time. Phase 2 gate: the agent drafts ≥ X of sample tickets to your reviewers' standard, with X agreed on day 2." Merge the review and auditor agents into one reviewer plus a run log.

## veikkaus v1: adequate
1. s1: architecture diagram: cloud data platform → in-house AI platform → BI → ERP, with a model path train → approve → deploy and the evidence point for D1–D3. Evidence: "assess how they fit together and how models reach production".
2. s1: D4 throughput row: "Measure peak load and batch/stream lag from task logs; streaming only where it pays, with the cost per tier" (P10). Evidence: "high-throughput data processing are paramount".
3. s2: week-4 gate: "≥80% of commitments have usage data and ≥10 debt items are log-evidenced; otherwise re-scope before phase 3" (P13). Evidence: "demanding tangible proof over vendor promises".
4. s2: "Week 1 vendor-neutral checklist; D4 patterns written for the platforms found."
5. "Roadmap changes are proposed, never applied; cut-overs get a human approval gate." Missing: AI-platform rollback and monitoring; cost guardrails in the target-state scoring.

## yliopiston-apteekki v1: adequate
1. s1: current-state diagram "ERP → nykyinen dataratkaisu → BI, julkinen pilvi; verkkoapteekki → palvelinpuolen keruu (selaimeen ei skriptejä)", unknown boxes marked "vahvistetaan vk 1".
2. s1: three target architectures in one diagram (lähteet → keruu → tallennus → BI, with where access control sits) and "Jokainen vaihtoehto läpäisee poissulkevan kriteerin: ei selainpuolen tunnisteita." Evidence: "hypersensitive to front-end browser telemetry".
3. s1: "Tunnisteinventaario: kaikki nykyiset selainpuolen skriptit ja pikselit listataan ja merkitään poistettaviksi tai korvattaviksi palvelinpuolella." Evidence: "regulatory scrutiny surrounding digital pharmacy tags".
4. s2: "Oletus: arviointi tehdään nykyisillä lisensseillä; vahvistetaan vk 1."
5. s1: "Gate 1 includes a spot test: one ERP flow and one online-pharmacy event run through each option on sample data."
