<!-- title: Oulun Energia · Dokumentti- ja ohjeavustaja -->
# Organisaatiolaajuinen RAG-avustaja ohjeille ja turvallisuusprotokollille

## Nopeat, lähteistetyt vastaukset suomeksi teidän pilvessänne ja chat-työkalussanne, jos se sallii omat botit. Kulut hallinnassa, Q1-jäädytystä kunnioittaen.

Tarjous Tiina Vartiaiselle, Development Manager for Data and Analytics · Recordly Oy · Helsinki

---
# Tekninen ratkaisu: avustaja rakennetaan teidän pilveenne

## Kaikki osat ajetaan teidän tenantissanne tai sen sallimalla alueella; mallikäyttö vahvistetaan vaiheessa 0. Palvelunimet sovitaan, kun pilvi, chat-työkalu ja dataympäristö on nimetty.

<div style="font-size:0.5em;line-height:1.2"><div style="background:#2A2A2A;border:2px dashed #E3FF87;border-radius:10px;padding:6px 12px;margin-bottom:8px"><b style="color:#E3FF87">ARVIOINTISILMUKKA:</b> suomenkielinen arviointijoukko ajetaan ennen jokaista aaltoa ja jokaisen päivityksen tai mallimuutoksen jälkeen. Dokumenttien omistajat arvioivat.</div><div style="display:flex;align-items:stretch;gap:8px"><div style="flex:1;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:10px"><b style="color:#E3FF87">1 · LÄHTEET</b><div style="margin-top:6px">Ohjeet, turvallisuusprotokollat, toimintadokumentit. Lähde, omistaja, versio, päiväys</div></div><div style="align-self:center;color:#E3FF87;font-size:1.6em">&rarr;</div><div style="flex:1;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:10px"><b style="color:#E3FF87">2 · POIMINTA JA PILKONTA</b><div style="margin-top:6px">Teksti irti, kappaleiksi. <b>Muutostunnistus:</b> vain muuttunut käsitellään uudelleen</div></div><div style="align-self:center;color:#E3FF87;font-size:1.6em">&rarr;</div><div style="flex:1;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:10px"><b style="color:#E3FF87">3 · INDEKSI</b><div style="margin-top:6px">Vektori- ja avainsanahaku, suomen taivutus ja yhdyssanat. Korvatut versiot pois</div></div><div style="align-self:center;color:#E3FF87;font-size:1.6em">&rarr;</div><div style="flex:1;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:10px"><b style="color:#E3FF87">4 · HAKU</b><div style="margin-top:6px">Rajataan käyttäjän lähdeoikeuksien mukaan. Testataan ennen käyttöönottoa</div></div><div style="align-self:center;color:#E3FF87;font-size:1.6em">&rarr;</div><div style="flex:1;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:10px"><b style="color:#E3FF87">5 · VASTAUS</b><div style="margin-top:6px">Vain löydetyistä kohdista: <b>lähde, versio, päiväys</b>. Heikko näyttö: ei arvausta, ohjaus omistajalle</div></div><div style="align-self:center;color:#E3FF87;font-size:1.6em">&rarr;</div><div style="flex:1;background:#E3FF87;color:#1B1B1B;border-radius:10px;padding:10px"><b>6 · CHAT-TYÖKALU</b><div style="margin-top:6px">Kysyminen suomeksi. Virheilmoituspainike. Jos omat botit eivät onnistu: vaihtoehtoinen pääsy sovitaan vaiheessa 0</div></div></div><div style="background:#2A2A2A;border:2px dashed #E3FF87;border-radius:10px;padding:6px 12px;margin-top:8px"><b style="color:#E3FF87">KUSTANNUSVALVONTA:</b> ajon ja kuukauden budjetti, hälytys, kova pysäytys ja kill switch päivitysajolle (seuraava sivu)</div></div>

**Ei lisäominaisuuksia:** ei agentteja, ei automaattisia toimia, ei ennusteita. Avustaja vastaa ja viittaa; se ei anna eikä muuta toimintaohjeita.

