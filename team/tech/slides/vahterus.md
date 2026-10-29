# Tech & architecture slides for the Vahterus deck
_Vahterus Oy: Two slides for deck-writer to insert after the answer-first slide_

## 2. Reports move to the cloud behind stable data contracts, so the new ERP rollout does not break them
- Today's data setup and the new ERP feed one integration layer with a contract per business object. Dashboards read a modelled reporting layer in the public cloud, not the ERP directly.
- Legacy applications are replaced one at a time, in parallel until proven.
[Sources: Current data setup, Legacy functional apps, New ERP (rolling out)] → [Integration layer: Data contract per object, ERP changes absorbed here, Daily reconciliation] → [Cloud data platform: Modelled reporting layer, Version-controlled in your repo, Every commit linked to a backlog item] → [BI tool: Modernised dashboards, Benefit per dashboard tracked, Legacy report switched off]
(Q1: build and test only, no production change. Go-live from April with rollback)

## 3. We modernise in ROI order, and you can trace every commit to its benefit
| Candidate | Action | Benefit measure | Timing |
| --- | --- | --- | --- |
| Highest-cost legacy app | Replace | Licence and support cost removed | Build Q1, live April |
| Production reports | Rebuild on the reporting layer | Hours saved per month | Build Q1, live April |
| Low-use reports | Retire | Maintenance removed | After discovery |
| ERP interfaces | Contract per object | Breakages avoided | With the ERP plan |

_Technical unknowns: new ERP timeline and APIs, the target public cloud, current data volumes. The ranking comes from the discovery you have already held with us._
