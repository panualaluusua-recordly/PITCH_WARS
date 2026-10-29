Buyer: yliopiston-apteekki | Project: yliopiston-apteekki-data-platform-architecture-and-tool-selection-as
(Pricing out of scope. Evidence: RFP in work/buyers_now.json, draft team/decks/yliopiston-apteekki/...-v1.md, team/buyers/yliopiston-apteekki.md)

Regimes:
- ePrivacy / Finnish Act on Electronic Communications Services sec. 205 (terminal-device cookies and trackers) + GDPR consent <- "Recent regulatory scrutiny surrounding digital pharmacy tags has left analytics leadership hypersensitive to front-end browser telemetry" (named, bio)
- GDPR Art. 9 special-category data: online pharmacy purchases and prescriptions reveal health <- "pharmacy chain and online pharmacy" (implied)
- Pharmacy sector rules: Fimea supervision, Medicines Act, e-prescription/Kanta data rules (implied; no detailed expertise claimed)
- Data Protection Ombudsman guidance on pharmacy tracking (implied; do not cite specifics we cannot source)
- Finnish-language documentation <- "daily operational documentation is in Finnish" (named, bio)
- EU AI Act: not triggered (no AI in scope)

Supplier obligations -> our answer:
- No client-side tracking -> knockout criterion: no browser scripts, pixels, tags; server-side collection only (draft s2, s3). Nuance GAP: server-side collection is not automatically exempt from GDPR/ePrivacy (server-side tagging that forwards identifiers to third parties can still need a legal basis). Say "criteria also test legal basis and consent, confirmed with your DPO", not "server-side = compliant". The draft line "Tieto kerätään palvelinpuolelta" reads as a compliance guarantee.
- Health data during the assessment -> we work on architecture, schemas, metadata; no access to customer or prescription-level records. The "pistokoe esimerkkidatalla" (s3 phase 3) must say synthetic or anonymised data supplied by the buyer. GAP.
- Processor role -> if any personal data is seen, DPA with Yliopiston Apteekki as controller; named read-only accounts; removed at close.
- Data residency in options -> every option reports data location (EU/EEA), subprocessors and transfer mechanism; non-EU transfer is a negative criterion. Add to criteria (draft lists only "tietosuoja").
- Retention/minimisation, access logging, pseudonymisation per option as weighted criteria; DPO as reviewer.
- Existing front-end tags: out of scope (draft correct); say "we do not assess existing tags legally; your DPO decides".
- Finnish documents: yes.

Matrix (derived from RFP asks):
- Approach: Yes
- Phases and timeline: Yes
- Team profiles: Yes
- Pricing model: Yes (not commented here)
- Licensing impact per option: Yes
- Payment terms: Yes
- At least two client references: Yes if two real anonymised cases exist and the clients allow contact on shortlist; otherwise Yes, not included (one honest reference only)
- No browser tracking in any recommendation: Yes
- Everything in Finnish: Yes
- No access to customer-level health data: Yes (synthetic or masked only)

Cannot promise (verify):
- Reference 2 "pohjoismainen terveysalan palveluntuottaja, 2025 ... tiukoilla tietosuojavaatimuksilla" -> profile says healthcare/pharma limited (verify). If no real case: "Terveysalan kokemuksemme on rajallista; vahvuutemme on vähittäiskaupan ja tietosuojatietoisen arkkitehtuurin arviointi", and list only existing references.
- Reference 1 retail chain case -> verify it exists.
- Architect "12 v; vähittäiskaupan ja terveysalan data-alustat", engineer "tietosuojaystävällinen tiedonkeruu" -> placeholders; verify.
- Certs (Azure Solutions Architect Expert, AWS SA, GCP DE, Azure DE) -> roster only; AWS not in profile's core stack.
- "Emme saa palkkioita toimittajilta" -> verify partner/reseller arrangements.
- Any statement that a design is GDPR-compliant -> not given; no legal advice.
- ISO 27001 -> not held; do not mention.

Unsupported claims in draft: (1) server-side collection framed as the solution; (2) "tietosuojaystävällinen" engineer expertise; (3) the two references.

Gate before build: none formal. Soft gate portti 1 (criteria approved with no-tracking and data-residency criteria, DPO review) before options are scored; plus week-1 confirmation that no health-level data is needed.

Slide additions: s3 phase 2 criteria add "DPO tarkastaa kriteerit; datan sijainti EU/ETA; oikeusperuste"; s3 phase 3 "pistokoe synteettisellä tai anonymisoidulla datalla"; s2 reword server-side line as above.
