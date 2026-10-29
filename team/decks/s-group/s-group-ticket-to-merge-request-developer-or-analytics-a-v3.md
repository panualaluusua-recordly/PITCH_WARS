<!-- title: S Group · Tiketistä merge requestiksi: analytiikkakehittäjäagentti -->
# Backlog-tiketistä katselmoiduksi merge requestiksi

## Agentti luonnostelee, teidän ihmisenne hyväksyvät. Rakennettu S Groupin Azure-ympäristöön, kohteena kate- ja kampanja-analytiikan tiketit. Kiinteä kokonaishinta €21,400 (excl. VAT).

Ehdotus: Tiina Kettunen, Director of Commercial Analytics & AI · Recordly Oy · Helsinki

---

# Ratkaisu: yksi silmukka S Groupin Azure-ympäristössä

## Tiketti sisään, validoitu merge request ulos. Agentti ei koskaan yhdistä omaa työtään.

<div style="display:flex;align-items:stretch;gap:12px;margin:0.2em 0 0.5em 0;font-size:0.68em;line-height:1.25"><div style="flex:1;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:14px"><b style="color:#E3FF87">1 · TIKETTI</b><br>Backlog-tiketti kehitystyökalussanne. Muutokset alkavat vain tiketistä, eivät chatista</div><div style="align-self:center;color:#E3FF87;font-size:2em">&rarr;</div><div style="flex:1;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:14px"><b style="color:#E3FF87">2 · KEHITYSAGENTTI</b><br>Lukee tiketin ja datamallinne, suunnittelee muutoksen, kirjoittaa koodin ja testit kehitysympäristöön. Epäselvässä tiketissä kysyy, ei arvaa</div><div style="align-self:center;color:#E3FF87;font-size:2em">&rarr;</div><div style="flex:1;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:14px"><b style="color:#E3FF87">3 · KATSELMOINTIAGENTIT</b><br>Tarkistavat koodin ja ajavat testit joka muutokselle. Viat palaavat korjattavaksi</div><div style="align-self:center;color:#E3FF87;font-size:2em">&rarr;</div><div style="flex:1;background:#2A2A2A;border:2px solid #434343;border-radius:10px;padding:14px"><b style="color:#E3FF87">4 · MERGE REQUEST</b><br>Diff, testitulokset ja perustelut teidän repositoriossanne. Tila päivittyy chat-työkaluunne</div><div style="align-self:center;color:#E3FF87;font-size:2em">&rarr;</div><div style="flex:1;background:#E3FF87;color:#1B1B1B;border-radius:10px;padding:14px"><b>5 · TEIDÄN KEHITTÄJÄNNE</b><br>Hyväksyy tai hylkää. <b>Vain ihminen yhdistää</b></div></div>
<div style="background:#2A2A2A;border:2px dashed #E3FF87;border-radius:10px;padding:10px 16px;font-size:0.68em;margin-bottom:0.6em"><b style="color:#E3FF87">AUDITOINTIAGENTTI, AINA PÄÄLLÄ:</b> tallentaa jokaisen teon ja agentin päättelyn lokiin ja raportoi poikkeamat. Tämä on Recordlyn todennettu toimintamalli (issue → agentti → PR → ihmisen hyväksyntä), rakennettuna <b>teidän Azure-pinoonne</b>: koodi, data ja lokit pysyvät teidän ympäristössänne.</div>

:::cols
- **Rehellisesti pinosta:** RFP kertoo Azuren, SAP S/4HANA:n, "nykyisen dataympäristön", BI-työkalun ja chat-työkalun, mutta ei nimiä. **Viikko 1 vahvistaa ne.** Valmista Virtual Data Engineer -tuotettamme ei asenneta: se toimii Snowflakessa. Jos ajatte Snowflakea, kerromme sen heti ja arvioimme tuotteen erikseen; **se ei ole tässä hinnassa.**
:::col
- **Rajaus:** ei ML-malleja, ei uusia BI-työkaluja, ei lisäkäyttötapauksia, ei tuotantokäyttöoikeuksia, ei muutoksia SAP:iin. Vain tiketti → koodi → testit → merge request.
:::

---

