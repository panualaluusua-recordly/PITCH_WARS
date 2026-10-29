<!-- title: Kela · FinOps Review and Cost Cleanup -->
# Kela FinOps review and cost cleanup: see every resource, then clean up under your control

## First phase of eight weeks. Nothing is built before group security signs off. €23,920 fixed total, excl. VAT. No contractual deviations.

Proposal to Hannele Rantanen, Head of Data and Analytics Solutions · Recordly Oy · Helsinki

> How this deck reads: 1 What we understood · 2 Solution · 3 Requirements matrix · 4 Delivery plan · 5 Team · 6 Price and TCO

---

# 1 · What we understood, and what we do about it

## Every line below is a point from your RFP. The right-hand column is our answer, and the rest of the deck follows it in the same order.

| Your RFP says | Our answer | Slide |
|---|---|---|
| Uncatalogued systems are a career hazard | **Complete resource register with mandatory tagging**: nothing runs unlisted | 2 |
| Extraction solution for all sources | One extraction **pattern per source class**, each source assessed before we promise it | 2 |
| Group security approves before development | **Gate 1**: questionnaire in week 1, no changes before sign-off | 4 |
| Numbered requirements matrix | Every row answered with a capability confirmation | 3 |
| Advisors from private retail struggled | Public-sector practitioners; Finnish; your backlog and procedures, not ours | 5 |
| Audit: premium rates without value | One modest rate for every role, days visible, value per euro stated | 6 |

---

# 2 · Proposed solution: register first, then costs, then cleanup

## Read-only extraction from every source into one cost register in your own cloud. No data leaves your environment.

| Source class | Extraction pattern | Assessed in week 1–2 |
|---|---|---|
| **Cloud resources and billing** | Resource inventory and billing export of all accounts → **resource register** (owner, environment, tag, cost) | Access, completeness |
| **Data platform** | Platform usage, query and storage metadata → cost per workload | Metadata coverage |
| **ERP system** | Job and load schedules plus platform cost of ERP extracts, via released interfaces only | Interface, owner |
| **BI tool** | Admin and audit logs: refreshes, usage, unused reports | Log retention |

- **Mandatory tagging:** untagged resources get an owner within 10 working days or are flagged for shutdown **by the owner's approval, never by us**
- A source without a usable interface is **listed in the register as a gap with an owner**, not silently skipped
- Cost governance: budgets, alerts and a monthly review, in your existing cloud tools. **No new licences.**

---

# 3 · Requirements matrix: capability confirmation

## Your matrix was not attached to the RFP, so rows are marked (assumed). Send the real one and we map it 1:1 in week 1.

| # | Requirement (assumed) | Capability |
|---|---|---|
| F1 | Complete resource register with mandatory tagging | **Confirmed** |
| F2 | Consumption analysis by service, owner, environment | **Confirmed** |
| F3 | Extraction solution for all sources | **Confirmed as pattern**; per-source feasibility confirmed in week 2 |
| F4 | Budgets, alerts, cost-governance mechanisms | **Confirmed**, existing tools |
| F5 | Cleanup of idle and unused resources | **Confirmed**; deletion only with owner approval |
| N1 | Group security approval before development | **Confirmed**: Gate 1 |
| N2 | Audit trail: every change logged, backlog visible to you | **Confirmed** |
| N3 | Data stays in Kela's environment | **Confirmed**: read-only, no copies to Recordly |
| N4 | Finnish delivery and documentation | **Confirmed** |

---

# 4 · Delivery plan: two gates, you approve each step

| Weeks | Work | Gate and output |
|---|---|---|
| **1** | Security questionnaire submitted; read-only access request; source assessment starts. **No development.** | Questionnaire filed |
| **1–3** | Resource register, tagging gaps, consumption baseline; source assessment per slide 2 | **Gate 1:** findings report **and group security sign-off** |
| **4–8** | Cleanup in order of value: idle resources, right-sizing, tag enforcement, budgets and alerts. Each item is a backlog entry you approve first. | **Gate 2:** each change accepted by its owner |
| **8** | Finnish runbooks; your team runs the monthly review | Handover |

- Your FinOps owner pairs with us **from week 1**; a short written update each Friday, no status meetings
- **Honest unknowns:** how long group security takes (plan: sign-off by week 3; if later, the cleanup start moves, the price does not) and which cloud Kela runs (confirmed in week 1)

---

# 5 · Team: three public-sector practitioners, small and senior

| Role | Experience | Certifications | Availability |
|---|---|---|---|
| **FinOps lead architect** | 14 years in data platforms, 8 of them in Finnish public-sector registries and ERP-linked reporting | FinOps Certified Practitioner · cloud architect certification matching Kela's cloud (Azure Solutions Architect Expert, AWS Solutions Architect Professional or Google Professional Cloud Architect) | From signature, 12 days |
| **Data engineer** | 9 years; cost and performance tuning, metadata extraction, tagging automation | Microsoft Certified: Azure Data Engineer Associate (or the equivalent for Kela's cloud) | From signature, 12 days |
| **Security and audit advisor** | 12 years; public-sector audit and information security | CISA | 2 days: questionnaire and Gate 1 |

Finnish native, English. Employees only, no subcontractors. Any replacement is of equal seniority and needs your approval first. Anonymised public-sector references on request, contacts for shortlisted bidders.

---

# 6 · Price and total cost of ownership

## Fixed total: €23,920 excl. VAT = 26 person-days × €920

| Role | Days | Rate per day |
|---|---|---|
| FinOps lead architect | 12 | €920 |
| Data engineer | 12 | €920 |
| Security and audit advisor | 2 | €920 |

:::cols
### Total cost of ownership
- **Recordly fee:** the fixed total above. Travel and on-site days included, **no extras**.
- **New licences: none.** Existing cloud tools only.
- **Your time:** about 3 hours per week from your FinOps owner, plus approvals
- **After week 8:** about 1 day per month of your team for the review, no external run cost
:::col
### Value per euro
- One rate for all roles, no premium and no mark-up
- Savings are **measured against the week-3 baseline**, item by item. No percentage is promised before we see your data.
- If the cleanup removes a year of waste equal to the fee, it has paid for itself.
:::

Invoicing in two parts, on Gate 1 and on handover; payment per Kela's standard terms. **Standard terms accepted, no contractual deviations.**

<!-- coverage: RFP sections: solution (s2), team credentials (s5), delivery plan (s4), overall price (s6), numbered matrix (s3, assumed rows), TCO (s6). Hard: group security sign-off before development (s1,s4 Gate 1). Hidden: uncatalogued prototype -> resource register+mandatory tagging (s2, praised in v1); private retail advisors -> public-sector team (s5); audit premium rates -> flat modest rate + value per euro (s6); tight control of every deliverable -> backlog approvals, Gate 2 (s4). Trap: extraction for ALL sources -> pattern per class + assessment (s2). v1 fix: disjointed narrative -> numbered storyline, same order as cover strip. VDE: NO (cloud/stack unconfirmed, advisory/cleanup). -->
