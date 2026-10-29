<!-- title: Sanoma · Analytics Backlog Agent -->
# An agent that drafts. Your engineers decide.

## Clear the analytics backlog with a pilot your team helps build, starting with a two-day hackathon. €54,440 fixed total, standard terms.

Proposal to Valtteri Salmela, Director of Data and AI Strategy · Recordly Oy · Helsinki

---

# Proposed technical solution

## From backlog ticket to a pull request your engineer reviews

<div style="display:flex;align-items:stretch;gap:12px;margin:0.2em 0 0.5em 0;font-size:0.68em;line-height:1.25"><div style="flex:1;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:14px"><b style="color:#E3FF87">1 · TICKET</b><br>Routine analytics request in your backlog. Changes start only from tickets, not chat</div><div style="align-self:center;color:#E3FF87;font-size:2em">&rarr;</div><div style="flex:1;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:14px"><b style="color:#E3FF87">2 · AGENT PLANS</b><br>Reads the ticket and your data model, decides which models must change, or asks back</div><div style="align-self:center;color:#E3FF87;font-size:2em">&rarr;</div><div style="flex:1;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:14px"><b style="color:#E3FF87">3 · AGENT DRAFTS</b><br>Writes model changes and tests in a dev environment</div><div style="align-self:center;color:#E3FF87;font-size:2em">&rarr;</div><div style="flex:1;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:14px"><b style="color:#E3FF87">4 · REVIEW AGENTS</b><br>SQL, dbt and general review. Tests run on every change. Failures go back for fixes</div><div style="align-self:center;color:#E3FF87;font-size:2em">&rarr;</div><div style="flex:1;background:#E3FF87;color:#1B1B1B;border-radius:10px;padding:14px"><b>5 · YOUR ENGINEER</b><br>Reviews the pull request, approves or rejects. <b>Only a person merges</b></div></div>

:::cols
- **Not a black box:** diff, test results and reasoning summary sit in the pull request. An auditor agent logs every step.
- **Your environment:** our proven pattern runs inside your own Snowflake with dbt, on your AI credits. The RFP says only "public cloud", so **hackathon day 1 confirms your stack.**
:::col
- **Real result (Recordly projects):** a semi-complex pipeline, build, test and validate, went from **12 h by hand to 30 min**, with a person approving.
- **Out of scope:** autonomous merges, production access, new BI tools, ambiguous or new-domain requests (those stay with your analysts).
:::

---

# Human oversight, and what happens when it fails

| When this happens | The agent does | A person decides |
|---|---|---|
| **Ticket is unclear** | Asks questions on the ticket. Does not guess | Ticket owner answers |
| **Tests fail** | Review agents send the work back for fixes, then it stops | Engineer takes over |
| **Agent is stuck** | It stops running and writes what it tried | Engineer |
| **Edge case** | Logged on an edge-case list, never hidden | Reviewed weekly with your team |
| **Wrong change passes the tests** | Cannot merge. The pull request shows its reasoning for review | **Engineer rejects it** |

> We do not promise zero defects. We promise that every defect is visible before it reaches your pipeline, and a weekly count of rejected pull requests and why.

**Measured in the pilot, on your tickets:** ticket-to-merge lead time, share approved without rework, review minutes per pull request.

---

# Implementation plan: hackathon first, then a measured pilot

| Phase | When | What happens | Gate |
|---|---|---|---|
| **1 · Co-build hackathon** | Week 1, 2 days, Helsinki | Your analytics team picks 5–8 real tickets. We run the agent on them **together**, check your stack, agree the developer workflow | Written feasibility note. **Sanoma decides go/no-go** |
| **2 · Setup** | Weeks 2–3 | Your engineers write the conventions and "perfect examples" with us. Agent team deployed in your environment | Agent passes your review on test tickets |
| **3 · Supervised pilot** | Weeks 4–16 | Agent works routine tickets, **your engineers approve every pull request.** Fixed 3-month term | Weekly written note with numbers |
| **4 · Decide** | Week 16 | Pilot report: scale, adjust or stop | Your call |

- **Staff have a role from day 1:** conventions, prompts and code live in your repository, owned by your team
- **Unknown until day 1:** how much of the backlog is routine enough for the agent. The sample tickets show it, and we say so if the answer is "little"
- No standing meetings. Written updates only

---

# Delivery team: three seniors, all in the work

| | Lead Data Architect | Senior Data Engineer | Senior AI Engineer |
|---|---|---|---|
| **Role** | Sets conventions, reviews the agent's work, leads the hackathon | Pairs with your analytics engineers, builds the dbt and test setup | Agent workflow, evaluation of output quality |
| **Required certifications** | SnowPro Advanced: Architect · dbt Analytics Engineering | SnowPro Core · dbt Analytics Engineering | SnowPro Core · Microsoft Certified: Azure AI Engineer Associate |
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
- No licences from Recordly. AI credits on your Snowflake account are billed by Snowflake
- **No contractual deviations.** Sanoma's standard terms


**Staffing review / Rauno:** role profiles are requirements, not verified people. Confirm CVs, certificates, languages and actual availability before submission. One day = 8 hours; DE minimum EUR 115/h, DA EUR 125/h, AI expertise adds EUR 5/h for the relevant specialist. Architect base EUR 115/h is proposed for owner confirmation, not a user-supplied minimum. At most two architects. Validate fixed scope and risk allowance before commitment.

Architect effort: hackathon 3 days + setup 8 days + run review 3 days = 14 days; DE 10 + AI engineer 5 = 29 human days total. Client approves all run changes.

<!-- coverage: technical solution=s2; delivery team=s5; implementation plan=s4; pricing model=s6; concise deck=6 slides incl cover; 2-day hackathon first=s4; no black box / staff role=s2,s4; no zero defects / edge cases=s3; human oversight central=s2,s3; routine tasks backlog weeks=s1,s2; stack unknown (public cloud)=s2,s4; headcount sensitivity=s5 no replace. Placeholders to verify: years, certs. -->
