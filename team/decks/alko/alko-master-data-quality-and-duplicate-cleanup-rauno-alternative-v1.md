<!-- title: Alko · Master Data Quality and Duplicate Cleanup -->
# Alkon tuote- ja toimittajatiedot kuntoon: kaksoiskappaleet pois, säännöt näkyviin

## Auditointi, kaksoiskappaleiden siivous ja automaattinen validointi 10 viikossa. Kiinteä hinta 21 320 € (+ alv). Ei sopimuspoikkeamia.

Ehdotus: Katariina Lehtonen, Head of Data and Analytics · Recordly Oy · Helsinki

---

# Tavoitteet ja tausta: mitä olemme lukeneet rivien välistä

| Alkon lähtökohta | Mitä lupaamme |
|---|---|
| Tuote- ja toimittajatiedot ohjaavat ERP:tä, nykyistä dataratkaisua ja BI-työkalua. **Kaksoiskappaleet vääristävät raportit ja toimintaa.** | **Rajattu ensimmäinen vaihe:** yhden ERP:n enintään 5 000 tuotetta ja 500 toimittajaa, 200 hyväksytyn yhdistämisen pilotti ja 10 validointisääntöä. Laajempi siivous erikseen. |
| Englanninkieliset työpajat ja ohjeet ovat jumittaneet käyttöönotot | **Kaikki suomeksi:** työpajat, sääntökirja, ohjeet ja koulutus. Suomen kieli on roolivaatimus; kielitaito vahvistetaan ennen lähettämistä. |
| Katariina tarkistaa jokaisen kyselyn parametrin itse | **Täysi läpinäkyvyys:** jokainen sääntö ja raja-arvo sääntökirjassa. Hän hyväksyy säännöt ja raja-arvot ennen käyttöönottoa, eikä mitään yhdistetä ilman hyväksyntää. |
| Tavoitteena näkyvä, merkittävä muutos | **Mitattava tulos:** laatumittaristo BI-työkaluun, ennen/jälkeen-luvut johdolle |

> Rehellinen tuntematon: kaksoiskappaleiden määrä selviää vasta auditoinnissa (vk 2). **Portti 1** päättää, mitä siivotaan.

---

# Suositeltu tekninen ratkaisu: hyväksytyt ja peruttavat yhdistämiset

<div style="display:flex;align-items:stretch;gap:14px;margin:0.2em 0 0.35em 0;font-size:22px;line-height:1.25;">
<div style="flex:1;background:#262626;border-radius:10px;padding:14px;"><div style="color:#E3FF87;font-weight:800;margin-bottom:10px;">Lähteet (Alkon omat)</div><div style="border:2px solid #E3FF87;border-radius:6px;padding:8px;margin-bottom:8px;">ERP: tuoterekisteri</div><div style="border:2px solid #E3FF87;border-radius:6px;padding:8px;margin-bottom:8px;">ERP: toimittajarekisteri</div><div style="border:2px solid #E3FF87;border-radius:6px;padding:8px;">Nykyinen dataratkaisu</div></div>
<div style="align-self:center;color:#E3FF87;font-size:40px;font-weight:800;">→</div>
<div style="flex:1;background:#262626;border-radius:10px;padding:14px;"><div style="color:#E3FF87;font-weight:800;margin-bottom:10px;">Auditointi ja tunnistus</div><div style="border:2px solid #E3FF87;border-radius:6px;padding:8px;margin-bottom:8px;">Profilointi: täyttöasteet, avainvirheet</div><div style="border:2px solid #E3FF87;border-radius:6px;padding:8px;">Säännöt T1–T4, S1–S2 koodina Alkon repossa</div></div>
<div style="align-self:center;color:#E3FF87;font-size:40px;font-weight:800;">→</div>
<div style="flex:1;background:#262626;border-radius:10px;padding:14px;"><div style="color:#E3FF87;font-weight:800;margin-bottom:10px;">Hyväksyntä</div><div style="border:2px solid #E3FF87;border-radius:6px;padding:8px;margin-bottom:8px;">Tarkistusjono: Alkon nimeämä omistaja hyväksyy</div><div style="border:2px solid #E3FF87;border-radius:6px;padding:8px;">Auditointitaulu: kuka, milloin, sääntö, ennen/jälkeen</div></div>
<div style="align-self:center;color:#E3FF87;font-size:40px;font-weight:800;">→</div>
<div style="flex:1;background:#262626;border-radius:10px;padding:14px;"><div style="color:#E3FF87;font-weight:800;margin-bottom:10px;">ERP-muutos</div><div style="border:2px solid #E3FF87;border-radius:6px;padding:8px;margin-bottom:8px;">Yhdistämislista ERP-muutosprosessiin</div><div style="border:2px solid #E3FF87;border-radius:6px;padding:8px;">Vanha avain säilyy, palautus mahdollinen</div></div>
<div style="align-self:center;color:#E3FF87;font-size:40px;font-weight:800;">→</div>
<div style="flex:1;background:#262626;border-radius:10px;padding:14px;"><div style="color:#E3FF87;font-weight:800;margin-bottom:10px;">Valvonta</div><div style="border:2px solid #E3FF87;border-radius:6px;padding:8px;margin-bottom:8px;">Validointi: ilmoitus kanavaanne</div><div style="border:2px solid #E3FF87;border-radius:6px;padding:8px;">Laatumittaristo Alkon BI-työkaluun</div></div>
</div>
<div style="background:#2b3118;border-radius:6px;padding:8px 14px;margin:0 0 0.6em 0;font-size:22px;color:#EFEFEF;">Kaikki ajetaan Alkon ympäristössä ja pääsynhallinnassa. ERP, dataratkaisu, BI ja pilvi ovat Alkon nykyiset (tarkennetaan vk 1). Ei uusia lisenssejä.</div>

