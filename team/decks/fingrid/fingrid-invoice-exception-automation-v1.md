<!-- title: Fingrid Oyj · Invoice Exception Automation -->
# Invoice exceptions resolved by rules you can audit

## Verify the data first, then automate two exception types. 21 person-days, €19,720 total excl. VAT, standard terms, no deviations.

Proposal to Leena Vainio, Head of Data and Analytics · Recordly Oy · Helsinki

---

# Solution: detect, validate, resolve, inside your lakehouse

## Deterministic rules on your Databricks, a human queue for everything uncertain. Scheduled batch fits hundreds of cases a month.

| Step | What happens | Where |
|---|---|---|
| Ingest | D365 F&SC invoices and meter master, meter-change source (to be confirmed) | Your Databricks, billing domain |
| Detect and validate | Versioned rules per exception type, meter change checked against D365 records | Delta tables, Workflows |
| Resolve | Rule-certain cases auto-resolved; the rest go to a review queue | Audit table, reversible, kill switch |
| Monitor | Run status, data-quality tests, alerts, exception counts against baseline | Unity Catalog lineage, Power BI or Databricks SQL |

- Exception handling is a data product in the billing domain with a data contract and an owner role on your side (data-mesh)
- **Why batch, not real-time:** hundreds of items a month do not justify streaming; hourly or daily runs are enough and keep reconciliation clean
- **Licensing:** no new licences, no Recordly licence. Compute runs on your account with a budget alert agreed in Phase 0 (estimate is an unknown until Phase 0)
- Code, repos and IaC stay in your tenant

---

# Measuring benefit and accuracy: a baseline before any automation

| Measure | How | Gate |
|---|---|---|
| Manual baseline | Time and error rate on a historical sample of exceptions | Finance analyst and billing team agree the numbers |
| Accuracy | Precision and recall of rules against labelled past resolutions | Numeric target set in Phase 0, no number promised before |
| Business benefit | Hours saved, share auto-resolved, days to close an exception | Reported monthly against baseline |

- We do not promise an auto-resolve share. We measure it and report it.
- Unknown: which two types are most common and whether labelled history exists. Phase 0 settles both in week 1 with your billing team.

---

# Plan: Phase 0 reconciles D365 against the lakehouse before any rule runs

| Phase | Days | Work | Gate (owner) |
|---|---|---|---|
| **0 Reconcile and baseline** | 6 | Match D365 and lakehouse records, remove duplicates, pick the two types from data, measure baseline, decide D365 interface | Finance accepts data baseline (your finance owner) |
| **1 Build and pilot** | 11 | Rules, review queue, audit table, monitoring, run in shadow mode beside manual work | Accuracy gate on your data (Recordly delivery lead and your billing lead) |
| **2 Go live and hand over** | 4 | Switch on auto-resolve for rule-certain cases, Finnish rule book and runbooks, handover | Your engineers run it |

- Resolution into D365 starts as proposals only. Write-back goes through an approved interface after the gate and your D365 owner's approval; no direct database writes.
- Open: D365 interface (data entities, OData or import journals) and meter data source, both decided in Phase 0.
- Written status every two weeks; the Senior Data Architect acts as delivery lead and owns gate reporting.

---

# Team: finance process expertise beside the engineers, available from contract signature

| Role | Focus | Credentials | Language |
|---|---|---|---|
| Senior Data Architect (delivery lead) | Lakehouse and data-mesh design, gates, plan | Databricks Data Engineer Professional, Azure Solutions Architect Expert | Finnish (native), English |
| Senior Data Engineer | Rules, pipelines, monitoring, reconciliation | Databricks Data Engineer Associate, Azure Data Engineer Associate | Finnish (native), English |
| Senior Business and Finance Process Analyst | Exception rules with billing, baseline, accuracy sampling, rule book | PL-300 Power BI Data Analyst, billing and finance reconciliation experience | Finnish (native), English |

- All documentation and runbooks in Finnish
- Two comparable client references with contact persons are given to shortlisted vendors
- Replacement right: equal seniority, handover overlap at our cost. We accept recruiting after 12 months.

---

# Price: €19,720 total, fixed, excl. VAT

| Role | Days | Day rate | Amount |
|---|---|---|---|
| Senior Data Architect | 5 | €920 | €4,600 |
| Senior Data Engineer | 11 | €920 | €10,120 |
| Senior Business and Finance Process Analyst | 5 | €1,000 | €5,000 |
| **Total, fixed, excl. VAT** | **21** | | **€19,720** |

- **Licensing:** none new. Run cost is Databricks compute on your account, capped and alerted.
- **Payment terms:** 50% at the Phase 0 gate, 50% at handover. Prices firm for 9 months.
- **Contract:** your standard agreement as is. **No contractual deviations.**
<!-- coverage: solution/measurement s2-3; phases s4; team s5; pricing/licensing/payment s6; references s5; finance analyst role s5; P3 phase 0; latency honesty s2; unknowns s3-4 -->
