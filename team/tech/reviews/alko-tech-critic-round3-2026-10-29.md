# Alko tech critic, round 3, 2026-10-29 (tech lens only; deck v6)

Verdict: **strong**. All three round-2 fixes landed. No invented vendor, no AI/ML, diagram present, gates measurable.
Sources: RFP "audit registries, eliminate redundant records, implement automated validation routines";
bio "reviewing every query parameter herself", "high-impact transformation that stands out".

## Round-2 fixes landed?
1. Survivorship and blanks to review queue (slide 4): YES ("Pääietue ja tyhjät arvot").
2. Recall on random sample + D5 metrics (slides 5, 6): YES (200-row sample, D5 names four measures).
3. Gate 2 overrun rule (slide 6): YES (lists handed over wk 6, ERP admins wk 7-10, D3 done at approval).
Not landed from round-2 "missing answers": the 10 validation rules list is still examples only.

## Top 3 new tech fixes

### 1. Slide 4 (last bullet) and slide 5 (D4): the 10 rules are undefined, and nothing stops duplicates coming back
Problem: "10 tärkeintä validointisääntöä (esim. EAN-tarkiste, Y-tunnus)" is open-ended; a parameter-checker cannot
approve it. Cleanup without a creation-time check lets duplicates return, so "eliminate redundant" is not durable.
Exact change, slide 4, append to the last bullet:
"Lista 10 säännöstä sovitaan portilla 1 auditoinnin löydösten mukaan; vähintään yksi säännöistä ajaa T1/T2-haun uusille tietueille ja ilmoittaa mahdollisen kaksoiskappaleen luontihetken jälkeen (ei estä tallennusta)."
Evidence: RFP "implement automated validation routines".

### 2. Slide 6 (Gate 1 and Gate 2): approval capacity and ERP change windows are not sized
Problem: every merge needs a named Alko owner's approval, but review-queue size only "arvioidaan vk 2" and no
reviewer throughput is stated. Merging open orders and price lists during a campaign or price-list cycle is a freeze risk.
Exact change, slide 6, Gate 1 row, append:
"Tarkistusjonon koko ja arvioitu hyväksyjän työmäärä (rivit/pv) raportoidaan D1:ssä; Alko nimeää hyväksyjän ja varahyväksyjän. Yhdistämisten ajoikkunat sovitaan ERP-ylläpidon kanssa niin, ettei avoimia tilauksia tai hinnastokierrosta häiritä."
Evidence: slide 3 "Alkon nimeämä omistaja hyväksyy"; bio "reviewing every query parameter herself".

### 3. Slide 4 (rules table): name normalisation and the precision target are vague
Problem: T2/T3/S2 depend on "normalisoitu nimi", but Finnish data (ä/ö, abbreviations, case, punctuation, vintage
format) is not specified; Gate 1 precision target has no example number while Gate 3 has "alle 5 %".
Exact change, slide 4, extend "Sääntöpohjainen" bullet:
"Normalisointi (isot/pienet kirjaimet, ä/ö, välimerkit, lyhenteet, vuosikerran muoto) kirjataan sääntökirjaan ja testataan 300 merkityllä parilla; varmojen sääntöjen tarkkuustavoite esim. vähintään 99 %, sovitaan portilla 1."
Evidence: bio "reviewing every query parameter herself".

## Missing technical answers
- Cloud/ERP/BI stay unnamed; deck says "vk 1", acceptable given the RFP says only "a public cloud".
- Rollback depends on ERP admins; unmerge turnaround time not stated (add rows/day from the Gate 2 pilot).
