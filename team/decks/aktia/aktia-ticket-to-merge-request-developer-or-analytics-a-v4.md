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
| Migration Matillion + Redshift → dbt + Snowflake, jobs included (a migration cost, not a cost per ticket) | **~30 Snowflake credits** per migrated table |
| Pipeline and availability questions answered in the chat thread | Developer context switches per day: **several → 0** |

> These are our results, not Aktia's. Your own baseline (ticket lead time, review load) is measured in Definition, so the pilot is judged on your numbers.

---

# Technical solution architecture

## The agent drafts, a person merges. One loop inside Aktia's tenant, with no path around review.

<div style="display:flex;align-items:stretch;gap:10px;margin:0.1em 0 0.4em 0;font-size:0.6em;line-height:1.22">
<div style="flex:1;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:12px"><b style="color:#E3FF87">1 · AKTIA'S INPUTS</b><div style="border:1px solid #E3FF87;border-radius:6px;padding:6px 8px;margin-top:8px">Analytics ticket in your ticket system. Never from chat</div><div style="border:1px solid #E3FF87;border-radius:6px;padding:6px 8px;margin-top:6px">Data model and conventions in your Git repo</div><div style="border:1px solid #E3FF87;border-radius:6px;padding:6px 8px;margin-top:6px">Analytics layer in dev, masked where needed. No Temenos or production access</div></div>
<div style="align-self:center;color:#E3FF87;font-size:2em">&rarr;</div>
<div style="flex:1;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:12px"><b style="color:#E3FF87">2 · AGENT IN YOUR TENANT</b><div style="border:1px solid #E3FF87;border-radius:6px;padding:6px 8px;margin-top:8px">Data engineer agent plans, writes code and tests</div><div style="border:1px solid #E3FF87;border-radius:6px;padding:6px 8px;margin-top:6px">Model behind one swappable interface</div><div style="border:1px solid #E3FF87;border-radius:6px;padding:6px 8px;margin-top:6px">Unclear ticket: questions back, no guessing</div></div>
<div style="align-self:center;color:#E3FF87;font-size:2em">&rarr;</div>
<div style="flex:1;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:12px"><b style="color:#E3FF87">3 · REVIEW AND LOG</b><div style="border:1px solid #E3FF87;border-radius:6px;padding:6px 8px;margin-top:8px">Review agents and tests on every change. Failures go back</div><div style="border:1px solid #E3FF87;border-radius:6px;padding:6px 8px;margin-top:6px">Schema-dependency paths flagged (CODEOWNERS)</div><div style="border:1px solid #E3FF87;border-radius:6px;padding:6px 8px;margin-top:6px">Auditor agent logs every action to your log store, append-only</div></div>
<div style="align-self:center;color:#E3FF87;font-size:2em">&rarr;</div>
<div style="flex:1;background:#E3FF87;color:#1B1B1B;border-radius:10px;padding:12px"><b>4 · AKTIA DECIDES</b><div style="border:1px solid #1B1B1B;border-radius:6px;padding:6px 8px;margin-top:8px">Pull request: diff, test evidence, reasoning</div><div style="border:1px solid #1B1B1B;border-radius:6px;padding:6px 8px;margin-top:6px">Named reviewer, never the ticket requester, approves or rejects</div><div style="border:1px solid #1B1B1B;border-radius:6px;padding:6px 8px;margin-top:6px"><b>Only a person merges.</b> Deploy via your pipeline</div></div>
</div>
<div style="background:#2A2A2A;border:2px dashed #E3FF87;border-radius:10px;padding:8px 14px;font-size:0.6em;margin-bottom:0.5em"><b style="color:#E3FF87">PERMISSIONS:</b> Aktia-issued identities, secrets in your vault. The agent writes only to its own branches and a dev schema, holds no production credentials, cannot approve, merge or change branch rules (owned by Aktia admins). Kill switch on its identity.</div>

:::cols
- **Your stack, honestly:** the RFP says "current data setup" and "public cloud"; ticket system and Git host are assumed. **Week 1 confirms all three.** On Snowflake + dbt we deploy our agent team. On another stack the agent is a new build, and scope is re-agreed at the gate. You can stop there.
:::col
- **Out of scope:** ML models or anomaly detection, new BI tools, extra use cases, any change to Temenos Transact. Only ticket → code → tests → pull request.
:::

---

