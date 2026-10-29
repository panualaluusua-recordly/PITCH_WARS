<!-- title: S Group · Data- ja tekoälypalvelujen toimittajapaneeli -->
# Toimittajapaneeli ja ensimmäinen tilaus: valmis aloittamaan heti

## Hintakortti roolin ja senioriteetin mukaan, määräalennukset ja ensimmäinen 3 kk:n tilaus kiinteään hintaan €55,200 (excl. VAT). Kaikki suomeksi. Ei sopimuspoikkeamia.

Ehdotus: Tiina Kettunen, Director of Commercial Analytics & AI · Recordly Oy · Helsinki

---

# Ehdotus yhdellä sivulla

| | |
|---|---|
| **Ensimmäinen tilaus** | 3 kk, **60 henkilöpäivää** eli noin yksi kokoaikainen konsultti: senior-datainsinööri |
| **Kaupallinen vaikutus** | Tilaus sidotaan **näkyviin kaupallisiin mittareihin**: kate tuoteryhmittäin, kassakonversio ja kampanjoiden myyntivaikutus. Ensimmäinen liiketoiminnan näkemä tulos viikolla 4, ei pelkkää taustaputkistoa. |
| **Lähestymistapa** | Rakennamme S Groupin nykyisen arkkitehtuurin päälle: Microsoft Azure, SAP S/4HANA, nykyinen dataympäristö ja BI-työkalu. **Ei uusia työkaluja, ei uusia lisenssejä.** |
| **Aloitus** | Nimetty konsultti vahvistetaan ennen allekirjoitusta ja aloittaa allekirjoituspäivänä. Ei ansioluetteloiden läpikäyntiä. |
| **Kieli** | **Työpajat, toimitettava dokumentaatio ja raportointi suomeksi.** Konsultit ovat äidinkieleltään suomenkielisiä. |
| **Konsultin siirto palkkalistoille** | Sallittu **ilman rekrytointipalkkiota 12 kk:n jälkeen** |
| **Kokonaishinta** | **€55,200 kiinteä** (60 pv × €920), excl. VAT |
| **Sopimus** | **Ei sopimuspoikkeamia.** S Groupin vakioehdot sellaisenaan. |

---

# Ratkaisu ja toteutussuunnitelma: 12 viikkoa

| Viikko | Mitä tapahtuu | Tulos |
|---|---|---|
| **0 · allekirjoitus** | S Group avaa pääsyt ja nimeää työn priorisoijan. Konsultti on valmiina. | Pääsyt auki 1. päivänä |
| **1** | Perehtyminen S Groupin Azure-, SAP S/4HANA- ja BI-käytäntöihin, koodikäytäntöihin ja nykyisiin putkistoihin | Ensimmäinen katselmoitu pull request |
| **2–4** | Ensimmäinen kaupallinen käyttötapaus kaupan johdon kanssa: **katedata tuoteryhmittäin ja kampanjoittain** S/4HANA- ja kassadatasta BI-työkaluun | **Viikko 4: kate- ja kampanjanäkymä kaupan johdon käytössä** |
| **5–11** | Toinen ja kolmas käyttötapaus S Groupin priorisoinnin mukaan, esim. **kassakonversio ja ostoskorin koko** myymälöittäin. Tarvittavat putkistot, mallit ja testit rakennetaan näiden ympärille. | Jokainen toimitus raportoi, mitä kaupallista mittaria se liikuttaa; viikkoraportti suomeksi |
| **12** | Dokumentaatio suomeksi, tulosten yhteenveto ja jatkosuositus | Päätös: jatko, uusi tilaus tai päättäminen |

> **Rajaus:** työ on S Groupin backlogia. Emme ehdota lisäkäyttötapauksia emmekä uusia alustoja. **Avoin kysymys:** backlogin tarkka sisältö ja ympäristöjen versiot selviävät viikolla 1. Jos työ vaatii toista roolia, vaihto tehdään hintakortin mukaan, ei lisämaksuin.

---

# Miten käytämme tekoälyä omassa toimituksessamme

## Virtual Data Engineer (VDE): tekoälyagenttien tiimi, jonka jokaisen muutoksen ihminen hyväksyy

| Vaihe | Mitä tapahtuu |
|---|---|
| 1 · Työ | GitHub-issue tai hälytys käynnistää data engineer -agentin |
| 2 · Muutos | Agentti tekee pull requestin ja ajaa testit |
| 3 · Katselmointi | Katselmointiagentit (SQL, dbt, yleinen) palauttavat työn korjattavaksi |
| 4 · Valvonta | Auditointiagentit tallentavat lokit ja päättelyn |
| 5 · **Hyväksyntä** | **Ihminen hyväksyy jokaisen muutoksen.** Agentti ei voi hyväksyä tai yhdistää omaa työtään. |

- **Tulokset oikeissa projekteissa:** puolimutkaisen putkiston rakennus, testaus ja validointi **12 h → 30 min**; migraatio noin 30 Snowflake-krediittiä taulua kohden
- **Rehellisesti:** VDE toimii Snowflakessa ja dbt:ssä. S Group on Azure/SAP, joten **VDE ei kuulu tähän tilaukseen eikä hintaan**, eikä sitä asenneta ympäristöönne. Tekoälyä käytetään S Groupin ympäristössä vain S Groupin hyväksymin ehdoin.

