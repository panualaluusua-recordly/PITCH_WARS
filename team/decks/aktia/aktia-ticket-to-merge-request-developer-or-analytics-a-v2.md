<!-- title: Aktia · Ticket-to-Merge Analytics Developer Agent -->
# Analytics tickets in, reviewed pull requests out

## An agent that drafts the code. Your people approve every change. Everything stays in Aktia's perimeter. €61,080 fixed total, Aktia's standard terms.

Proposal to Camilla Engblom, Head of Data and Analytics · Recordly Oy · Helsinki

---

# Supplier profile, financial standing, subcontractors

| | |
|---|---|
| **Supplier** | Recordly Oy, Helsinki. Data and AI consultancy. Our own agent product, the Virtual Data Engineer, is the pattern we propose here |
| **Financial standing** | Latest financial statements and a third-party credit report supplied with the formal tender |
| **Subcontractors** | **None.** Recordly employees only. Any later change needs Aktia's written approval |

## Concrete AI implementation case examples

| Case (Recordly agent team on Snowflake + dbt) | Measured result |
|---|---|
| Semi-complex pipeline: build, test, validate. A person approves the PR | **12 h by hand → 30 min** |
| Migration Matillion + Redshift → dbt + Snowflake, jobs included | **~30 Snowflake credits** per migrated table |
| Pipeline and availability questions answered in the chat thread | Developer context switches per day: **several → 0** |

> These are our results, not Aktia's. Your own baseline (ticket lead time, review load) is measured in Definition, so the pilot is judged on your numbers.

---

# Technical solution architecture

## One loop, inside Aktia's cloud tenant. The agent never merges.

<div style="display:flex;align-items:stretch;gap:12px;margin:0.2em 0 0.5em 0;font-size:0.68em;line-height:1.25"><div style="flex:1;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:14px"><b style="color:#E3FF87">1 · TICKET</b><br>Analytics ticket in your ticket system. Changes start only here, never from chat</div><div style="align-self:center;color:#E3FF87;font-size:2em">&rarr;</div><div style="flex:1;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:14px"><b style="color:#E3FF87">2 · DATA ENGINEER AGENT</b><br>Reads ticket and your data model, plans the change, writes transformation code and tests in a dev environment</div><div style="align-self:center;color:#E3FF87;font-size:2em">&rarr;</div><div style="flex:1;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:14px"><b style="color:#E3FF87">3 · REVIEW AGENTS</b><br>SQL, dbt and general review. Tests run on every change. Failures go back for fixes</div><div style="align-self:center;color:#E3FF87;font-size:2em">&rarr;</div><div style="flex:1;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:14px"><b style="color:#E3FF87">4 · PULL REQUEST</b><br>Diff, test evidence and reasoning summary in your repository</div><div style="align-self:center;color:#E3FF87;font-size:2em">&rarr;</div><div style="flex:1;background:#E3FF87;color:#1B1B1B;border-radius:10px;padding:14px"><b>5 · AKTIA REVIEWER</b><br>A named person approves or rejects. <b>Only a person merges</b></div></div>
<div style="background:#2A2A2A;border:2px dashed #E3FF87;border-radius:10px;padding:10px 16px;font-size:0.68em;margin-bottom:0.6em"><b style="color:#E3FF87">AUDITOR AGENT, ALWAYS ON:</b> keeps the log of every action and the agent's reasoning and reports deviations. Code, data, logs and model calls stay in Aktia's tenant. Temenos Transact is read for reporting data only; no core changes.</div>

:::cols
- **Your stack, honestly:** the RFP says "current data setup" and "public cloud". Our proven pattern runs in Snowflake with dbt. **Definition week 1 confirms what you run.** If it is not Snowflake + dbt, we adapt the same guardrails to your stack and re-agree scope at the gate. You can stop there.
:::col
- **Out of scope:** ML models or anomaly detection, new BI tools, extra use cases, any change to Temenos Transact. Only ticket → code → tests → pull request.
:::

---

# Compliance posture: FIN-FSA, EBA, DORA

| What you told us | What we build in |
|---|---|
| **Last winter a script bypassed peer review and altered schema dependencies** | The agent **cannot approve or merge its own work.** Branch protection needs a named Aktia reviewer. Changes touching schema dependencies are labelled and need the data owner |
| **Supervisors scrutinise foreign-headquartered AI API dependencies** | Definition delivers model-hosting options: models served in your own tenant in an EU region, no ticket text, code or data to external APIs, every provider named with an exit plan |
| **AI governance and operational resilience** | Auditor agent keeps the audit trail. The agent stops when stuck instead of improvising. A control matrix maps each control to FIN-FSA, EBA and DORA requirements. Aktia compliance signs it off; we do not certify |
| **Runbooks in English caused friction** | Matrix, runbooks and training in **Finnish and Swedish** |
| **IP** | Everything made for Aktia (code, prompts, conventions, docs) is Aktia's property, stated in the contract |

