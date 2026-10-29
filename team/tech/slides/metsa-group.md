# Tech & architecture slides for the Metsä Group deck
_Metsä Group: Two slides for deck-writer to insert after the answer-first slide_

## 2. Forecasts run on your Azure Databricks and SAP feeds, with a proven library rather than bespoke algorithms
- SAP S/4HANA demand, stock and production data feed Databricks, which runs established open-source forecasting methods. Planners see forecasts and inventory recommendations in your BI tool.
- Kiln-type anomalies are flagged for planners, never modelled case by case.
- Timeline: weeks 1-2 buy-vs-build check and data audit; weeks 3-8 pilot on one product line and two hubs; scale only if the error beats today's plan.
[SAP S/4HANA: Sales orders & deliveries, Stock per hub, Production plans] → [Azure Databricks: Feature tables per product line, Proven forecasting library, Accuracy tracked vs. today's plan] → [Inventory logic: Safety stock per hub, Anomaly flags for planners] → [BI dashboards: Planner view per hub, Forecast accuracy vs. plan]
(Pilot first: one product line, two hubs. Scale only when forecast error beats the current plan)

## 3. Buy before build: we check commercial packages first and say which wins
| Option | When it wins | Our view now |
| --- | --- | --- |
| A commercial forecasting package, if one is already licensed | You already license it, or planners need its workflows | Checked first in week 1 |
| Open-source forecasting library on Databricks | Fits your stack, no new licence, low upkeep | Our default |
| Bespoke algorithms | Only for a gap the others cannot cover | Not proposed |

_Technical unknowns: data history depth per product line, hub master data quality, existing planning licences. The effort and price come from our own calculation, not from published figures._