---

# Tiimi, sertifikaatit ja käyttöönotto

| Rooli | Kokemus | Sertifikaatit | Kieli |
|---|---|---|---|
| **Senior Data Engineer** (1. tilaus) | 9 v; Azure-dataputkistot, SAP S/4HANA -lähteet, BI-valmiit mallit | Microsoft Certified: Azure Data Engineer Associate | suomi (äidinkieli), englanti |
| **Lead Data Engineer / Data Architect** | 12 v; arkkitehtuuri ja katselmointi | Microsoft Certified: Azure Solutions Architect Expert | suomi (äidinkieli), englanti |
| **Senior Data Analyst** | 8 v; BI-mallit ja raportointi | Microsoft Certified: Power BI Data Analyst Associate | suomi (äidinkieli), englanti |
| **Senior AI/ML Engineer** | 8 v; tuotantoon vietävät mallit | Microsoft Certified: Azure AI Engineer Associate | suomi (äidinkieli), englanti |

- **Käyttöönotto:** ensimmäinen tilaus alkaa allekirjoituspäivänä; muiden roolien nimetty konsultti 10 työpäivän kuluessa tilauksesta
- Jokainen konsultti on Recordlyn työntekijä. Ei alihankkijoita.

---

# Korvaamiskäytäntö ja siirto S Groupin palkkalistoille

:::cols
### Konsultin korvaaminen
- S Group voi vaatia konsultin vaihtoa **milloin tahansa, ilman perustelua**
- Korvaaja on vähintään yhtä senior ja esitellään **5 työpäivän** kuluessa
- Perehdytysjakso (enintään 3 pv) **Recordlyn kustannuksella**
- Sairastuminen tai poissaolo yli 5 pv: korvaaja samalla käytännöllä, poissaoloajalta ei laskuteta
:::col
### Poikkeava konsultti S Groupin omaksi
- S Group saa palkata Recordlyn konsultin **ilman rekrytointipalkkiota 12 kk:n jälkeen**
- Ennen sitä siirto sovitaan yhdessä; **ei prosenttipalkkioita eikä "lunnaita"**, vain sovittu siirtymäjakso
- Kaikki dokumentaatio ja koodi ovat S Groupin omistuksessa jo työn aikana, joten siirto ei katkaise mitään
:::

---

# Hintakortti, määräalennukset ja ensimmäisen tilauksen kokonaishinta

| Rooli (€/pv, 8 h, excl. VAT) | Taso 1: 0–119 pv | Taso 2: 120–299 pv | Taso 3: 300+ pv |
|---|---|---|---|
| Senior Data Engineer (6+ v) | **920** | 920 | 920 |
| Lead Data Engineer (10+ v) | **1,000** | 950 | 920 |
| Data Architect (12+ v) | **1,100** | 1,045 | 1,012 |
| Senior AI/ML Engineer (6+ v) | **960** | 960 | 960 |
| Senior Data Analyst (6+ v) | **1,000** | 1,000 | 1,000 |
| Lead Data Analyst (10+ v) | **1,100** | 1,045 | 1,012 |

Tasot lasketaan kaikista S Groupin tilauksista kertyvistä päivistä. Senior-hinnat ovat jo alin paneelihinta; niillä tason 2 ja 3 etuna on **1 ja 2 maksutonta suomenkielistä työpajapäivää vuosineljännestä kohden**.

**Ensimmäinen tilaus: 60 pv × €920 = €55,200 kiinteä, excl. VAT.** Laskutus 3 × €18,400 kuukausittain S Groupin maksuehdoin. Matkat ja Helsingin työpäivät sisältyvät. Hinnat voimassa 12 kk, sen jälkeen vain yhdessä sovittu tarkistus. **Ei sopimuspoikkeamia.**

<!--
coverage:
RFP "solution and implementation plan" -> slides 2-3 (12-week plan, scope fence, open unknown)
"leverages AI internally to enhance delivery efficiency" -> slide 4 (VDE, honest Snowflake+dbt limit, not priced, human approval, real results from vde-facts)
"team capabilities, certifications" -> slide 5 (roles, years, Microsoft certs, languages)
"ramp-up timelines" -> slides 2,3,5 (signature day; week 1 first PR; other roles 10 working days)
"consultant replacement policy" -> slide 6 (any time, 5 days, overlap at our cost)
"rate cards by role and seniority" -> slide 7 (6 rows; all >= team minimums 920/960/1000)
"volume discount tiers" -> slide 7 (3 tiers; floor-respecting; free workshop days at min-rate rows)
"total pricing for initial call-off" -> slides 1,2,7: EUR 55,200 = 60 x 920
"contract deviations" -> "Ei sopimuspoikkeamia" slides 1,2,7
Hint fix 1 (language) -> whole deck Finnish; Finnish workshops/docs/reporting; native Finnish speakers
Hint fix 2 (conversion to payroll without ransom) -> slides 2, 6: fee-free after 12 months, no percentage fees before, code/docs owned by S Group
Praised kept: ready to plug in immediately (slide 2, 3), accept their architecture, no new tools (slides 2,3,4)
Bio: self-governing teams, cuts fluff -> concise, concrete; consultant works as member of their team, S Group prioritises
-->
