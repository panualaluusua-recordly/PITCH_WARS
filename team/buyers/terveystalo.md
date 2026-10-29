# Terveystalo Oyj – Riikka Voutilainen, Director of Data & Analytics

(No earlier local notes or decks existed; everything below comes from the live API, which includes teammates' requests.)

## 2026-10-29 09:01Z brief (buyer-analyst dry run) - RESULT: WAIT until 09:13:02Z

Snapshot: open=terveystalo-architecture-or-tool-assessment status=open (no conversation yet) available_at=2026-10-29T09:13:02Z (about 12 min from now) time_left=231 min stats=won 0 / lost 1 / feedback rounds 1 (on the closed project) / penalties €0 / fees €4,500 / net -€4,500
**Teammate active, coordinate before acting.** The last request (proposal v3) was answered at 08:58:02Z, about 3 min before this check. No project is `thinking`; the new project only opens at available_at. The roster (`consultants`) is not returned by /api/me at the moment.

Fit: terveystalo · terveystalo-architecture-or-tool-assessment
Decision: WAIT(2026-10-29T09:13:02Z)
Gates: failed: available_at in the future ← "available_at": "2026-10-29T09:13:02.064690+00:00". Full brief deliberately not produced (per agent definition). Re-run after 09:13Z.
Not scored. Hard gates are the only thing evaluated.

### History digest (project 1: terveystalo-agent-accelerated-migration, LOST)
- 08:53 feedback (teammate, deck v2, price not logged) → hints: liked "named senior engineers to personally inspect and approve every pipeline alteration"; disliked "inconsistent and distinctly unfinished"; "relying on English for delivery and documentation introduces pointless friction ... day-to-day work runs strictly in our local language"; "rigid adherence to established reporting principles beats disruptive vendor experimentation"; price "seems quite high, though it might still be within budget" (over-soft).
- 08:58 proposal (teammate, deck v3, price not logged) → LOST: "patient-facing conversational AI tools is conspicuously absent". Ratings price good / buyer_fit good / project_fit excellent / presentation excellent. 7 of 8 preferences met; the one "not addressed" is patient-facing conversational AI. Presentation: all strong except explanatory_visuals adequate ("relies on text cards rather than process diagrams") and **recordly_style weak** ("white backgrounds and teal accents instead of the required dark background and lime theme").
- A loss still opened the next project (cooldown 15 min: last_closed 08:58:02 → available 09:13:02). The buyer is not out_of_budget.

### Carry-over (for the architecture/tool-assessment RFP, use when it opens)
- Language: Finnish delivery and documentation (high: hint "relying on English ... friction"; verdict "met" for all-native-Finnish team).
- Missing patient-facing conversational AI cost the win (high: verdict text). Bio hope: "digital appointment assistant progressed once a seasoned external consultancy was brought in". Recordly's healthcare experience is "limited (verify)" per recordly-profile.md: show it only as a conditional or anonymised case, never as a claim we cannot back.
- Persona: cautious continuity, "rigid legacy reporting principles", resists "disruptive experimentation" (high: bio + hint). Recommend conservative, proven-pattern recommendations for an assessment (guess).
- Praised and to keep: named-senior review gate, EU-only processing and non-patient test data, no new tools beyond Databricks, fixed-price pilot with a decision gate, unit prices.
- Format: must use the Recordly dark background and lime theme (verdict: recordly_style "weak"). Needs process diagrams. Avoid "inconsistent, unfinished" feel (hint).
- Price: unknown what was sent. Verdict "good" at the proposal and "quite high, maybe within budget" at feedback. Needs the actual figures from the teammate who sent them (open question).
- The new RFP asks for at least two client references, licence cost implications and payment terms, and says "Shortlisted vendors will be invited to present". These are traps for rfp-trap-scan once the project is open.

Open questions: what prices were sent with v2 and v3, and what was the project budget? Who is the teammate sending to Terveystalo, and do they plan to send on the new project at 09:13?

## 2026-10-29 C-batch draft (v2)
Deck decks/terveystalo/terveystalo-architecture-or-tool-assessment-v2.pdf, 6 slides, Finnish, 19 pd x €920 = €17,480. Bets: Finnish deck; patient-facing conversational AI assessed (bio hope, assessment only); 2 anonymised references, licence impact + payment terms. Open: references are generic and must be verified as real before sending; healthcare experience limited; ERP docs quality unknown. Not sent.

<!-- replies:auto -->
## Buyer replies (auto, from the game API; do not edit inside the markers)

### terveystalo-agent-accelerated-migration
- 2026-10-29T08:53 · **hints** · deck `terveystalo-agent-accelerated-migration-v2.pdf` (unknown) · price signal: **over-soft**
  > I reviewed the submission. Requiring named senior engineers to personally inspect and approve every pipeline alteration is sound, as I have no interest in seeing unvetted code corrupting our reporting pipelines again. That said, working through the material was an aggravating exercise; it felt inconsistent and distinctly unfinished, which makes it hard to take seriously or defend upward. Beyond that, relying on English for delivery and documentation introduces pointless friction across our clinical operations where day-to-day work runs strictly in our local language. During our original Databricks rollout across the organization, we saw firsthand that rigid adherence to established reporting principles beats disruptive vendor experimentation every time. On the commercial side, the proposed fee for the trial seems quite high, though it might still be within budget, but I am certainly not committing to anything until these matters are resolved.
- 2026-10-29T08:58 · **verdict** · deck `terveystalo-agent-accelerated-migration-v3.pdf` (unknown) · price signal: **verdict lost, price good**
  > We are not moving forward with this proposal, not least because the entire matter of patient-facing conversational AI tools is conspicuously absent.
  ratings: price good, buyer_fit good, project_fit excellent, presentation excellent
  - [met] Slide 4 and slide 8 specify test environments with non-patient data only and EU-only processing.
  - [met] Slide 2 and slide 7 commit to an all-native-Finnish delivery team, workshops, and documentation in Finnish.
  - [met] Slide 2 and slide 4 explicitly state no new tools will be added besides Databricks inside our tenant.
  - [not addressed] The slides focus strictly on ETL and reporting migration without addressing patient-facing conversational AI tools.
  - [met] Slide 2 and slide 9 offer a fixed-price 5-week pilot with a strict decision gate before any broader commitment.
  - [met] Slide 6 establishes empirical timing against a manual baseline with a firm gate requiring at least 40% measured time reduction.
  - [met] Slide 9 sets clear unit prices per remaining ETL job and report rather than a lump-sum migration fee.
  - [met] Slide 4 and slide 5 mandate branch protection requiring named senior engineer approval on every single pull request without auto-merges.
### terveystalo-architecture-or-tool-assessment
- 2026-10-29T11:37 · **no_reply** · deck `terveystalo-architecture-or-tool-assessment-probe-v1.pdf` (unknown) · price signal: **no reply**
  > No reply.
- 2026-10-29T11:55 · **verdict** · deck `terveystalo-architecture-or-tool-assessment-v2-eur17480.pdf` (€17,480) · price signal: **verdict lost, price over budget**
  > Once again, your commercial expectations remain well beyond what our operational framework can accommodate, so we will not be taking this forward.
  ratings: price over budget, buyer_fit fair, project_fit weak, presentation excellent
  - [not addressed] Kalvoilla ei mainita lainkaan synteettisen tai anonymisoidun datan hyödyntämistä kehityksessä.
  - [met] Kalvolla 2 todetaan kaikkien työpajojen ja dokumenttien olevan suomeksi ja tiimin äidinkieleltään suomenkielinen.
  - [met] Kalvolla 2 painotetaan nykyisen Databricks-ympäristön säilyttämistä eikä uusia työkaluja tai lisenssejä oteta oletuksena.
  - [not addressed] Kalvolla 2 puhutaan keskustelevan tekoälyn arvioinnista, mutta ulkoisen kumppanin ja sisäisen kehityksen työnjaosta ei sanota mitään.
  - [leans against] Kalvolla 3 tarjotaan kahden viikon välein pidettäviä tilannekatsauksia asynkronisen viestinnän sijaan.
  - [leans against] Kalvolla 3 katsaukset on sovittu kahden viikon välein eikä viikoittaisina hands-on-tarkistuspisteinä.
  - [against] Koko 19 työpäivän kokonaisuus myydään yhdellä kerralla ilman kevyttä aloitusauditoinnin vaihetta.
  - [against] Kokonaishinta 17 480 euroa ylittää suoraan tähän työhön varattavan raamin.
### terveystalo-analytics-engineer-for-6-months
- 2026-10-29T12:14 · **verdict** · deck `terveystalo-analytics-engineer-for-6-months-v1-eur15640.pdf` (€15,640) · price signal: **verdict won, price excellent**
  > We can proceed with this proposal as it sticks to our established setup without unnecessary noise, though I expect absolute discipline around our boundaries once work begins.
  ratings: price excellent, buyer_fit good, project_fit fair, presentation excellent
  - [met] Sivuilla 3 ja 4 rajataan kehitys ja testaus nimenomaisesti vain maskattuun tai synteettiseen dataan.
  - [met] Sivuilla 2 ja 5 luvataan työ, dokumentaatio ja koodikommentit suomeksi äidinkielen tasolla.
  - [met] Sivuilla 2 ja 5 vahvistetaan, että työ tehdään meidän nykyisessä Databricksissämme ilman uusia alustoja tai lisenssejä.
  - [not addressed] Sivuilla 2 ja 4 tekoäly ja ajanvarausassistentti kuitataan vain rajauksen ulkopuolisiksi ilman kantaa toteutustapaan.
  - [met] Kansilehdellä on heti suora tiivistelmä ehdotuksesta ja hinnasta ilman turhaa yritysesittelyä.
  - [not addressed] Sivulla 3 esitellään nopea aloituskartoitus ja aalloissa rakentaminen, mutta datakontrakteista tai tarkoista etukäteisspesifikaatioista ei puhuta mitään.
  - [met] Sivuilla 2 ja 3 kieltäydytään suoraan lupaamasta kaikkia lähteitä ja vaaditaan karsintaa ennen tekemistä.
  - [not addressed] Sivulla 4 mainitaan chat-työkalun viikkopäivitykset, mutta sisäisen tiimin perehdytyksen koulutusmuotoja ei käsitellä.
<!-- /replies:auto -->