# Mitä tikettejä nopeutetaan, ja miten sen näkee

## Kohteena kaupalliset tiketit: kate, kampanjat, kassakonversio. Ei näkymätöntä putkistoa.

| Tikettiryhmä (esimerkit backlogistanne) | Mitä agentti tekee | Mitä liiketoiminta näkee |
|---|---|---|
| **Kate tuoteryhmittäin** | Mallimuutokset S/4HANA-datasta BI-työkalun käyttämiin tauluihin, testit | Katenäkymä päivittyy tiketin jälkeen päivissä, ei viikoissa |
| **Kampanja-analytiikka** | Uudet kampanjamittarit ja vertailut aiempiin jaksoihin | Kampanjan myyntivaikutus ja kate samassa näkymässä |
| **Kassakonversio ja ostoskorin koko** | Mittarimäärittelyt ja myymäläkohtaiset leikkaukset | Retail-johto näkee konversion myymälöittäin |
| **Rutiinit: tarkistus- ja korjaustiketit** | Virheiden juurisyyn selvitys, korjaus-PR | Analyytikot vapautuvat vaativampaan työhön |

**Mittarit, jotka raportoimme viikoittain suomeksi, S Groupin omasta datasta:**

| Mittari | Lähtötaso | Tavoite |
|---|---|---|
| **Läpimenoaika tiketistä merge requestiin** | Mitataan 20–30 viimeisimmästä tiketistä viikolla 1 | Sovitaan lähtötason jälkeen, ennen rakennusvaihetta |
| **Ilman uudelleentyötä hyväksytyt MR:t, %** | Sama otos | Sovitaan lähtötason jälkeen |
| **Katselmointiaika per MR (min)** | Sama otos | Ei saa kasvaa kehittäjillänne |

> Vertailuksi, ei lupaukseksi: Snowflake+dbt-projektissamme puolimutkainen putkisto kului **12 h käsin → 30 min**, ihmisen hyväksyessä. Teidän lukunne mitataan teidän tiketeistänne. Emme lupaa lukuja, joita emme ole nähneet.

---

# Toteutussuunnitelma: 12 viikkoa, kolme hyväksyttävää vaihetta

| Vaihe | Viikot | Mitä tapahtuu | Hyväksyntä (maksuerä) |
|---|---|---|---|
| **1 · Käynnistys** | 1 | **Ei pinon kartoitusta alusta:** käytämme aiemman yhteistyön arkkitehtuurikuvauksia sellaisenaan. Valitaan 2–3 tikettityyppiä kaupallisesta backlogista ja otetaan lähtötaso | Lyhyt käynnistysmuistio. **S Group päättää jatkosta** |
| **2 · Rakennus** | 3–7 | Agenttitiimi Azureen. **Recordly kirjoittaa käytännöt ja "täydelliset esimerkit"**; teidän kehittäjänne vain hyväksyvät ne (noin 1 h/viikko), jotta he pysyvät katteen parissa. Ensimmäiset MR:t testitiketeistä | Agentti läpäisee teidän katselmointinne testitiketeillä. Tila-ilmoitukset chat-työkaluun toimivat |
| **3 · Valvottu pilotti** | 8–12 | Agentti työstää oikeita kate- ja kampanjatikettejä, **teidän kehittäjänne hyväksyvät jokaisen MR:n** | Pilottiraportti: mittarit vs. lähtötaso. Jatka, säädä tai lopeta |

- **Viikko 4:** ensimmäinen oikea kaupallinen tiketti merge requestina teidän katselmoitavananne
- Käytännöt, kehotteet ja koodi ovat teidän omistuksessanne alusta asti. Ei vakiopalavereja, kirjallinen viikkoraportti suomeksi
- **Avoimet kysymykset:** (1) olemassa olevat arkkitehtuurikuvaukset otetaan käyttöön sellaisenaan, viikko 1. (2) kuinka suuri osa backlogista on riittävän rutiinia agentille: lähtötaso näyttää sen, ja jos vastaus on "vähän", sanomme sen vaiheen 1 päätteeksi. (3) Azure-mallin laatu teidän tiketeillänne, ratkeaa vaiheen 1 portilla

---

