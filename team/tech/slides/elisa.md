# Tech & architecture slides for the Elisa deck
_Elisa Oyj: Two slides for deck-writer: the architecture slide replaces the tier table on the solution slide, the gates slide goes right after it_

## 2. Real-time where a domain needs it, on your own Google Cloud stack. Literal zero-batch is not achievable for reconciled finance
- **Freshness per domain, not one rule:** each domain gets the slowest tier that still meets its tested need. Target ranges per tier are agreed at Gate 1, after we measure current freshness.
- **Why not literally everything real-time:** finance close reconciles daily, and streaming all data raises run cost, failure surface and the retention exposure of traffic data. Option C, all real-time as written, is scored with its cost so the committee decides.
- **Existing services first:** Pub/Sub and change capture are proposed Google Cloud options, not assumed to be in your stack today. No new licence, no AI or ML, no new platform unless a tested need fails.
[Your sources: Network and operational events, ERP (vendor and change capture confirmed in sprint), Other transactional sources, listed in sprint] → [Freshness tier: Streaming, seconds: Pub/Sub to BigQuery Storage Write API (proposed), Change capture, minutes: if the ERP supports it; otherwise API polling, Micro-batch: Cloud Composer incremental loads, Daily: Composer, reconciled finance] → [BigQuery: Raw, as received, Curated and joined, Marts per domain] → [Serving: Looker on live BigQuery, Power BI: DirectQuery or import, mode assessed per tier]
(DAGs and CI/CD in your repos · same IAM and policy tags in Looker and Power BI · cost per tier · we read metadata only; no subscriber rows leave your GCP project)

## 3. Technical gates: nothing is locked before it is measured
| Gate | When | Passes when |
| --- | --- | --- |
| Access ready | Before sprint day 1 | NDA and secrecy undertaking signed; read-only Elisa-issued roles on BigQuery, Composer and Looker metadata and logs; no subscriber rows leave your GCP project; a sandbox dataset for the latency test |
| Gate 1 | End of week 2 | Each priority domain (3 to 5) has an owner, a stated freshness need and current freshness measured from logs; one real feed run Pub/Sub to BigQuery to Looker, end-to-end latency measured; ERP named with its change-capture options; target range per tier agreed |
| Checkpoint B | Week 8 | Options A tuned, B tiered, C all real-time scored on latency, cost and quota per tier, Composer load, failure mode and effort; every score cites a measurement or is marked 'not tested' |
| Final | Week 10 | Target architecture and roadmap accepted by the steering committee; anything untested marked 'not tested' |

_Unknowns and how each is settled: which ERP and its change capture (sprint; without CDC, API polling or micro-batch at an interval set at Gate 1) · Power BI connectivity (import refreshes on a schedule; DirectQuery freshness is bounded by query load, limits and cost; measured per report in the sprint) · real freshness need per domain (owners answer in your chat tool by week 2) · where Composer code, CI/CD and access policies live (recorded in the sprint; existing pipelines stay unless a test fails)._

---

## Rationale (solution-architect, 2026-10-29)

- **Patterns applied:** P10 honest latency (tiers, "slowest tier that meets the tested need", option C priced so the committee sees the cost of literal all-real-time; fingrid praised exactly this), P4 small scoping sprint before milestones lock, P7 existing services first (Pub/Sub and CDC labelled "proposed"), P3 ERP probed in the sprint, P5 same IAM/policy tags across Looker and Power BI (assessment criterion only), P6 where DAG code and CI/CD live is recorded, not built.
- **Tech-critic fixes (team/tech/reviews/ville-drafts-tech-review.md, elisa):** #1 honest "not literally zero-batch" title; #2 measured proof (latency test on one real feed in the sprint, as in v3, plus current freshness from logs); #3 Power BI connectivity mode named as a risk instead of assumed live (plus the v3 review point: DirectQuery freshness bounded by query load, measured per report); #4 cost and quota per tier, failure mode in Checkpoint B; #5 ERP named at Gate 1, fallback stated.
- **Tech-analyst notes:** "proposed" labels (n2), Power BI import vs DirectQuery (n3), target ranges agreed at Gate 1 instead of illustrative numbers (n5), access/lineage criteria and what happens to existing Composer pipelines (n6), ERP identity and BI mode as unknowns (n8).
- **Compliance input (work/compliance/elisa.md):** read-only Elisa-issued roles, metadata only, no subscriber rows leave the GCP project, NDA and secrecy undertaking before sprint day 1; retention exposure of traffic data as a reason not to stream everything.
- **Assessment input (work/assessment/elisa.md):** options A/B/C, measured freshness on 3 to 5 domains, "not tested" marking.
- **Effort basis:** unchanged from the deck (sprint 4, A 6, B 7, C 5 person-days). The one-feed latency test sits in the 4-day sprint (kept from v3); it needs a sandbox dataset and a feed Elisa can point at it, otherwise the sprint is the variable phase. Not a price.
- **Left out on purpose:** AI/ML, new platforms or licences, any build or migration, Data Vault, EU sovereignty, FinOps tooling, naming an ERP or a CDC product.
- **Used in:** team/decks/elisa/elisa-data-platform-architecture-and-tool-selection-as-v4.md, slides 3 (architecture, replaces the v3 tier table) and 4 (gates). Built on v3 (commit 2c89941, another session), keeping its fixes; v3 itself left unchanged.
