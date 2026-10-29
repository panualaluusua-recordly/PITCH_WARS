# Alko tech critic, 2026-10-29 (tech lens only; deck v4 + team/tech/slides/alko.md)

Verdict: **strong** (adequate-to-strong; three gaps below would make it hard to attack).
Checked against RFP ("audit registries, eliminate redundant records, implement automated validation
routines"; "an ERP system, its current data setup, and a BI tool operating on a public cloud") and bio
("reviewing every query parameter herself"). No vendor named by the buyer is invented. No AI/ML. Good.

## Top 3 tech fixes

### 1. Slide 3 (rules) and slide 6 (Gate 1): rule precedence and match precision are unspecified
Problem: T1 (same EAN = sure candidate) and T4 (different pack size/vintage = never merge) can
contradict; the same EAN can be reused across pack sizes. S1 (same IBAN = sure candidate) can hit
different legal entities (group companies, payment agents). A reader who checks every parameter will
find this. Gate 1 says only "merkityn otoksen tarkkuus": no sample size, no target, no labeller
(v3 had >=300 pairs; v4 lost it).
Exact change:
- Slide 3, add under the table: "**Ensisijaisuus:** T4 on veto, se ohittaa T1, T2 ja S1. Sama IBAN eri Y-tunnuksella menee tarkistusjonoon, ei varmaksi ehdokkaaksi."
- Slide 6, Gate 1 row: replace "merkityn otoksen tarkkuus" with "vähintään 300 merkittyä ehdokaspariä (Alkon asiantuntija merkitsee, noin 0,5 pv); varmojen sääntöjen tarkkuustavoite sovitaan ja vahvistetaan ennen yhtään yhdistämistä".
Evidence: "reviewing every query parameter herself"; enfuce reply (won) on rule matching rated "partly met".

### 2. Slide 3 and slide 6 (Gate 2): merge path depends on an unknown, with no fallback; unmerge not defined for it
Problem: slide 3 claims references (open orders, price lists, supplier contracts) "ohjataan pääietueeseen"
and Gate 2 requires "viitteet siirretty", but the ERP write-back route is unknown (interface vs ERP admins).
Restore "palauttaa ennen-arvot" also breaks if new orders were placed against the survivor after the merge.
Exact change:
- Slide 6, Gate 2 row, append: "Jos ERP:ssä ei ole rajapintaa: yhdistämislista ja viiteluettelo luovutetaan ERP-ylläpidolle, pilotti mitataan heidän läpimenoajallaan (rivit/pv), ja koko erän koko mitoitetaan sen mukaan."
- Slide 3 bullet "Yhdistäminen ja palautus", append: "Auditointitaulu tallentaa myös siirretyt viitteet; palautus siirtää viitteet takaisin ja ohittaa viitteet, joita on luotu yhdistämisen jälkeen (käsin tarkistukseen)."
Evidence: RFP "eliminate redundant records"; own slide 6 unknown "Yhdistämisreitti ERP:hen (rajapinta vai ylläpito)".

### 3. Slide 5 and slide 6 (Gate 3): validation gate is tight and has no measurable pass number
Problem: the plan puts validation in weeks 6-9, but Gate 3 at week 8 requires a 2-week dry run, so rules must
be running by week 6 (they overlap Phase 2). "Väärät hälytykset alle sovitun tason" gives no number or
measuring method. Existing duplicates and bad rows will also raise a flood of alerts on day one of dry run.
Exact change:
- Slide 6, Gate 3 row: "Säännöt ajettu 2 vk koeajona (vk 6-8) ilman ilmoituksia kanavaan; väärien hälytysten osuus mitataan Alkon tarkistamasta 100 hälytyksen otoksesta, tavoite (esim. alle 5 %) sovitaan portilla 1. Nykyiset poikkeamat luetellaan lähtötasona, ilmoitetaan vain uudet."
- Slide 5, Phase 3 row: change "6-9" to "6-9, koeajo alkaa vk 6" so plan and gate agree.
Evidence: RFP "implement automated validation routines"; bio "reviewing every query parameter herself".

## Already good (keep)
- Architecture diagram present, tool-neutral, all boxes marked "Alkon omat"; no vendor invented; "Ei uusia lisenssejä".
- Detection is rule-based and explainable; fuzzy matches go only to the review queue; similarity metric named as "ehdotus", thresholds labelled "esimerkki" and tuned on Alko's data.
- Validation (read-only, alerts) is separated from merges (need approval): no approval bottleneck.
- Audit table (who, when, rule, before/after), nothing deleted, old key kept, rollback tested in pilot.
- Gate 1 at week 2 is the de-risking first step: duplicate rate, exact vs fuzzy share, write-back route. Gate 2 pilot of 200 before the full batch.
- Honest unknowns listed with the gate that resolves each; read access in week 1 named as the biggest schedule risk.
- Data protection line for IBAN and addresses; scope fenced to item and supplier masters.
- Prior review items (diagram, merge mechanics, survivorship/references, Gate 1 inputs) are now addressed in v4.

## Missing technical answers
- Survivorship per attribute (which record's values win) is still only "sovittu säännöllä": say it is agreed and listed in the rule book at Gate 1.
- Volumes unknown; fine, but Gate 1 should state they set review-queue size and effort.
