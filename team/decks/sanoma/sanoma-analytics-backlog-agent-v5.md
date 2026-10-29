<!-- title: Sanoma · Analytics Backlog Agent -->
# An agent that drafts. Your engineers decide.

## Clear the analytics backlog with a pilot your team helps build, starting with a two-day hackathon. €54,440 fixed total, standard terms.

Proposal to Valtteri Salmela, Director of Data and AI Strategy · Recordly Oy · Helsinki

---

# Proposed technical solution

## The agent drafts in a sandbox. Only your engineer can merge

<div style="display:flex;align-items:stretch;gap:12px;margin:0.2em 0 0.3em 0;font-size:0.7em;line-height:1.25"><div style="flex:1;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:12px 14px"><b style="color:#E3FF87">1 · YOUR BACKLOG</b><div style="border-top:1px solid #434343;padding:5px 0">Routine ticket, 2–3 classes agreed at the hackathon</div><div style="border-top:1px solid #434343;padding:5px 0">Unclear ticket: questions back on the ticket</div><div style="border-top:1px solid #434343;padding:5px 0">No changes from chat</div></div><div style="align-self:center;color:#E3FF87;font-size:2em">&rarr;</div><div style="flex:1;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:12px 14px"><b style="color:#E3FF87">2 · AGENT, DEV SANDBOX</b><div style="border-top:1px solid #434343;padding:5px 0">Reads ticket, code and model metadata</div><div style="border-top:1px solid #434343;padding:5px 0">Plans which models change</div><div style="border-top:1px solid #434343;padding:5px 0">Writes change and tests on non-prod or masked data</div></div><div style="align-self:center;color:#E3FF87;font-size:2em">&rarr;</div><div style="flex:1;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:12px 14px"><b style="color:#E3FF87">3 · CHECKS</b><div style="border-top:1px solid #434343;padding:5px 0">Review agent: SQL and your conventions</div><div style="border-top:1px solid #434343;padding:5px 0">Your CI tests + edge-case regression set</div><div style="border-top:1px solid #434343;padding:5px 0">Retry cap, then stops and writes what it tried</div></div><div style="align-self:center;color:#E3FF87;font-size:2em">&rarr;</div><div style="flex:1;background:#E3FF87;color:#1B1B1B;border-radius:10px;padding:12px 14px"><b>4 · YOUR ENGINEER</b><div style="border-top:1px solid #1B1B1B;padding:5px 0">Merge request: diff, tests, reasoning</div><div style="border-top:1px solid #1B1B1B;padding:5px 0">Approves or rejects</div><div style="border-top:1px solid #1B1B1B;padding:5px 0"><b>Only a person merges to main</b></div></div></div><div style="background:#2B3118;border-left:6px solid #E3FF87;padding:8px 14px;margin:0 0 0.5em 0;font-size:0.66em;color:#EFEFEF">In your repository and cloud tenant: <b>branch protection with required approval by your engineers</b>, no agent merge right, no production credentials, run log and cost cap per ticket, any engineer can pause the agent</div>

**Model hosting and caps:** the model runs in your cloud tenant on your credits; tickets and code leave it nowhere. Retry cap 3 attempts per ticket; cost cap per ticket proposed on day 2 from the hackathon runs.

:::cols
- **Your stack, named after day 1:** the RFP says only "public cloud". If your warehouse is Snowflake with dbt, our running agent pattern deploys as is; otherwise the hackathon shows whether it ports, and you can stop.
- **Not a black box:** conventions, examples, prompts and the test set live in your repository. Your engineers change the rules without us.
:::col
- **Real result, one Recordly project (Snowflake + dbt):** one pipeline, build, test and validate, went from **12 h by hand to 30 min**, a person approving. Not a promise for your tickets; the pilot measures yours.
- **Out of scope:** autonomous merges, production access, new BI tools, ambiguous or new-domain requests (those stay with your analysts).
:::

---
# Human oversight, and what happens when it fails

| When this happens | The agent does | A person decides |
|---|---|---|
| **Ticket is unclear** | Asks questions on the ticket. Does not guess | Ticket owner answers |
| **Tests fail** | The review agent sends the work back, up to a set retry cap, then it stops | Engineer takes over |
| **Agent is stuck** | It stops running and writes what it tried | Engineer |
| **Edge case** | Scored first on a test set of 30–50 of your closed tickets; every rejected merge request adds a case | Reviewed weekly with your team |
| **Wrong change passes the tests** | Cannot merge. The merge request shows its reasoning for review | **Engineer rejects it** |

