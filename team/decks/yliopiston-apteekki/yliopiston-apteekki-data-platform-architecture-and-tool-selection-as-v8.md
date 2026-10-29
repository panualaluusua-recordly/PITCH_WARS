<!-- title: Yliopiston Apteekki · Data Platform Architecture and Tool Selection -->
# Selkeä tietoalustan arkkitehtuuri ja työkaluvalinta, ilman selainseurantaa

## Kuuden viikon arvio nykyisen ympäristön pohjalta, kirjoitettu suomeksi ja arjen kielellä. Kiinteä hinta 16 560 € (+ alv).

Ehdotus: Saara Niemistö, Development Manager, Data & Analytics · Recordly Oy · Helsinki

---

# Lähestymistapa: mitä olemme lukeneet rivien välistä

| Mitä kerroitte | Mitä lupaamme |
|---|---|
| Haluatte **nopean, kivuttoman** tuloksen, joka ei häiritse apteekkien arkea | **6 viikkoa.** Teiltä noin 2 h viikossa, 4 haastattelua (45 min), ei status-palavereja. Kirjalliset viikkoviestit. |
| Arkkitehtuuri on uusi alue, vastuu tuli yllättäen | **Päätösmuistio selkokielellä:** sanasto, vaihtoehdot kuvina, suositus perusteluineen. Te päätätte, me valmistelemme. |
| Digiapteekin tunnisteet ovat viranomaistarkastelussa | **Ei selainpuolen seurantaa missään suosituksessa.** Poissulkeva kriteeri: työkalu ei saa vaatia selaimeen asennettavia skriptejä, pikseleitä tai tunnisteita. Palvelinpuolinen keruu ei sekään ole automaattisesti sallittua: oikeusperusteen arvioi tietosuojavastaavanne, me listaamme kysymykset. |
| Englanninkieliset projektit aiheuttivat väärinkäsityksiä | **Kaikki suomeksi:** haastattelut, dokumentit, päätöksenteko. Suomen kieli on roolivaatimus; kielitaito vahvistetaan ennen lähettämistä. |

> Rehellinen tuntematon: ERP:n, BI-työkalun ja pilven tarkat tiedot eivät ole tarjouspyynnössä. Selvitämme ne viikolla 1.

---

# Yksi kuva nykytilasta ja kolmesta vaihtoehdosta: tieto tulee järjestelmistä, ei selaimesta

<div style="display:flex;align-items:stretch;gap:0.5em;font-size:0.72em;line-height:1.25;margin:0.2em 0 0.5em 0;">
<div style="flex:1;border:2px solid #434343;background:#262626;padding:0.5em;"><div style="color:#E3FF87;font-weight:800;text-transform:uppercase;letter-spacing:0.05em;font-size:0.8em;margin-bottom:0.4em;">Lähteet</div><div style="border:2px solid #E3FF87;padding:0.35em;margin-bottom:0.35em;">ERP <span style="color:#8a8a8a;">(vahvistetaan vk 1)</span></div><div style="border:2px solid #E3FF87;padding:0.35em;margin-bottom:0.35em;">Verkkoapteekin palvelin: tilaukset ja tapahtumat</div><div style="border:2px solid #E3FF87;padding:0.35em;">Myymälät ja muut kanavat</div></div>
<div style="align-self:center;color:#E3FF87;font-weight:900;font-size:1.4em;">→</div>
<div style="flex:1;border:2px solid #434343;background:#262626;padding:0.5em;"><div style="color:#E3FF87;font-weight:800;text-transform:uppercase;letter-spacing:0.05em;font-size:0.8em;margin-bottom:0.4em;">Keruu</div><div style="border:2px solid #E3FF87;padding:0.35em;margin-bottom:0.35em;">Järjestelmistä ja palvelimilta: eräajo tai rajapinta</div><div style="border:2px solid #E3FF87;padding:0.35em;background:#2b3118;color:#FFFFFF;font-weight:600;">Ei selainskriptejä, pikseleitä eikä tunnisteita</div></div>
<div style="align-self:center;color:#E3FF87;font-weight:900;font-size:1.4em;">→</div>
<div style="flex:1;border:2px solid #434343;background:#262626;padding:0.5em;"><div style="color:#E3FF87;font-weight:800;text-transform:uppercase;letter-spacing:0.05em;font-size:0.8em;margin-bottom:0.4em;">Tallennus, julkinen pilvi</div><div style="border:2px solid #E3FF87;padding:0.35em;margin-bottom:0.35em;">Nykyinen dataratkaisu <span style="color:#8a8a8a;">(EU/ETA, vahvistetaan vk 1)</span></div><div style="border:2px solid #E3FF87;padding:0.35em;">A siistitty · B yksi osa lisätään tai vaihdetaan · C suurempi muutos</div></div>
<div style="align-self:center;color:#E3FF87;font-weight:900;font-size:1.4em;">→</div>
<div style="flex:1;border:2px solid #434343;background:#262626;padding:0.5em;"><div style="color:#E3FF87;font-weight:800;text-transform:uppercase;letter-spacing:0.05em;font-size:0.8em;margin-bottom:0.4em;">Raportointi</div><div style="border:2px solid #E3FF87;padding:0.35em;margin-bottom:0.35em;">Nykyinen BI-työkalu</div><div style="border:2px solid #E3FF87;padding:0.35em;">Pääsynhallinta ja lokitus arvioidaan joka vaihtoehdossa</div></div>
</div>
<div style="background:#2b3118;padding:0.4em 0.6em;font-size:0.68em;margin-bottom:0.6em;">Arviointi tehdään lukuoikeuksin, nykyisillä lisensseillä ja irrotetuilla otteilla tai synteettisellä datalla. Tuotantojärjestelmiin ei tehdä muutoksia eikä niiden kuormaa lisätä.</div>

