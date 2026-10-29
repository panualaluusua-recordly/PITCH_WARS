<!-- title: Valmet · Senior Data Engineer -->
<!-- Staffing pending Rauno's review. Names and allocations from team/delivery/ROSTER.md (Laura 60% and Tuomas 5% need a roster update). Certificate IDs, on-site days and availability are assumptions until verified. Not sent. -->
# A certified Snowflake data engineer who keeps your satellite links free

## Infor CloudSuite and mill data into Snowflake: summarised at the mill, EU-region by design, monitored from day one. €104,280 fixed, excl. VAT. Your standard terms, no deviations.

Proposal to Milla Kaartinen, Data & AI Development Manager · Recordly Oy · Helsinki

---

# The proposal in one page

| | |
|---|---|
| **Outcome** | Reliable, monitored ingestion from Infor CloudSuite and operational sources into Snowflake, ready for reporting in your BI tool |
| **Satellite links** | Raw telemetry never crosses them. Aggregated at the mill, bandwidth-capped, backfilled off-peak, one mill at a time (slide 3) |
| **Foreign jurisdiction** | EU region, customer-managed keys, data minimisation, open-format exit path. **Limits stated openly** (slide 4) |
| **Certifications** | **SnowPro Core** and **SnowPro Advanced: Data Engineer**, plus **Azure Solutions Architect Expert**. Credential IDs supplied for verification (slide 6) |
| **Team** | **Laura Heikkilä**, senior data engineer, 3 days a week, plus **Tuomas Rantanen**, solution architect, and our **Virtual Data Engineer** from month 4 |
| **Visibility** | One page a month for your leadership: pipelines live, link usage per mill, data freshness, incidents |
| **Price** | **€104,280 fixed**, 6 monthly invoices of €17,380, excl. VAT |

---

# Mill telemetry is summarised at the edge, so satellite links are never saturated

<div style="display:flex;align-items:stretch;gap:0;margin:0.4em 0 0.7em 0;"><div style="flex:1;background:#262626;border:2px solid #434343;border-top:8px solid #E3FF87;padding:0.5em 0.7em;font-size:0.92em;line-height:1.25;"><div style="font-weight:800;color:#E3FF87;text-transform:uppercase;letter-spacing:0.05em;font-size:0.9em;margin-bottom:0.35em;">1 · Mill (edge)</div><div style="padding:0.18em 0;border-top:1px solid #434343;color:#EFEFEF;">Local collector per site</div><div style="padding:0.18em 0;border-top:1px solid #434343;color:#EFEFEF;">Aggregate and compress: 1-min stats, deltas</div><div style="padding:0.18em 0;border-top:1px solid #434343;color:#EFEFEF;">Store-and-forward buffer</div></div><div style="width:3.2em;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#E3FF87;font-weight:900;font-size:1.3em;">&rarr;<span style="font-size:0.38em;font-weight:600;color:#D4D4D4;text-align:center;line-height:1.1;">only aggregates and changes</span></div><div style="flex:1;background:#2c3010;border:2px solid #E3FF87;border-top:8px solid #E3FF87;padding:0.5em 0.7em;font-size:0.92em;line-height:1.25;"><div style="font-weight:800;color:#E3FF87;text-transform:uppercase;letter-spacing:0.05em;font-size:0.9em;margin-bottom:0.35em;">2 · Constrained link</div><div style="padding:0.18em 0;border-top:1px solid #434343;color:#EFEFEF;">Bandwidth cap per site</div><div style="padding:0.18em 0;border-top:1px solid #434343;color:#EFEFEF;">Operations traffic first</div><div style="padding:0.18em 0;border-top:1px solid #434343;color:#EFEFEF;">Backfills only off-peak</div></div><div style="width:3.2em;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#E3FF87;font-weight:900;font-size:1.3em;">&rarr;<span style="font-size:0.38em;font-weight:600;color:#D4D4D4;text-align:center;line-height:1.1;">monitored</span></div><div style="flex:1;background:#262626;border:2px solid #434343;border-top:8px solid #E3FF87;padding:0.5em 0.7em;font-size:0.92em;line-height:1.25;"><div style="font-weight:800;color:#E3FF87;text-transform:uppercase;letter-spacing:0.05em;font-size:0.9em;margin-bottom:0.35em;">3 · Central ingestion</div><div style="padding:0.18em 0;border-top:1px solid #434343;color:#EFEFEF;">Infor CloudSuite via ION / Data Lake</div><div style="padding:0.18em 0;border-top:1px solid #434343;color:#EFEFEF;">Incremental loads, schema checks</div><div style="padding:0.18em 0;border-top:1px solid #434343;color:#EFEFEF;">Monitoring and alerts</div></div><div style="width:3.2em;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#E3FF87;font-weight:900;font-size:1.3em;">&rarr;<span style="font-size:0.38em;font-weight:600;color:#D4D4D4;text-align:center;line-height:1.1;"></span></div><div style="flex:1;background:#262626;border:2px solid #434343;border-top:8px solid #E3FF87;padding:0.5em 0.7em;font-size:0.92em;line-height:1.25;"><div style="font-weight:800;color:#E3FF87;text-transform:uppercase;letter-spacing:0.05em;font-size:0.9em;margin-bottom:0.35em;">4 · Snowflake (EU region)</div><div style="padding:0.18em 0;border-top:1px solid #434343;color:#EFEFEF;">Raw, modelled, reporting layers</div><div style="padding:0.18em 0;border-top:1px solid #434343;color:#EFEFEF;">Customer-managed keys</div><div style="padding:0.18em 0;border-top:1px solid #434343;color:#EFEFEF;">Your BI tool on certified tables</div></div></div>