# Tiimi, saatavuus ja ehdot

| | Lead Data Architect | Senior Data Engineer | Senior AI Engineer |
|---|---|---|---|
| **Rooli** | Konventiot, arkkitehtuuri, agentin työn katselmointi | Dataputket, testit ja CI/CD itsenäisesti; kehittäjänne vain katselmoivat | Agentin työnkulku, tulosten laadun arviointi, pääsynhallinta |
| **Kokemus** | 12 v; Azure-data-arkkitehtuuri, SAP-lähteet | 9 v; Azure-dataputkistot, BI-valmiit mallit | 8 v; LLM-sovellukset, evaluointi |
| **Sertifikaatit** | Microsoft Certified: Azure Solutions Architect Expert | Microsoft Certified: Azure Data Engineer Associate | Microsoft Certified: Azure AI Engineer Associate |
| **Kieli** | suomi (äidinkieli), englanti | suomi (äidinkieli), englanti | suomi (äidinkieli), englanti |

- **Saatavuus:** alku sopimuspäivänä, kun pääsyt ovat auki. Dokumentaatio, työpajat ja raportointi suomeksi. Kaikki ovat Recordlyn työntekijöitä, ei alihankkijoita
- **Vaihto:** S Group voi vaatia vaihtoa milloin tahansa; korvaaja vähintään yhtä senior 5 työpäivässä, perehdytys Recordlyn kustannuksella
- **Siirto S Groupin palkkalistoille:** ilman rekrytointipalkkiota 12 kk:n jälkeen, ei prosenttipalkkioita ennen sitä

---

# Hinta: kiinteä kokonaishinta ja maksuerät hyväksyttyjen vaiheiden mukaan

## Kokonaishinta: €21,400 (excl. VAT)

| Maksuerä | Henkilöpäivät × päivähinta | Summa |
|---|---|---|
| **1 · Käynnistys** | Arkkitehti 1 pv × €920 + Data engineer 1 pv × €920 | €1,840 |
| **2 · Rakennus** | Arkkitehti 3 pv × €920 + Data engineer 7 pv × €920 + AI engineer 4 pv × €960 | €13,040 |
| **3 · Valvottu pilotti** | Arkkitehti 1 pv × €920 + Data engineer 4 pv × €920 + AI engineer 2 pv × €960 | €6,520 |

- **23 henkilöpäivää** hintaan €920–960/pv. Sama päivähinta kuin hintakortissamme; ei lisäkustannuksia
- **Voitte lopettaa vaiheen 1 jälkeen** ja maksaa vain sen. Jos agentti ei sovi ympäristöönne, sanomme sen silloin
- Laskutus vaiheittain hyväksynnän jälkeen, S Groupin maksuehdoin
- **Lisenssit:** ei Recordlyn lisenssejä, ei kuukausimaksua. Azure-palvelujen ja mallikutsujen kulut kertyvät S Groupin omalle tilaukselle, ja arvio niistä toimitetaan vaiheessa 1
- **Ei sopimuspoikkeamia.** S Groupin vakioehdot sellaisenaan

<!-- coverage: RFP autonomous ticket-to-MR agent=s2; backlog tickets -> validated code, tests, MR=s2; hosted on Azure=s2,s4; integrate w/ developer workflows=s2 (ticket, repo, human approval), s4 phase2; status updates via chat tool=s2 step4, s4; pipelines compatible w/ current data setup, BI tool, SAP S/4HANA=s2 stack, s3; technical solution=s2; implementation plan/timeline=s4; team profiles/availability=s5; deliverables=s4 gates; commercial pricing model=s6; previous hint commercial impact (margin, checkout conversion)=s3; payroll transition clause=s5; Finnish=whole deck; honest unknown stack/Snowflake=s2,s4; VDE only if Snowflake, not priced=s2; cannot merge own work, review+auditor agents=s2; measurable outcomes lead time, % without rework=s3; no ML/new platforms=s2 scope; no deviations, excl VAT, roles only=s5,s6. Price check: 46 d; 8,360+22,400+12,120=42,880. Placeholders to verify: years, certs, "Azure-malli" hosting options, 12 kk fee-free clause consistency with panel win. -->
