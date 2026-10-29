Buyer: yliopiston-apteekki | Decision to enable: which data setup to run next (including "keep what we have"), chosen without browser-side tracking and explained in plain Finnish ← "define a future-state architecture alongside clear technology recommendations"

Source note: the RFP does not mention tracking or Finnish. The knockout comes from the buyer bio ("hypersensitive to front-end browser telemetry"; Finnish operational documentation). Slide text quotes the RFP where it can and marks bio-sourced rows as "mitä kerroitte".

Method: inputs | criteria (weight) | options compared | evidence log
- Inputs: (1) one 45-min walk-through each of the ERP data flow, the BI tool and the online pharmacy data flow; (2) list of current data sources, reports and their users (one sheet, filled in together during the walk-throughs); (3) licence and contract list for ERP, BI and cloud (names, renewal dates); (4) one anonymised or synthetic data sample per flow for a small trial; (5) three 30-min interviews with pharmacy-side report users, in Finnish. No new tools: existing BI and cloud accounts, read-only.
- Knockout (pass/fail before any scoring): the option must not need scripts, pixels or tags in the browser. Data comes from servers and systems only. A failing option is dropped and the reason written down. We do not touch or remove existing tags; if we see any we only report them.
- Criteria and weights (0-4, only for options that pass the knockout):

| Criterion | Weight | Source | Why |
|---|---|---|---|
| Fits daily work without disruption | 30 | bio: "quick, painless implementations that keep daily operations quietly moving"; RFP: "modernize from our current data setup to better support retail and digital pharmacy services" | Her stated top priority |
| Data protection and traceability | 25 | bio: "regulatory scrutiny surrounding digital pharmacy tags" | Pharmacy data, regulator attention |
| Easy to run with the team she has | 20 | RFP: "clear technology recommendations"; bio: "still finding her footing with complex architecture" | A tool nobody can run is a bad recommendation |
| Licence impact and 3-year cost direction | 15 | RFP: "licensing impact" | RFP asks for it per option |
| Supports retail and online pharmacy needs | 10 | RFP: "omnichannel operations", "retail and digital pharmacy services" | Capability check, not a wish list |

  Rule: "keep current setup, tidied" (option A) must be beaten by at least 0.5 points of weighted score, with no knockout, before we recommend change. If it is not beaten, the recommendation is to keep it, with a short to-do list.
- Options compared: A Current setup, tidied. B Same cloud, one component added or swapped (named after week 2). C One larger change to a new target architecture. Tools are compared only inside B and C, only for the ERP, BI and cloud she already has; no market-wide vendor search.
- Evidence log: one Excel sheet in Finnish, rows = option x criterion, columns: score, one-sentence reason, source (who said it, which document, which trial result), date. Readable in 10 minutes. Knockout checks on a separate tab (yes/no and source). Glossary tab for every technical word used.

Plan: <week: activity, who from the buyer, output>
- Wk 1: scoping. 30-min start call, inventory of ERP, BI, cloud and online pharmacy flows from existing licences and read-only access. Buyer: Saara (~1 h) plus names of system owners. Output: one-page current-state map in Finnish, glossary v1.
- Wk 2: three 45-min walk-throughs, licence list. Buyer: system owners. Output: knockout list and criteria draft.
- Wk 3: Gate 1 (30 min): Saara approves criteria and weights before anything is scored. Output: signed-off criteria sheet.
- Wk 3-5: define three options, small trial on sample data per flow (no browser data), scoring. Workshop (60 min, Finnish) with Saara and two pharmacy-side users to check scores against real work. Output: scored option matrix.
- Wk 5-6: licence impact per option, 12-month plan, plain-Finnish decision memo. Decision meeting (90 min). Output: memo and plan.
- Saara's time about 2 h per week; a short written note replaces status meetings.

Deliverables:
- Current-state map, one page, Finnish
- Criteria sheet with weights and knockout, signed off at Gate 1
- Scored option matrix A/B/C with evidence per cell (Excel, Finnish)
- Licence impact per option: what stays, comes, goes; 3-year cost direction
- Target-state diagram of the recommended option (or of the tidied current setup)
- 12-month plan with owners and stop/go checks at months 3 and 6
- Plain-Finnish decision memo (2 pages) and glossary
- Day 30 (end of wk 4): current-state map, signed-off criteria, knockout results per option, first scores for A and B with reasons, trial results.

Effort basis: 18 person-days (not a price): current state 4, criteria and Gate 1 3, options and trial 6, recommendation, memo and decision meeting 5. Shrink path: trial on two flows instead of three (-1), option C only as a sketch (-2).

Unknowns and access needed:
- Which ERP, BI tool and public cloud are in use (not in RFP): named by Saara by end of wk 1; the option set depends on it.
- Whether tracking tags already exist on the online pharmacy site: we ask, do not scan, by wk 1; if they exist they are reported as a finding, removal is outside scope.
- Licence list with renewal dates by wk 2; without it licence impact is direction only.
- Sample data without personal data by wk 3; without it the trial becomes documentation checks and the scores are marked less certain.
- Two pharmacy users for one 60-min workshop in wk 4; without them the work-fit score rests on Saara's view alone.
- The two client references must match real Recordly cases (Ville's verify item).

Left out on purpose:
- Any build, migration or setup work
- Removing or changing existing browser tags
- AI features and new platform commitments
- Market-wide vendor search or demos
- Pharmacy process redesign
- English-language documents

--- Ready slide text (Finnish) ---

Otsikko: Näin valitsemme: yksi poissulkeva ehto ja viisi painotettua kriteeriä

Poissulkeva ehto: vaihtoehto ei saa vaatia selaimeen asennettavia skriptejä, pikseleitä tai tunnisteita. Tieto kerätään palvelimilta ja järjestelmistä.

| Kriteeri | Paino | Mistä se tulee |
|---|---|---|
| Sopii arkeen ilman häiriötä | 30 % | nopeat ja kivuttomat muutokset, jotka eivät häiritse apteekkien arkea (mitä kerroitte) |
| Tietosuoja ja jäljitettävyys | 25 % | digiapteekin tunnisteet viranomaistarkastelussa (mitä kerroitte) |
| Helppo ylläpitää nykyisellä tiimillä | 20 % | "clear technology recommendations" |
| Lisenssivaikutus ja 3 vuoden kustannussuunta | 15 % | "licensing impact" |
| Tukee apteekki- ja verkkoapteekkitarpeita | 10 % | "retail and digital pharmacy services" |

Vaihtoehdot: A nykyinen siistittynä, B yksi komponentti lisätään tai vaihdetaan, C suurempi muutos. "Pidä nykyinen" voittaa, ellei muutos ole selvästi parempi (vähintään 0,5 pistettä). Kriteerit hyväksytetään teillä portilla 1 ennen pisteytystä. Jokaisen pisteen perustelu ja lähde on Excel-taulukossa suomeksi.

Otsikko: Mitä saatte

- Nykytilakartta (1 sivu)
- Hyväksytyt kriteerit ja poissulkevan ehdon tarkistus
- Pisteytetty vaihtoehtovertailu perusteluineen
- Lisenssivaikutus vaihtoehdoittain
- Tavoitearkkitehtuurikuva
- 12 kk:n suunnitelma vastuineen ja tarkistuspisteineen
- Päätösmuistio selkokielellä ja sanasto
- Päivänä 30: nykytilakartta, hyväksytyt kriteerit, poissulkevan ehdon tulokset ja ensimmäiset pisteet
