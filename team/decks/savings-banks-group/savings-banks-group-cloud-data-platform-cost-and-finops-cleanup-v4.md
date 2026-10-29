<!-- title: Säästöpankkiryhmä · Cloud Data Platform FinOps -->
# Know what every member bank costs on Snowflake, then keep it under control

## FinOps cleanup of your Snowflake, Azure and Power BI landscape. FIN-FSA, EBA and DORA by design. Finnish and Swedish. €45,080 in three phases, excl. VAT.

Proposal to Rasmus Lindqvist, Head of Data and Analytics · Recordly Oy · Helsinki

---

# Three phases, each with a gate you control

| Phase | Timing | What you get | Your gate |
|---|---|---|---|
| **Definition** | 4 weeks from 1 Dec 2026 (planned) | Cost baseline per member bank and workload, with an attribution method. Inventory of pipelines tied to non-European AI toolchains. DORA register entries. Read-only access only | Baseline (at least 3 months of usage) signed off by you, architecture board approves. **You may stop here, no further commitment** |
| **Delivery** | 8 weeks | Guardrails, budgets and alerts: alert-only for 2 weeks, then enforced, rollback ready. Warehouse right-sizing. Top-20 query tuning. Power BI refresh tuning. Cost report per bank | Savings measured against the baseline. Write access only on approved changes |
| **Ongoing** | Monthly, first 3 months | Monthly cost review and anomaly follow-up | Cancel with one month's notice |

| | |
|---|---|
| **Team** | **Proposed FinOps lead** (FinOps lead; banking experience required), **Proposed DE** (Snowflake on Azure), **Proposed DORA advisor** (regulatory and DORA advisor). Finnish, Swedish and English are requirements; candidate evidence is pending |
| **Price** | **€45,080 total, excl. VAT**: 49 person-days × €920 (slide 7) |

---

# Cost visibility per member bank and workload, with guardrails inside your own Snowflake and Azure

<div style="display:flex;align-items:stretch;gap:0;margin:0.4em 0 0.7em 0;"><div style="flex:1;background:#262626;border:2px solid #434343;border-top:8px solid #E3FF87;padding:0.5em 0.7em;font-size:0.86em;line-height:1.25;"><div style="font-weight:800;color:#E3FF87;text-transform:uppercase;letter-spacing:0.05em;font-size:0.9em;margin-bottom:0.35em;">1 · Cost sources</div><div style="padding:0.18em 0;border-top:1px solid #434343;color:#EFEFEF;">Snowflake account usage</div><div style="padding:0.18em 0;border-top:1px solid #434343;color:#EFEFEF;">Azure cost management</div><div style="padding:0.18em 0;border-top:1px solid #434343;color:#EFEFEF;">Power BI capacity metrics</div><div style="padding:0.18em 0;border-top:1px solid #434343;color:#EFEFEF;">Temenos feeds, via your Snowflake loads</div></div><div style="width:3.2em;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#E3FF87;font-weight:900;font-size:1.3em;">&rarr;<span style="font-size:0.38em;font-weight:600;color:#D4D4D4;text-align:center;line-height:1.1;"></span></div><div style="flex:1;background:#262626;border:2px solid #434343;border-top:8px solid #E3FF87;padding:0.5em 0.7em;font-size:0.86em;line-height:1.25;"><div style="font-weight:800;color:#E3FF87;text-transform:uppercase;letter-spacing:0.05em;font-size:0.9em;margin-bottom:0.35em;">2 · Cost model (Snowflake)</div><div style="padding:0.18em 0;border-top:1px solid #434343;color:#EFEFEF;">Tags per member bank</div><div style="padding:0.18em 0;border-top:1px solid #434343;color:#EFEFEF;">Cost per workload and query</div><div style="padding:0.18em 0;border-top:1px solid #434343;color:#EFEFEF;">Trend and anomaly flags</div></div><div style="width:3.2em;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#E3FF87;font-weight:900;font-size:1.3em;">&rarr;<span style="font-size:0.38em;font-weight:600;color:#D4D4D4;text-align:center;line-height:1.1;">as code</span></div><div style="flex:1;background:#2c3010;border:2px solid #E3FF87;border-top:8px solid #E3FF87;padding:0.5em 0.7em;font-size:0.86em;line-height:1.25;"><div style="font-weight:800;color:#E3FF87;text-transform:uppercase;letter-spacing:0.05em;font-size:0.9em;margin-bottom:0.35em;">3 · Guardrails</div><div style="padding:0.18em 0;border-top:1px solid #434343;color:#EFEFEF;">Resource monitors and budgets</div><div style="padding:0.18em 0;border-top:1px solid #434343;color:#EFEFEF;">Auto-suspend, right-sized warehouses</div><div style="padding:0.18em 0;border-top:1px solid #434343;color:#EFEFEF;">Alerts to cost owners</div></div><div style="width:3.2em;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#E3FF87;font-weight:900;font-size:1.3em;">&rarr;<span style="font-size:0.38em;font-weight:600;color:#D4D4D4;text-align:center;line-height:1.1;">reviewed</span></div><div style="flex:1;background:#262626;border:2px solid #434343;border-top:8px solid #E3FF87;padding:0.5em 0.7em;font-size:0.86em;line-height:1.25;"><div style="font-weight:800;color:#E3FF87;text-transform:uppercase;letter-spacing:0.05em;font-size:0.9em;margin-bottom:0.35em;">4 · Reporting</div><div style="padding:0.18em 0;border-top:1px solid #434343;color:#EFEFEF;">Power BI FinOps view</div><div style="padding:0.18em 0;border-top:1px solid #434343;color:#EFEFEF;">Monthly report per bank, fi and sv</div><div style="padding:0.18em 0;border-top:1px solid #434343;color:#EFEFEF;">Savings vs. baseline</div></div></div>

