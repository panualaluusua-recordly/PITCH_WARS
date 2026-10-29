<!-- title: Alko · Master Data Quality and Duplicate Cleanup -->
# Alkon tuote- ja toimittajatiedot kuntoon: kaksoiskappaleet pois, säännöt näkyviin

## Auditointi, kaksoiskappaleiden siivous ja automaattinen validointi iikossa. Kiinteä hinta 35 280 € (+ alv). Ei sopimuspoikkeamia.

Ehdotus: Katariina Lehtonen, Head of Data and Analytics · Recordly Oy · Helsinki

---

# Tavoitteet ja tausta: mitä olemme lukeneet rivien välistä

| Alkon lähtökohta | Mitä lupaamme |
|---|---|
| Tuote- ja toimittajatiedot ohjaavat ERP:tä, nykyistä dataratkaisua ja BI-työkalua. **Kaksoiskappaleet vääristävät raportit ja toimintaa.** | **Ensimmäinen vaihe:** tuote- ja toimittajarekisterit. Muut rekisterit vasta tuloksen perusteella. |
| Englanninkieliset työpajat ja ohjeet ovat jumittaneet käyttöönotot | **Kaikki suomeksi:** työpajat, sääntökirja, ohjeet ja koulutus. Suomen kieli on roolivaatimus; kielitaito vahvistetaan ennen lähettämistä. |
| Katariina tarkistaa jokaisen kyselyn parametrin itse | **Täysi läpinäkyvyys:** jokainen sääntö ja raja-arvo sääntökirjassa. Mikään sääntö ei aja ilman hänen hyväksyntäänsä. |
| Tavoitteena näkyvä, merkittävä muutos | **Mitattava tulos:** laatumittaristo BI-työkaluun, ennen/jälkeen-luvut johdolle |

> Rehellinen tuntematon: kaksoiskappaleiden määrä selviää vasta auditoinnissa (vk 2). **Portti 1** päättää, mitä siivotaan.

---

# Suositeltu tekninen ratkaisu: säännöt auki, ei mustaa laatikkoa

## ERP + nykyinen dataratkaisu → profilointi → sääntömoottori (Alkon repo) → tarkistusjono (Katariina hyväksyy) → ERP-muutosprosessi → BI-laatumittaristo

| Sääntö (esimerkki; mitta ja raja-arvot tavoitteita, Katariina hyväksyy) | Tulos |
|---|---|
| **T1** Sama EAN/GTIN-koodi | Varma ehdokas |
| **T2** Sama toimittaja + normalisoitu nimi + pakkauskoko + vahvuus-% | Varma ehdokas |
| **T3** Nimen samankaltaisuus ≥ 0,85 + sama pakkauskoko ja vahvuus | Tarkistusjono |
| **T4** Eri pakkauskoko tai vuosikerta | **Ei koskaan yhdistetä** |
| **S1** Sama Y-tunnus tai IBAN | Varma ehdokas |
| **S2** Nimi ilman Oy/Ab/Ltd + osoite ≥ 0,9 | Tarkistusjono |

- **Sääntöpohjainen, ei koneoppimista:** jokainen osuma selitettävissä. Ei poistoja: pääietue valitaan sovitulla säännöllä, viitteet ohjataan uuteen avaimeen, vanha avain säilyy, palautus testataan pilotissa.
- Koodi Alkon repossa, lukuoikeus **päivästä 1**. 10 validointisääntöä joka latauksella: virhe → varoitus ja rivi karanteeniin, ei latauksen pysäytystä.

---

# Toimitukset, toteutussuunnitelma ja aikataulu