---

# Kulut hallintaan: vektoripäivitys ei enää yllätä laskulla

## Ajastettu täysi uudelleenindeksointi on tyypillinen laskun syy. Korvaamme sen rajatulla, mitatulla päivityksellä.

| Kustannusvipu | Hallinta |
|---|---|
| **Vektoripäivitys** | Inkrementaalinen, muutostunnistuksella; ei kokonaan uudelleen upotettavia ajoja |
| **Ajon katto** | Ajokohtainen ja kuukausikohtainen budjetti; ajastus ja enimmäismäärä sovitaan teidän kanssanne |
| **Hälytys ja pysäytys** | Budjettihälytys kynnyksillä, **kova pysäytys** ylityksessä, kill switch päivitysajolle. **Kova pysäytys pysäyttää vain päivitysajon; kysymyksiin vastaaminen jatkuu.** |
| **Upotuskutsut ja indeksin koko** | Uudelleenupotus vain muuttuneille kappaleille; vanhat versiot poistetaan indeksistä |
| **Mallin tokenit per kysymys** | Kappalemäärän raja per vastaus; kustannus per kysymys mitataan |
| **Näkyvyys** | Kustannus per ajo ja per kuukausi raportoidaan BI-työkalussanne, jos se soveltuu; muuten pilven kustannusnäkymässä |

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
- Ruotsin- ja englanninkielisen sisällön laajuus ja mittaus sovitaan vaiheessa 0
:::col
### Mittari ja portti
- **Lähtötaso mitataan ensin:** haun osuvuus, vastauksen oikeellisuus, viitteen oikeellisuus, kieltäytyminen heikolla näytöllä
- **Hyväksymisraja sovitaan lähtötason jälkeen** yhdessä teidän kanssanne, ei etukäteen arvaten
- Ajetaan uudelleen ennen jokaista aaltoa sekä jokaisen päivityksen ja mallimuutoksen jälkeen
- **Vastausaika (mediaani ja p95)** mitataan pilotissa chat-työkalussa; tavoite sovitaan lähtötason jälkeen
- Pilotin virhetaso raportoidaan avoimesti: emme lupaa "nolla virhettä"
:::

---
# Pilotti ensin, sitten aallot: aikataulu ja Q1-jäädytys

## Rakennus ja testaus ei-tuotannossa ennen Q1:tä, noin 8 viikon rakennusikkuna. Tuotantoon ei kosketa jäädytyksen aikana.

<div style="font-size:0.5em;line-height:1.2;margin:0.2em 0 0.5em 0"><div style="display:flex;gap:6px"><div style="flex:2;background:#2A2A2A;border:2px solid #434343;border-radius:8px;padding:8px 10px"><b>Vko 1-2 · Vaihe 0</b><br>Inventaario, laatunäyte, suomen lähtötaso, Go/no-go</div><div style="flex:4;background:#2A2A2A;border:2px solid #434343;border-radius:8px;padding:8px 10px"><b>Vko 3-8 · Pilottiviipale ei-tuotannossa</b><br>Oikeudet, viitteet, kustannusvalvonta, arviointi; testaus ennen Q1:tä</div><div style="flex:1.4;background:#2A2A2A;border:2px solid #E3FF87;border-radius:8px;padding:8px 10px"><b>Tuotantoikkuna</b><br>vain jos Go/no-go täyttyy</div><div style="flex:3;background:repeating-linear-gradient(45deg,#3a3a3a,#3a3a3a 10px,#2A2A2A 10px,#2A2A2A 20px);border:2px dashed #E3FF87;color:#E3FF87;border-radius:8px;padding:8px 10px"><b>Q1-jäädytys: ei tuotantomuutoksia</b><br>Kehitys ja testaus ei-tuotannossa jatkuvat</div><div style="flex:2.4;background:#2A2A2A;border:2px solid #434343;border-radius:8px;padding:8px 10px"><b>Jäädytyksen jälkeen</b><br>Tuotantopilotti ja aallot</div></div></div>
| Vaihe | Sisältö | Portti |
|---|---|---|
| **0 · Lähde- ja suomi-koe** (vko 1-2) | Dokumenttien inventaario ja laatunäyte; ensimmäinen suomen mittaus | **Go/no-go:** mitä indeksoidaan |
| **1 · Pilottiviipale** (ei-tuotannossa ennen Q1:tä) | Muutama kokoelma ja käyttäjäryhmä; oikeudet, viitteet, kustannusvalvonta | Arviointiportti ja kustannus suunnitelmassa |
| **2 · Aallot** | Kokoelmat ja käyttäjäryhmät laajenevat aalloittain kohti 260 hengen organisaatiota | Portti ennen jokaista aaltoa |