- **Your tenant, EU only.** No data goes to non-European AI toolchains. **Inventory method:** scan Snowflake external functions, integrations, tasks and query history, plus Azure app registrations and egress. Each finding is classed as remove, replace or exit plan, and feeds the DORA register-of-information entries. Replacement of a pipeline larger than 2 days is scoped as a change request after Definition.
- **Survives restructuring:** a member-bank mapping table lets costs be re-pointed when banks integrate, without rebuilding the model.
- **Attribution:** query and role tags where warehouses are per bank, usage-based allocation where shared. The remainder goes to a visible "unallocated" line. Definition reports the unallocated % and you approve the allocation rules.
- **Definition gate:** baseline = at least 3 months of usage, read-only roles, signed off by you.

---

# Optimisation plan: every lever has a measure and a baseline

| Lever or control | How it is measured or proven | Phase |
|---|---|---|
| Non-European AI toolchain pipelines | Inventory and decision log (DORA ICT risk) | Definition, then Delivery |
| Warehouse right-sizing and auto-suspend | Credits per workload, before and after | Delivery |
| Query and model optimisation, top 20 spenders | Runtime and credits per query | Delivery |
| Storage and retention settings | Storage cost trend | Delivery |
| Power BI refresh schedules | Capacity utilisation | Delivery |
| Budgets, monitors and alerts per cost owner | Anomalies caught before the invoice | Delivery, Ongoing |

> **Honest unknown:** the savings potential is quantified in Definition from your real consumption. We quote no savings percentage before we have measured it, and you set the targets.

**Out of scope:** new tools or licences, re-platforming of the data platform, changes to Temenos feeds. A flagged non-European pipeline larger than 2 days to replace is a separate change request. Every guardrail change goes through your change board.

**Guardrails go live in two steps:** alert-only for 2 weeks, then enforce. Hard suspend only on non-production warehouses. Every change is code in your repo, reviewed by your change board, with a rollback.

**Access:** read-only to Snowflake account usage, Azure Cost Reader and Power BI capacity metrics in Definition. Write access only in Delivery, on approved changes.

---

# AI-driven cost management: real results, and the limits we state

:::cols
### Recordly Virtual Data Engineer, real projects
| Case | Outcome |
|---|---|
| Migration Matillion + Redshift to dbt + Snowflake | About 30 Snowflake credits per migrated table |
| Semi-complex pipeline: build, test, validate | 12 h by hand, 30 min |
| Power BI report rebuilt after a migration | Tens of seconds |
| Business questions about pipelines | Developer context switches per day: several to 0 |

Cost and performance optimisation is a standard task for it. **None of these is a FinOps saving figure, and we have no saving percentage to quote.**
:::col
### How it would work for you
- Agents run **inside your Snowflake account** on your Snowflake AI credits, built on Snowflake and dbt
- They open **pull requests**. Review agents test every change, auditor agents keep an audit trail. **They cannot approve or merge: your change board does.**
- **Limit:** it uses Snowflake's AI services, so we do not call it a European toolchain. It adds no vendor beyond the platform you already run. Where those services process your data is confirmed in Definition and enabled only if your architecture board approves.
- **Option, not in the total:** from Delivery's end, €9,000 per month for a 3-month fixed term plus separately nominated AI-qualified architecture setup and about 1 architect day/month. Scope and cost require a separate agreement.
:::

