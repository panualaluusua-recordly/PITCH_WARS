# Tech critic round 3: yliopiston-apteekki v7 (2026-10-29)

Deck: team/decks/yliopiston-apteekki/...-v7.md (s1 approach, s2 diagram, s3 phases, s4 gates, s5 team, s6 price, s7 statement).
Tech lens only; price, names, terms, storyline not judged. No game API calls.

## Verdict: strong (lower end)
Round-2 fixes all landed. Remaining gaps are criteria coverage, pilot prerequisites and one unit.

## Round-2 fixes landed
1. Scoring scale 1-5, weights at gate 1, 0,5 rule on weighted average (s4 Portti 1): yes.
2. Pilot evidence (browser network capture, run log) and shrink path (A and B piloted, C as sketch) (s4 Pistokoe): yes.
3. Tag-inventory fallback when no tag manager (s4 Nykytilakartta): yes.
Round-2 smaller items: per-option diagrams in memo NOT landed; latency unit NOT landed.

## Top 3 new tech fixes

1. s3 phase 2 (Kriteerit) and s4 Portti 1. Criteria list is only privacy, no browser tracking, ease of upkeep, cost. Add:
   " sekä yhteensopivuus nykyisen ERP:n ja BI-työkalun kanssa, datan tuoreus raportoinnissa ja skaalautuvuus verkkoapteekin kasvuun."
   Why: a platform choice scored without fit to ERP/BI or freshness lets a cheap, private option win that breaks reporting.
   Evidence: RFP "modernize ... to better support retail and digital pharmacy services" and "connects an ERP system, omnichannel operations, and a BI tool".

2. s4 row "Pistokoe", column "Läpäisyehto". Add unit and prerequisite:
   " Viive mitataan minuutteina lähdetapahtumasta raporttiin. Lukuoikeudet ja irrotetut otteet pyydetään vk 1; jos ne puuttuvat vk 3, pistokoe korvataan dokumenttitarkistuksella ja pisteet merkitään epävarmoiksi."
   Why: the pilot depends on buyer-side access that is not scheduled; the unit is still missing from round 2.
   Evidence: bio "quick, painless implementations that keep daily operations quietly moving"; deck "Tuotantojärjestelmiin ei tehdä muutoksia".

3. s4 row "Päätös" or s3 phase 4 "Toimitus". Add:
   "Päätösmuistiossa jokaisesta vaihtoehdosta oma arkkitehtuurikuva, sanasto ja yhden sivun riskilista (tietosuoja, ylläpito, siirtymän vaikeus)."
   Why: s2 shows A/B/C as one box; the memo is the real artefact for a reader new to architecture.
   Evidence: bio "Still finding her footing with complex architecture"; RFP "future-state architecture".

## Smaller gaps
- Source box "Myymälät ja muut kanavat" is unstated for pilot: say which two flows are piloted (ERP stream, web-pharmacy event) at gate 1; deck already implies it.
- Keep: no vendors named, no AI, server-side collection not claimed compliant.

## Missing technical answers
None. All RFP asks map to slides; references are a staffing/claims matter, out of lane.
