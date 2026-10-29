<!-- title: Terveystalo · Analytics-insinööri 6 kk -->
# Senior-analytics-insinööri Databricksiin kuudeksi kuukaudeksi

## Ensin lähteiden seulonta, sitten rakennus aalloissa. Suomeksi, teidän ympäristössänne, ilman uusia työkaluja. 15 640 € excl. VAT.

Ehdotus: Riikka Voutilainen, Director of Data & Analytics · Recordly Oy · Helsinki

---

# Ehdotus yhdellä sivulla

:::cols
### Mitä tarjoamme
- **Yksi senior data engineer** vahvistamaan keskitettyä Data & Analytics -tiimiä Helsingissä, 6 kuukautta, osa-aikaisesti (17 henkilöpäivää)
- Putkien ja tietomallien rakennus **Databricksissa** raportointiin (BI) ja ERP-datavirtoihin
- **Ei uusia alustoja, ei lisenssikuluja.** Kaikki koodi teidän tenantissanne ja repoissanne
- **Suomi:** työ, dokumentaatio ja koodikommentit suomeksi
- Saatavilla **sopimuksen allekirjoituksesta**
:::col
### Mitä tämä ei ole
- Ei lupausta "kaikista lähteistä" ennen seulontaa. Teidän kokemuksenne mukaan jokainen lähde ei ole mahdollinen tai tarpeellinen.
- Ei tekoälyä, ei Data Vault -mallinnusta, ei uudelleenalustointia. Vain perustyötä jatkuvuuden hengessä.
- **Hinta: 15 640 € excl. VAT**, 17 pv × 920 €
- Sopimus: **Terveystalon vakioehdot sellaisinaan, ei poikkeamia**
:::

---

# Tekninen ratkaisu ja vaiheet

| Lähteet | Yksi yleinen poimintamalli | Teidän Databricks-tasonne | Käyttö |
|---|---|---|---|
| ERP (luku ensin; kirjoitus takaisin vain erillisellä päätöksellä) | Konfiguroitava poiminta teidän tenantissa, EU-alue | Nykyiset kerrokset (bronze / silver / gold, vahvistetaan) | BI-raportit ja semanttinen kerros |
| Operatiiviset järjestelmät | Uusi lähde = konfiguraatio, ei uusi räätälöity putki | Testit + rivimääräsovitus vanhaan raporttiin | Vanha raportti rinnalla ennen käyttöönottoa |
| Lähteet, joiden määrä selviää vaiheessa 0 | | Kehitys maskatulla tai synteettisellä datalla, tuotanto vain teidän roolimallinne kautta | |

**Seulonta:** kartoitetut lähteet → toteutettavissa → tarpeellisia → rakennetaan aalloissa. Pudotuslista kirjataan näkyviin.

| Vaihe | Kuukausi | Pv | Sisältö |
|---|---|---|---|
| **0 Kevyt aloitusauditointi** | 1 | 3 | Lähdekartoitus: omistaja, pääsy, volyymi, päivitystarve, mikä raportti tarvitsee. Kirjallinen go/no-go ja pudotuslista |
| **Aalto 1** | 2-3 | 6 | Arvokkaimmat lähteet tuotantoon, mallit ja testit |
| **Aalto 2** | 4-5 | 6 | Seuraavat hyväksytyt lähteet ja ERP-virrat |
| **Luovutus** | 6 | 2 | Dokumentaatio suomeksi, lineage ja tietosanakirja, tiimin perehdytys |

---

# Laadunvarmistus: jokainen muutos katselmoidaan

- **Jokainen pull request vaatii nimetyn senior-katselmoijan hyväksynnän.** Ei automaattisia yhdistämisiä, ei suoria tuotantoon vientejä. Estää sen, että tarkistamaton logiikka pääsee kliinisiin raportteihin.
- Ennen käyttöönottoa **rivimäärä- ja summasovitus** vanhaan raporttiin, ero selitetään kirjallisesti
- Kehitys- ja testiympäristöt **vain ei-potilasdatalla** (maskattu tai synteettinen), käsittely vain EU:ssa
- **Kuka tekee mitä:** Recordlyn insinööri rakentaa ja kirjoittaa dokumentaation; Terveystalon nimetty senior hyväksyy jokaisen muutoksen ja omistaa tuotantoon viennin
- **Työtapa:** viikoittainen hands-on-tarkistuspiste ja asynkroninen päivitys yhteisessä chat-työkalussa, ei raskaita statuspalavereja
- **Potilaille näkyvät digipalvelut** (esim. ajanvarausassistentti): ei tässä laajuudessa, mutta jos sen data laskeutuu Databricksiin, se on yksi lähdekandidaatti vaiheen 0 seulonnassa

**Rehellinen tuntematon:** ERP-tuote, rajapinnan tyyppi ja lähteiden määrä eivät ole tiedossa. Ne selvitetään vaiheessa 0, ja laajuus lukitaan go/no-go-portilla.

---

# Tiimi, referenssit, hinta ja ehdot

| | Senior Data Engineer |
|---|---|
| **Kokemus** | 10+ vuotta; Databricks-putket, terveydenhuollon ja ERP-datan integraatiot, CI/CD |
| **Sertifioinnit** | Databricks Certified Data Engineer Professional · Microsoft Certified: Azure Data Engineer Associate |
| **Kielet** | Suomi (äidinkieli), englanti |
| **Saatavuus** | Sopimuksen allekirjoituksesta, 3 pv/kk (17 pv yhteensä) |

**Referenssit** (kontaktihenkilöt annetaan lyhytlistatuille): pohjoismainen terveydenhuollon toimija, 2025: Databricks-putket ja raportointimallit; pohjoismainen vähittäiskauppias, 2025: lähdekartoitus ja ERP-integraatio aalloissa.

Terveystalolla on oikeus rekrytoida konsultti suoraan 12 kuukauden jälkeen ilman palkkio- tai siirtomaksuja. Hyväksymme ehdon. Konsultin vaihto-oikeus hyväksytään.

## Hinta ja ehdot

| Rooli | Päiviä | Päivähinta | Yhteensä |
|---|---|---|---|
| Senior Data Engineer | 17 | 920 € | 15 640 € |
| **Kokonaishinta (excl. VAT)** | | | **15 640 €** |

- **Laskutus:** kuukausittain toteutuneiden päivien mukaan (3+3+3+3+3+2 pv), maksuehto Terveystalon vakioehtojen mukaan
- **Lisenssit:** ei yhtään, työ tehdään nykyisessä Databricksissä ja BI-työkalussa
- **Sisältää:** matkat Helsingissä, dokumentaation, katselmointiin osallistumisen
- **Sopimus:** vakioehdot sellaisenaan, ei poikkeamia