- **Yhdistäminen ja palautus:** pääietue valitaan sovitulla säännöllä, viitteet (avoimet tilaukset, hinnastot, toimittajasopimukset) ohjataan pääietueeseen, vanha avain säilyy passiivisena. Palautus palauttaa auditointitaulun ennen-arvot; testataan pilotissa. Auditointitaulu tallentaa myös siirretyt viitteet; palautus siirtää viitteet takaisin ja ohittaa viitteet, joita on luotu yhdistämisen jälkeen (käsin tarkistukseen).
- **Validointi on lukevaa:** virhe tuottaa ilmoituksen ja poikkeamalistan, ei muuta dataa eikä pysäytä latausta. Siksi hyväksyntä tarvitaan vain yhdistämisille.
- **Tietosuoja:** toimittajien IBAN- ja osoitetiedot käsitellään vain Alkon ympäristössä Alkon pääsynhallinnalla, ei kopioita ulos.

---

# Säännöt auki, ei mustaa laatikkoa

## Esimerkkisäännöt: raja-arvot sovitaan yhdessä portilla 1

| Sääntö (esimerkki, raja-arvot sovitaan yhdessä) | Tulos |
|---|---|
| **T1** Sama EAN/GTIN-koodi | Varma ehdokas |
| **T2** Sama toimittaja + normalisoitu nimi + pakkauskoko + vahvuus-% | Varma ehdokas |
| **T3** Nimen samankaltaisuus ≥ 0,85 + sama pakkauskoko ja vahvuus | Tarkistusjono |
| **T4** Eri pakkauskoko tai vuosikerta | **Ei koskaan yhdistetä** |
| **S1** Sama Y-tunnus tai IBAN | Varma ehdokas |
| **S2** Nimi ilman Oy/Ab/Ltd + osoite ≥ 0,9 | Tarkistusjono |

**Ensisijaisuus:** T4 on veto, se ohittaa T1, T2 ja S1. Sama IBAN eri Y-tunnuksella menee tarkistusjonoon, ei varmaksi ehdokkaaksi.

**Pääietue ja tyhjät arvot:** attribuuttikohtainen voittosääntö (esim. aktiivinen ennen passiivista, täydempi tietue, uusin muutos) kirjataan sääntökirjaan portilla 1. Jos pakkauskoko tai vahvuus-% puuttuu, pari menee tarkistusjonoon, ei varmaksi ehdokkaaksi.

- **Sääntöpohjainen, ei koneoppimista:** jokainen osuma selitettävissä. Samankaltaisuus lasketaan avoimella merkkijonomitalla (ehdotus: Jaro-Winkler). Raja-arvot 0,85 ja 0,9 ovat esimerkkejä: ne viritetään Alkon omasta datasta merkityllä otoksella.
- **Ei poistoja:** yhdistäminen Alkon ERP-muutosprosessin kautta, jokainen päätös auditointitaulussa ja peruttavissa.
- Koodi ja säännöt Alkon omassa repossa ja ympäristössä, lukuoikeus **päivästä 1**. 10 tärkeintä validointisääntöä (esim. EAN-tarkiste, Y-tunnus) ajetaan Alkon nykyisessä latauksessa tai ajastettuna; tarkennetaan vk 1.

