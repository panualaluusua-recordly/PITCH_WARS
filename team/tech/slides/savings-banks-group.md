# Tech & architecture slides for the Savings Banks Group deck
_Savings Banks Group (Säästöpankkiryhmä): Two slides for deck-writer to insert after the answer-first slide_

## 2. Cost visibility per member bank and workload, with guardrails inside your own Snowflake and Azure
- Snowflake usage, Azure cost data and Power BI capacity are combined in one cost model, tagged by member bank and workload. Guardrails stop runaway spend before the invoice.
- Everything runs in your tenant in the EU. No data goes to non-European AI toolchains.
- DORA: an ICT-risk register entry per tool, an exit plan, and an audit log of every guardrail change.
[Cost sources: Snowflake account usage, Azure cost management, Power BI capacity metrics, Temenos feeds via your Snowflake loads] → [Cost model (Snowflake): Tags per member bank, Cost per workload & query, Trend and anomaly flags] → [Guardrails: Resource monitors & budgets, Auto-suspend, right-sized warehouses, Alerts to cost owners] → [Reporting: Power BI FinOps view, Monthly report per bank, Savings vs. baseline]
(Pipelines tied to non-European AI toolchains are inventoried in the definition phase and replaced or documented with an exit plan)

## 3. Savings levers we measure against your baseline, and the controls your regulators expect
| Lever or control | How it is measured or proven |
| --- | --- |
| AI-driven example: Recordly's Virtual Data Engineer | Agents in your Snowflake propose cost and performance fixes as pull requests; your change board approves each one |
| Warehouse right-sizing and auto-suspend | Credits per workload before and after |
| Query and model optimisation for top spenders | Top 20 queries: runtime and credits |
| Storage and retention settings | Storage cost trend |
| Power BI refresh schedules | Capacity utilisation |
| EU-only processing, no foreign AI toolchain | Inventory and decision log (DORA ICT risk) |
| Change through your change board | Every guardrail as code, reviewed |

_Phases: definition = baseline + toolchain inventory; delivery = guardrails and optimisation; ongoing = monthly review. Savings targets are set after the baseline; we do not quote % savings before measuring._
