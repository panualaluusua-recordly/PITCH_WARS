<!-- title: Säästöpankkiryhmä · Snowflake FinOps -->
# Snowflake FinOps for Säästöpankkiryhmä: clean up once, then keep costs under control

## Cost governance on Snowflake and Power BI, compliant with FIN-FSA, EBA and DORA. Delivered in Finnish and Swedish. Everything runs inside your own Azure and Snowflake environment.

Proposal to Rasmus Lindqvist, Head of Data and Analytics · Recordly Oy · Helsinki

---

# The proposal in one page

| | |
|---|---|
| **Definition** (3 weeks) | Cost baseline per member bank, workload and warehouse; governance model; FinOps target state |
| **Delivery** (2 months) | Cleanup: warehouse sizing, auto-suspend, unused objects, query and dbt model optimisation, Power BI refresh tuning, tagging and chargeback |
| **Ongoing** (3 months) | Recordly **Virtual Data Engineer in run mode**: 24/7 cost and performance monitoring inside your Snowflake account. **Your team approves every change.** |
| **Price** | **€57,360 total** (breakdown on slide 6) |
| **Team** | **Johanna Berg** (FinOps lead, ex-bank), **Markus Ek** (Snowflake on Azure) and **Kaisa Virta** (DORA advisor). All three speak **Finnish and Swedish**. |

---

# Compliance and governance

| Requirement | How we meet it |
|---|---|
| **DORA** | Change control through pull requests with human approval; audit trail of every agent action (auditor agent); exit plan, since everything stays in your repositories |
| **FIN-FSA / EBA outsourcing** | Recordly as an ICT third party: information for your register of information, audit and access rights, no subcontractors |
| **Non-European AI toolchains** | **The VDE runs inside your Snowflake account**, in your Azure region, using Snowflake's own AI services on your credits. Data isn't copied to Recordly systems. |
| **Member banks** | Cost reports and chargeback per bank, in Finnish and Swedish |

---

# How the cost cleanup works

| Step | Action | Typical savings levers |
|---|---|---|
| **Baseline** | Credits by warehouse, user, dbt model and Power BI dataset; tag coverage | Visibility first |
| **Quick fixes** | Right-size warehouses, auto-suspend, resource monitors, remove unused tables and clones | Idle compute, storage |
| **Optimise** | Rewrite the most expensive queries and dbt models; incremental models; Power BI refresh schedules | Compute per report |
| **Govern** | Budgets and alerts per member bank, tagging policy, monthly FinOps review | No relapse |
| **Run** | The VDE watches cost and performance daily and opens PRs for fixes; **your team approves** | Continuous |

> Honest unknown: the savings potential is quantified in Definition, from your real consumption data. We don't promise a percentage before we've seen it.

---

# Company, team and AI in our delivery

:::cols
### Recordly and the team
- Helsinki-based data and AI consultancy; financial statements and credit rating provided with the final offer; **no subcontractors**
- **Johanna Berg**, FinOps lead, ex-bank: FinOps Certified Practitioner, SnowPro Core; fi, sv, en
- **Markus Ek**, data engineer, Snowflake on Azure: SnowPro Core, Azure DE Associate; sv, fi, en
- **Kaisa Virta**, regulatory and DORA advisor: CISA; fi, sv, en
:::col
### AI-driven delivery: measured results
- Virtual Data Engineer, real projects: a semi-complex pipeline built, tested and validated in **30 min instead of 12 h**
- Migration to dbt + Snowflake: **about 30 credits per migrated table**, a predictable cost
- Business questions answered by the agent: **developer context switches per day went to zero**
- Cost and performance optimisation is a standard VDE task
:::

---

# Preliminary pricing: definition, delivery, ongoing

| Phase | Effort | Price |
|---|---|---|
| **Definition** | 8 days × €920 | €7,360 |
| **Delivery** | 22 days × €920 | €20,240 |
| **Ongoing** (3 months) | VDE 3 × €9,000 flat + 3 lead days × €920 | €29,760 |
| **Total** | | **€57,360 (VAT 0%)** |

- You may stop after Definition with no further commitment.
- Snowflake AI credits used by the agents are billed on your account and reported monthly.
- Standard terms accepted; no contractual deviations.
