# Tech & architecture input: second batch (VR Group, UPM, Metsä Group, Savings Banks Group, Vahterus)

Source: RFPs and bios only (2026-10-29). No feedback requested yet. Pattern ids (P1..P16) refer to `TECH_SCOPE.md`.
Ready-made slides: `team/tech/slides/<buyer>.json` (+ `.pdf` preview): architecture with a diagram, then tech gates
and risks. The deck-writer copies the two slide objects into the buyer's spec after the answer-first slide and keeps
the `note` text out of the buyer-facing slide unless it is phrased for the buyer.

Related work already in git:
- Ville's VDE variants (`team/vde/offers/`) for savings-banks-group, upm, valmet and vr-group. Our slides fit them. VDE
  fits only on Snowflake (+ dbt): VR, UPM, Savings Banks. Not Metsä (Azure Databricks) or Vahterus (target cloud unknown).
- Delivery input (team, plan, governance): `team/delivery/batch2.md`, `team/delivery/slides/`.

## VR Group: analytics engineer, 6 months (P9, P12, extraction for all sources)

- **Tech hooks:** "the supplier shall propose the extraction solution for all sources" → a slide that names the
  method per source type (CDC, API/events, files) through one metadata-driven loader. AWS + Snowflake + Data Vault 2.0
  → hubs, links and satellites on rail business keys. "Strictly no production changes during Q1" → build and test in
  non-production in Q1; releases in December and from April.
- **Bio (Samuli):** railway concepts were lost "across foreign-led workshops" → Finnish business-key glossary. "Masking
  architectural tensions behind tech hype" → no hype; plain gates.
- **Trap:** do not assume dbt or a specific Data Vault loader; use theirs if one exists.

## UPM: forward-deployed AI engineer, 6 months (P6, P8, P2)

- **Tech hooks:** "bespoke data pipeline whose fragile setup collapsed during a critical quarterly close" → one tested
  pipeline template Snowflake + dbt → Databricks ML → staged, reconciled write-back to SAP S/4HANA; no releases around
  quarterly close. "Open billing drifted" → a cost cap per pipeline (tech) alongside fixed fees (commercial).
- **Production checklist** as the gate: contracts and tests, registry approval, monitoring, rollback, cost cap.

## Metsä Group: demand and inventory forecasting (P7, P4, P13)

- **Tech hooks:** "maintenance overhead of bespoke algorithms when mature commercial packages already existed" →
  buy-before-build table (commercial planning suite / open-source library on Databricks / bespoke = not proposed).
  Bio: a rollout stalled on "contingencies for every freak kiln anomaly" → anomalies flagged for planners, not
  modelled. Bio: "little patience for… theoretical architectures" and "sprawling transformation blueprints" → one
  pilot product line, two hubs.
- **Gate:** forecast error beats the current plan before scaling.
- **Effort and price:** from our own calculation, not anchored to published figures (RFP).

## Savings Banks Group: FinOps cleanup (P1, P8)

- **Tech hooks:** "compliance exposure… pipelines tied to proprietary non-European AI toolchains" → inventory and
  replace or document with an exit plan, EU-only processing. Snowflake on Azure + Power BI + Temenos → one cost model
  tagged per member bank and workload; resource monitors, budgets, auto-suspend, alerts.
- **"Concrete AI-driven cost management case examples":** use only the VDE facts (cost and performance optimisation
  inside Snowflake, `vde-facts.md`). Do not quote savings percentages before a baseline.
- **Bio (Rasmus):** process over innovation → every guardrail as code through their change board.

## Vahterus: legacy application & reporting modernisation (P9, P5, P13)

- **Tech hooks:** "no production changes take place during Q1" → build Q1, go live from April. A new ERP is rolling
  out → an integration layer with a data contract per object, so reports survive ERP changes. Moving to "a public cloud"
  (unnamed) → do not name a vendor.
- **Bio (Ronja):** "ROI-obsessed… monitors every code commit" → ROI-ranked backlog; every commit linked to a backlog
  item with its benefit measure.
- **"Concise presentation deck"** → keep both tech slides tight.
