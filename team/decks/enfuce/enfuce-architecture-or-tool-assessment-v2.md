<!-- title: Enfuce · Architecture and Tool Assessment -->
# Find where delivery really stalls: handoffs first, tools second

## An org-wide assessment of your bottlenecks, pipelines and toolchain, run at your Espoo whiteboards. 4 weeks, €20,240 fixed, excl. VAT. No contractual deviations.

Proposal to Kari Holmberg, VP of Data & Analytics · Recordly Oy · Helsinki

---

# Recommended solution: measure the friction, then rank the fixes

## Your own reviews say handoffs, sign-offs and routines cause most of the friction. So we measure those first.

| Step | What we do | Evidence |
|---|---|---|
| **1 · Map** | One handoff map per squad: every handoff and sign-off from request to production | Squad sessions at the whiteboard, ticket and PR history |
| **2 · Measure** | Wait time vs work time per stage. Pipeline failures, reruns, manual steps. Duplicate cardholder profiles baseline. | Snowflake usage history, AWS job logs, Looker usage |
| **3 · Rank** | Each bottleneck scored on days lost per month and effort to fix | Findings with a number each |
| **4 · Recommend** | Ownership split across squads, templated infrastructure, sign-off stages cut or automated | Roadmap with owners |

**Out of scope:** building, new tools, the card-issuing platform internals. We assess how data leaves it.

---

# What we read between the lines

| Your signal | How the assessment answers it |
|---|---|
| **Handoffs, sign-offs and routines** cause the bulk of friction | Process is the lead lens, not an add-on. Every sign-off stage gets a wait time. |
| Teams **with platform background avoided the learning curve** | We do not claim card-issuing platform experience. Two sessions in week 1 with your platform experts; they stay our reference for anything on that side. |
| **Duplicate profiles, mismatched IDs** hurt earlier | Identity layer is the first pipeline we measure: duplicate rate, ID mismatches, where they enter. |
| **Single central squad** is a bottleneck | Recommendations assume ownership split across squads, with data contracts and codeowners. |
| Fragile, handcrafted pipelines | We check what deploys from repeatable Terraform and CI/CD, and what does not. |
| No bureaucracy | No steering committee, no review rounds from us. One written finding per squad; you decide. |

---

# Proposed delivery roles and platform requirements

| | Lead Data Architect | Senior Data Engineer (Snowflake) |
|---|---|---|
| **Required certificates** | SnowPro Advanced: Architect · AWS Certified Solutions Architect - Professional | SnowPro Core · AWS Certified Data Engineer - Associate · HashiCorp Certified: Terraform Associate |
| **Days** | 12 | 10 |
| **Required languages** | Finnish required, English | Finnish required, English |
| **Availability** | **Target at signature; verification pending** | **Target at signature; verification pending** |

On site in Espoo three days a week in weeks 1 to 3. Your platform experts and one contact per squad give us the context. Replacement of either consultant on request, equal seniority.

---

# Implementation roadmap: 4 weeks, 22 person-days

| Week | Work | Output |
|---|---|---|
| **1** | Kick-off in Espoo. Platform expert sessions. Handoff mapping with every squad. Read access requested day 1. | Handoff maps |
| **2** | Measurements from logs and history. Duplicate baseline. | **Quick wins list:** fixes needing no new tool |
| **3** | Ranking, options for ownership split and sign-off changes, checked with squads | Ranked bottlenecks |
| **4** | Roadmap with owners, effort in days and expected days saved | Written findings and read-out |

> **Honest unknowns:** which logs exist (settled in week 1; where none exist we estimate from interviews and mark confidence low). Number of squads: plan assumes up to six. More squads or access delays change days and price only by agreement.

**Option after the assessment, not in this price:** if the findings confirm backlog in simple pipeline work and reviews, our Snowflake-native Virtual Data Engineer can take that work inside your account, every change approved by your people. Benchmark: a semi-complex pipeline build, test and validation went from 12 hours to 30 minutes.

---

# Pricing model

## Fixed total: €20,240 (excl. VAT)

| Role | Person-days | Day rate (8 h) |
|---|---|---|
| Lead Data Architect | 12 | €920 |
| Senior Data Engineer (Snowflake) | 10 | €920 |
| **Total** | **22 days** | **22 × €920 = €20,240** |

- **Invoicing:** one invoice on delivery of the written findings; payment on your standard terms
- **Fixed price:** effort above plan is Recordly's risk. Travel to Espoo included.
- **Licences:** none. Read access to your existing tools only.
- **Contract:** Enfuce's standard terms as they are. **No contractual deviations.**


**Staffing basis:** one person-day is 8 hours. DE EUR 115/h; DA EUR 125/h; required AI expertise adds EUR 5/h for the relevant role. Architect and other-role base EUR 115/h is a proposed commercial rate for owner review. The team has at most one architect and complementary roles. CVs, credentials, language proficiency, actual availability and exact start dates remain unverified. These are role requirements, not booked people. Fixed-price scope, client dependencies and risk allowance need agreement before commitment.

<!-- coverage: RFP asks in order: recommended solution = slide 2; proposed delivery team = slide 4; implementation roadmap = slide 5; pricing model = slide 6; evaluate architectural bottlenecks / pipelines / toolchain across all teams = slide 2 table. Hidden: handoffs/sign-offs/routines friction = slide 2 intro, step 1-2, slide 3 row 1; platform experience gap = slide 3 row 2 (no claim, pairing, ramp-up week 1); budget undisclosed -> propose low, 22 pd x 920. Previous win carried: identity/dedup first (slide 2 step 2, slide 3 row 3), builders on site at Espoo whiteboards (slide 1, 4, 5), no fluff (slide 3 last row, short), distributed ownership (slide 3 row 4), Terraform templates (row 5), honest unknowns (slide 5), "Stop asking for reviews" (slide 3 last row). VDE = MENTION on slide 5 only, unpriced. -->
