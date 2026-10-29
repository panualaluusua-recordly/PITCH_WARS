# Tech & architecture slides for the UPM deck
_UPM-Kymmene Oyj: Two slides for deck-writer to insert after the answer-first slide_

## 2. Models reach SAP through one tested pipeline pattern, not fragile one-off scripts
- The embedded engineer builds this template in your repos in the first 30 days, then reuses it for each model.
- Every production model uses the same template: features from Snowflake + dbt, training and registry in Databricks, scored output written back to SAP S/4HANA through a staged, reconciled interface.
- No release in the days around quarterly close.
[Features: Snowflake + dbt models, Tested feature tables, Data contracts on inputs] → [Databricks ML: Training from the template, Model registry with approvals, Drift & accuracy monitoring] → [Scoring pipeline: Scheduled batch scoring, paused in your quarterly close window, Tests on every output, Retry & alert, no silent failure] → [SAP S/4HANA: Staged write-back, Reconciled before posting, Owner per integration]
(Run cost capped per pipeline and reported monthly, so compute spend cannot drift past the estimate)

## 3. A pipeline goes to production only when it passes the same checklist
| Check | Why it matters to UPM |
| --- | --- |
| Data contract + dbt tests on inputs | Upstream changes fail loudly, not at quarter close |
| Model registry approval by your owner | No model reaches SAP without a named sign-off |
| Monitoring and alert to the owner | A failing pipeline is fixed the same day |
| Rollback to the previous model version | Business continues if a release misbehaves |
| Weekly timesheet vs. agreed monthly cap, plus compute cost per pipeline | Spend stays inside the department estimate |

_Quarter-close dates come from your finance calendar. Every release has a named owner and a rollback._