| Vaihe | Viikot | Toimitus | Pv |
|---|---|---|---|
| **1 · Auditointi** | 1–2 | D1: auditointiraportti (kaksoiskappaleaste, täyttöasteet, avainvirheet) | 7 |
| **Portti 1** | vk 2 | Alko päättää laajuuden ja sääntöjen raja-arvot | – |
| **2 · Kaksoiskappaleet** | 3–6 | D2: sääntökirja (suomeksi), D3: hyväksytyt yhdistämislistat | 13 |
| **Portti 2** | vk 5 | 200 yhdistämisen pilotti ennen koko erää | – |
| **3 · Validointi** | 6–9 | D4: 10 automaattista sääntöä; **portti 3:** 2 vk varoitustila ennen estoja | 12 |
| **4 · Vakiinnutus** | 10 | D5: laatumittaristo BI:ssä, suomenkieliset ohjeet, koulutus | 6 |

- **Yhdessä tekeminen viikosta 1:** Alkon osaajat työskentelevät rinnalla, ei loppusiirtoa. Lyhyt kirjallinen viikkoraportti, ei status-palavereja.
- **Edellytykset:** lukuoikeus tuote- ja toimittajadataan vk 1, yhdistämiset ERP-ylläpidon kautta; tarkistusjonon koko arvioidaan vk 2.

---

# Tiimi: pieni, kokenut, suomeksi

| | Lead Data Architect | Senior Data Engineer | Senior Data Analyst |
|---|---|---|---|
| **Vaaditut sertifikaatit** | Azure Solutions Architect Expert · AWS Certified Solutions Architect | Azure Data Engineer Associate · Google Cloud Professional Data Engineer · dbt | Power BI Data Analyst Associate |
| **Vaaditut kielet** | Suomi (vaatimus), englanti | Suomi (vaatimus), englanti | Suomi (vaatimus), englanti |
| **Saatavuus** | 1 pv/vk allekirjoituksesta | 2–3 pv/vk allekirjoituksesta | vk 8–10 |

Pilvialusta ei ole tarjouspyynnössä nimetty: tiimi kattaa kolme suurta pilveä, ja täsmennämme vk 1. Alkolla on oikeus vaatia konsultin vaihtoa; korvaaja on yhtä kokenut, perehdytys meidän kustannuksellamme.

---

# Hinta ja sopimus

| Rooli | Päivät | Päivähinta |
|---|---|---|
| Lead Data Architect | 10 | 920 € |
| Senior Data Engineer | 24 | 920 € |
| Senior Data Analyst | 4 | 1 000 € |

## Kiinteä kokonaishinta: 38 henkilöpäivää = 35 280 € (+ alv)

- **Maksu:** kolme yhtä suurta laskua (portti 1, vk 6, vk 10), 30 pv netto. **Lisenssit:** ei uusia, rakennetaan nykyisen ympäristön päälle.
- **Kiinteä hinta:** ylitykset ovat Recordlyn riski. Kaikki toimitukset ja koodi ovat Alkon omaisuutta.
- **Sopimuspoikkeamat: ei ole. Alkon vakiosopimusehdot sellaisenaan.**


**Staffing-tarkistus / Rauno:** roolit ovat vaatimuksia, eivät vahvistettuja henkilöprofiileja. CV:t, sertifikaatit, kielitaito ja todellinen saatavuus vahvistetaan ennen lähettämistä. Työpäivä = 8 h; DE vähintään 115 €/h, DA 125 €/h, AI-osaaminen +5 €/h. Arkkitehdin perushinta 115 €/h on ehdotus hyväksyttäväksi, ei käyttäjän antama vähimmäishinta. Enintään kaksi arkkitehtia. Kiinteän hinnan laajuus ja riskit vahvistetaan ennen sitoutumista.

<!-- coverage: RFP aims/background=slide2; solution+deliverables=slide3+4(D1-D5); plan+timeline=slide4; team+certs+availability=slide5; total pricing=slide6; contract deviations=none slide1+6. Hidden: English workshops->all Finnish (s2,s4,s5); reviews every parameter->rule table, repo access day 1, approval before run (s3); high-impact->BI scorecard before/after (s2,s4). Traps: no AI/ML (s3 rule-based); no new licences; honest unknown dup rate + ERP write-back; scope fence = item+supplier masters only. -->
