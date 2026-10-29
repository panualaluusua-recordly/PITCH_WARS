<!-- title: Vahterus Oy · Raportoinnin ja vanhojen sovellusten modernisointi -->
# Raportointi suoraan uuteen ERP-järjestelmään, ei erillistä alustaa

## Pragmaattinen modernisointi Uudenkaupungin tehtaalle. Kiinteä hinta 27 400 € ilman alv:tä. Vakiosopimus ilman poikkeamia.

Ehdotus Ronja Lehtomäelle, Head of Digitalization and Analytics · Recordly Oy · Helsinki

---

# Ratkaisuarkkitehtuuri

:::cols
### Näin se toimii
- **Raportit uuden ERPin sisään:** tuotanto- ja toimitusraportit käyttäjän omassa ERP-näkymässä, ei toista työkalua
- **Yksi tietokerros:** nykyinen tietoratkaisu → julkinen pilvi, ja jokaiselle ERP-objektille oma tietosopimus, jotta raportit kestävät ERP-käyttöönoton muutokset
- **BI-työkalu vain siellä, missä ERP ei riitä** (esim. johdon yhteenvedot), ei uusia lisenssejä
- Vanhat sovellukset ja raportit käydään läpi ja priorisoidaan **euromääräisen hyödyn** mukaan
:::col
### Rajaukset
- Ei ERP-toteutusta eikä ERP-konfigurointia: sen tekee ERP-toimittajanne, me parituemme
- Ei uusia alustoja
- Ei tuotantomuutoksia Q1:llä
:::

---

# Tuottolaskuri: jokainen commit perustellaan

| Mitä | Miten |
|---|---|
| **ROI-lista** | Jokaisella työlistan kohdalla arvioitu euromääräinen hyöty ja mittari, sovitaan kanssanne viikolla 1 |
| **Commit → hyöty** | Jokainen koodimuutos linkitetty työlistan kohtaan. Voitte seurata muutoksia kehittäjän tasolla. |
| **Kuukausiraportti** | Toteutunut vs. arvioitu hyöty per kohta, yksi sivu |
| **Karsinta** | Kohta, jonka hyöty ei kata työtä, pudotetaan listalta |

Kaikki työpajat, dokumentaatio ja koulutus **suomeksi**.

---

# Suunnitelma: rakennetaan Q1:llä, tuotantoon huhtikuussa

| Ajankohta | Työ | Tuotannossa? |
|---|---|---|
| **Joulu** | Jatkokeskustelu, ROI-lista, ERP-aikataulun sovitus | Ei |
| **Tammi–maalis** | Raporttien ja sovellusten korvaajien rakennus ja testaus testiympäristössä | **Ei: Q1-jäädytys pitää** |
| **Huhtikuu** | Käyttöönotto sovituissa ikkunoissa, palautus mahdollinen, vanha rinnalla kuukauden | Kyllä |
| **Toukokuu** | Toinen aalto, suomenkieliset ohjeet, luovutus | Kyllä |

**Rehellinen tuntematon:** mitä raportointia uusi ERP tukee sisäisesti. Selvitämme viikolla 1, ja se ratkaisee, mitkä raportit menevät ERPiin ja mitkä BI-työkaluun.

---

# Tiimi: saatavilla sopimuksen allekirjoituksesta

| Rooli | Sertifikaatit | Kielet | Saatavuus |
|---|---|---|---|
| **Data Engineer (vetäjä), 10 v** | Azure Data Engineer Associate · Fabric Analytics Engineer | suomi, englanti | 60 %, paikalla Uudessakaupungissa 2 pv/vko, sopimuksen allekirjoituksesta |
| **Data Analyst, 7 v** | Power BI Data Analyst Associate (PL-300) | suomi, englanti | 40 %, sopimuksen allekirjoituksesta |
| **Solution Architect, 14 v** | Azure Solutions Architect Expert | suomi, englanti | osa-aikainen, sopimuksen allekirjoituksesta |

Vaihto-oikeus hyväksytty. Matkat sisältyvät hintaan.

---

# Hinta ja ehdot

| Rooli | Päivät | Päivähinta | Yhteensä |
|---|---|---|---|
| Data Engineer | 18 | 920 € | 16 560 € |
| Data Analyst | 9 | 1 000 € | 9 000 € |
| Solution Architect | 2 | 920 € | 1 840 € |
| **Kiinteä kokonaishinta, 29 henkilöpäivää** | | | **27 400 € ilman alv:tä** |

- **Ei sopimuspoikkeamia.** Hyväksymme työntekijöiden rekrytoinnin 12 kk jälkeen, vaihto-oikeuden ja hintojen pysyvyyden 9 kuukautta.
- Ei lisenssejä Recordlyltä.

> Kiinteä hinta: suunnitelman ylittävä työ on Recordlyn riski.

<!-- coverage: solution architecture(s2), project team(s5), delivery plan(s4), price(s6), concise(6 slides), Finnish deck, reporting inside ERP(s2), Q1 freeze(s4), ROI/commits(s3), honest unknown ERP capability(s4), new ERP + cloud + BI(s2) -->