---

# Company, governance and team

:::cols
### Recordly Oy and DORA terms
- Helsinki data and AI consultancy. Recordly employees only, **no subcontractors**
- **Financial stability:** financial statements and credit rating provided with the shortlist
- **Accepted:** audit and access rights, register-of-information data, exit plan, no subcontracting without approval, EU-only processing
- **Finnish and Swedish:** workshops, reports and documentation in both languages, for member banks in both language areas
- Process first: every change through your change board, a written decision log, monthly steering
:::col
### Team, in Finnish and Swedish
| Person | Role | Required certificates | Days |
|---|---|---|---|
| **Proposed FinOps lead** | FinOps lead; banking experience required | **FinOps Certified Practitioner · SnowPro Core** | 22 |
| **Proposed DE** | Data engineer, Snowflake on Azure | **SnowPro Core · Azure DE Associate** | 23 |
| **Proposed DORA advisor** | Regulatory and DORA advisor | **CISA** | 4 |

Planned from 1 Dec 2026, subject to CV, language, certification and availability verification before commitment. Replacement only with your approval, equal seniority, 2-week overlap at our cost.
:::

---

# Preliminary pricing: definition, delivery, ongoing

| Phase | Effort | Price |
|---|---|---|
| **Definition** | 14 days × €920 (lead 6, DE 6, advisor 2) | €12,880 |
| **Delivery** | 26 days × €920 (lead 10, DE 14, advisor 2) | €23,920 |
| **Ongoing**, first 3 months | 9 days × €920 (3 a month: lead 2, DE 1) | €8,280 |
| **Total, excl. VAT** | **49 days × €920** | **€45,080** |

- **Preliminary:** Definition and Delivery are fixed once your architecture board approves the baseline. Anything extra only by your written change request.
- **Ongoing** continues after 3 months at the same monthly rate (€2,760), cancellable with one month's notice.
- **Terms:** your standard terms and DORA ICT third-party terms accepted. No new licences. **No contractual deviations.**


**Staffing basis:** one person-day is 8 hours. DE EUR 115/h; DA EUR 125/h; required AI expertise adds EUR 5/h for the relevant role. Architect and other-role base EUR 115/h is a proposed commercial rate for owner review. The team has at most one architect and complementary roles. CVs, credentials, language proficiency, actual availability and exact start dates remain unverified. These are role requirements, not booked people. Fixed-price scope, client dependencies and risk allowance need agreement before commitment.

**Allocation correction:** Definition advisor 2/20 days = 10%; Delivery advisor 2/40 days = 5%, within the roster 10% cap. Lead/DE totals stay 22/23 days and advisor 4 days; price remains EUR 45,080. The optional VDE is not part of this total and requires separately costed AI architecture setup and run support before adoption.

<!--
coverage: RFP ask -> slide
- Company background, financial stability -> s6 (financials + credit rating provided with shortlist: ASSUMPTION, no numbers invented; Recordly to supply)
- Governance frameworks FIN-FSA, EBA, DORA -> s1, s6 (DORA ICT third-party terms), s3 (register entry per tool, exit plan, decision log), s4 (change board)
- Technical solution -> s3 (diagram: cost sources -> model -> guardrails -> reporting; Snowflake on Azure, Power BI, Temenos feeds)
- Optimisation plan -> s4 (levers, measures, phase)
- Concrete AI-driven cost management case examples with outcomes -> s5 (only vde-facts.md results; no saving % claimed; stated honestly)
- Team incl. financial-sector experience and language capabilities -> s6 (ex-bank FinOps lead, DORA advisor with CISA, fi/sv/en)
- Implementation roadmap -> s2 (phases, timing, gates)
- Preliminary pricing partitioned into definition, delivery, ongoing -> s7
- v3 tech fixes (tech-critic 2026-10-29): attribution method + 3-month baseline gate (s2,s3); alert-only guardrail rollout, non-prod hard suspend, access (s2,s4); toolchain inventory method + 2-day replacement cap, scope conflict resolved (s3,s4)
- Hidden: non-European AI toolchain concern -> s3, s4, s5; Finnish + Swedish -> cover, s3 (fi/sv reports), s6; stability -> s6; cautious process-first bio + restructuring -> s2 stop-after-Definition, s3 mapping table, s6 process
- Scope choice: Panu 25+70+3/mo (=95+ pd) vs Ville 8+22+VDE run (EUR 57,360); chosen 14+26+9 pd human-led, VDE as option outside the total
-->