- **Poissulkeva ehto:** vaihtoehto ei saa vaatia selaimeen skriptejä, pikseleitä tai tunnisteita. Palvelinpuolinen keruu voi silti olla henkilötietojen käsittelyä: oikeusperusteen arvioi tietosuojavastaavanne.
- **Nykyinen siistittynä (A) on aito vaihtoehto:** muutosta suositellaan vain, jos se voittaa A:n vähintään 0,5 pisteellä.
- **Jokaisesta vaihtoehdosta raportoidaan** lisenssit (säilyy, tulee, poistuu), datan sijainti (EU/ETA) ja kuka sitä ylläpitää.

---

# Vaiheet ja aikataulu: neljä vaihetta, kuusi viikkoa

## Nykytila → kriteerit → vaihtoehtojen vertailu → suositus ja päätös

| Vaihe | Viikot | Mitä tapahtuu | Toimitus | Pv |
|---|---|---|---|---|
| **1 · Nykytila** | 1–2 | ERP:n, nykyisen dataratkaisun, BI:n, pilven ja verkkoapteekin tietovirtojen kartoitus; nykyiset selaintunnisteet listataan havaintoina. Poissulkeva ehto todennetaan jokaiselle työkalulle toimittajadokumentaation ja arkkitehtuurikuvauksen katselmuksella (mitä komponenttia selaimessa tarvitaan); selaintunnisteet inventoidaan sivuston tunnistehallinnan asetuksista, ei lisäämällä mitään seurantaa | Nykytilakartta (1 sivu) | 4 |
| **2 · Kriteerit** | 2–3 | Painotetut kriteerit: tietosuoja (datan sijainti EU/ETA, tietosuojavastaava tarkastaa), ei selainseurantaa, ylläpidon helppous, kustannus sekä yhteensopivuus nykyisen ERP:n ja BI-työkalun kanssa, datan tuoreus raportoinnissa ja skaalautuvuus verkkoapteekin kasvuun | Kriteeristö, hyväksytty **portti 1** | 3 |
| **3 · Vaihtoehdot** | 3–5 | 3 tavoitearkkitehtuuria (mm. "nykyinen siistittynä"), työkalujen pisteytys, pistokoe synteettisellä tai anonymisoidulla datalla | Vertailu | 6 |
| **4 · Suositus** | 5–6 | Tavoitearkkitehtuuri, lisenssivaikutus, 12 kk:n tiekartta, 90 min päätöstilaisuus; päätösmuistiossa jokaisesta vaihtoehdosta oma arkkitehtuurikuva, sanasto ja yhden sivun riskilista (tietosuoja, ylläpito, siirtymän vaikeus) | Päätösmuistio | 5 |

Vertailu on puolueeton: emme saa palkkioita toimittajilta. "Älä muuta mitään" on sallittu lopputulos.

---

# Neljä tarkistuspistettä: te hyväksytte kriteerit ennen pisteytystä, pistokoe ilman asiakastietoja

| Tarkistuspiste | Milloin | Läpäisyehto |
|---|---|---|
| **Nykytilakartta** | vk 2 | ERP, BI, pilvi ja verkkoapteekin tietovirrat nimetty; nykyiset selaintunnisteet listattu havaintoina (emme poista niitä). Jos tunnistehallintaa ei ole, tunnisteet listataan sivuston lähdekoodin ja verkkopyyntöjen läpikäynnillä lukuoikeuksin; löydökset raportoidaan vain havaintoina |
| **Portti 1: kriteerit** | vk 3 | Hyväksytte kriteerit ja painot; tietosuojavastaava on nähnyt poissulkevan ehdon, EU/ETA-ehdon ja oikeusperustekysymykset. Kriteerit: tietosuoja, ei selainseurantaa, ylläpidon helppous, kustannus sekä yhteensopivuus nykyisen ERP:n ja BI-työkalun kanssa, datan tuoreus raportoinnissa ja skaalautuvuus verkkoapteekin kasvuun. Pisteytys: asteikko 1–5 kriteeriä kohti, painot sovitaan portilla 1; 0,5 pisteen sääntö lasketaan painotetusta keskiarvosta |
| **Pistokoe** | vk 4–5 | Pistokoe läpäisty vaihtoehdolle, kun sama ERP-virta ja sama verkkoapteekin tapahtuma saapuvat perille ilman selainpuolen skriptiä; viive mitataan minuutteina lähdetapahtumasta raporttiin ja ajokustannus mitataan, molemmat raportoidaan vaihtoehdoittain; lukuoikeudet ja irrotetut otteet pyydetään vk 1, ja jos ne puuttuvat vk 3, pistokoe korvataan dokumenttitarkistuksella ja pisteet merkitään epävarmoiksi; epäonnistuminen kirjataan pisteisiin. Data on synteettistä tai anonymisoitua, ei asiakas- tai reseptitason tietoja. Todiste: selaimen verkkoliikenteen tallenne (ei kolmannen osapuolen kutsuja) ja ajoloki. Jos esimerkkidataa ei ole vk 3, pilotoidaan kaksi virtaa vaihtoehdoille A ja B; C kuvataan luonnoksena, ei pilotoida |
| **Päätös** | vk 6 | Vaihtoehto valittu (myös A); päätösmuistiossa jokaisesta vaihtoehdosta oma arkkitehtuurikuva, sanasto ja yhden sivun riskilista; 12 kk:n tiekartta, tarkistukset kk 3 ja 6 |