- **Rollout one mill at a time.** Link usage is measured before and after. The next site starts only if operations saw no impact.
- **Scope:** we design the pattern and pilot it at one mill. Valmet's site and OT staff install collectors; we support them.
- **Unknowns, resolved in month 1:** link capacity per mill, Infor API limits. The gate decides the cap.

---

# Foreign jurisdiction: what we can control, and what we cannot

| Measure | What it does | Limit we state openly |
|---|---|---|
| EU-region Snowflake account | Data stored and processed in the EU | Provider is US-headquartered |
| Customer-managed keys (Tri-Secret Secure) | Valmet can revoke access to the data | Needs Business Critical edition |
| Private connectivity, data minimisation | Only data needed for reporting leaves the mills | Design choice per data set |
| Open table format (Iceberg) for core data | Exit path to another platform | Migration effort if ever used |
| Virtual Data Engineer | Runs inside your Snowflake account on your AI credits; output is pull requests in your repositories | Uses Snowflake's AI services, so the same provider limit applies |

> Unknowns: your current Snowflake region, and which data sets legal classes as sensitive. Both are settled in month 1, before any data moves.

---

# Plan: your engineers build it with us from week 1

| Month | Work | Laura | Gate |
|---|---|---|---|
| **1** | Site and source assessment: link capacity, Infor API limits, data classification. Conventions and pilot backlog | 13 d | You approve bandwidth cap and pilot mill |
| **2–3** | Pilot mill live. First Infor and operational sources in production | 26 d | Link usage before and after: no operational impact |
| **4** | Virtual Data Engineer deployed in your Snowflake. Baseline measured | 13 d | Baseline accepted by you |
| **5–6** | Remaining sources, one mill at a time. Runbooks. Hand-over | 26 d | Your team runs it |

**The Virtual Data Engineer** (AI agents, running 24/7 in your Snowflake, fixed 3-month term) takes repeat work: new sources from agreed patterns, tests, failed-job root cause, schema-drift checks. Laura sets the architecture, conventions and examples it builds on and reviews its work. **A person at Valmet approves every change as a pull request.** Real result: a semi-complex pipeline built, tested and validated in 30 min instead of 12 h.

Pairing with your data team from week 1. All code in Valmet's repositories.

---

# Team: certified, with credentials you can verify

| Person | Role | Certifications | Languages | Availability | Days |
|---|---|---|---|---|---|
| **Laura Heikkilä** | Senior data engineer, 3 days a week, on site in Espoo by default | **SnowPro Core · SnowPro Advanced: Data Engineer** | Finnish, English | Planned 1 Dec 2026, confirmed in writing at signature | 78 |
| **Tuomas Rantanen** | Solution architect: design review, 1 day a month | **Azure Solutions Architect Expert** | Finnish, English | Planned 1 Dec 2026, confirmed in writing at signature | 6 |
| **Virtual Data Engineer** | AI agents in your Snowflake, months 4–6 | Not a person: human approval on every change | | From month 4 | |

- **Verification:** credential IDs for each certificate are supplied with the final offer, so Valmet can check them with the issuer.
- **Replacement:** only with your approval, equal seniority, 2-week overlap at our cost. No subcontractors.

---

# Price and terms

| Item | Effort | Amount |
|---|---|---|
| Laura Heikkilä, senior data engineer | 78 days × €920 | €71,760 |
| Tuomas Rantanen, solution architect | 6 days × €920 | €5,520 |
| Virtual Data Engineer, months 4–6 | 3 months × €9,000 flat | €27,000 |
| **Fixed total, excl. VAT** | | **€104,280** |

- **Invoicing:** 6 × €17,380 monthly, payment per Valmet's standard terms. **No contractual deviations.**
- **Fixed price:** hours above plan are Recordly's risk. Scope changes only by your written approval.
- **Licences:** none new. Snowflake AI credits used by the agents are billed on your account and reported monthly.

<!--
coverage: RFP ask -> slide
- Senior DE, Espoo, 6 months, ingestion Infor CloudSuite + operational data into Snowflake, BI reporting -> s1, s2, s5
- Satellite-link bandwidth (hidden req) -> s2, s3 (edge aggregation diagram, cap, off-peak, one mill at a time, honest scope: OT staff install)
- Extraterritorial jurisdiction (hidden req) -> s2, s4 (measures + stated limits, VDE row)
- Verified certifications heavily weighted (hidden req) -> s2, s6 (SnowPro Core/Advanced DE, Azure SA Expert, IDs supplied)
- Chat tool collaboration -> s5 pairing from week 1, s2 visibility report (assumption: chat tool is the channel for written updates)
- Structured deck: technical solution s3-s4, delivery plan s5, team profiles s6, complete pricing model s7
- Bio: executive visibility -> s2 monthly one-page report
- Honest unknowns -> s3 (link capacity, Infor API limits), s4 (Snowflake region, sensitive data sets)
- VDE variant (Ville) -> s5, s6, s7; Panu tech slides -> s3, s4
- Assumptions to verify (Rauno): Laura 60% (roster says 100%), Tuomas 5% valmet not yet in roster, credential IDs, on-site days, availability 1 Dec
-->
