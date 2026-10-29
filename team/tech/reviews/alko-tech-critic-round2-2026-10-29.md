# Alko tech critic, round 2, 2026-10-29 (tech lens only; deck v5)

Verdict: **strong**. Round-1 fixes all landed. No invented vendor, no AI/ML, diagram present,
unknowns tied to gates. Remaining gaps are narrower and would only be found by a reader who checks every parameter.
Sources: RFP "audit registries, eliminate redundant records, implement automated validation routines";
bio "reviewing every query parameter herself", "high-impact transformation that stands out".

## Round-1 fixes
1. Rule precedence + Gate 1 precision/sample (slides 4, 6): YES. T4 veto and IBAN-different-Y-tunnus rule on slide 4;
   Gate 1 has 300 labelled pairs, labeller, ~0.5 pv, target agreed before any merge.
2. ERP write-back fallback + unmerge of references (slides 3, 6): YES. Handover to ERP admins, throughput in rows/day,
   audit table stores moved references, post-merge references go to manual review.
3. Gate 3 measurable + plan/gate agree (slides 5, 6): YES. 2-week dry run wk 6-8, 100-alert sample, example <5 %,
   baseline listed, plan row says "koeajo alkaa vk 6".

## Top 3 new tech fixes

### 1. Slide 4 (rules): survivorship and empty values are not defined
Problem: "pääietue valitaan sovitulla säännöllä" (slide 3) is the only survivorship statement. T2/T3 need pack size
and strength %, but master data often has these empty; the rule outcome for blanks is undefined. A parameter-checker
asks "which record's price/supplier/status wins, and what if the field is empty?"
Exact change, slide 4, add bullet under the precedence line:
"**Pääietue ja tyhjät arvot:** attribuuttikohtainen voittosääntö (esim. aktiivinen ennen passiivista, täydempi tietue, uusin muutos) kirjataan sääntökirjaan portilla 1. Jos pakkauskoko tai vahvuus-% puuttuu, pari menee tarkistusjonoon, ei varmaksi ehdokkaaksi."
Evidence: "reviewing every query parameter herself".

### 2. Slide 6 (Gate 1) and slide 5 (D5): recall and the scorecard metrics are unmeasured
Problem: precision is measured on labelled candidate pairs only; duplicates the rules miss are never counted, yet the
goal is "eliminate redundant records". D5 "laatumittaristo" has no named measures, so "ennen/jälkeen-luvut" is vague.
Exact change:
- Slide 6, Gate 1 row, append: "Löydettyjen kaksoiskappaleiden kattavuus arvioidaan käsin tarkistetusta satunnaisotoksesta (esim. 200 riviä), ja puuttuvien osuus raportoidaan D1:ssä."
- Slide 5, D5 cell: replace "laatumittaristo BI:ssä" with "laatumittaristo BI:ssä: kaksoiskappaleaste, täyttöaste, avainvirheet ja avoimet poikkeamat rekistereittäin, ennen/jälkeen".
Evidence: RFP "eliminate redundant records"; bio "high-impact transformation that stands out".

### 3. Slides 5 and 6 (Gate 2): full batch has about one week after the pilot
Problem: pilot at wk 5, phase 2 ends wk 6. If merges go through ERP admins, the full batch cannot finish in one
week, and D3 ("hyväksytyt yhdistämislistat") is the only phase-2 deliverable. Gate 2 says size "mitoitetaan" but not what
happens to the plan.
Exact change, slide 6, Gate 2 row, append: "Jos koko erä ei ehdi vk 6 mennessä, viimeistellyt listat luovutetaan vk 6 ja loput yhdistämiset ajetaan ERP-ylläpidon aikataulussa vk 7-10 rinnakkain validoinnin kanssa; D3 on valmis kun lista on hyväksytty, ei kun ERP on ajanut sen."
Evidence: own slide 6 unknown "Yhdistämisreitti ERP:hen (rajapinta vai ylläpito)".

## Missing technical answers
- Volumes unknown: slide 6 says review-queue size is estimated wk 2; say it sets Alko-side review effort.
- Which 10 validation rules: only examples (EAN check digit, Y-tunnus). Add "lista sovitaan portilla 1 auditoinnin löydösten mukaan" to slide 4.