> We do not promise zero defects. We promise that every defect is visible before it reaches your pipeline, and a weekly count of rejected merge requests and why.

**Technical unknowns, resolved on day 1:** your warehouse and transformation tool, Git and ticket host, personal data in ticket or data samples (masking rules agreed before day 1).

---
# Implementation plan: hackathon first, then a measured pilot

| Phase | When | What happens | Gate |
|---|---|---|---|
| **1 · Co-build hackathon** | Week 1, 2 days, Helsinki | Access and a dev schema ready before day 1. Your analytics team picks 5–8 real tickets. We run the agent on them **together**, check your stack, agree the developer workflow | Feasibility note: stack fit, routine share, edge cases, baseline lead time. **Sanoma decides go/no-go**. Port check on day 1 (≤ 2 h): repo and CI access, a dev schema, a model change built and tested by hand. If any fails we say so and the plan stops there |
| **2 · Setup** | Weeks 2–3 | Your engineers write the conventions and "perfect examples" with us. Agent team deployed in your environment | Agent scored on 30–50 of your closed tickets; pass share agreed with you after the first run |
| **3 · Supervised pilot** | Weeks 4–16 | Agent works routine tickets, **your engineers approve every merge request.** Fixed 3-month term | Weekly note: lead time vs baseline, approved without rework, rejected and why, review minutes. Changes to prompts or model replay the test set first |
| **4 · Decide** | Week 16 | Pilot report: scale, adjust or stop | Your call |

- **Staff have a role from day 1:** conventions, prompts and code live in your repository, owned by your team
- **Unknown until day 1:** how much of the backlog is routine enough for the agent. The sample tickets show it, and we say so if the answer is "little"
- No standing meetings. Written updates only

---
# Delivery team: three seniors, all in the work

| | Lead Data Architect | Senior Data Engineer | Senior AI Engineer |
|---|---|---|---|
| **Role** | Sets conventions, reviews the agent's work, leads the hackathon | Pairs with your analytics engineers, builds the model and test setup | Agent workflow, evaluation of output quality |
| **Certifications** | Held for the platform you confirm on day 1 (Snowflake/dbt, or your cloud's equivalent); matching profile confirmed before hackathon dates | Held for the platform you confirm on day 1 (Snowflake/dbt, or your cloud's equivalent); matching profile confirmed before hackathon dates | Held for the platform you confirm on day 1 (Snowflake/dbt, or your cloud's equivalent); matching profile confirmed before hackathon dates |
| **Required languages** | Finnish required, English | Finnish required, English | Finnish required, English |

Target start at signature, subject to candidate and availability verification; hackathon dates agreed with your team. The agent team supports your engineers and **does not replace them**.

---
# Pricing model

## Fixed total: €54,440 (excl. VAT)

| Part | Days × day rate | Amount |
|---|---|---|
| **1 · Hackathon** | AI architect 3 d × €960 + Data engineer 2 d × €920 + AI engineer 2 d × €960 | €6,640 |
| **2–3 · Setup and pilot, human work** | AI architect 8 d × €960 + Data engineer 8 d × €920 + AI engineer 3 d × €960 | €17,920 |
| **2–4 · Agent team and run review** | 3 months × €9,000 + AI architect 3 days × €960 | €29,880 |

- **Stop after the hackathon** and pay only part 1. If the agent does not fit your stack, we say so then
- Invoiced per part on completion, 21 days net
- No licences from Recordly. AI and compute credits run on your own cloud account, billed by your provider
- **No contractual deviations.** Sanoma's standard terms


**Staffing review / Rauno:** role profiles are requirements, not verified people. Confirm CVs, certificates, languages and actual availability before submission. One day = 8 hours; DE minimum EUR 115/h, DA EUR 125/h, AI expertise adds EUR 5/h for the relevant specialist. Architect base EUR 115/h is proposed for owner confirmation, not a user-supplied minimum. At most two architects. Validate fixed scope and risk allowance before commitment.

Architect effort: hackathon 3 days + setup 8 days + run review 3 days = 14 days; DE 10 + AI engineer 5 = 29 human days total. Client approves all run changes.

<!-- coverage: technical solution=s2; delivery team=s5; implementation plan=s4; pricing model=s6; concise deck=6 slides incl cover; 2-day hackathon first=s4; no black box / staff role=s2,s4; no zero defects / edge cases=s3; human oversight central=s2,s3; routine tasks backlog weeks=s1,s2; stack unknown (public cloud)=s2,s4; headcount sensitivity=s5 no replace. Placeholders to verify: years, certs. -->
