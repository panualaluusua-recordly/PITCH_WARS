# Tech & architecture slides for the Varma deck
_Varma Mutual Pension Insurance Company: Two slides for deck-writer to insert after the answer-first slide_

## 2. One MLOps golden path replaces twenty one-off deployment scripts
- Every model, current and future, uses the same repo template, configuration schema, pipeline and monitoring. A new use case starts from the template, not from a blank script.
- Built on your existing cloud data platform; MLflow-compatible registry, so the pattern is not tied to one vendor.
[Data: Existing data platform, Versioned training datasets, Feature definitions in code] → [Build: Repo template per model, One config schema, Automated tests & validation] → [Release: CI/CD pipeline (same for all), Model registry with approvals, Reproducible: data + code + model] → [Run: Monitoring: drift & performance, Alerts to model owner, Audit trail per prediction]
(Models support pension decisions, they do not make them: human approval stays in the process, and explanations are logged)

## 3. Use case 1 in production by month 2; your new specialists ship use case 3 themselves
| Month | Use case | Who builds | Technical proof |
| --- | --- | --- | --- |
| 1–2 | Use case 1 on the golden path (quick win) | Recordly, your specialists pairing | In production with monitoring |
| 3–4 | Use case 2 on the same template | Your specialists, Recordly pairing | Built without new deployment scripts |
| 5–6 | Use case 3 + triage of the other ~17 experiments | Your specialists lead, Recordly reviews | Handover check: your team releases unaided |

_Technical unknowns we price in: which of the three use cases has production-ready data; access to personal data for training (minimised, pseudonymised); EU AI Act classification per use case. Documentation uses Finnish pension terms (työeläke, TyEL, eläkepäätös), no translation needed._
