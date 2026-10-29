# Alko – Katariina Lehtonen, Head of Data and Analytics

## v1 draft (not sent)
- File: work/decks/alko/alko-master-data-quality-and-duplicate-cleanup-v1.md (.pdf), 6 slides, Finnish.
- Price: 38 pv = EUR 35,280 fixed (architect 10 x 920, DE 24 x 920, DA 4 x 1,000), 10 weeks. Anchor: BI platform < EUR 61k over budget; no direct evidence. Next if over budget: ~EUR 26k (28 pv, audit + dedupe only, validation reduced to 5 rules).
- Bets: (1) all Finnish (bio: English workshops stalled rollouts); (2) rule book with actual matching rules/thresholds, repo read access day 1, nothing runs without her approval (she reviews every query parameter); (3) visible impact: before/after quality scorecard in BI tool for execs, scope fenced to item + supplier masters.
- Deliberately out: AI/ML (rules are deterministic), VDE (no Snowflake stated), other masters, new licences.
- Honest unknowns in deck: duplicate rate (audit wk 2, Gate 1), ERP write-back route (assumed Alko ERP admins apply merges), cloud/BI vendor not named.
- Rule examples (EAN, vintage/pack size never merged, Y-tunnus/IBAN) are illustrative, labelled "esimerkki".

## Rauno / Codex feedback round 2026-10-29

Sent 5 (source version), kind feedback; fee EUR 1,000.

> First and foremost, the total price presented in this deck is above our budget, which stands as the primary obstacle to moving forward with the proposal. On a positive note, I appreciate the absolute commitment to conducting all workshops and documentation in Finnish, which prevents the operational friction that so often stalls retail rollouts. However, having our internal specialists tied up in continuous side-by-side working sessions from the opening week threatens to drain our daily capacity on basic execution when our staff is already fully committed to maintaining ongoing operations. When I integrated our ERP system with our BI tool upon joining Alko, I learned exactly how sensitive our catalog integrity is, and I still review every query parameter myself to ensure nothing subpar ever reaches the executive table.

Response-led final candidate: v7, EUR 21320.

## Final outcome observed by Rauno / Codex

2026-10-29T12:14:14.667129+00:00 — Another team agent submitted `alko-master-data-quality-and-duplicate-cleanup-v7-eur35280.pdf` at 2026-10-29T12:09:25.592714+00:00. Result: **lost**. Rauno's subsequent final send aborted during pre-check (project already closed), before POST and with no additional fee.

> This proposal cannot proceed because the overall commercial commitment stretches past the financial boundary I am willing to justify to executive leadership.

```json
{
  "ratings": {
    "price": "over budget",
    "buyer_fit": "fair",
    "project_fit": "fair",
    "presentation": "excellent"
  },
  "preferences": [
    {
      "area": "buyer",
      "verdict": "not addressed",
      "evidence": "Kalvoilla ei käsitellä katteeseen tai konversioon kytkettyjä kaupallisia pilotteja."
    },
    {
      "area": "buyer",
      "verdict": "met",
      "evidence": "Kalvoilla 2 ja 7 vaaditaan suomen kieli työpajoihin, dokumentaatioon ja kaikille asiantuntijoille."
    },
    {
      "area": "buyer",
      "verdict": "met",
      "evidence": "Kalvoilla 3 ja 4 koodi ja säännöt sijoitetaan Alkon repoon ilman uusia lisenssejä tai suljettuja laatikoita."
    },
    {
      "area": "buyer",
      "verdict": "not addressed",
      "evidence": "Tarjous ei ota kantaa hinnoittelu- tai valikoima-algoritmeihin."
    },
    {
      "area": "project",
      "verdict": "against",
      "evidence": "Kalvo 5 edellyttää Alkon asiantuntijoiden työskentelyä rinnalla heti viikosta 1 alkaen."
    },
    {
      "area": "project",
      "verdict": "met",
      "evidence": "Kalvoilla 3 ja 8 ratkaisu rajataan Alkon nykyiseen ympäristöön ilman uusia SaaS- tai pilvilisenssejä."
    },
    {
      "area": "project",
      "verdict": "not addressed",
      "evidence": "Esityksessä ei mainita ennustavaa inventaariota tai täydennysmalleja."
    },
    {
      "area": "project",
      "verdict": "met",
      "evidence": "Kalvoilla 3 ja 4 esitellään sääntöpohjainen malli, auditointitaulu ja täysin peruttavat yhdistämiset."
    }
  ],
  "presentation": [
    {
      "criterion": "client_understanding",
      "rating": "strong",
      "evidence": "Kalvolla 2 Alkon järjestelmät, taustat ja toiminnan reunaehdot kuvataan suoraan ja osuvasti."
    },
    {
      "criterion": "storyline",
      "rating": "strong",
      "evidence": "Kokonaisuus etenee suoraviivaisesti tavoitteista tekniseen malliin, aikatauluun, tiimiin ja kiinteään hintaan."
    },
    {
      "criterion": "honest_unknowns",
      "rating": "strong",
      "evidence": "Kalvoilla 2 ja 6 tuodaan avoimesti esiin nimeämättömät järjestelmät ja datan saannin pääsyriskit."
    },
    {
      "criterion": "concreteness",
      "rating": "strong",
      "evidence": "Toimitukset D1–D5, tekniset portit, henkilöpäivät ja roolikohtaiset hinnat on määritelty täsmällisesti."
    },
    {
      "criterion": "slide_clarity",
      "rating": "strong",
      "evidence": "Jokaisella kalvolla on ytimekäs pääviesti ja tekstimäärä on pidetty helposti hahmotettavana."
    },
    {
      "criterion": "explanatory_visuals",
      "rating": "strong",
      "evidence": "Kalvon 3 prosessikaavio sekä kalvojen 4–8 taulukkorakenteet välittävät todellista teknistä sisältöä."
    },
    {
      "criterion": "recordly_style",
      "rating": "strong",
      "evidence": "Tumma pohja, limenvihreä tehosteväri, korttiasettelut ja sivunumeroitu alatunniste toistuvat moitteettomasti."
    }
  ]
}
```