---

# Toimitukset, toteutussuunnitelma ja aikataulu

| Vaihe | Viikot | Toimitus | Pv |
|---|---|---|---|
| **1 · Auditointi** | 1–2 | D1: auditointiraportti (kaksoiskappaleaste, täyttöasteet, avainvirheet) | 4 |
| **Portti 1** | vk 2 | Alko päättää laajuuden ja sääntöjen raja-arvot | – |
| **2 · Kaksoiskappaleet** | 3–6 | D2: sääntökirja (suomeksi), D3: hyväksytyt yhdistämislistat | 7 |
| **Portti 2** | vk 5 | Enintään 200 hyväksytyn yhdistämisen pilotti; ei koko rekisterin massasiivousta | – |
| **3 · Validointi** | 6–9, koeajo alkaa vk 6 | D4: 10 automaattista sääntöä, virheilmoitukset kanavaanne; **portti 3:** 2 vk koeajo ennen ilmoituksia | 8 |
| **4 · Vakiinnutus** | 10 | D5: laatumittaristo BI:ssä: kaksoiskappaleaste, täyttöaste, avainvirheet ja avoimet poikkeamat rekistereittäin, ennen/jälkeen; suomenkieliset ohjeet, koulutus | 4 |

- **Ei jatkuvaa rinnakkain työskentelyä:** Recordly tekee profiloinnin, koodin ja testit itsenäisesti. Alkolta yhteensä enintään 12 tuntia: aloitus 1 h, merkintäotos 4 h, sääntö- ja porttipäätökset 3 h, hälytysotos 2 h, luovutus 2 h. Kirjallinen viikkoraportti, ei toistuvia statuspalavereja. Opastus tallenteena ja suomenkielisin ohjein.
- **Edellytykset:** lukuoikeus tuote- ja toimittajadataan vk 1, yhdistämiset ERP-ylläpidon kautta; tarkistusjonon koko ja ERP-ajon vaatima asiakastyö arvioidaan vk 2. Pilotin edellytys on toimiva nykyinen yhdistämismekanismi ja että hyväksynnät sekä ERP-ajo mahtuvat 12 tunnin asiakaspanokseen; muuten portilla pysähdytään tai pilotin eräkokoa pienennetään.

---

# Tekniset portit: ensin luvut Alkon datasta, sitten yhdistäminen

| Portti | Milloin | Läpäisyehto |
|---|---|---|
| **1 · Laajuus** | vk 2 | Kaksoiskappaleaste rekistereittäin; varmojen (T1, T2, S1) ja tarkistusjonon osuus; ERP:n yhdistämisreitti vahvistettu; enintään 300 merkittyä ehdokasparia (Alkon asiantuntija merkitsee, noin 0,5 pv); varmojen sääntöjen tarkkuustavoite sovitaan ja vahvistetaan ennen yhtään yhdistämistä. Alko päättää laajuuden ja raja-arvot. Löydettyjen kaksoiskappaleiden kattavuus arvioidaan käsin tarkistetusta satunnaisotoksesta (esim. 200 riviä), ja puuttuvien osuus raportoidaan D1:ssä. |
| **2 · Pilotti** | vk 5 | 200 hyväksyttyä yhdistämistä ERP-muutosprosessin kautta; viitteet siirretty; vähintään yksi palautus testattu. Jos ERP:ssä ei ole rajapintaa: yhdistämislista ja viiteluettelo luovutetaan ERP-ylläpidolle, pilotti mitataan heidän läpimenoajallaan (rivit/pv), ja koko erän koko mitoitetaan sen mukaan. Tämän hinnan toimitus päättyy enintään 200 hyväksyttyyn yhdistämiseen ja lopun aineiston hyväksyttyyn siivousjonoon. Koko rekisterin jatkoajo ja uudet ERP-integraatiot eivät sisälly hintaan. |
| **3 · Validointi** | vk 8 | Säännöt ajettu 2 vk koeajona (vk 6-8) ilman ilmoituksia kanavaan; väärien hälytysten osuus mitataan Alkon tarkistamasta 100 hälytyksen otoksesta, tavoite (esim. alle 5 %) sovitaan portilla 1. Nykyiset poikkeamat luetellaan lähtötasona, ilmoitetaan vain uudet. |

