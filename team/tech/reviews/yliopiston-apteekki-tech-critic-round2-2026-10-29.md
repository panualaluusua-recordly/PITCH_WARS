# Tech critic round 2: yliopiston-apteekki v6 (2026-10-29)

Deck: team/decks/yliopiston-apteekki/...-v6.md (s1 approach, s2 diagram, s3 phases, s4 gates, s5 team, s6 price, s7 statement).
Read against: RFP and bio in work/buyers_now.json. Tech lens only; price, names, terms, storyline not judged.

## Verdict: adequate, upper end (moving to strong once the three fixes below land)
All three round-1 fixes are in. Remaining weakness: the "0,5 pisteen" decision rule and the pilot have no defined
scale, no evidence method, and no stated fallback if the unknown sample data or capacity does not arrive.

## Round-1 fixes
1. s4 pilot pass criterion (same stream and event arrive without browser script; latency and run cost measured; failure scored): LANDED yes.
2. s2 band contradicts pilot ("Tuotantoon ei kosketa"): LANDED yes. Now "lukuoikeuksin ... irrotetuilla otteilla tai synteettisellä datalla".
3. Phase 1 states how knockout is verified and tags inventoried: LANDED yes (vendor docs and architecture review; tag-manager settings).
Smaller round-1 items: "C luonnoksena" fallback NOT landed; scoring scale NOT landed; cert/cloud-fit note is staffing, out of lane.

## Top 3 new tech fixes

1. s4 (Tarkistuspisteet), row "Portti 1: kriteerit", column "Läpäisyehto". Add at the end:
   " Pisteytys: asteikko 1-5 kriteeriä kohti, painot sovitaan portilla 1; 0,5 pisteen sääntö lasketaan painotetusta keskiarvosta."
   Why: the central decision rule (s2 "vähintään 0,5 pisteellä") is unmeasurable without a scale, and a sceptical
   architect cannot check it. Evidence: bio "still finding her footing with complex architecture" (needs a rule she can verify);
   RFP "technology recommendations".

2. s4 (Tarkistuspisteet), row "Pistokoe", column "Läpäisyehto". Add:
   " Todiste: selaimen verkkoliikenteen tallenne (ei kolmannen osapuolen kutsuja) ja ajoloki. Jos esimerkkidataa ei ole vk 3, pilotoidaan kaksi virtaa vaihtoehdoille A ja B; C kuvataan luonnoksena, ei pilotoida."
   Why: the knockout is the buyer's core fear, and "arrive without script" has no evidence artefact. Also the
   phase 3 workload (2 flows x 3 options, 6 pd) has no stated shrink path when the sample-data unknown bites.
   Evidence: bio "hypersensitive to front-end browser telemetry"; RFP "evaluate our existing environment".

3. s4 (Nykytilakartta row) or s3 phase 1: add a fallback for the tag inventory, which currently assumes a tag manager exists.
   Add: "Jos tunnistehallintaa ei ole, tunnisteet listataan sivuston lähdekoodin ja verkkopyyntöjen läpikäynnillä lukuoikeuksin; löydökset raportoidaan vain havaintoina."
   Why: "sivuston tunnistehallinnan asetuksista" is an unverified assumption about the stack; the RFP names only ERP, BI and a public cloud.
   Evidence: bio "regulatory scrutiny surrounding digital pharmacy tags"; deck's own "Rehellinen tuntematon: ERP:n, BI-työkalun ja pilven tarkat tiedot".

## Smaller gaps
- s2 diagram shows A/B/C as one box. The decision memo promises "vaihtoehdot kuvina"; consider stating that each option gets its own diagram in the memo (s3 phase 4 Toimitus).
- Pilot measures "viive ja ajokustannus" but no unit is given (e.g. minutes from source event to report); fine as honest, add unit at gate 1.
- Deck correctly avoids vendors, AI add-ons and claiming server-side collection is compliant. Keep.

## Missing technical answers
None outright. RFP asks (approach, phases, team, pricing model, licensing impact, terms, references) all map to slides; only the evidence and scale gaps above remain.