# Compliance posture: FIN-FSA, EBA, DORA

| What you told us | What we build in |
|---|---|
| **Last winter a script bypassed peer review and altered schema dependencies** | The agent **cannot approve or merge its own work.** Branch protection needs a named Aktia reviewer who is not the requester. Schema-dependency changes are blocked until the data owner approves. Week 1 bypass test: pushing or merging as the agent must fail |
| **Supervisors scrutinise foreign-headquartered AI API dependencies** | EU residency alone does not remove a foreign-HQ provider. Definition compares three hosting options with what each leaves: open-weight model in your tenant (no outside call); EU-headquartered provider; hyperscaler or Snowflake-hosted model in an EU region (foreign-HQ provider). **Aktia compliance chooses.** One swappable interface, exit tested |
| **AI governance and operational resilience** | Audit log in your log store, append-only, retention per your policy. A bad merge is reverted by a normal revert PR and logged in your DORA incident process. The agent stops when stuck. A control matrix maps each control to FIN-FSA, EBA and DORA requirements. Aktia compliance signs it off; we do not certify |
| **Runbooks in English caused friction** | Matrix, runbooks and training in **Finnish and Swedish** |
| **IP** | Everything made for Aktia (code, prompts, conventions, docs) is Aktia's property, stated in the contract |

---

# Technical gates and failure risks

## Three gates before the agent touches real work

- **Week 1, integrations:** stack, ticket system, Git host and CI confirmed; bypass test passes
- **Week 3, Definition gate:** hosting options run on 20 of your tickets, reported with their exposure; Aktia picks one or stops. Baseline: rework rate, review minutes, lead time
- **Week 9, pilot gate:** approved-without-rework rate, review minutes and cost per ticket vs. baseline. Targets set at week 3; a miss means stop or adjust

| Failure risk | What we do |
|---|---|
| Plausible but wrong PR; reviewer fatigue | Reasoning in every PR; review minutes and approval trend tracked; sampled second review |
| Prompt injection or vague ticket | Ticket is untrusted input; worst case is a PR a person rejects; unclear tickets go back |
| Flaky tests give a false green | Tests re-run; a pass a reviewer rejects is counted and reviewed |
| Model or provider changes behaviour | Pinned versions; your test set replayed before any switch; worse result blocks release |
| No model option good enough or accepted | Scope narrows to simple ticket types, or Aktia stops at the gate |
| Agent loops or gets stuck | Retry cap; it stops and writes what it tried |

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
| **Delivery** | 4–9 | Conventions and "perfect examples" written with your engineers. Agent team deployed in your tenant. Supervised pilot on the chosen ticket types | Merged-without-rework rate, test pass rate, review minutes per PR, run cost per ticket vs baseline. Targets set at week-3 gate; a miss means stop or adjust |
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
- **Licences:** none from Recordly. Model compute is billed to Aktia under the hosting option Aktia compliance chooses (on Snowflake, as AI credits on your account)
- **No contractual deviations.** Aktia's standard terms and key-person penalties accepted


**Staffing review / Rauno:** role profiles are requirements, not verified people. Confirm CVs, certificates, languages and actual availability before submission. One day = 8 hours; DE minimum EUR 115/h, DA EUR 125/h, AI expertise adds EUR 5/h for the relevant specialist. Architect base EUR 115/h is proposed for owner confirmation, not a user-supplied minimum. At most two architects. Validate fixed scope and risk allowance before commitment.

Architect effort: definition 5 days + setup 8 + run review 3 = 16 days, including the AI premium. DE 12 + AI engineer 8 = 36 human days total. Customer approves run changes.

<!-- coverage: supplier profile/financial/subcontractors=s2; case examples=s2; architecture=s3; compliance FIN-FSA/EBA/DORA=s4; post-mortem script bypassing review=s3,s4,s5; foreign-HQ AI API=s3,s4 (hosting options with residual exposure); tech gates + failure risks=s5; team FI/SV=s6; plan/timeline=s7; pricing definition/delivery/ongoing ops=s8; ML add-on trap (lost previous)=s3 out of scope; key-person praised=s6; written updates instead of status meetings=s7; FI/SV docs=s4; IP buy-out=s4; code in Aktia tenant=s3; stack unknown=s3,s5,s7; no deviations=s8. Placeholders to verify: financials, years, certs, Swedish reviewer. v4 tech lane: team/tech/slides/aktia.md -->
