<!-- title: Oulun Energia · Dokumentti- ja ohjeavustaja -->
# Organisaatiolaajuinen RAG-avustaja ohjeille ja turvallisuusprotokollille

## Nopeat, lähteistetyt vastaukset suomeksi omassa pilvessänne ja chat-työkalussanne. Kulut hallinnassa, Q1-jäädytystä kunnioittaen.

Tarjous Tiina Vartiaiselle, Development Manager for Data and Analytics · Recordly Oy · Helsinki

---

# Tekninen ratkaisu: avustaja rakennetaan teidän pilveenne

## Kaikki osat ajetaan teidän tenantissanne ja kytketään teidän chat-työkaluunne. Palvelunimet sovitaan vaiheessa 0, kun pilvi, chat-työkalu ja nykyinen dataympäristö on nimetty.

| Vaihe | Mitä tapahtuu | Suoja |
|---|---|---|
| **1. Lähteet** | Ohjeet, turvallisuusprotokollat ja toimintadokumentit nykyisestä dataympäristöstänne | Dokumenttivarasto: lähde, omistaja, versio, päiväys |
| **2. Poiminta ja pilkonta** | Teksti ja rakenne irti, jaetaan kappaleisiin | **Muutostunnistus** (tiiviste tai muokkauspäivä): vain muuttunut sisältö käsitellään uudelleen |
| **3. Indeksi** | Vektori- ja avainsanahaku, suomen taivutus ja yhdyssanat huomioiden | Korvatut versiot suljetaan pois |
| **4. Haku** | Haku rajataan käyttäjän lähdeoikeuksien mukaan | Oikeudet periytyvät lähteestä; testataan ennen käyttöönottoa |
| **5. Vastaus** | Vastaus vain löydetyistä kohdista, **lähdeviite, dokumentin versio ja päiväys** | Heikko näyttö: ei arvausta, ohjaus dokumentin omistajalle |
| **6. Chat-työkalu** | Kysyminen suomeksi siinä työkalussa, jota väki jo käyttää | Virheellisen vastauksen ilmoituspainike |

**Ei lisäominaisuuksia:** ei agentteja, ei automaattisia toimia, ei ennusteita. Avustaja vastaa ja viittaa; se ei anna eikä muuta toimintaohjeita.

---

# Kulut hallintaan: vektoripäivitys ei enää yllätä laskulla

## Ajastettu täysi uudelleenindeksointi on tyypillinen laskun syy. Korvaamme sen rajatulla, mitatulla päivityksellä.

| Kustannusvipu | Hallinta |
|---|---|
| **Vektoripäivitys** | Inkrementaalinen, muutostunnistuksella; ei kokonaan uudelleen upotettavia ajoja |
| **Ajon katto** | Ajokohtainen ja kuukausikohtainen budjetti; ajastus ja enimmäismäärä sovitaan teidän kanssanne |
| **Hälytys ja pysäytys** | Budjettihälytys kynnyksillä, **kova pysäytys** ylityksessä, kill switch päivitysajolle |
| **Upotuskutsut ja indeksin koko** | Uudelleenupotus vain muuttuneille kappaleille; vanhat versiot poistetaan indeksistä |
| **Mallin tokenit per kysymys** | Kappalemäärän raja per vastaus; kustannus per kysymys mitataan |
| **Näkyvyys** | Kustannus per ajo ja per kuukausi raportoidaan BI-työkalussanne |

Aiemman pilotin asetukset ja laskupiikin laukaisija käydään läpi vaiheessa 0: uudelleen käytetään vain se, mikä oli turvallista.

---

# Suomen kielen laatu mitataan, ei luvata

## "Täysi tuki suomen kielen vivahteille" osoitetaan teidän omilla dokumenteillanne ja teidän väkenne kysymyksillä.

:::cols
### Suomenkielinen arviointijoukko
- Kysymykset **teidän dokumenteistanne**: taivutusmuodot, yhdyssanat, alan sanasto
- Kirjoitettu niin kuin kunnossapitotyöntekijät ja laitosvalvojat kysyvät
- Vastausten arvioijina **dokumenttien omistajat** teiltä
- Upotus- ja vastausmallit valitaan **mittaamalla suomella**, ei oletuksella
- Malli on vaihdettavissa abstraktiokerroksen takaa
:::col
### Mittari ja portti
- **Lähtötaso mitataan ensin:** haun osuvuus, vastauksen oikeellisuus, viitteen oikeellisuus, kieltäytyminen heikolla näytöllä
- **Hyväksymisraja sovitaan lähtötason jälkeen** yhdessä teidän kanssanne, ei etukäteen arvaten
- Ajetaan uudelleen ennen jokaista aaltoa sekä jokaisen päivityksen ja mallimuutoksen jälkeen
- Pilotin virhetaso raportoidaan avoimesti: emme lupaa "nolla virhettä"
:::

---

# Pilotti ensin, sitten aallot: aikataulu ja Q1-jäädytys

