# Tech critic: yliopiston-apteekki v5 (2026-10-29)

Deck: team/decks/yliopiston-apteekki/...-v5.md (s1 approach, s2 diagram, s3 phases, s4 gates, s5 team, s6 price, s7 statement).
Read against: RFP/bio as quoted in team/tech/batch3/yliopiston-apteekki.md, prior findings in
team/tech/reviews/ville-drafts-tech-review.md. Tech lens only; price, terms, names, storyline not judged.

## Verdict: adequate (upper end)
Vendor-neutral, honest about unknowns, assessment-only, diagram present. It loses fit points on measurability:
the knockout and the spot test have no stated evidence or pass numbers, and one sentence contradicts the pilot.

## Top 3 tech fixes

1. s4 (Tarkistuspisteet), row "Pistokoe", column "Läpäisyehto" (open item from the prior review, still not in v5).
   Replace the cell text with:
   "Pistokoe läpäisty vaihtoehdolle, kun sama ERP-virta ja sama verkkoapteekin tapahtuma saapuvat perille ilman
   selainpuolen skriptiä; viive ja ajokustannus mitataan ja raportoidaan vaihtoehdoittain; epäonnistuminen kirjataan pisteisiin."
   Evidence: bio "hypersensitive to front-end browser telemetry"; v5 today only says "jokaisen vaihtoehdon läpi".

2. s2 (diagram band under the diagram) contradicts the pilot. It says "Tuotantoon ei kosketa" while s4 runs a real
   ERP stream and a web-pharmacy event through each option. Replace the band text with:
   "Arviointi tehdään lukuoikeuksin, nykyisillä lisensseillä ja irrotetuilla otteilla tai synteettisellä datalla.
   Tuotantojärjestelmiin ei tehdä muutoksia eikä niiden kuormaa lisätä."
   Evidence: bio "keep daily operations quietly moving without friction".

3. s2 or s3 (add one bullet to phase 1 "Mitä tapahtuu"): say how the knockout is verified and how tags are inventoried,
   because a sceptical architect asks "how do you know a tool needs no browser script?":
   "Poissulkeva ehto todennetaan jokaiselle työkalulle toimittajadokumentaation ja arkkitehtuurikuvauksen katselmuksella
   (mitä komponenttia selaimessa tarvitaan); selaintunnisteet inventoidaan sivuston tunnistehallinnan asetuksista, ei lisäämällä mitään seurantaa."
   Evidence: bio "regulatory scrutiny surrounding digital pharmacy tags"; unknown in batch3: "which e-pharmacy tags/tracking exist today".

## Smaller gaps (not in top 3)
- s3 phase 3: pilot on 2 flows x 3 options plus scoring is 6 pd of the work. The shrink path
  (pilot on 2 flows only, option C as a sketch) is in team/tech/slides but not in the deck; add "C kuvataan luonnoksena, ei pilotoida"
  as a stated fallback so the unknown "sample data wk 3" does not silently overrun.
- Scoring scale for the "0,5 pisteen" rule is not defined (scale, weights set at gate 1). Add "asteikko 1-5, painot portilla 1".
- s5 lists AWS, Azure and GCP certifications for a buyer on "a public cloud": do not imply cloud fit. Staffing owner's call.
- Typos "iikkoa", "uoden" from the earlier note no longer appear in v5.

## Already good
- Diagram added: current state, three options, access control and logging placement (answers "diagram conspicuously absent" in aktia, enfuce).
- No vendor named that the buyer did not name; ERP, cloud, BI and EU/ETA marked "vahvistetaan vk 1" (avoids the outokumpu anti-pattern).
- Server-side collection is not sold as compliant: legal basis left to their data protection officer (the main trap in batch3).
- Option A "nykyinen siistittynä" is real, with the 0,5-point rule (P7); licence impact reported per option.
- Existing tags reported as findings, not removed; explicit "Emme tee" list: no build, migration, tag removal, legal opinion, AI.
- Gate 1 before scoring; pilot restricted to synthetic or anonymised data, no customer or prescription-level data.
- Stated unknowns with fallbacks: licence list wk 2, sample data wk 3 (document check, scores marked less certain).