### Tekniset tuntemattomat ja miten ne ratkeavat
- ERP-tuote, dataratkaisu, BI ja pilvi: ei nimetty, selvitetään vk 1.
- Yhdistämisreitti ERP:hen (rajapinta vai ylläpito): vahvistetaan portilla 1.
- Viittaukset muista tauluista: kartoitetaan auditoinnissa; kaksoiskappale on siivottu vasta, kun viitteet on siirretty.
- Lukuoikeus tuote- ja toimittajadataan vk 1 on aikataulun suurin riski.

---

# Tiimi: pieni, kokenut, suomeksi

| | Lead Data Architect | Senior Data Engineer | Senior Data Analyst |
|---|---|---|---|
| **Vaaditut sertifikaatit** | Azure Solutions Architect Expert · AWS Certified Solutions Architect | Azure Data Engineer Associate · Google Cloud Professional Data Engineer · dbt | Power BI Data Analyst Associate |
| **Vaaditut kielet** | Suomi (vaatimus), englanti | Suomi (vaatimus), englanti | Suomi (vaatimus), englanti |
| **Suunniteltu panos** | 5 pv / 10 vk | 16 pv / 10 vk | 2 pv, loppuvaihe |

Pilvialusta ei ole tarjouspyynnössä nimetty: roolien vaadittu pilviosaaminen täsmennetään alustanne mukaan vk 1; henkilöt ja aloitus vahvistetaan ennen nimeämistä. Alkolla on oikeus vaatia konsultin vaihtoa; korvaaja on yhtä kokenut, perehdytys meidän kustannuksellamme.

---

# Hinta ja sopimus

| Rooli | Päivät | Päivähinta |
|---|---|---|
| Lead Data Architect | 5 | 920 € |
| Senior Data Engineer | 16 | 920 € |
| Senior Data Analyst | 2 | 1 000 € |

## Kiinteä kokonaishinta: 23 henkilöpäivää = 21 320 € (+ alv)

- **Maksu:** portti 1: 3 680 €, hyväksytty pilotti: 6 440 €, validointi ja luovutus: 11 200 € (yhteensä 21 320 €), 30 pv netto. **Lisenssit:** ei uusia, rakennetaan nykyisen ympäristön päälle.
- **Kiinteä hinta:** ylitykset ovat Recordlyn riski. Kaikki toimitukset ja koodi ovat Alkon omaisuutta.
- **Sopimuspoikkeamat: ei ole. Alkon vakiosopimusehdot sellaisenaan.**


**Rajaus ja hinta:** 23 henkilöpäivää, 8 h/pv: arkkitehti 5 × 920 €, DE 16 × 920 €, DA 2 × 1 000 €. Enintään yksi arkkitehti. CV:t, vaaditut sertifikaatit ja aloituspäivä vahvistetaan ennen henkilöiden nimeämistä. Vaiheittain: auditointi A1+DE3 = 3 680 €; siivous A2+DE5 = 6 440 €; validointi A1+DE6+DA1 = 7 440 €; luovutus A1+DE2+DA1 = 3 760 €. Portilla 1 voidaan lopettaa 3 680 €:n auditointiin. Laajempi siivous, uudet integraatiot ja muut rekisterit vain erillisellä kirjallisella tilauksella.

<!-- coverage v6 (v5 + survivorship/blanks, recall sample + D5 metrics, Gate 2 overrun) / v5 (v4 + three tech fixes): RFP aims/background=slide2; technical solution=slide3 (architecture diagram)+slide4 (rules); deliverables+plan+timeline=slide5 (D1-D5); tech gates+unknowns=slide6; team+certs+availability=slide7; total pricing=slide8; contract deviations=none slide1+8. Hidden: English workshops->all Finnish (s2,s5,s7); reviews every parameter->rule table, metric named, thresholds tuned on labelled sample, repo access day 1 (s4), approval before any merge, audit table + unmerge (s3); high-impact->BI scorecard before/after (s2,s5). Traps: no AI/ML (s4 rule-based); no new licences (s3 band); honest unknowns stack, dup rate, ERP write-back, references (s6); scope fence = item+supplier masters only. -->
