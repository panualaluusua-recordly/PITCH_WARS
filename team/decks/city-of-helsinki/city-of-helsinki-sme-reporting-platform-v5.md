<!-- title: City of Helsinki · SME Reporting Platform -->
# SME reporting platform: technical briefing

## Fixed discovery, then a capped build you steer. €43,440 maximum, firm for 9 months. Standard agreement, no deviations.

| You told us | Our answer |
|---|---|
| Council scrutiny of agency markups | **One rate card, no markup.** Every euro is days × rate |
| One rigid lump sum is uneasy | **Fixed discovery, then a capped build.** Scope shifts inside the cap |
| Legacy quirks surface late | **Weeks 1–2 probe raw tables first.** A gate decides the build |
| **Mandatory:** on site 2+ days a week | **Team coverage on site every Tue and Thu; specialists attend within their allocated days** |
| **Mandatory:** prices firm 9 months | **Binding for 9 months from submission** |

Proposal to Kari Voutilainen, Head of Data and Analytics Architecture · Recordly Oy · Helsinki

---

# Technical solution: from SAP record to self-service report

<div style="display:flex;gap:12px;align-items:stretch;margin:0.2em 0 0.3em 0"><div style="flex:1;border:2px solid #434343;border-radius:10px;padding:14px 16px;background:#232323;display:flex;flex-direction:column;gap:10px"><div style="font-weight:800;color:#E3FF87;font-size:0.66em;text-transform:uppercase;letter-spacing:0.05em">1 · Extract</div><div style="border:2px solid #E3FF87;border-radius:6px;padding:8px 12px;font-size:0.68em;line-height:1.25;color:#EFEFEF">SAP S/4HANA Cloud: released CDS views and OData, incremental loads, no custom ABAP</div><div style="border:2px solid #E3FF87;border-radius:6px;padding:8px 12px;font-size:0.68em;line-height:1.25;color:#EFEFEF">City's current data setup</div><div style="border:2px solid #E3FF87;border-radius:6px;padding:8px 12px;font-size:0.68em;line-height:1.25;color:#EFEFEF">Conventions from our earlier City squad work, reused where they fit</div><div style="margin-top:auto;border-top:2px solid #434343;padding-top:8px;font-size:0.62em;line-height:1.25;color:#D4D4D4"><b>Done when:</b> Row counts reconcile to source</div></div><div style="align-self:center;color:#E3FF87;font-size:1.4em;font-weight:800">→</div><div style="flex:1;border:2px solid #434343;border-radius:10px;padding:14px 16px;background:#232323;display:flex;flex-direction:column;gap:10px"><div style="font-weight:800;color:#E3FF87;font-size:0.66em;text-transform:uppercase;letter-spacing:0.05em">2 · Model · your current data setup</div><div style="border:2px solid #E3FF87;border-radius:6px;padding:8px 12px;font-size:0.68em;line-height:1.25;color:#EFEFEF">Raw → cleaned → business-ready</div><div style="border:2px solid #E3FF87;border-radius:6px;padding:8px 12px;font-size:0.68em;line-height:1.25;color:#EFEFEF">One definition per SME KPI, documented in Finnish</div><div style="margin-top:auto;border-top:2px solid #434343;padding-top:8px;font-size:0.62em;line-height:1.25;color:#D4D4D4"><b>Done when:</b> Automated tests pass on every load</div></div><div style="align-self:center;color:#E3FF87;font-size:1.4em;font-weight:800">→</div><div style="flex:1;border:2px solid #434343;border-radius:10px;padding:14px 16px;background:#232323;display:flex;flex-direction:column;gap:10px"><div style="font-weight:800;color:#E3FF87;font-size:0.66em;text-transform:uppercase;letter-spacing:0.05em">3 · Serve · your BI tool</div><div style="border:2px solid #E3FF87;border-radius:6px;padding:8px 12px;font-size:0.68em;line-height:1.25;color:#EFEFEF">Certified SME dashboards</div><div style="border:2px solid #E3FF87;border-radius:6px;padding:8px 12px;font-size:0.68em;line-height:1.25;color:#EFEFEF">Self-service semantic model, <b>row-level security</b> per unit, access test per unit before go-live</div><div style="margin-top:auto;border-top:2px solid #434343;padding-top:8px;font-size:0.62em;line-height:1.25;color:#D4D4D4"><b>Done when:</b> SME team builds its own report unaided</div></div><div style="align-self:center;color:#E3FF87;font-size:1.4em;font-weight:800">→</div><div style="flex:1;border:2px solid #434343;border-radius:10px;padding:14px 16px;background:#232323;display:flex;flex-direction:column;gap:10px"><div style="font-weight:800;color:#E3FF87;font-size:0.66em;text-transform:uppercase;letter-spacing:0.05em">4 · Find · your catalog</div><div style="border:2px solid #E3FF87;border-radius:6px;padding:8px 12px;font-size:0.68em;line-height:1.25;color:#EFEFEF">Owner, Finnish description, refresh time</div><div style="border:2px solid #E3FF87;border-radius:6px;padding:8px 12px;font-size:0.68em;line-height:1.25;color:#EFEFEF">Lineage from every figure back to the SAP table</div><div style="margin-top:auto;border-top:2px solid #434343;padding-top:8px;font-size:0.62em;line-height:1.25;color:#D4D4D4"><b>Done when:</b> Anyone can trace a figure to its source</div></div></div><div style="margin:12px 0 0.7em 0;background:#2b3118;border-left:6px solid #E3FF87;padding:8px 14px;font-size:0.64em;color:#EFEFEF"><b>Access and data handling:</b> City-issued read-only accounts · code, tests and runbooks in the City's repos and cloud tenant · no data copy outside the tenant · access removed at close</div>

