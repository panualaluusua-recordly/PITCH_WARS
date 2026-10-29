<!-- title: Alma Media · AI Prototypes to Production MLOps -->
# Your first AI prototype in production, on real data, inside your governance

## Deploy, retrain, version and monitor on your AWS, Google Cloud, Redshift, BigQuery and dbt. Two dedicated engineers, 4 weeks. €37,600 fixed, excl. VAT. No contractual deviations.

Proposal to Mikael Rantala, Director of Data Platforms · Recordly Oy · Helsinki

---

# Solution: one governed path from prototype to production

## Built in your existing cloud accounts. No new platforms, no new licences.

| 1 · Mirror access | 2 · Prove on real data | 3 · Deploy | 4 · Retrain | 5 · Monitor |
|---|---|---|---|---|
| Row-level permissions copied to Redshift **and** BigQuery as code | Pilot model scored on your actual data, read-only, under those permissions | CI/CD, versioned model registry, shadow run, then live | Scheduled and drift-triggered retraining, automated tests | Performance, drift and data-quality alerts to your chat tool |
| **Gate G1:** permission parity test passed | **Week 2:** numbers, not slides | **Gate G2:** shadow metrics accepted | Rollback to previous version in one step | Runbook owned by your team |

- **Pilot:** one prototype chosen with you in week 1. Features built in dbt, models served from the cloud where the data lives.
- **Out of scope:** new AI use cases, new tools, changes to platform core. Further prototypes follow only after the week-4 read-out.

---

# Your signals, our safeguards

| What you told us | What we do |
|---|---|
| Past crews created **coordination overhead** | **Two dedicated engineers**, no subcontractors, no project layer. One written note a week. |
| Steering committee **governance before external contributors** | We follow your contributor protocol as written: access requests on day 1, least privilege, read-only first, all actions in your audit log. We never touch platform core. |
| **Delayed onboarding** creates friction | **Mobilised on signature day.** Until access is approved we work from metadata, so no idle weeks. |
| **Row-level access mirrored** before any live deployment | **Gate G1** blocks go-live until Redshift and BigQuery permission parity is tested and the report is with your oversight board. |
| Decks that **hid whether models work on real data** | Week 2: your prototype on your data, with measured results. |
| **Your team's** platform | Your team owns repos, registry and runbooks from day 1. We pair with your engineers. |

---

# Plan: 4 weeks, two gates, a visible result for your steering committee

| Week | Work | Result |
|---|---|---|
| **1** | Protocol paperwork and access requests on day 1. Prototype inventory, pilot chosen. Permission inventory in Redshift and BigQuery. Repo and CI in your organisation. | Pilot and access plan agreed |
| **2** | Permissions mirrored as code, parity tests per role. Pilot scored on real data. | **G1 passed. Real-data result.** |
| **3** | Deployment pipeline, model registry and versioning. Shadow run next to current process. | **G2:** shadow metrics |
| **4** | Go-live, retraining, monitoring, runbook. Pairing handover. | One-page steering committee summary |

> **Honest unknowns:** which prototype and how far along (week 1). How long access approval takes (your protocol decides; delays move the plan day for day and show in the weekly note). Orchestrator and registry choice (week 1, existing services only). Beyond the pilot, scope and price are set only after week 4.

---

# Team: a lean pair of platform engineers, dedicated 100%

| | MLOps Engineer (lead) | Senior Data Engineer |
|---|---|---|
| **Focus** | Deployment, registry, retraining, monitoring | Redshift and BigQuery access mirroring, dbt features, CI/CD |
| **Experience** | 9 years, models in production on AWS and Google Cloud | 11 years, Redshift, BigQuery, dbt |
| **Certifications** | AWS Certified Machine Learning Engineer - Associate · Google Cloud Professional Machine Learning Engineer | Google Cloud Professional Data Engineer · AWS Certified Data Engineer - Associate · dbt Analytics Engineering |
| **Languages** | Finnish (native), English | Finnish (native), English |
| **Availability** | **From contract signature, confirmed** | **From contract signature, confirmed** |

Alma may require replacement of either engineer at any time; replacements are of equal seniority.

---

# Price and terms

## Fixed total: €37,600 (excl. VAT)

| Role | Person-days | Day rate (8 h) |
|---|---|---|
| MLOps Engineer | 20 | €960 |
| Senior Data Engineer | 20 | €920 |
| **Total** | **40 days, 4 weeks, two dedicated engineers** | **€19,200 + €18,400 = €37,600** |

- **Invoicing:** half at gate G1 (end of week 2), half at acceptance of the week-4 summary
- **Fixed price:** effort above plan is Recordly's risk. Cloud usage costs stay on your accounts.
- **Licences:** none. **Ownership:** all code, models and documents are Alma Media's.
- **Contract:** Alma Media's standard terms as they are. **No contractual deviations.**

<!-- coverage: RFP explicit asks (technical solution = slide 2; delivery plan = slide 4; core team capabilities = slide 5; pricing = slide 6; end-to-end framework: deployment, automated retraining, versioning, continuous monitoring = slide 2 steps 3-5; integrated into existing cloud = slide 2 subtitle + out of scope). Hidden: coordination overhead = slide 3 row 1 + slide 5; real data proof = slide 2 step 2, slide 3, slide 4 week 2; AWS+GCP / Redshift+BigQuery+dbt = slide 2. Hint v1: lean pair kept (praised); governance protocols = slide 3 row 2; delayed onboarding = slide 3 row 3, slide 4 week 1 day 1; RLS mirroring before live = G1 on slides 2,3,4. Bio: team owns it / visible win = slide 3 last row, slide 4 week 4 summary. No Snowflake -> no VDE. Honest unknowns = slide 4 callout. Price 40 pd within 35-45 pd rule; rates 960 AI/ML, 920 DE. -->
