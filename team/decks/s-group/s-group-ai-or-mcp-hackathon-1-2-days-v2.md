<!-- title: S Group · AI- ja MCP-hackathon -->
# Kaksi päivää, toimivat MCP-prototyypit teidän Azure-ympäristössänne

## Rakennamme sovitun suunnitteluvaiheen päälle, emme uudelleen sen ohi. Kiinteä kokonaishinta €9,400 (excl. VAT). Ei sopimuspoikkeamia.

| | |
|---|---|
| **Lähtökohta** | Toinen toimittaja on tehnyt suunnitteluvaiheen. Sen tuotokset ja käyttötapaukset ovat **sitovia**, joten emme kartoita tai määrittele mitään uudelleen |
| **Tavoite** | Kaupallisen analytiikan tiimin rakentamat agenttiprototyypit, jotka lukevat S Groupin dataa MCP-palvelimien kautta ja toimivat **Azuressa ja S/4HANA-datan päällä** |
| **Meidän linjamme** | Vain lukuoikeus. Agentti ehdottaa, **ihminen hyväksyy**. Ei autonomista kirjoitusta SAP:iin |
| **Teidän aikanne** | 60 minuutin aloituskeskustelu ja 45 minuutin loppukatselmus. Ei viikoittaisia statuspalavereita |

Ehdotus: Tiina Kettunen, Director of Commercial Analytics & AI · Recordly Oy · Helsinki

---

# Tekninen ratkaisu: MCP-palvelimet S Groupin omassa Azuressa

## Agentti kysyy MCP:n kautta, MCP-palvelin lukee hallittua dataa, ihminen päättää.

<div style="display:flex;align-items:stretch;gap:12px;margin:0.2em 0 0.5em 0;font-size:0.68em;line-height:1.25"><div style="flex:1;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:14px"><b style="color:#E3FF87">1 · KÄYTTÄJÄ</b><br>Kaupallisen analytiikan tiimin jäsen kysyy chat-työkalussa</div><div style="align-self:center;color:#E3FF87;font-size:2em">&rarr;</div><div style="flex:1;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:14px"><b style="color:#E3FF87">2 · AGENTTI</b><br>Azuressa, malli-endpoint jonka S Group on jo hyväksynyt. Epäselvässä kysyy, ei arvaa</div><div style="align-self:center;color:#E3FF87;font-size:2em">&rarr;</div><div style="flex:1;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:14px"><b style="color:#E3FF87">3 · MCP-PALVELIN</b><br>Paljastaa vain sovitut, lukuoikeudella olevat näkymät nykyisestä dataympäristöstä ja S/4HANA-datasta</div><div style="align-self:center;color:#E3FF87;font-size:2em">&rarr;</div><div style="flex:1;background:#E3FF87;color:#1B1B1B;border-radius:10px;padding:14px"><b>4 · TEIDÄN IHMISENNE</b><br>Hyväksyy ehdotuksen. <b>Mitään ei kirjoiteta takaisin</b></div></div>

:::cols
- **Ei uutta alustaa, ei lisenssejä.** Kaikki S Groupin Azure-tilauksessa. Mallikäyttö teidän kustannuksellanne, tiimikohtainen katto sovitaan valmistelussa
- **Tuotannon ajokustannus jokaiselle prototyypille erikseen:** mittaamme tapahtuman aikana jokaisen kaupallisen käyttötapauksen todellisen kulutuksen (tokenit, Azure-laskenta, kutsut per tiketti tai kysely) ja annamme **prototyyppikohtaisen arvion kuukausikustannuksesta tuotannossa** kolmella volyymitasolla. Go/no-go-muistiossa näkyy jokaisesta tapauksesta hyöty ja ajokustannus rinnakkain, jotta skaalaatte vain sen, minkä voitte mitata
- **Omistus:** koodi, MCP-palvelimet ja kehotteet ovat S Groupin. Emme tuo omaa mallia tai tuotetta, johon jäisitte kiinni
:::col
- **Lokit:** jokainen ajo tallentuu (kysely, työkalukutsut, vastaus, hyväksyjä). Arkaluonteiset kentät maskataan ennen mallia
- **Rajaus:** ei ML-mallien koulutusta, ei tuotantobottia, ei lisäkäyttötapauksia. Valmis Virtual Data Engineer -tuotteemme toimii Snowflakessa, joten sitä ei käytetä eikä se kuulu hintaan
:::

---

# Sitova suunnitteluvaihe: mitä se tarkoittaa meille

## Käyttötapaukset otetaan sellaisinaan. Emme ehdota omia, emme kartoita arkkitehtuuria uudelleen.

| Sitova lähtötieto | Mitä teemme | Mitä emme tee |
|---|---|---|
| **Edellisen toimittajan käyttötapausmäärittelyt** | Rakennamme prototyypit **juuri niistä**. Jokainen prototyyppi viittaa määrittelyn kohtaan | Emme lisää, vaihda tai laajenna käyttötapauksia |
| **Arkkitehtuurikuvaukset** | Arkkitehti lukee ne ennen kisaa ja käyttää niitä rakennuspohjana | Ei uutta kartoitusta, ei "detektiivityötä" |
| **Ristiriita tai aukko määrittelyssä** | Kysymme yhden listan valmistelussa ja kirjaamme vastauksen | Emme tulkitse hiljaa omalla tavallamme |

**Rehelliset rajat, kerrotaan etukäteen:**