> Tuntemattomat: lisenssiluettelo vk 2 (ilman sitä kustannus on vain suunta) ja esimerkkidata ilman henkilötietoja vk 3 (ilman sitä pistokoe on dokumenttitarkistus ja pisteet merkitään epävarmemmiksi).

**Emme tee:** toteutusta, migraatiota, tunnisteiden poistoa, oikeudellista arviota emmekä tekoälyä.

---

# Tiimi ja asiakasviitteet

| | Lead Data Architect | Senior Data Engineer |
|---|---|---|
| **Vaaditut sertifikaatit** | Azure Solutions Architect Expert · AWS Certified Solutions Architect | Google Cloud Professional Data Engineer · Azure Data Engineer Associate |
| **Vaaditut kielet** | Suomi (vaatimus), englanti | Suomi (vaatimus), englanti |
| **Saatavuus** | 11 päivää kuuden viikon aikana, tavoite | vk 2–5, tavoite; vahvistus puuttuu |

- Asiakasviite vahvistetaan oikeasta toteutuksesta ennen tarjouksen lähettämistä.
- Viitteet ja yhteyshenkilöt puuttuvat vielä; edelliset esimerkkikuvaukset eivät ole todennettuja referenssejä.

---

# Hinnoittelumalli, lisenssivaikutus ja maksuehdot

| Rooli | Päivät | Päivähinta |
|---|---|---|
| Lead Data Architect | 11 | 920 € |
| Senior Data Engineer | 7 | 920 € |

## Kiinteä kokonaishinta: 18 henkilöpäivää = 16 560 € (+ alv)

- **Lisenssivaikutus:** arviointi ei vaadi uusia lisenssejä. Jokaiselle vaihtoehdolle raportoimme, mitkä lisenssit säilyvät, tulevat tai poistuvat, ja suuntaa-antavan 3 vuoden kustannusarvion (tarkentuu, kun lisenssiluettelo on saatu vk 2).
- **Maksuehdot:** kaksi yhtä suurta laskua (aloitus ja hyväksytty päätösmuistio), 30 pv netto.
- **Kiinteä hinta:** ylitykset ovat Recordlyn riski. Dokumentit ovat Yliopiston Apteekin omaisuutta.

---

<!-- statement -->
# Selkeä päätös kuudessa viikossa. Suomeksi. Ilman selainseurantaa.

## 18 henkilöpäivää · kiinteä hinta · ei uusia lisenssejä

Recordly Oy · Helsinki


**Staffing-tarkistus / Rauno:** roolit ovat vaatimuksia, eivät vahvistettuja henkilöprofiileja. CV:t, sertifikaatit, kielitaito ja todellinen saatavuus vahvistetaan ennen lähettämistä. Työpäivä = 8 h; DE vähintään 115 €/h, DA 125 €/h, AI-osaaminen +5 €/h. Arkkitehdin perushinta 115 €/h on ehdotus hyväksyttäväksi, ei käyttäjän antama vähimmäishinta. Enintään kaksi arkkitehtia. Kiinteän hinnan laajuus ja riskit vahvistetaan ennen sitoutumista.

<!-- coverage v4 (tech lane added s3 architecture diagram, s5 gates and risks; slide numbers below shifted: approach=s2+s3, phases=s4, gates=s5, team=s6, price=s7). Original v2 note: RFP approach=s2+s3; phases+timeline=s3; team profiles=s4; pricing model=s5 (fixed total, days x rate); licensing impact=s5; payment terms=s5; >=2 references=s4 (anonymised, contacts to shortlisted; VERIFY against real cases). Hidden: no client-side telemetry=s2 knockout criterion+s3 criteria; Finnish=s2,s4; quick painless=s2 (6 weeks, 2h/week); new to architecture=plain-language decision memo+glossary. Traps: no AI add-ons, no VDE, no new platform; honest unknown=stack details wk1. -->
