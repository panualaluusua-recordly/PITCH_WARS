# Tech critic round 4: yliopiston-apteekki v8 (2026-10-29)

Deck: ...-v8.md (s2 approach, s3 diagram, s4 phases, s5 gates, s6 team, s7 price, s8 statement). Tech lens only; no price, names, terms, storyline. No game API calls.

## Verdict: strong
All round-3 content is in the deck. Remaining gaps are narrow: pilot correctness, server-side evidence, migration effort.

## Round-3 fixes landed
1. Criteria add ERP/BI fit, freshness, scalability (s4 phase 2, s5 Portti 1): yes.
2. Latency in minutes, read access and extracts asked wk 1, wk 3 fallback to document check with uncertain scores (s5 Pistokoe): yes.
3. Per-option architecture picture, glossary, one-page risk list in memo (s4 phase 4, s5 Päätös): yes.
Also landed: two flows piloted (ERP stream, web-pharmacy event), C sketched only.

## Top 3 new concrete tech fixes

1. s5 row "Pistokoe", Läpäisyehto. Pass test only says data "arrives"; add completeness:
   " ja rivimäärät ja summa-arvot täsmäävät lähteeseen sovitulla toleranssilla (sovitaan portilla 1); poikkeamat kirjataan pisteisiin."
   Why: an option can arrive fast and still drop or double rows; a wrong reporting number is the costly failure.
   Evidence: RFP "connects an ERP system, omnichannel operations, and a BI tool"; bio "daily operations quietly moving".

2. s5 Pistokoe "Todiste" and s3 Keruu box. Browser capture proves only the browser side. Add:
   " Palvelinpuolen ulosmenevät yhteydet (kohdeosoitteet) listataan ajolokista ja hyväksytään tietosuojavastaavan kanssa; tapahtumatiedot minimoidaan (ei suoria tunnisteita, pseudonymisointi lähteessä) ennen tallennusta."
   Why: server-side flow can still ship data to third parties; buyer is hypersensitive after tag scrutiny.
   Evidence: bio "Recent regulatory scrutiny surrounding digital pharmacy tags ... hypersensitive to front-end browser telemetry".

3. s4 phase 4 "Mitä tapahtuu" and s5 Päätös. Add migration effort per option:
   " Jokaiselle vaihtoehdolle arvio siirtymän työmäärästä (haarukka, henkilöpäivinä), katko- ja paluusuunnitelma sekä ensimmäinen 90 päivän askel."
   Why: B/C are recommended on score, yet the memo gives no sense of how hard or reversible the change is; roadmap needs it.
   Evidence: RFP "define a future-state architecture alongside clear technology recommendations"; deck risk list lists only "siirtymän vaikeus" as a heading.

## Smaller gaps
- "Ei selainseurantaa" is both a knockout and a scored criterion (s4, s5); keep as knockout only, so scores are not diluted.
- Keep: no vendors named, no AI, no legal conclusion, no production changes.

## Missing technical answers
None. References are staffing, out of lane.
