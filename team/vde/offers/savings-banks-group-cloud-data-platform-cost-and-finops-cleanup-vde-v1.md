<!-- title: Säästöpankkiryhmä · Snowflake FinOps -->
# Snowflake FinOps pilot for one member bank

## Cost governance on Snowflake and Power BI, compliant with FIN-FSA, EBA and DORA. Delivered in Finnish and Swedish. Everything runs inside your own Azure and Snowflake environment.

Draft proposal to Rasmus Lindqvist, Head of Data and Analytics · Recordly Oy · Helsinki

---

# The proposal in one page

| | |
|---|---|
| **Definition** (3 weeks) | Pilot baseline for one member bank and account; ten prioritised cost objects; governance model |
| **Delivery** (2 months) | Cleanup: warehouse sizing, auto-suspend, unused objects, query and dbt model optimisation, Power BI refresh tuning, tagging and chargeback |
| **Ongoing** (3 months) | Recordly **Virtual Data Engineer in run mode**: 24/7 cost and performance monitoring inside your Snowflake account. **Your team approves every change.** |
| **Price** | **€59,440 total** (breakdown on slide 6) |
| **Team** | **Proposed FinOps lead** (FinOps lead with banking experience required), **Proposed data engineer** (Snowflake on Azure) and **Proposed DORA advisor** (DORA advisor). **Finnish and Swedish are role requirements; candidate evidence is pending**. |

---

# Compliance and governance

| Requirement | How we meet it |
|---|---|
| **DORA** | Change control through pull requests with human approval; audit trail of every agent action (auditor agent); exit plan, since everything stays in your repositories |
| **FIN-FSA / EBA outsourcing** | Recordly as an ICT third party: information for your register of information, audit and access rights, no subcontractors |
| **Non-European AI toolchains** | **The VDE runs inside your Snowflake account**, in your Azure region, using Snowflake's own AI services on your credits. Data isn't copied to Recordly systems. |
| **Member banks** | Pilot reports for one member bank in Finnish and Swedish; wider rollout scoped separately |

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
### Required profiles; candidate evidence pending
- Helsinki-based data and AI consultancy; financial statements and credit rating provided with the final offer; **no subcontractors**
- **Proposed FinOps lead**, FinOps lead with banking experience required: FinOps Certified Practitioner, SnowPro Core; fi, sv, en
- **Proposed data engineer**, data engineer, Snowflake on Azure: SnowPro Core, Azure DE Associate; sv, fi, en
- **Proposed DORA advisor**, regulatory and DORA advisor: CISA; fi, sv, en
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
| **Definition** | 4 FinOps days × €1,000 + 3 DE days × €920 + 1 advisor day × €1,200 | €7,960 |
| **Delivery** | 6 FinOps days × €1,000 + 6 DE days × €920 + 8 AI architect days × €960 + 2 advisor days × €1,200 | €21,600 |
| **Ongoing** (3 months) | VDE 3 × €9,000 + 3 AI architect days × €960 | €29,880 |
| **Total** | | **€59,440 (VAT 0%)** |

- You may stop after Definition with no further commitment.
- Snowflake AI credits used by the agents are billed on your account and reported monthly.
- Standard terms accepted; scope, staffing and commercial terms require owner confirmation.

---

# Staffing, scope and price assumptions

- Eight hours/day. Proposed rates: FinOps lead EUR 125/h, DE EUR 115/h, AI DE EUR 120/h, DORA advisor EUR 150/h, AI architect EUR 120/h. Non-DE rates are commercial proposals for owner review. AI rates include EUR 5/h premium.
- Delivery includes 8 AI architect days for VDE setup and 6 DE days of cleanup. In run mode the client approves every change; Recordly provides 1 architect day/month.
- This reduced 30-day build estimate covers a **pilot in one member bank and one Snowflake account, with ten prioritised cost objects**. Wider rollout is estimated after definition; it is not included in this price. Confirm dbt readiness before VDE deployment.
- CVs, banking experience, certifications, languages and actual availability remain unverified. Nominate the run architect and verify all profiles before submission.
- The fixed phase fees cover the specified scope and capacity. Agree acceptance criteria and source-access assumptions before commitment; customer AI credits, licences and travel are excluded.
