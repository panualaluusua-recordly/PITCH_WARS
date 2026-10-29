# Tech & architecture slides for the VR Group deck
_VR-Yhtymä Oyj (VR Group): Two slides for deck-writer to insert after the answer-first slide_

## 2. Every source gets a named extraction method, landing in your Data Vault without new tools
- We propose the extraction for all sources, as asked: one metadata-driven loading pattern on AWS, configured per source, not one script per feed.
- Business keys follow the railway terms your operations people already use, documented in Finnish.
[Rail sources: Passenger sales & ticketing, Freight orders & wagons, Traffic & timetable events, ERP] → [Extraction on AWS: CDC for operational databases, API / event feeds for traffic data, File drops for partners, Config per source in Git] → [Snowflake Raw Vault: Hubs on business keys, Links: train, wagon, order, Satellites keep full history] → [Business Vault & marts: Business rules in code, Marts for the BI tool, ERP-facing extracts]
(Q1: build and test in non-production only. Production releases in December and from April, each with a rollback)

## 3. Technical gates protect operations: nothing reaches production in Q1
| Gate | When | Pass criterion |
| --- | --- | --- |
| Extraction inventory | Week 2 | Every source has a method, owner and load frequency |
| First satellites live | Before 20 Dec | Row counts reconcile to source, no load errors for 5 days |
| Q1 release package | End of March | All Q1 work tested in non-production, release plan approved |
| April release | Agreed weekend window | Reconciliation green; rollback tested |

_Technical unknowns: source system access on AWS, change-data-capture support per database, the current Data Vault loader (we use yours if one exists). Snowflake makes Recordly's Virtual Data Engineer a possible add-on (see team/vde)._
