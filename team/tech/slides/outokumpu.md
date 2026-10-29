# Tech & architecture slides for the Outokumpu deck
_Outokumpu Oyj: Two slides for deck-writer to insert after the answer-first slide_

## 2. Our engineers work inside your lakehouse as it is: lineage from SAP to report, no stock graphics
- We plug into your existing Azure Databricks setup, repos and conventions; we add no tools of our own.
- Every pipeline we touch is visible end to end in Unity Catalog lineage, and that lineage is what we show in reviews.
[SAP sources: MM / SD: supply chain, PP / QM: production & quality, FI/CO where reports need it] → [Ingest: Your existing extraction pattern, Incremental loads, schema checks, Reusable job templates] → [Azure Databricks lakehouse: Bronze → silver → gold, Unity Catalog: lineage & access, Asset Bundles + CI/CD in your repo] → [Enterprise reporting: Certified gold tables, BI tool semantic models, Data quality checks visible to users]
(Team works in your chat tool and your sprint board · code reviewed by your leads · nothing outside your tenant)

## 3. Productive in week 2, fully handed over at the end
| When | Technical onboarding and transition | Evidence you see |
| --- | --- | --- |
| Week 1 | Access, repo, Unity Catalog, coding standards; pair with one of your engineers on a live ticket | First merged pull request |
| Weeks 2–4 | Own backlog items end to end on the SAP → gold flow | Lineage view per delivered table |
| Monthly | Short written update: delivered tables, data-quality results, open risks | No standing status meetings |
| Last 4 weeks | Runbooks in repo, recorded walkthroughs, your engineer leads, we review | Your team runs every delivered pipeline unaided |

_Certifications on the proposed engineers: Databricks Certified Data Engineer Professional; Microsoft Azure (AZ-305 / DP-series). Technical unknowns: access lead times, SAP extraction throughput, backlog readiness. A 12-month extension keeps the same people and the same patterns._