**Unknown we will test:** whether an EU-hosted model is good enough on your tickets. Decided at the Definition gate with numbers.

---

# Core team: three seniors who do the work

| | Lead Data Architect | Senior Data Engineer | Senior AI Engineer |
|---|---|---|---|
| **Required certifications** | SnowPro Advanced: Architect · dbt Analytics Engineering | SnowPro Core · dbt Analytics Engineering | SnowPro Core · Microsoft Certified: Azure AI Engineer Associate |
| **Required languages** | Finnish required, Swedish, English | Finnish required, English | Finnish required, English |
| **Availability** | From signature, start date fixed in the contract | From signature | From signature |

- **Swedish:** every Swedish deliverable is reviewed by a native Swedish speaker before delivery
- **Key-person terms:** named people, substitution only with Aktia's approval, equal seniority, overlap at our cost, financial penalty if breached. Aktia may require replacement at any time

---

# Delivery plan and timeline

| Phase | Weeks | What happens | Gate |
|---|---|---|---|
| **Definition** | 1–3 | Confirm stack. Baseline on 20–30 recent tickets. Control matrix (FI/SV). Model-hosting options. Pick 2–3 ticket types | **Aktia decides go/no-go** |
| **Delivery** | 4–9 | Conventions and "perfect examples" written with your engineers. Agent team deployed in your tenant. Supervised pilot on the chosen ticket types | Pilot numbers vs baseline |
| **Ongoing operations** | 10–22 | Agent in run mode on a fixed 3-month term. **Aktia staff approve every change.** About 1 architect day per month from us | Scale, adjust or stop |

- Your engineers co-build from week 1 and own conventions, prompts and code. Nothing is handed over at the end
- **No status meetings.** Written update every two weeks
- **Unknowns:** ticket quality (unclear tickets get questions back, not guesses; measured on the baseline set) and stack fit (week 1)

---

# Preliminary pricing: definition, delivery, ongoing operations

## Fixed total: €61,080 (excl. VAT)

| Phase | Days × day rate | Amount |
|---|---|---|
| **Definition** | AI architect 5 d × €960 + AI engineer 3 d × €960 | €7,680 |
| **Delivery** | AI architect 8 d × €960 + Data engineer 12 d × €920 + AI engineer 5 d × €960 | €23,520 |
| **Ongoing operations** | Agent team 3 months × €9,000 + AI architect 3 d × €960 | €29,880 |

- **36 human days at €920–960/day**, plus the agent team on a **fixed 3-month term from go-live**. Pilot runs in Delivery are included
- **Stop after Definition** and pay only that phase. Invoiced per phase on acceptance, 21 days net
- **Licences:** none from Recordly. If you run Snowflake, AI credits are consumed on your account and billed by Snowflake
- **No contractual deviations.** Aktia's standard terms and key-person penalties accepted


**Staffing review / Rauno:** role profiles are requirements, not verified people. Confirm CVs, certificates, languages and actual availability before submission. One day = 8 hours; DE minimum EUR 115/h, DA EUR 125/h, AI expertise adds EUR 5/h for the relevant specialist. Architect base EUR 115/h is proposed for owner confirmation, not a user-supplied minimum. At most two architects. Validate fixed scope and risk allowance before commitment.

Architect effort: definition 5 days + setup 8 + run review 3 = 16 days, including the AI premium. DE 12 + AI engineer 8 = 36 human days total. Customer approves run changes.

<!-- coverage: supplier profile/financial/subcontractors=s2; case examples=s2; architecture=s3; compliance FIN-FSA/EBA/DORA=s4; post-mortem script bypassing review=s3,s4; foreign-HQ AI API=s4; team FI/SV=s5; plan/timeline=s6; pricing definition/delivery/ongoing ops=s7; ML add-on trap (lost previous)=s3 out of scope; key-person praised=s5; written updates instead of status meetings=s6; FI/SV docs=s4; IP buy-out=s4; code in Aktia tenant=s3; stack unknown=s3,s6; no deviations=s7. Placeholders to verify: financials, years, certs, Swedish reviewer. -->
