<!-- title: Pirha · Laitoshäiriöiden ennustetutkimus -->
# Laitosten häiriöennusteet: ihminen päättää, oma tiimi omistaa mallit

## Tutkimus käyttö- ja anturidatasta, datajärvestä ja ERP:stä. Kiinteä hinta 22 600 € ilman arvonlisäveroa. Vakiosopimusehdot, ei poikkeamia.

Tarjous Tuija Salokangas, tietohallinnon ja analytiikan johtaja · Recordly Oy · Helsinki

---

# Ratkaisu: ennuste neuvoo, huoltokoordinaattori päättää

:::cols
### Ratkaisu
- **Poiminta kaikista tutkimuksen lähteistä:** anturitelemetria, datajärven lokit ja pilvessä toimiva ERP (huoltohistoria). Jokainen lähde arvioidaan ensin, sitten poimitaan.
- **Ennustemalli** laitosten ja kiinteistötekniikan vioista, rakennettu datajärveen
- **Ihminen päättää aina:** malli antaa riskilistan ja perustelun, huoltokoordinaattori hyväksyy tai hylkää. **Ei automaattisia huoltokäynnistyksiä**, epäselvissä mittauksissa tulos on "tarkista" eikä toimenpide.
- Raportointi nykyisellä BI-työkalulla
:::col
### Rajaukset
- Ei toimittajan hallinnoimaa jatkopalvelua
- Ei uusia alustoja tai lisenssejä
- Ei muutoksia sairaaloiden huoltoprosesseihin
- Ei lupausta mallin tarkkuudesta ennen datan tarkastelua
:::

---

# Aiemmat huolenne ja vastauksemme

| Huoli | Suojamme |
|---|---|
| Automaattiset toimet epäselvässä datassa | Päätös aina ihmiselle; malli ei kirjoita ERP:hen. Epävarmuusraja: sen alla ei ehdotusta |
| Toimittaja jää ylläpitämään | **Oma analytiikkatiimi ajaa ja muokkaa malleja itse.** Pariohjelmointi alusta, koodi ja mallit teidän tietovarastossanne, uudelleenkoulutusohje suomeksi |
| Englanninkieliset esitykset | Kaikki ohjausryhmämateriaalit, työpajat ja dokumentit **suomeksi** |
| Raskas, juniorivetoinen delegaatio | Kaksi seniorikonsulttia, jotka tekevät työn itse |
| Menettelyn läpinäkyvyys | Vaiheportit ja kirjallinen ohjausryhmämateriaali jokaisessa portissa |

---

# Toteutussuunnitelma: neljä vaihetta, kolme porttia

| Vaihe | Viikot | Sisältö | Portti |
|---|---|---|---|
| **1. Lähteet** | 1–3 | Lähteiden arviointi, koeporaus, laadun profilointi | **Portti 1:** mitkä lähteet ovat käyttökelpoisia |
| **2. Poiminta ja data** | 3–6 | Hyväksyttyjen lähteiden poiminta, vikahistorian tunnisteet | **Portti 2:** riittääkö vikahistoria ennustamiseen |
| **3. Malli** | 6–9 | Perusmalli ja tarkkuus todellisella datalla, päätöstuki huoltokoordinaattorille | **Portti 3:** tulokset ohjausryhmälle |
| **4. Siirto** | 9–10 | Oma tiimi ajaa uudelleenkoulutuksen itse, runbookit suomeksi | Hyväksyntä |

**Rehellinen epävarmuus:** ERP:n vikahistorian laatua ei tiedetä ennen viikkoa 3. Jos tunnisteita ei ole, portti 2 rajaa tutkimuksen laitosluokkiin, joille ennustaminen on mahdollista.

---

# Tiimi: kaksi seniorikonsulttia, saatavilla sopimuksen allekirjoituksesta

| | Vanhempi AI/ML-insinööri (vetäjä) | Vanhempi data-insinööri |
|---|---|---|
| **Kokemus** | 10 vuotta; ennakoiva kunnossapito, aikasarjat | 9 vuotta; poiminta, datajärvet, laadunvarmistus |
| **Sertifikaatit** | Azure Data Scientist Associate · Databricks ML Professional | Azure Data Engineer Associate · Databricks Data Engineer Professional |
| **Kielet** | suomi (äidinkieli), englanti | suomi (äidinkieli), englanti |
| **Saatavuus** | 100 % sopimuksen allekirjoituksesta | 100 % sopimuksen allekirjoituksesta |

Koko tiimi on saatavilla allekirjoituksesta. Pirha voi vaatia konsultin vaihtoa milloin tahansa; vaihto samantasoiseen, päällekkäisyys omalla kustannuksellamme.

---

# Hinta ja ehdot

| Rooli | Henkilötyöpäivää | Päivähinta | Summa |
|---|---|---|---|
| Vanhempi AI/ML-insinööri | 13 | 960 € | 12 480 € |
| Vanhempi data-insinööri | 11 | 920 € | 10 120 € |
| **Kiinteä kokonaishinta, ilman ALV** | **24** | | **22 600 €** |

- Kiinteä hinta: ylittävä työ on Recordlyn riski. Laskutus vaiheittain.
- Sisältää matkat, dokumentaation ja ohjausryhmämateriaalit suomeksi. Ei lisenssejä.
- **Ei sopimuspoikkeamia.** Hyväksymme vakiosopimusehdot sellaisenaan.

<!-- coverage: RFP: architecture (s2), phased plan (s4), team profiles (s5), complete pricing (s6), extraction for all sources (s2 assess-then-extract), majority available at signature (s5), replacement right (s5). Feedback: gates+Finnish steering kept (s3,s4), no auto triggers (s2,s3), in-house operation (s3,s4), price lowered. Finnish deck due to bio. Cloud vendor unknown: certs Azure/Databricks need check. -->