**Out of scope:** new platforms or licences, AI features, other service areas.

> **Honest unknown:** the RFP does not name the current data setup, BI tool or catalog, and legacy tables hide quirks. Week 1 confirms the stack; the week 2 gate sizes the build.

---

# Plan and team: 10 weeks, your engineers pair with us from day 1

| Weeks | Work | With your team |
|---|---|---|
| **1–2 Discovery (fixed)** | KPI workshop with the SME team, source probing, data model. City-issued access and NDA before any extraction. **Go/no-go gate:** 3 priority SME KPIs trace to raw SAP tables, row counts reconcile, data-quality issues listed and sized. Fail: re-scope or stop | City engineers join probing and design decisions |
| **3–7 Build** | SAP and current-data pipelines, core model, first dashboard in use by week 5. KPIs ranked at the gate: if work grows, the lowest-ranked move out first | Pair programming, City co-owner per pipeline |
| **8–10 Rollout** | Remaining KPIs, self-service model, access test per unit, Finnish runbooks and training | City engineers lead, we review |

| Role | Required expertise and certifications | Days |
|---|---|---|
| Senior data engineer (lead) | SAP S/4HANA Cloud extraction. Azure Data Engineer Associate · Databricks Data Engineer Professional. Finnish, English | 30 |
| Senior data analyst (BI) | semantic models, public-sector self-service. Power BI Data Analyst Associate · Fabric Analytics Engineer Associate. Finnish, Swedish, English | 14 |
| Data architect (review) | TOGAF 9 Certified. Finnish, English | 2 |

Helsinki-based, on site Tue and Thu, target start at signature, subject to verification. Short written note every two weeks, no recurring status meetings.

---

# Price and terms

## Maximum total €43,440 (excl. VAT), firm and binding for 9 months from submission

| Role | Days | Day rate | Amount |
|---|---|---|---|
| Senior data engineer | 30 | €920 | €27,600 |
| Senior data analyst (BI) | 14 | €1,000 | €14,000 |
| Data architect | 2 | €920 | €1,840 |
| **Total** | **46** | | **€43,440** |

| Part | How it is charged |
|---|---|
| **Discovery, weeks 1–2** | **Fixed fee €10,440** (11 days) |
| **Build, weeks 3–10** | **Capped at €33,000** (35 days). Billed on actual days at the same rates, never above the cap. Unused days are not billed |

- Scope changes found at the gate or later are swapped **inside the cap**, with no change request
- Invoiced monthly, payment per the City's standard agreement. Travel and on-site days included
- No new licences. Built on the City's existing platform
- **City's standard purchase agreement as is. No deviations, no tracked changes**


**Staffing review / Rauno:** role profiles are requirements, not verified people. Confirm CVs, certificates, languages and actual availability before submission. One day = 8 hours; DE minimum EUR 115/h, DA EUR 125/h, AI expertise adds EUR 5/h for the relevant specialist. Architect base EUR 115/h is proposed for owner confirmation, not a user-supplied minimum. At most two architects. Validate fixed scope and risk allowance before commitment.

<!-- coverage:
RFP: technical solution -> slide 2; implementation plan -> slide 3; team qualifications -> slide 3 (roles + certs); transparent price breakdown -> slide 4 (days x rate table, fixed vs capped).
Mandatory: on site >=2 days/wk -> slide 1 + 3 (Tue+Thu); prices firm 9 months -> slide 1 + 4.
Hidden: heavy markups for global agency letterheads -> rate card, no markup (slide 1, 4); monolithic lump sum -> fixed discovery + capped build; legacy quirks -> weeks 1-2 probe + gate; council scrutiny -> transparent days x rate; <5 slides -> 4 slides.
v4 tech: slide 2 table -> architecture diagram with done-when per step + access band (P5, P6, P7, P15, compliance); slide 3 discovery row carries access precondition and gate pass criteria (P3), build row KPI ranking (P4), rollout access test (P5).
Earlier praise kept: standard agreement/no deviations, pairing from week 1, Finnish runbooks, catalog/lineage (step 4), no AI, source gate.
Rate floor: DE 920, DA 1000, architect 920 (1 architect). 46 days, avg ~EUR 944/day = EUR 118/h.
Checks: 10,440 + 33,000 = 43,440; discovery days 6 DE + 4 DA + 1 arch = 5,520+4,000+920 = 10,440; build 24 DE + 10 DA + 1 arch = 22,080+10,000+920 = 33,000.
-->
