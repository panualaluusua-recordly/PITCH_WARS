# Tech analysis: yliopiston-apteekki

Buyer: yliopiston-apteekki | Project: yliopiston-apteekki-data-platform-architecture-and-tool-selection-as (open, no conversation, 0 replies)
Stack: "an ERP system, omnichannel operations, and a BI tool across a public cloud" (RFP); bio: "current data setup alongside an ERP system"; cloud vendor field: "a public cloud"
Unknown: ERP vendor; cloud vendor (AWS/Azure/GCP); BI tool; what the "current data setup" is (DW? lake? scripts?); which e-pharmacy tags/tracking exist today and what the "regulatory scrutiny" concerned; sources behind omnichannel (web shop, POS, loyalty); who runs ERP/data ops; existing licences; data volumes. All are Phase 0 (week 1 inventory), not guesses.

Triggers:
- P7 (use what they own) <- "licensing impact" + "modernize from our current data setup" + "tool selection" (confidence high; the RFP asks for licence impact explicitly; "keep current" must be a real outcome). Same pattern praised in kemira: "builds strictly on ... existing SAP and Azure estate with no new platforms or licences".
- P5 (access inherited) <- "digital pharmacy" / pharmacy chain handling customer and health-adjacent data (confidence low; RFP does not mention access, taken from domain; the registry already lists it).
- P15 (findability) <- none in RFP (confidence low; only as a lightweight deliverable inside the target state: data/flow map. Do not add as scope).
- P3 (data foundation first) <- "evaluate our existing environment" + unknown sources (confidence medium; here it is the current-state inventory, phase 1).
- P4 (small blast radius) <- bio "quick, painless implementations that keep daily operations quietly moving without friction" (confidence medium; assessment first, pilot sample, no migration commitment).
- P1 (EU sovereignty) <- "Recent regulatory scrutiny surrounding digital pharmacy tags" (confidence low; not an AI-API case but EU-region and data-residency belong in the criteria).
- Not triggered: P2, P6, P8, P9, P10, P11, P12, P13, P14, P16.

Hard constraints:
- No front-end/browser telemetry: "hypersensitive to front-end browser telemetry" and "regulatory scrutiny surrounding digital pharmacy tags" (bio). Treat as knockout criterion for any recommended tool.
- Deck must contain: "recommended approach, project phases and timeline, team profiles, pricing model, licensing impact, payment terms, and at least two client references" (RFP).
- Scope: "data platform architecture and tool selection assessment" with "future-state architecture alongside clear technology recommendations" (RFP): an assessment, not a build.
- Language: "past cross-team initiatives run in English generated lingering misunderstandings ... documentation is in Finnish" (bio): Finnish deliverables, glossary (not tech-owned, noted for hand-off).
- Operational continuity: "keep daily operations quietly moving without friction" (bio): no production changes.

Traps:
- "Server-side data only" bet could overreach -> honest answer: the criterion is about what the tools we *recommend* require. Server-side collection of web-shop events is not automatically free of GDPR/ePrivacy issues: if server-side tracking still links identifiers to health-related purchases it is still personal data processing and needs a legal basis. Also server-side tagging (GTM server container etc.) usually still has a client-side component. Say: "no browser scripts required; legal basis for what is collected is for their DPO, we list the questions". Do not claim regulatory compliance.
- "Remove existing front-end tags" could be tempting -> out of scope; the RFP asks for no such thing. Report existing tags as findings only (the deck already says so; good).
- Unknown ERP/BI/cloud -> honest answer: vendor-neutral method, name nothing; "three target options incl. 'current tidied up'". Do not name Snowflake/Databricks/Fabric as theirs (anti-pattern, outokumpu).
- Licence impact without knowing licences -> honest answer: we report per option what stays/comes/goes from their own contracts; numbers only after they share licence lists. A "3-year cost estimate" needs inputs: state it as an estimate range with assumptions.
- "Quick and painless" vs. a real comparison -> honest answer: 3 options, scored, small sample proof; say what is not covered (no build, no migration plan detail).
- Pharmacy data is sensitive (health-adjacent): do not propose AI/ML or new platforms (bio does not ask).

Praised/punished before:
- P7 in kemira: "I like that they build right on our existing Azure setup" and "[met] Builds strictly on Kemira's existing SAP and Azure estate with no new platforms or licences" (but over budget; price is not our lane).
- P3 phase-0 in helsinki (won), enfuce (won), per patterns.md.
- Naming tools the buyer never mentioned as their stack: punished in outokumpu v2 (TECH_SCOPE section 7).
- Missing diagram: "an architectural diagram is conspicuously absent" (aktia), "architecture diagrams are omitted" (enfuce). Ville's v1 has no diagram.
- No reply from this buyer yet.

VDE: NO (vde-check applies only to Snowflake + dbt; neither named. Buyer notes also say deliberately out.)

Effort drivers:
- Number of source systems to inventory (ERP, web shop, POS, BI, cloud accounts): unknown; each adds interview + mapping time in phase 1.
- Depth of the tracking/tag inventory (needs read access or someone from web team; not in RFP).
- Number of options scored and whether a sample proof is run on real data (needs data access/security approval: can be a lead time risk).
- Licence data availability (contracts from procurement).
- Small if: they give a source list and licence list in week 1 and the sample is run on a schema extract.
- Large if: multiple clouds/ERP instances, no documentation, and access approvals slow.

## Notes for deck owner (Ville)
1. No architecture diagram in v1; reviews punished absence (aktia, enfuce). Add one vendor-neutral current-state to target-state diagram (sources: ERP, web shop/omnichannel, BI, public cloud; mark "server-side collection only" and where access control sits). Label vendors as "to confirm week 1".
2. "Tieto kerätään palvelinpuolelta" (s2) reads as a promise that server-side collection is the data approach. Rephrase to: the criterion excludes tools needing browser scripts/pixels/tags; legal basis of any collection remains for their data protection officer, and we list the open questions. Server-side collection can still be personal data processing.
3. "Pistokoe esimerkkidatalla" (s3): state what data and who approves access; for pharmacy data prefer synthetic or masked extracts. Not specified in the deck.
4. Name any "3-vuoden kustannusarvio" assumptions: it depends on licence lists the RFP does not give. Say "arvio, tarkentuu viikolla 1 saatujen lisenssitietojen perusteella" (not price content, only the technical basis).
5. Honest unknown box mentions ERP/BI/cloud: good. Add tag/tracking inventory and data-flow of omnichannel to the unknown list.
6. Gate 1 exists after criteria (good, T4). Consider a short "what we do not cover" line: no build, no migration, no tag removal, no AI.
7. Team slide claims AWS/Azure/GCP certifications for a buyer on "a public cloud": fine, but do not imply fit to a specific cloud. Claims-auditor must verify certification claims against the roster (not tech lane to judge).
