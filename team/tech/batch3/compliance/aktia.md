Buyer: aktia | Project: aktia-ticket-to-merge-request-developer-or-analytics-a
(Pricing out of scope. Evidence: RFP in work/buyers_now.json, draft team/decks/aktia/...-v1.md, replies in team/buyers/aktia.md)

Regimes:
- FIN-FSA/EBA/DORA AI governance and operational resilience <- "must strictly satisfy FIN-FSA, EBA, and DORA regulatory frameworks for AI governance and operational resilience" (named)
- DORA ICT third-party risk (register of information, subcontractor chain, exit, audit rights, concentration risk) <- "supplier profile, financial standing, and any subcontractors"; "exposure to foreign-headquartered AI API dependencies" (implied; DORA Art. 28-30, EBA outsourcing guidelines)
- Change management / segregation of duties <- "automated maintenance script that bypassed peer review and altered schema dependencies" (implied)
- EU AI Act <- bank + "AI governance" (implied). A code agent for internal analytics is most likely minimal/limited risk (not creditworthiness or employment scoring); the deck commits to documenting the classification, not to a legal opinion. Art. 4 AI literacy applies to users; GPAI obligations sit with the model vendor.
- GDPR <- tickets and data may contain customer data (implied; Aktia is controller, no data egress)
- Aktia's own security policy <- replies: "leaving our pipelines and development workflows sitting inside vendor-managed environments while merely handing our team guest access leaves our operational perimeter far too exposed for a regulated bank"; "supervisory audits" (named in replies)

Supplier obligations -> our answer:
- Four-eyes / no review bypass -> agent has no merge right; branch protection requires a named Aktia reviewer; schema-dependency changes labelled and need data owner; agent service account has no admin or bypass rights. slide 4. Draft supports this.
- Audit trail -> auditor agent logs every action and reasoning; logs stored in Aktia tenant, retention per Aktia policy, exportable for supervisor. slide 3-4. Add: append-only/immutable logs (mechanism to confirm in Definition).
- Foreign-HQ AI API dependency (DORA concentration and exit) -> in-tenant EU-region model hosting options, each provider named, exit plan and substitutability (model behind one interface, swap tested). Draft says "options" in Definition: good. Do NOT claim a sovereign model is already chosen. A hyperscaler model in an EU region still has a foreign-HQ provider: wording must be "EU data residency, no call outside the tenant", not "no foreign dependency". slide 4.
- DORA Art. 30 contract provisions (audit and access rights for Aktia and supervisors, sub-outsourcing approval, incident notification, exit and termination assistance) -> add a slide-4 row: "We accept DORA Art. 30 clauses; no subcontractors, any change needs written approval; audit/inspection rights for Aktia and FIN-FSA; incident notice to Aktia on an agreed timeline; exit plan with code/doc return". GAP in draft: only subcontractors and model exit are covered.
- Access (P5 inherited access) -> agent runs with ticket-scoped identity, read-only on data, writes only to dev branches; credentials in Aktia's secret store; Recordly staff use Aktia-issued identities in Aktia's tenant (answers the "guest access" complaint). GAP in draft: identity model not stated.
- AI governance -> model inventory entry, risk classification, human-oversight description, eval log in the control matrix (draft has matrix, not these items). Add.
- FI/SV runbooks and control matrix: draft ok. IP to Aktia: draft ok.

Matrix (RFP has no numbered list; derived):
- Operate fully inside Aktia tenant: Yes
- No external AI API calls: Yes if Aktia-approved EU-hosted model reaches acceptable quality (tested at Definition gate)
- Agent cannot merge or approve: Yes
- Full audit trail of agent actions: Yes
- DORA Art. 30 clauses, audit rights, exit plan: Yes (state explicitly)
- Subcontractors: Yes, none
- Financial standing evidence: Yes if credit report/financials obtainable (verify)
- FIN-FSA/EBA/DORA compliance: Yes, as a control matrix Aktia compliance signs; we do not certify
- Incident notification timeline: Yes if Aktia's timeline agreed (verify hours)
- Temenos Transact: read-only reporting data Yes; core changes not included

Cannot promise (verify):
- ISO 27001 / SOC 2 / any certification -> not in capability profile; do not mention. Honest wording: "We work under Aktia's security policy inside Aktia's tenant, make no certification claim in this offer and will complete Aktia's supplier security questionnaire."
- Third-party credit report "supplied with the formal tender" -> verify obtainable; else "latest financial statements on request".
- "Our own agent product, the Virtual Data Engineer" and measured cases (12 h -> 30 min, ~30 credits per table, context switches) -> internal VDE material; run claims-auditor before sending; keep labelled anonymised Recordly results.
- Team years, certs, native Swedish reviewer -> placeholders (draft flags).
- Key-person "financial penalty" -> commercial commitment, confirm.
- Regulatory sign-off: say Aktia compliance signs; no statement of FIN-FSA conformance from us.

Unsupported or risky claims in draft:
1. "Code, data, logs and model calls stay in Aktia's tenant" while model hosting is only an option decided in Definition. Soften to "design requirement".
2. Slide 7 says AI credits are consumed on the customer's Snowflake account: implies provider-hosted LLM, contradicting "no external APIs". Reconcile: state as one hosting option with its DORA implications.
3. "Only a person merges" holds only if Aktia admins own the branch-protection settings; say so.
4. Case table is not Aktia-specific; labelled, ok.

Gate before build: Definition go/no-go (weeks 1-3) must close (a) stack confirmed, (b) model-hosting option approved by Aktia security/compliance, (c) control matrix signed by Aktia compliance, (d) Aktia-side third-party onboarding and DORA register entry done. No agent runs on real tickets, and gets no write access beyond dev branches, before that.

Slide additions: s4 row "DORA third-party terms: audit rights for Aktia and supervisor, subcontractor approval, incident notice, exit plan"; s4 row "Access model: Aktia-issued identities, least privilege, secrets in Aktia vault"; s4 control matrix add "model inventory and risk class".
