# Tekniset diat: Alko, tuote- ja toimittajatietojen laatu
_Alko Oy: Two slides: architecture after 'Tavoitteet ja tausta', gates and risks after the plan slide (as in deck v4)_

## 2. Suositeltu tekninen ratkaisu: hyväksytyt ja peruttavat yhdistämiset
- **Yhdistäminen ja palautus:** pääietue valitaan sovitulla säännöllä, viitteet (avoimet tilaukset, hinnastot, toimittajasopimukset) ohjataan pääietueeseen, vanha avain säilyy passiivisena. Palautus palauttaa auditointitaulun ennen-arvot; testataan pilotissa.
- **Validointi on lukevaa:** virhe tuottaa ilmoituksen ja poikkeamalistan, ei muuta dataa eikä pysäytä latausta. Siksi hyväksyntä tarvitaan vain yhdistämisille.
- **Tietosuoja:** toimittajien IBAN- ja osoitetiedot käsitellään vain Alkon ympäristössä Alkon pääsynhallinnalla, ei kopioita ulos.
[Lähteet (Alkon omat): ERP: tuoterekisteri, ERP: toimittajarekisteri, Nykyinen dataratkaisu] → [Auditointi ja tunnistus: Profilointi: täyttöasteet, avainvirheet, Säännöt T1–T4, S1–S2 koodina Alkon repossa] → [Hyväksyntä: Tarkistusjono: Alkon nimeämä omistaja hyväksyy, Auditointitaulu: kuka, milloin, sääntö, ennen/jälkeen] → [ERP-muutos: Yhdistämislista ERP-muutosprosessiin, Vanha avain säilyy, palautus mahdollinen] → [Valvonta: Validointi: ilmoitus kanavaanne, Laatumittaristo Alkon BI-työkaluun]
(Kaikki ajetaan Alkon ympäristössä ja pääsynhallinnassa. ERP, dataratkaisu, BI ja pilvi ovat Alkon nykyiset (tarkennetaan vk 1). Ei uusia lisenssejä.)

## 3. Tekniset portit: ensin luvut Alkon datasta, sitten yhdistäminen
| Portti | Milloin | Läpäisyehto |
| --- | --- | --- |
| 1 · Laajuus | vk 2 | Kaksoiskappaleaste rekistereittäin; varmojen (T1, T2, S1) ja tarkistusjonon osuus; ERP:n yhdistämisreitti vahvistettu; merkityn otoksen tarkkuus. Alko päättää laajuuden ja raja-arvot. |
| 2 · Pilotti | vk 5 | 200 hyväksyttyä yhdistämistä ERP-muutosprosessin kautta; viitteet siirretty; vähintään yksi palautus testattu. Vasta sitten koko erä. |
| 3 · Validointi | vk 8 | Säännöt ajettu 2 viikkoa koeajona; väärät hälytykset alle sovitun tason ennen ilmoituksia kanavaan. |

_Tekniset tuntemattomat: ERP-tuote, dataratkaisu, BI ja pilvi (selvitetään vk 1); yhdistämisreitti ERP:hen, rajapinta vai ylläpito (portti 1); viittaukset muista tauluista (kartoitetaan auditoinnissa); lukuoikeus tuote- ja toimittajadataan vk 1 on aikataulun suurin riski._
