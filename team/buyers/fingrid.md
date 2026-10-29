# Fingrid – Leena Vainio, Head of Data and Analytics (Fingrid Oyj)

## 2026-10-29 · brief 09:02Z (dry run of upgraded buyer-analyst)
## fingrid · fingrid-financial-and-margin-reporting-automation · brief 2026-10-29T09:02Z
Snapshot: open=fingrid-financial-and-margin-reporting-automation status=open (no "thinking" field in API; last request 08:49:52Z, 12 min ago, so not "active") available_at=null time_left=231 min stats=won 0 / lost 0 / fb rounds 1 / penalties €0 (fees €1,000, net -€1,000). consultants roster: NOT in /api/me (field absent), so roster unknown.
Fit:
  Fit: fingrid · fingrid-financial-and-margin-reporting-automation
  Decision: BID-WITH-CONDITIONS (priority C, marginal; flips to NO-BID if the price floor is near the Kemira-size range and the v1 price turns out to be already low)
  Gates: pass (open project, no cooldown, ~231 min left, no teammate in last 3 min; nothing "Not us": we do Databricks/Power BI reporting, D365 is only a read source)
  Scores: capability=3 ("Databricks lakehouse ... Power BI" = Core) deliverability=2 (roster unknown; bounded 2-3 person scope) req_risk=1 ("real-time ... cannot permit any batch" vs finance reporting; the functional/non-functional requirement list the matrix must answer is NOT in the RFP) hidden_pref=2 (bio fears map to reconciliation/process/cost control; nothing we can't show) relationship=1 (1 feedback, "plainly above our approved budget") commercial=1 (cost-guarding persona, likely low budget, "rigidly keeping external consulting spend in check") -> 10/18
  EV: P=0.35 x B=€20,000 (guess) - C=€4,500 (1 more feedback + proposal; the €1,000 already spent is sunk) (+ follow-on 0.3 x 20k x 0.35 = €2,100) = €4,600  [B from: kemira 100-day roadmap €16.5k won / helsinki SME reporting €61.1k "above budget"; no Fingrid price known]
  Conditions: - Real-time: answer "Yes if": streaming/incremental for operational monitoring, batch/reconciled for financial close; never "no batch ever" (buyer praised this honesty)
              - Compliance matrix needs requirements the RFP omits: list them as "assumed requirements" and mark each Yes / Yes but not included / Yes if
              - Don't claim Fingrid-specific or D365 F&O configuration experience; we read from it
  Spend plan: 1 feedback round (price cut + baseline step) then proposal
  Biggest risk: budget is unknown and may be below our cost floor; EV is only ~€5k even if everything goes right.
History digest:
- 08:49Z feedback (teammate, deck fingrid-...-v1.pdf, price NOT recorded in API or work/log.md; no local deck file) -> hints: praise for "transparent acknowledgement regarding lakehouse latency boundaries"; worry that "automated reporting deliverables while our underlying ledger records and duplicate entries across Dynamics and the lakehouse remain unaddressed"; "quoted fee is plainly above our approved budget ... cannot advance an engagement that exceeds our authorized expenditure limits" (price: over-hard).
Fears -> hidden requirements:
- Reconcile/dedupe ledger records between D365 and the lakehouse BEFORE any reporting output, as a first phase with a gate <- "ledger records and duplicate entries across Dynamics and the lakehouse remain unaddressed ... unverified baseline data carries distinct operational risk"
- Strict data-integrity control inside the data-mesh (finance domain data product with owner, quality checks, lineage) <- "maintaining strict control over data integrity was essential"
- Capped, procurement-compliant spend <- "rigidly keeping external consulting spend in check"; "authorized expenditure limits"
- No unproven modernisation <- "strict process compliance over unproven modernization"
Hopes -> hidden preferences:
- Fits the existing Databricks lakehouse + data-mesh model + Power BI, no new platform/licences (guess; bio "steered the rollout of a Databricks lakehouse with a data-mesh model", and Helsinki/Kemira rewarded no-new-licence builds)
- Honest limits stated up front <- "appreciate their transparent acknowledgement regarding lakehouse latency boundaries ... aligns well with our architectural guidelines"
- Visible cost savings / low TCO (guess; "aggressive personal wealth goals")
rfp-trap-scan:
  Buyer: fingrid · Leena Vainio, Head of Data and Analytics · Project: fingrid-financial-and-margin-reporting-automation
  Deck sections (RFP order): 1. Compliance response to functional + non-functional requirements (Yes / Yes but not included / Yes if) 2. Proposed technical solution 3. Delivery team capabilities 4. Rollout plan 5. Complete pricing model reflecting total cost of ownership
  Hard constraints: - "answering each requirement with Yes, Yes but not included, or Yes if" (exact three-value vocabulary) - "real-time access to all underlying data; ... cannot permit any batch processing, scheduled pipelines, or delayed data refreshes" - "complete pricing model reflecting total cost of ownership" (TCO = build + run, not only a build fee)
  Hidden requirements: see Fears above
  Traps: - "no batch ever" -> "Yes if": streaming (e.g. Delta Live Tables/Structured Streaming, change feed from D365) for operational monitoring, reconciled batch for finance close; state latency in seconds/minutes, not "real time"; state cost impact of always-on compute - Requirement list missing -> state assumed requirements, 8-12 rows - TCO trap: real-time raises run cost -> show run cost per month with caps/alerts [catalog: surprise cloud bills] - Margin reporting = finance numbers -> reconciliation to ledger, human sign-off, no "guaranteed accuracy"
  Persona: language=en (guess; Finnish company, bio silent; chat-tool channel) team=small (guess 2-3) tone=formal, process-compliance, engineering-precise hates=unvetted modernisation, budget overruns wants=controls, reconciliation, honest limits
  Scope fence: IN baseline reconciliation + finance/margin reporting on existing D365 + Databricks + Power BI | OUT gen AI/ML add-ons (bio not AI-enthusiast; Aktia lesson), new platforms/licences, D365 configuration, operational (OT) monitoring itself
  Slide target: 6-7 (guess; matrix needs 1-2 slides; "slide proposal"); never >8 given Helsinki "sprawling" lesson
  Price signals: v1 "plainly above our approved budget" (price unknown). Reference: kemira €16.5k won (roadmap), helsinki €84k won (6-month squad). Cut steeply: Helsinki needed -58% (198->84), Kemira -79% (78->16.5).
Carry-over: no earlier Fingrid projects. Cross-buyer lessons that apply: 5-7 slides; no scope creep; no new licences; standard terms no deviations; probe/baseline before build with a go/no-go; budgets ~1/3 of market; pairing from week 1 if enablement is mentioned (it isn't).
Top 3 to win: 1. Price cut deep (first complaint is budget, "cannot advance") 2. Phase 0 reconciliation/dedupe of D365 vs lakehouse with a gate before reporting 3. Keep the honest "Yes if" real-time answer and latency table (praised)
Top 3 ways to lose: 1. Price still over limit (it blocks everything) 2. Promising true zero-batch real time, or any AI add-on 3. Reporting-first plan that ignores the data-quality worry; or >8 slides
Next request: feedback (round 2/3 used 1/3) at a much lower price with the Phase 0 step. Reason: price class over-hard, first round, reply-reader says one more feedback. Caveat: two changes at once (price + Phase 0); acceptable because only 3 rounds exist and both were explicitly requested, but then price effect vs content effect is not separable. After round 2 with no price complaint, propose.
Open questions:
- What price and deck content did the teammate send in v1? (not in API, log or work/decks/fingrid; ask whoever sent it. Without it we can't choose the cut)
- Roster: /api/me has no consultants; is there a roster for Finnish finance/Databricks roles?
- Which functional/non-functional requirements does the buyer have in mind? (RFP omits them; only a feedback hint can reveal)
- Is the buyer likely to go out_of_budget soon? out_of_budget_message exists ("fiscal allocations are completely locked down"), so a win may not open a follow-on project (guess).

## 2026-10-29 C-batch draft (v2)
Deck decks/fingrid/fingrid-financial-and-margin-reporting-automation-v2.pdf, 6 slides, 21 pd x €920 = €19,320. Bets: Phase 0 reconciliation gate; Yes/Yes but not included/Yes if matrix (10 assumed rows) with latency tiers; price cut to budget-class. Open: real requirement list unknown; v1 price unknown; run-cost cap number set only in Phase 0. Not sent.
