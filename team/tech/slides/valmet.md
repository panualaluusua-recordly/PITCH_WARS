# Tech & architecture slides for the Valmet deck
_Valmet Oyj: Two slides for deck-writer to insert after the answer-first slide_

## 2. Mill telemetry is summarised at the edge, so satellite links are never saturated
- Raw telemetry stays at the mill. Only aggregates and changes travel, under a bandwidth cap, and bulk backfills run off-peak.
- Infor CloudSuite and operational data land in Snowflake through the same monitored ingestion pattern.
[Mill (edge): Local collector per site, Aggregate + compress (e.g. 1-min stats, deltas), Store-and-forward buffer] → [Constrained link: Bandwidth cap per site, Priority: operations first, Off-peak backfill window] → [Central ingestion: Infor CloudSuite via ION / Data Lake, Incremental loads, schema checks, Pipeline monitoring & alerts] → [Snowflake (EU region): Raw → modelled → reporting, Customer-managed keys, BI tool on certified tables]
(Rollout one mill at a time: link usage is measured before and after, and the next site starts only if operations saw no impact)

## 3. We reduce foreign-jurisdiction exposure honestly: what can be controlled, and what cannot
| Measure | What it does | Limit we state openly |
| --- | --- | --- |
| EU-region Snowflake account | Data stored and processed in the EU | Provider is US-headquartered |
| Customer-managed keys (Tri-Secret Secure) | Valmet can revoke access to the data | Needs Business Critical edition |
| Private connectivity, data minimisation | Only data needed for reporting leaves the mills | Design choice per data set |
| Open table format (Iceberg) for core data | Exit path to another platform | Migration effort if ever used |

_Technical unknowns: link capacity per mill, Infor API limits, which data sets legal classifies as sensitive. Certifications on the proposed engineer: SnowPro Core and SnowPro Advanced: Data Engineer._
