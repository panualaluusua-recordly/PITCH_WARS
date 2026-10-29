# Tech analysis: oulun-energia (project oulun-energia-internal-rag-document-and-policy-assistant)

Source: GET /api/buyers read 2026-10-29 (raw in work/buyers/oulun-energia-raw.json, git-ignored). Conversation history: empty (no replies yet, no feedback round). Scope: tech and architecture only.

Buyer: oulun-energia | Project: oulun-energia-internal-rag-document-and-policy-assistant
Stack: "a public cloud", "our chat tool", "its current data setup", "a BI tool" (bio). None is named. | Unknown: which cloud, which chat tool, which BI tool, what "current data setup" is, where documents live, document formats and volume, access model, Finnish model/embedding choice, who runs it after go-live.

## 1. Technical asks (quoted)

| # | Ask | Quote |
|---|---|---|
| A1 | Organisation-wide internal RAG assistant over guidelines, safety protocols, operational docs | "organisation-wide internal RAG document and policy assistant" / "rapid, reliable answers from internal guidelines, safety protocols, and operational documentation" |
| A2 | Finnish language quality, not just "supports Finnish" | "full support for Finnish language nuance" |
| A3 | Integrate with their cloud, chat tool and existing data | "must integrate smoothly with a public cloud, our chat tool, and its current data setup" |
| A4 | Cost control on vector refresh | "A recent cloud pilot generated surprise billing spikes when automated vector refresh jobs ran unchecked" |
| A5 | Respect the Q1 change freeze | "our utility infrastructure maintains strict change restrictions during the critical Q1 winter heating peak" |
| A6 | Scale: 260 users, multi-utility | "Serving our 260 employees" / "municipal multi-utility operations in Oulu" |
| A7 | Deck content wanted | "technical solution, project timeline and implementation approach, core team profiles including certifications and availability, key deliverables" (non-tech parts belong to other owners) |

## 2. Hidden tech preferences (inferred; confidence marked)

- Finnish end to end including delivery materials: "quickly local maintenance crews and plant supervisors tune out whenever external partners present in English" (bio). Applies to the assistant's answers and UI, runbooks and training for crews and supervisors (high).
- Safety protocols are an answer domain: a wrong or stale answer on a safety procedure is a safety risk. Expect a preference for citations to the source passage, document version/date, and "I do not know" over guessing (medium; inferred from "safety protocols" + "reliable answers").
- Evidence over demos: she is a systems-science PhD who "relies on cheerful humor and analytical frameworks" (bio). Expect a wish for a measured evaluation method for Finnish retrieval and answers, not a demo (medium; matches P13 and Kemira "live demo on our own ... data").
- Permissions: internal policy and operational docs likely have different audiences (crews, office, management). Access inherited from source, not reinvented (P5) (low; not stated, common RAG failure).
- Conversational tooling is an unstated preference at other buyers (UPM "corporate chatbots and conversational tooling", Terveystalo "conversational AI"). Here it is the ask, so the chat-tool front end is core, not a side quest (medium).
- No tool sprawl: "integrate smoothly with ... its current data setup" suggests building on what they have (P7, P6) (medium).
- Operations after the engagement: she "recently joined" and is "still adapting"; a small team will inherit the service (low).

## 3. Triggered patterns