- **Liite ei näy meille kokonaan ennen tarjouksen jättöä.** Jos jokin sidottu käyttötapaus vaatii kirjoitusoikeuden SAP:iin tai tuotantodataa, teemme siitä lukuoikeudella toimivan version ja sanomme rajauksen ääneen
- **Kaupallinen vaikutus mitataan, ei luvata.** Jokaisen prototyypin hyöty (kate, kampanjat tai kassakonversio, sen mukaan mitä määrittely koskee) arvioidaan S Groupin omalla datalla. Emme anna keksittyjä prosenttilukuja
- **Kehittäjien aikaa säästetään:** valmisteluvaiheessa vain aloituskeskustelu ja datanäkymän vahvistus (yhteensä noin 2 tuntia), kisapäivinä vain osallistujat

---

# Toteutussuunnitelma: toimiva agentti ennen ensimmäistä tuntia

| Vaihe | Mitä | Tulos |
|---|---|---|
| **Valmistelu, 2 viikkoa** | Aloitus sopimuspäivänä. Sitovien tuotosten läpikäynti, 60 min keskustelu, lukuoikeus yhteen datanäkymään, siemenagentti valmiiksi | **Live-demo kisan päivän 1 ensimmäisellä tunnilla** |
| **Hackathon, 2 päivää Helsingissä** | Päivä 1 rakennus, päivä 2 reunatapausten testaus ja demot. Kaksi fasilitaattoria paikan päällä molempina päivinä. Kieli: suomi | Prototyypit sidotuista käyttötapauksista |
| **Jatko, viikko kisan jälkeen** | Koodin siivous teidän repoonne, reunatapausrekisteri, 45 min katselmus | Go/no-go jokaiselle prototyypille |

> **Auki valmisteluun, päätetään yhdessä:** (1) liitteen käyttötapausten lukumäärä ja laajuus, (2) datayhteys sovitaan ennen kisaa, muuten käytetään maskattua otetta ja sanomme sen heti, (3) osallistujamäärä ja taso (oletus 8–12 henkeä).

**Toimitukset:** D1 siemenagentti · D2 prototyypit teidän repossanne · D3 reunatapausrekisteri · D4 go/no-go-muistio. Dokumentaatio ja työpaja suomeksi.

---

# Tiimi: kolme senioria, suomenkielinen, päivät sovitaan allekirjoituksessa

| Rooli | Kokemus ja sertifikaatit | Päiviä |
|---|---|---|
| **Senior AI-insinööri** (vetäjä ja fasilitaattori) | 9 v, agenttiratkaisut Azuressa. Azure AI Engineer Associate · Azure Data Scientist Associate. Suomi, englanti | 5 |
| **Senior data-insinööri** (SAP S/4HANA, fasilitaattori) | 10 v, S/4HANA-data Azureen. Azure Data Engineer Associate. Suomi, englanti | 4 |
| **Data-arkkitehti** (arkkitehtuurikuvausten hyödyntäminen, katselmointi) | 12 v, SAP- ja Azure-analytiikka. Azure Solutions Architect Expert. Suomi, englanti | 1 |

Korvaaja on aina vähintään yhtä senior ja sovitaan S Groupin kanssa ensin. S Group voi palkata kisaan osallistuneen konsultin 12 kuukauden jälkeen **ilman välitys- tai siirtomaksuja**.

---

# Hinta ja ehdot

## Kiinteä kokonaishinta €9,400 (excl. VAT)

| Rooli | Päivää | Päivähinta | Summa |
|---|---|---|---|
| Senior AI-insinööri | 5 | €960 | €4,800 |
| Senior data-insinööri | 4 | €920 | €3,680 |
| Data-arkkitehti | 1 | €920 | €920 |
| **Yhteensä** | **10** (valmistelu 4, kisa 4, jatko 2) | | **€9,400** |

- **Kiinteä hinta:** ylitykset ovat Recordlyn riski. Matkat ja paikan päällä olo Helsingissä sisältyvät
- **Ei lisenssejä.** Mallikäyttö S Groupin omassa Azure-tilauksessa
- **S Groupin vakiosopimus: ei poikkeamia.** Laskutus S Groupin ehtojen mukaan katselmoinnin hyväksynnän jälkeen. Koodi ja tulokset ovat S Groupin

<!-- coverage:
RFP: delivery solution -> slide 2; operational event plan -> slide 4; nominated delivery team -> slide 5; complete pricing model -> slide 6; presentation -> all.
Hard constraint: prior vendor design deliverables and use case definitions strictly binding -> slide 1 (Lahtokohta), slide 3 (table, no new use cases, ask list for conflicts); attachment not visible to us -> honest unknown slide 3 + 4.
Persona (Tiina): day-one start -> slide 4 (agreed at signature, live demo day 1 hour 1); Finnish -> whole deck, workshop and docs in Finnish; Azure + S/4HANA only, no new platform -> slide 2; honest no-fairy-tale claims -> slide 3; commercial impact margin/campaigns/checkout, measured -> slide 3; reuse existing blueprints no re-mapping -> slide 3; minimal developer time -> slide 1, 3; lean price -> slide 6; no invisible plumbing -> prototypes tied to commercial metric; hiring after 12 months free -> slide 5. Customer-service AI model ownership (earlier 'not addressed') -> slide 2 ownership line.
Kemira structure reused: seed agent hour 1, read-only, person approves, no autonomous write-back, edge-case honesty (slide 3 limits; edge-case register D3).
VDE: one line slide 2, not priced. Slides: 6.
Price: 5 x 960 + 4 x 920 + 1 x 920 = 4,800 + 3,680 + 920 = 9,400; 10 days; avg EUR 940/day. Days: prep AI2 DE1 Arch1; hackathon AI2 DE2; follow-up AI1 DE1.
-->