## Rakennus ja testaus ei-tuotannossa ennen Q1:tä. Tuotantoon ei kosketa jäädytyksen aikana.

| Vaihe | Sisältö | Portti |
|---|---|---|
| **0 · Lähde- ja suomi-koe** | Dokumenttien inventaario ja laatunäyte (skannaukset, kaksoiskappaleet, vanhentuneet versiot); ensimmäinen suomen mittaus | **Go/no-go:** mitä indeksoidaan |
| **1 · Pilottiviipale** | Muutama dokumenttikokoelma ja muutama käyttäjäryhmä; oikeudet, viitteet ja kustannusvalvonta käytössä | Arviointiportti ja kustannus suunnitelmassa |
| **2 · Aallot** | Kokoelmat ja käyttäjäryhmät laajenevat aalloittain kohti koko 260 hengen organisaatiota | Portti ennen jokaista aaltoa |
| **Q1-jäädytys** | **Tuotantomuutoksia ei tehdä.** Kehitys ja testaus ei-tuotannossa jatkuvat; käyttöönotto-ikkunat ennen jäädytystä ja sen päätyttyä | Jäädytyksen laajuus ja päivät vahvistetaan vaiheessa 0 |

Jos jäädytys kattaa myös uuden botin chat-työkalussa, se ajoitetaan ikkunaan ennen jäädytystä tai sen jälkeen. Jäädytyksen aikana vain luku -käyttö tai ei-tuotantopilotti vain, jos sääntönne sallivat.

---

# Mitä emme vielä tiedä, ja miten ratkaisemme sen

| Tuntematon | Miksi sillä on väliä | Ratkaisu |
|---|---|---|
| Mikä pilvi, mitkä alueet sallittu | Palveluvalinnat ja käsittelysijainti | Vaihe 0, ensimmäinen viikko |
| Chat-työkalu: sallitaanko omat botit, kuka hyväksyy | Käyttöliittymän toteutus ja aikataulu | Vaihe 0 |
| Dokumenttien sijainti, muoto, määrä ja kieli | Indeksoinnin työmäärä, skannausten tekstintunnistus | Inventaario ja laatunäyte |
| Lähdeoikeudet ja tunnistautuminen | Käyttäjäryhmäsuodatus haussa | Oikeuskartoitus; jos oikeuksia ei voi lukea, pilotti yhdellä kaikille avoimella kokoelmalla |
| Q1-jäädytyksen laajuus ja päivät | Käyttöönotto-ikkunat | Vahvistus teiltä vaiheessa 0 |
| Aiemman pilotin rakenne ja laskupiikki | Uudelleenkäyttö vai korvaus | Läpikäynti yhdessä |
| Kuka ylläpitää dokumentit ja palvelun käyttöönoton jälkeen | Vastausten tuoreus; hälytysten omistus | Nimetty omistaja per kokoelma; ylläpitäjä sovitaan |
| Kyselylokien säilytys, henkilötiedot kysymyksissä | Auditointi ja tietosuoja | Linjataan vaiheessa 0 |

**Rehellinen rajaus:** emme sitoudu kattamaan lähteitä, joiden laatua emme ole nähneet. Vaiheen 0 portti päättää.

---

# Toimitettavat ja mitä tarvitsemme teiltä

:::cols
### Toimitettavat
- **D1 · Vaihe 0:** lähde- ja laatuinventaario, suomen lähtötaso, go/no-go
- **D2:** RAG-avustaja pilottiviipaleelle teidän pilvessänne ja chat-työkalussanne, lähdeviitteineen
- **D3:** suomenkielinen arviointijoukko ja ajettava mittaus
- **D4:** kustannusvalvonta: budjetit, hälytykset, kova pysäytys, raportti BI-työkalussanne
- **D5:** aaltokohtainen käyttöönotto Q1-jäädytys huomioiden
- **D6:** suomenkieliset käyttö- ja ylläpito-ohjeet sekä koulutus kunnossapitoväelle ja laitosvalvojille
- **D7:** koodi ja infrastruktuuri teidän repoissanne ja tenantissanne
:::col
### Tarvitsemme teiltä
- Pilven, chat-työkalun ja BI-työkalun tiedot sekä pääsy ei-tuotantoympäristöön
- Lukuoikeus pilottikokoelmiin ja tieto lähteiden oikeusmallista
- **Dokumenttien omistajat arvioijiksi:** rajattu, ennalta sovittu aika; ei jatkuvaa parityötä
- Q1-jäädytyksen laajuus ja päivät
- Tieto aiemmasta pilotista ja laskupiikistä
- Nimetty vastuuhenkilö palvelulle käyttöönoton jälkeen
:::

---

<!-- statement -->
# Mittaa ensin. Pilotoi pienesti. Älä koske tuotantoon talven huipulla.

## Suomenkielinen, lähteistetty avustaja omassa pilvessänne, kulut hallinnassa

Recordly Oy · Helsinki
