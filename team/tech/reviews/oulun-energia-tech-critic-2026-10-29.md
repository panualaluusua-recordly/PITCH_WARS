# Tech critic: oulun-energia v1 (2026-10-29)
Scope: tech only. Price, terms, names and storyline not judged. Deck: team/decks/oulun-energia/oulun-energia-internal-rag-document-and-policy-assistant-v1.md

Tech verdict: strong (lower end). Every RFP ask has a slide: Finnish -> s4, cost spike -> s3, Q1 freeze -> s5, integration -> s2, unknowns -> s6.

## Top 3 fixes
1. Slides 2 and 5, visuals. The architecture is a 6-row table and the freeze is a table row. A buyer cannot see the flow or the freeze at a glance.
   Change: draw slide 2 as a left-to-right flow (sources -> extract/chunk with change detection -> index -> permission-filtered retrieval -> cited answer -> chat tool). Put a cost-guardrail band under it and an evaluation loop above it.
   Change slide 5: add a timeline strip with a shaded block "Q1-jäädytys: ei tuotantomuutoksia" and the Phase 0/1 build windows before it.
   Evidence: "must integrate smoothly with a public cloud, our chat tool, and its current data setup"; "strict change restrictions during the critical Q1 winter heating peak".
2. Slide 5, schedule realism. Today is 2026-10-29 and Q1 is about 2 months away. The deck gives no dates or weeks, so the buyer cannot tell whether a pilot lands before the freeze.
   Paste: "Vaihe 0 viikot 1-2, pilottiviipale ei-tuotannossa ennen Q1:tä; tuotantoikkuna ennen jäädytystä vain, jos Go/no-go täyttyy; muuten tuotantopilotti jäädytyksen jälkeen."
   Evidence: "critical Q1 winter heating peak".
3. Slides 1 and 4, "nopeat" has no measure. "Rapid" is an ask and the deck only measures quality. Add a latency line to the metrics on slide 4:
   "Vastausaika (mediaani ja p95) mitataan pilotissa chat-työkalussa; tavoite sovitaan lähtötason jälkeen." Also state what the hard stop on slide 3 halts: "Kova pysäytys pysäyttää vain päivitysajon; kysymyksiin vastaaminen jatkuu."
   Evidence: "rapid, reliable answers"; "surprise billing spikes when automated vector refresh jobs ran unchecked".

## Already good
- No stack names invented (T6). Cloud, chat tool and BI are all "your".
- Incremental refresh, per-run and monthly cap, alert, hard stop and kill switch, plus the other cost levers (embeddings, index size, tokens).
- Finnish quality is measured on their own documents, with a gate agreed after the baseline (P13). It does not promise "zero errors".
- Citation with version and date, refusal on weak evidence, owner routing, wrong-answer button (T5).
- Source permissions at retrieval, with a fallback of one open collection (T7). Pilot slice, then waves (P4).
- No AI extras. Phase 0 go/no-go. Honest unknowns table. Time-boxed reviewers.

## Overstated claims (stack)
- Slide 2 "Kaikki osat ajetaan teidän tenantissanne": the buyer only said "a public cloud". A managed model API may not run inside their tenant, and the cloud and region are unknown (slide 6 says so).
  Soften to: "Kaikki osat ajetaan teidän tenantissanne tai sen sallimalla alueella; mallikäyttö vahvistetaan vaiheessa 0."
- Slide 3 "raportoidaan BI-työkalussanne": the bio mentions a BI tool for operational metrics, not for cost reporting. Add "jos BI-työkalu soveltuu; muuten pilven kustannusnäkymä".
- Slide 1 "omassa pilvessänne ja chat-työkalussanne" assumes the chat tool accepts custom bots. Slide 6 asks this, so say "jos työkalu sallii omat botit" or keep a fallback.

## Missing technical answers
- Swedish and English document content (language scope) is not addressed. It sits only in the analysis doc, not on a slide.
- Query-log retention is listed as an unknown. No default is proposed.
