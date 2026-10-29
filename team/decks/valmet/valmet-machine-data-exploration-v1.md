<!-- title: Valmet · Sensor Data Exploration -->
# Which sensor channels predict failures, and why a flag fired

## A 6–8 week exploration inside your Snowflake: failure patterns, explainable maintenance indicators and a roadmap. €24,480 fixed (excl. VAT). Your terms as written, no deviations.

Proposal to Milla Kaartinen, Data & AI Development Manager · Recordly Oy · Helsinki

---

# Solution: everything runs inside your Snowflake, on your data

:::cols
### What we do
- **Read-only exploration in your existing Snowflake account.** SQL and Snowpark in a sandbox schema. No new tools, no data copied out, no external service.
- **Working demo on your real equipment data at the week-3 gate**, not slides: failure patterns found so far, with an indicator and its reason
- **Every flag carries a plain-language reason**, for example "bearing vibration 2.4x its 30-day norm for 5 days"
- Roadmap for service operations, ranked by value and effort
:::col
### Our position on process modelling
- **Start transparent:** per-asset baselines, thresholds, degradation trends and survival curves
- **Add statistical models only where they beat the baseline** on your history, and only if the reason stays readable
- **Physics-based models** are a roadmap option, judged on evidence
- **Out of scope:** production alerting, new platforms, dashboards, model deployment
:::

---

# Past failures answered

| What went wrong before | Our safeguard |
|---|---|
| **Technicians could not understand why alert flags fired** | Each indicator is rule-readable and ships with a **plain-language reason per flag**. In week 6 we run a **90-minute technician walkthrough** (Finnish or English) on real flags, inside the view they already use. |
| **Locked work breakdowns kept auditing uninformative telemetry** | **Adaptive scope:** the **week-2 data triage** scores every channel (coverage, variance, link to maintenance events) and **drops uninformative ones**. At each gate you re-prioritise the effort. |
| **Your engineers are scarce** | **Your time is capped at half a day (4 h) per week**: one 2 h review, the rest as chat questions. No pairing. We work alone between reviews. |

> Honest unknown: we do not yet know how many failure events are labelled in Snowflake. The week-2 triage reports this, and the gate decides how far indicators can go.

---

# Plan: 8 weeks maximum, three gates, three milestones

| Week | Work | Gate and milestone |
|---|---|---|
| **1** | Access, data inventory, confirm Q1 freeze dates | |
| **2** | **Data triage:** score every channel, drop uninformative ones | **M1** triage report |
| **3** | **Working demo on your real data** | **Gate 1 (go/no-go) · M2** |
| **4–5** | Failure patterns, indicators with reasons | **Gate 2:** re-prioritise or stop |
| **6** | Technician walkthrough, roadmap, handover | **M3** final report |
| **7–8** | Reserve if Gate 2 asks for it, same price | |

**Q1 change freeze:** the work only reads data and writes to a sandbox schema, so it needs no production change. Roadmap go-lives are scheduled after the freeze.

---

# Team: two seniors, fully on this

| | Senior data scientist (industrial) | Data engineer (Snowflake) |
|---|---|---|
| **Experience** | 10 years; condition monitoring, failure analysis, survival modelling | 9 years; Snowflake pipelines, sensor and time-series data |
| **Certifications** | SnowPro Core · SnowPro Advanced: Data Scientist | SnowPro Core · SnowPro Advanced: Data Engineer |
| **Languages** | Finnish (native), English | Finnish (native), English |
| **Availability** | Full-time for the engagement; start date fixed at signature | Full-time for the engagement; start date fixed at signature |

A senior Recordly architect reviews methods at each gate. Recordly employees only, no subcontractors.

---

# Price and terms

| | |
|---|---|
| **Fixed total** | **€24,480 (excl. VAT)** · 14 data scientist days × €960 + 12 data engineer days × €920 |
| **Invoicing** | **Per accepted milestone:** M1 triage 27% · M2 week-3 demo 27% · M3 final 46% of the total |
| **Included** | Roadmap, technician walkthrough, documentation, travel to Espoo |
| **Licences** | None. Your Snowflake only. No data leaves it. |
| **Contract** | **Accepted as written: 60 days net, 3% per started week late (cap 10%), 7 days' written termination. No deviations.** |

> Fixed price: effort above plan is Recordly's risk. Your staff time stays within half a day a week.

<!-- coverage: RFP outcome (failure patterns, PdM indicators, roadmap) -> s1,s2,s4; Snowflake only/no new tools/no data leaves/US platform concern -> s2,s6; hidden req alert flags unexplained -> s2,s3 (reason per flag, technician walkthrough wk6); locked breakdown -> s3,s4 (wk2 triage, gates re-prioritise); previous review: working demo real data -> s2,s4 wk3 gate; training/in-workflow onboarding -> s3; process modelling position -> s2; Q1 freeze -> s4; half day/week cap -> s3,s6; milestone invoicing -> s6; terms 60d/3% cap10%/7d accepted -> s6; team roles+certs -> s5; honest unknown -> s3; no VDE; no AI add-ons; roles only. Price 14*960+12*920=24480; milestones 6560/6600/11320 (27/27/46%) -->
