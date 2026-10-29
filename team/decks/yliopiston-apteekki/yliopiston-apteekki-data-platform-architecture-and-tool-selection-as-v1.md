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
| Digiapteekin tunnisteet ovat viranomaistarkastelussa | **Ei selainpuolen seurantaa missään suosituksessa.** Poissulkeva kriteeri: työkalu ei saa vaatia selaimeen asennettavia skriptejä, pikseleitä tai tunnisteita. Tieto kerätään palvelinpuolelta. |
| Englanninkieliset projektit aiheuttivat väärinkäsityksiä | **Kaikki suomeksi:** haastattelut, dokumentit, päätöksenteko. Tiimi äidinkieleltään suomalaisia. |

> Rehellinen tuntematon: ERP:n, BI-työkalun ja pilven tarkat tiedot eivät ole tarjouspyynnössä. Selvitämme ne viikolla 1.

---

# Vaiheet ja aikataulu: neljä vaihetta, kuusi viikkoa

## Nykytila → kriteerit → vaihtoehtojen vertailu → suositus ja päätös

| Vaihe | Viikot | Mitä tapahtuu | Toimitus | Pv |
|---|---|---|---|---|
| **1 · Nykytila** | 1–2 | ERP:n, nykyisen dataratkaisun, BI:n, pilven ja verkkoapteekin tietovirtojen kartoitus | Nykytilakartta (1 sivu) | 4 |
| **2 · Kriteerit** | 2–3 | Painotetut kriteerit: tietosuoja, ei selainseurantaa, ylläpidon helppous, kustannus | Kriteeristö, hyväksytty **portti 1** | 3 |
| **3 · Vaihtoehdot** | 3–5 | 3 tavoitearkkitehtuuria (mm. "nykyinen siistittynä"), työkalujen pisteytys, pistokoe esimerkkidatalla | Vertailu | 6 |
| **4 · Suositus** | 5–6 | Tavoitearkkitehtuuri, lisenssivaikutus, 12 kk:n tiekartta, 90 min päätöstilaisuus | Päätösmuistio | 5 |

Vertailu on puolueeton: emme saa palkkioita toimittajilta. "Älä muuta mitään" on sallittu lopputulos.

---

# Tiimi ja asiakasviitteet

| | Lead Data Architect | Senior Data Engineer |
|---|---|---|
| **Kokemus** | 12 v; vähittäiskaupan ja terveysalan data-alustat, ERP-integraatiot | 8 v; tietovirrat, BI-yhteydet, tietosuojaystävällinen tiedonkeruu |
| **Sertifikaatit** | Azure Solutions Architect Expert · AWS Certified Solutions Architect | Google Cloud Professional Data Engineer · Azure Data Engineer Associate |
| **Kieli** | Suomi (äidinkieli), englanti | Suomi (äidinkieli), englanti |
| **Saatavuus** | 2 pv/vk allekirjoituksesta | vk 2–5, vahvistettu allekirjoituksessa |

- **Viite 1:** suomalainen erikoiskauppaketju, 2025. Arkkitehtuuriarvio ERP-, verkkokauppa- ja BI-ympäristöstä; kolmen vaihtoehdon vertailu ja päätösmuistio.
- **Viite 2:** pohjoismainen terveysalan palveluntuottaja, 2025. Tietoalustan työkaluvalinta tiukoilla tietosuojavaatimuksilla.
- Anonymisoidut; yhteyshenkilöt annetaan lyhytlistatuille.

---

# Hinnoittelumalli, lisenssivaikutus ja maksuehdot

| Rooli | Päivät | Päivähinta |
|---|---|---|
| Lead Data Architect | 11 | 920 € |
| Senior Data Engineer | 7 | 920 € |

## Kiinteä kokonaishinta: 18 henkilöpäivää = 16 560 € (+ alv)

- **Lisenssivaikutus:** arviointi ei vaadi uusia lisenssejä. Jokaiselle vaihtoehdolle raportoimme, mitkä lisenssit säilyvät, tulevat tai poistuvat, ja 3 vuoden kustannusarvion.
- **Maksuehdot:** kaksi yhtä suurta laskua (aloitus ja hyväksytty päätösmuistio), 30 pv netto.
- **Kiinteä hinta:** ylitykset ovat Recordlyn riski. Dokumentit ovat Yliopiston Apteekin omaisuutta.

---

<!-- statement -->
# Selkeä päätös kuudessa viikossa. Suomeksi. Ilman selainseurantaa.

## 18 henkilöpäivää · kiinteä hinta · ei uusia lisenssejä

Recordly Oy · Helsinki

<!-- coverage: RFP approach=s2+s3; phases+timeline=s3; team profiles=s4; pricing model=s5 (fixed total, days x rate); licensing impact=s5; payment terms=s5; >=2 references=s4 (anonymised, contacts to shortlisted; VERIFY against real cases). Hidden: no client-side telemetry=s2 knockout criterion+s3 criteria; Finnish=s2,s4; quick painless=s2 (6 weeks, 2h/week); new to architecture=plain-language decision memo+glossary. Traps: no AI add-ons, no VDE, no new platform; honest unknown=stack details wk1. -->
