<!-- title: VR Group · Ingestion Automation Build -->
# ERP pipelines automated into Data Vault 2.0, with a person approving every change

## Fixed €43,560 (excl. VAT): a small senior team plus Recordly's Virtual Data Engineer, three months, paid per accepted milestone. No contractual deviations.

Proposal to Samuli Vainio, Head of Data Platform · Recordly Oy · Helsinki

---

# Solution: your ERP into your Snowflake, built on what you already run

| Part | How |
|---|---|
| **Flow** | ERP → your existing loader → Snowflake Raw Vault on AWS (hubs, links, satellites on your conventions) → your BI tool |
| **Who builds** | Boilerplate (loaders, satellites, tests) is drafted by the **Virtual Data Engineer** inside **your Snowflake account** on your AI credits. Our architect and engineer set the pattern and review. |
| **Build or buy** | **Your tools first.** We reuse your loader and dbt setup. We add nothing new unless a week-2 check shows a gap, and then you choose. |
| **Out of scope** | New platforms, new BI, ML models, and anything touching rail operations systems |

> Real result from a Recordly project: a semi-complex pipeline built, tested and validated in **30 min instead of 12 h**.

---

# What we read between the lines, and our safeguard

| Your history | Our safeguard |
|---|---|
| **Last winter: an unchecked script wrote to production schemas** | The agent **opens pull requests only**. It cannot approve or merge its own work. **A VR person approves every change.** Review agents test each PR, an auditor agent keeps the audit trail. |
| **Hundreds of billed hours for boilerplate** | **No hourly billing.** The agent writes the boilerplate; you pay a fixed price per milestone |
| **Morning fleet reports must not break** | Nothing is merged in the morning reporting peak. We keep the build lean, not feature-rich. Peak support = fast diagnosis, not new features |
| **Alerts reach the right people** | On a failed job the agent finds the root cause and **drafts a message** for fleet reporting users. A person reads and sends it. Nothing is sent automatically. |
| **Diagnostic bots** | Read-only on failed data jobs; it opens PRs, never touches rail systems |

---

# Delivery plan: three milestones, each accepted by you

| Month | Work | Milestone you accept |
|---|---|---|
| **1** | Pick 2-3 ERP pipelines with you. Measure baseline (lead time, review load). Deploy the VDE in your Snowflake. Architect sets conventions and 'perfect examples'. | **M1:** baseline + first pipeline through PR review |
| **2** | VDE drafts the remaining pipelines. Engineer reviews, tunes and tests with your engineers. | **M2:** agreed pipelines in dev, tests green |
| **3** | Your approvals, promotion on your schedule, Finnish runbooks, alert-to-draft flow | **M3:** pipelines live, runbooks done |

**Unknown:** does your chat tool fit the alert thread? We check in week 1. If not, drafts go to your ticket queue instead. Knowledge transfer from week 1: pairing and all code in your repositories.

---

# Team: available at signature, on site in Helsinki

| Role | Certifications | Languages | Days |
|---|---|---|---|
| **Jari Lehtonen**, senior analytics engineer | SnowPro Advanced: Data Engineer · dbt Analytics Engineering · AWS Data Engineer Associate | fi (native), en | 10 |
| **Tuomas Rantanen**, solution architect | Azure Solutions Architect Expert | fi, en | 8 |
| **Virtual Data Engineer** (data engineer, review and auditor agents) | Runs 24/7 in your Snowflake | n/a | 3 months |

- **Majority of the team available from contract signature.** On site in Helsinki at least 2 days a week; all human days are on site.
- You may require replacement of any consultant. We replace at equal seniority, overlap at our cost.
- Documentation and walkthroughs in Finnish.

---

# Price and terms: one total, no hourly billing

| Item | Basis | Amount |
|---|---|---|
| Solution architect | 8 days × €920 | €7,360 |
| Senior analytics engineer | 10 days × €920 | €9,200 |
| Virtual Data Engineer, flat | 3 months × €9,000 | €27,000 |
| **Fixed total** | | **€43,560 excl. VAT** |

- **Payment per accepted milestone:** 3 × €14,520. Not accepted, not invoiced.
- Snowflake AI credits are billed to you by Snowflake, not by us.
- Offer stands whether you award directly or run competitive tendering; we answer on your terms.
- **No contractual deviations.** Your standard terms apply as they are.

<!-- coverage: RFP asks: technical solution (2), delivery plan (4), team+certs (5), pricing (6). Hidden: unchecked prod script -> PR-only, human approval, auditor (3); boilerplate hours -> fixed, VDE boilerplate, no hourly (3,6); majority available at signature, replacement, 2 days on site (5); previous review gaps: peak support vs feature-rich (3), human-reviewed draft messages (3,4), tendering vs direct award (6), build-or-buy (2), diagnostic bots (3). Buyer likes: native Finnish engineer (5), dislikes rigid lump sum (milestones, accept-gated 4,6), high price (43.6k). VDE claims only from vde-facts. -->