Tuotantoikkuna ennen jäädytystä vain, jos Go/no-go täyttyy; muuten tuotantopilotti jäädytyksen jälkeen. Jäädytyksen laajuus ja päivät vahvistetaan vaiheessa 0. Jos se kattaa myös uuden botin chat-työkalussa, botti ajoitetaan ikkunaan ennen jäädytystä tai sen jälkeen.

---

# Mitä emme vielä tiedä, ja miten ratkaisemme sen

| Tuntematon | Miksi sillä on väliä | Ratkaisu |
|---|---|---|
| Mikä pilvi, mitkä alueet sallittu; sijaitseeko mallikäyttö tenantissanne | Palveluvalinnat ja käsittelysijainti | Vaihe 0, ensimmäinen viikko |
| Chat-työkalu: sallitaanko omat botit, kuka hyväksyy | Käyttöliittymän toteutus ja aikataulu | Vaihe 0; jos ei, vaihtoehtoinen pääsy sovitaan |
| Dokumenttien sijainti, muoto, määrä ja kieli | Indeksoinnin työmäärä, skannausten tekstintunnistus | Inventaario ja laatunäyte |
| Lähdeoikeudet ja tunnistautuminen | Käyttäjäryhmäsuodatus haussa | Oikeuskartoitus; jos oikeuksia ei voi lukea, pilotti yhdellä kaikille avoimella kokoelmalla |
| Q1-jäädytyksen laajuus ja päivät | Käyttöönotto-ikkunat | Vahvistus teiltä vaiheessa 0 |
| Aiemman pilotin rakenne ja laskupiikki | Uudelleenkäyttö vai korvaus | Läpikäynti yhdessä |
| Kuka ylläpitää dokumentit ja palvelun käyttöönoton jälkeen | Vastausten tuoreus; hälytysten omistus | Nimetty omistaja per kokoelma; ylläpitäjä sovitaan |
| Kyselylokien säilytys, henkilötiedot kysymyksissä | Auditointi ja tietosuoja | Ehdotus: lyhyt säilytys ja henkilötietojen minimointi; linjataan vaiheessa 0 |

**Rehellinen rajaus:** emme sitoudu kattamaan lähteitä, joiden laatua emme ole nähneet. Vaiheen 0 portti päättää.

---

# Toimitettavat ja mitä tarvitsemme teiltä

:::cols
### Toimitettavat
- **D1 · Vaihe 0:** lähde- ja laatuinventaario, suomen lähtötaso, go/no-go
- **D2:** RAG-avustaja pilottiviipaleelle teidän pilvessänne ja chat-työkalussanne (tai sovitussa vaihtoehtoisessa pääsyssä), lähdeviitteineen
- **D3:** suomenkielinen arviointijoukko ja ajettava mittaus
- **D4:** kustannusvalvonta: budjetit, hälytykset, kova pysäytys, raportti BI-työkalussanne tai pilven kustannusnäkymässä
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

## Suomenkielinen, lähteistetty avustaja teidän pilvessänne, kulut hallinnassa

Recordly Oy · Helsinki