- P8 Cost guardrails <- "surprise billing spikes when automated vector refresh jobs ran unchecked" (high)
- P9 Respect freezes <- "strict change restrictions during the critical Q1 winter heating peak" (high). Today is 2026-10-29, so Q1 2027 is close: build and test before, no production change inside it (see T2).
- P13 Proof on their data <- "rapid, reliable answers", "Finnish language nuance" (medium): Finnish question set from their own documents, baseline, numeric gate whose target is agreed after the first measurement (not fixed up front; oriola anti-pattern).
- P6 Code in client tenant + IaC <- "integrate smoothly with a public cloud ... current data setup" (medium).
- P7 Use what they own <- "its current data setup", "our chat tool" (medium).
- P5 Access inherited <- "internal guidelines, safety protocols, and operational documentation" across multi-utility roles (low-medium).
- P2 Human gate <- safety protocols as the answer domain (low-medium): the assistant answers and cites; it never issues or changes a procedure; a named document owner is the source of truth. Not an automation trigger in the RFP text.
- P4 Small blast radius <- "organisation-wide" for 260 users (low-medium): pilot slice, then waves.
- P3 Data foundation first <- unknown document sources ("current data setup") (low): a source probe is the honest Phase 0.
- P15 Findability <- (low): citations and a source/document inventory as deliverables.
- P1 EU sovereignty: NOT triggered by text ("a public cloud" is unspecified). EU-region processing is a safe default for a municipal utility but do not build the pitch on it (low).

## 4. Hard constraints

- Q1 freeze: "strict change restrictions during the critical Q1 winter heating peak".
- Cost: refresh must be bounded ("surprise billing spikes ... ran unchecked").
- Finnish: "full support for Finnish language nuance".
- Integration targets: "a public cloud, our chat tool, and its current data setup".
- Reach: "organisation-wide ... Serving our 260 employees".

## 5. Traps and honest answers

| # | Trap | Honest answer |
|---|---|---|
| T1 | "Organisation-wide" go-live for all documents and users at once | Pilot slice first (a few document sets, a few user groups), measured, then widen in waves. P4. |
| T2 | Q1 freeze vs a rollout that lands in it | Timeline shows the freeze as a labelled block: build and test in non-production before Q1, production release before the freeze or after it ends, nothing changing production inside it. Ask what exactly is frozen (cloud account, chat tool, data setup, or all); a new bot in the chat tool may itself count as a change. P9. |
| T3 | Vector refresh cost: a scheduled full re-index is what billed them | Incremental refresh by change detection (hash or modified date), not full re-embedding; refresh budget and schedule cap; budget alerts and a hard stop; cost per run and per month reported; kill switch. Also show the other cost levers (embedding calls, index size, model tokens per question), not only the refresh job. P8. |
| T4 | "Full support for Finnish language nuance" cannot be promised blind | Do not claim it. Propose a Finnish evaluation set from their own documents (inflection, compounds, domain vocabulary, questions phrased as crews ask them), a measured baseline, and a gate agreed after the first measurement. Pick embedding and answer models by test on Finnish. P13. |
| T5 | "Reliable answers" on safety protocols: hallucination risk | Answers only from retrieved passages, with citation and document version/date; refuse or route to the named owner when retrieval is weak; no advice outside the corpus; superseded versions excluded. Report the honest error rate from the pilot, never "zero defects". P2, P13. |
| T6 | Unnamed cloud, chat tool and data setup: tempting to assume a stack | Do not name a stack. Show components (ingest, index, retrieve, generate, chat front end, monitoring) "mapped to your cloud's services once named"; ask in Phase 0. Anti-pattern: outokumpu v2 named tools the buyer never mentioned. |
| T7 | Assistant surfaces a document the user should not see | Apply source permissions at retrieval (filter by user group), test before go-live. If source permissions cannot be read, start with one corpus open to all staff. P5. |
| T8 | AI extras (agents, auto-actions, predictions) | None. RAG answering with citations only. Aktia was lost on extras: "predictive modeling bells and whistles is precisely what sank this proposal." |
| T9 | Foreign-hosted model API at a municipal utility | Not stated, so ask. Default: processing in an EU region inside their tenant, model access behind an abstraction layer so it can be swapped. P1 (low). |
| T10 | Document quality: scanned PDFs, duplicates, outdated versions | Phase 0 document inventory and quality sample; go/no-go on what is indexed; no promise to cover unknown sources. P3. |

## 6. Earlier replies of this buyer and of similar buyers

No reply from oulun-energia yet (empty conversation).

