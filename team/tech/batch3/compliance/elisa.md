Buyer: elisa | Project: elisa-data-platform-architecture-and-tool-selection-as
(Pricing out of scope. Evidence: RFP in work/buyers_now.json, draft team/decks/elisa/...-v1.md, team/buyers/elisa.md)

Regimes:
- Telecommunications secrecy and confidentiality of communications (Act on Electronic Communications Services, traffic and location data) <- "telecom and software with 6,700 employees ... enterprise data platform function" (implied; subscriber, traffic and location data are the sensitive domains)
- GDPR + ePrivacy: retention, purpose limitation of traffic data (implied)
- NIS2 / Finnish cybersecurity rules and Traficom requirements for telecom operators (implied; Elisa is critical infrastructure; no expertise claimed)
- Corporate procurement protocol <- bio: "strictly adhering to procurement protocols", "keeps steering committees satisfied and risk strictly minimized" (named); RFP: "Elisa may recruit deployed consultants after 12 months without a fee" (named)
- Technical constraint <- "real-time access to all data is required, with no batch processing or delayed refreshes permitted" (named trap)
- DORA: not applicable to Elisa; omit. EU AI Act: not triggered (draft excludes AI).

Supplier obligations -> our answer:
- Access to subscriber/traffic data -> assessment needs metadata, schemas, query logs and cost reports from BigQuery, not subscriber-level rows. Rule: read-only, Elisa-issued identities (least-privilege IAM), no export of rows outside Elisa's GCP project; masked sample only if unavoidable. GAP: draft has no access or data-handling statement.
- Telecom secrecy -> anyone who could see message/traffic data must be bound by Elisa's secrecy undertakings; we avoid access by design and sign Elisa's NDA/secrecy forms. No telecom-regulation expertise claimed.
- Data residency -> each option (BigQuery region, Looker, Power BI) scored on data location/EU criterion; the assessment moves no data.
- Supply chain -> no subcontractors, replacement terms (draft).
- Security of options -> criteria: access control, audit logging, encryption/key management, lineage, resilience; each freshness tier also carries failure mode and recovery (NIS2-relevant resilience).
- "Real-time for all" trap -> Yes if four freshness tiers (draft). Compliance add: streaming personal/traffic data increases retention and access exposure, so add "retention and minimisation per tier". Never promise zero-batch for finance close.
- Recruit after 12 months, no fee -> accepted (draft). Check with the delivery lane that this does not conflict with our employment terms.

Matrix (derived from RFP asks):
- Solution approach: Yes
- Team capabilities and availability: Yes if roster confirms (verify)
- Implementation plan: Yes
- Pricing: Yes (not commented here)
- Real-time access to all data, no batch: Yes if read as tiered freshness tested in the scoping sprint; No for blanket zero-batch. Draft says so.
- Recruiting after 12 months without fee: Yes
- Existing stack (GCP, BigQuery, Composer, Looker, Power BI): Yes
- No subscriber-level data access by consultants: Yes
- Standard procurement terms: Yes

Cannot promise (verify):
- Certs (GCP Professional Cloud Architect, Professional Data Engineer, PL-300) -> roster only; GCP partner status unverified in profile.
- "14 years enterprise data platforms, telecom and service sector" -> telecom is not among profile industries (finance, retail, energy, manufacturing, public sector, media, logistics). Remove "telecom" unless a named person has it. Wording: "Platform assessment experience in energy, retail and finance; we pair with your platform leads on telecom specifics."
- "9 years BigQuery, Composer, streaming and CDC" -> verify.
- Telecom/NIS2 expertise -> none claimed.
- ISO 27001 -> not held; do not mention. If asked: "Certification status provided on request" only if verified, else omit.
- "Availability from contract signature, confirmed" -> not backed by roster.

Unsupported claims in draft: (1) "telecom" sector experience; (2) no data-handling statement at all; (3) availability "confirmed". CDC "where the ERP supports it" is properly hedged.

Gate before build: this is an assessment. Gate 1 after the 4-day scoping sprint exists (draft). Add precondition: Elisa-issued access, NDA/secrecy undertaking signed and read-only IAM scope agreed before the sprint touches any platform.

Slide additions: s2 safeguard table add row "Access and data: read-only Elisa-issued roles, metadata only, no subscriber data leaves your GCP project"; s3 tier table add "retention and minimisation per tier".