Praised/punished before (quotes from the API read):
- Tenant containment: s-group hint: "keep the entire agent footprint strictly confined within our existing Azure tenant rather than peddling an external wrapper" (praised). Kemira (won): "Sticking squarely to our Azure tenant and Datasphere views means no rogue architectures." (P6, P7)
- Proof on their data: Kemira (won): "Demanding a live demo on our own plant's Datasphere data on day one." (P13)
- Human gate: vr-group hint: "keeping the automation strictly confined to drafting pull requests with human sign-off" (praised). (P2)
- AI extras punished: aktia (lost): "indulging in predictive modeling bells and whistles is precisely what sank this proposal."
- Conversational tooling gap punished: upm (lost): "leaves the broader domain of corporate chatbots and conversational tooling unaddressed"; terveystalo (lost): "patient-facing conversational AI tools is conspicuously absent". Here chat is in scope; make it explicit.
- Finnish delivery praised broadly: helsinki, lahitapiola, s-group, vr-group, terveystalo.
- Pairing caution: valmet (lost): "Tying up my engineering team in continuous hands-on pairing and co-building sessions". Do not assume constant client-staff time.
- Freeze handling (P9): no confirmed verdict seen in this read; candidate pattern only.

## 7. VDE

VDE: NO. It applies only to Snowflake + dbt; the RFP names neither ("a public cloud", "its current data setup"). Revisit only if Phase 0 shows Snowflake and dbt.

## 8. Unknowns to raise with the buyer (Phase 0 work, not guesses)

1. Which public cloud; which regions and subscriptions are allowed (EU-only?).
2. Which chat tool; does it allow custom bots or apps; who approves them.
3. What "current data setup" is: where documents live (file shares, document management, intranet, ERP, wiki), formats (PDF, Word, scans, drawings), volume, languages (Finnish only, Swedish, English), update frequency.
4. Which BI tool (bio: operational metrics into a BI tool); is usage analytics of the assistant expected there.
5. What exactly the Q1 freeze covers and its dates; is a read-only or non-production pilot allowed during it.
6. Source permission model: who may see which documents; identity provider and groups.
7. What the cloud pilot was (vector store, model, refresh schedule), and the trigger and size of the bill spike; reuse or replace.
8. Finnish quality: which document types and question styles matter most; who can judge answers (domain owners for the evaluation set).
9. Document ownership: who keeps documents current and retires superseded ones.
10. Who operates the service after delivery (monitoring, budget alerts, refresh schedule).
11. Auditability: query-log retention, personal data in questions.

## 9. What the architecture slide must show

1. Flow diagram: document sources -> inventory, extract, chunk (with change detection) -> index (vector plus keyword, Finnish-aware) -> retrieval with user-group filter -> answer with citation -> chat tool front end; all inside the buyer's cloud tenant, labelled "mapped to your named services in Phase 0".
2. Cost guardrail layer in the flow: incremental refresh, scheduled cap, budget alert, hard stop, cost per question and per month.
3. Access: source permissions applied at retrieval, tested before go-live.
4. Evaluation loop: Finnish question set from their documents, baseline, gate; rerun before every wave and after every refresh or model change.
5. Human and safety gate: citations with version/date, refusal when evidence is weak, named owner per collection, a flag-wrong-answer button.
6. Timeline strip with the Q1 freeze as a block: build and test before, production windows around it, no production change inside it.
7. Gates and risks slide: Phase 0 source and Finnish probe (go/no-go), pilot wave, widening waves; risks tied to the unknowns above.
8. Everything in Finnish; no stack names the buyer did not give; no AI extras.

## 10. Effort drivers (no figures)

- Larger: number and messiness of document sources; scanned or unstructured files; permission mapping; building and iterating the Finnish evaluation set; chat-tool integration constraints; fitting delivery around the Q1 freeze; cost-monitoring build.
- Smaller: clean text-based sources in one place; a chat tool that supports bots simply; one corpus with uniform access in the pilot wave; reuse of pieces from the earlier pilot.
