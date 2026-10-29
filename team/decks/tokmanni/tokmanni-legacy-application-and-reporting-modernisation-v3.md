# Modernise legacy tools and reporting without disturbing store operations, with margin data locked to the right roles
_Tokmanni Group Oyj: Recordly proposal, 29 October 2026_

## 2. In 5 months we replace legacy tools and reports for €92,000 fixed, with zero new licences
- **Outcome measured in your ledger, not in hypothetical hours:** named legacy tools and reports switched off, and their running costs removed (target list agreed in month 1)
- **Margin data protected by design:** row- and role-level security on by default; margin figures visible only to roles your business owners approve; access tested before every go-live
- **Stable daily operations:** releases outside store peak hours and campaign weeks, parallel running, tested rollback per app
- **Team that works your way:** Finnish-speaking, on site in Mäntsälä 2 days per week, follows your central office routines
- **Builds on what you have:** your BI tool, public cloud and ERP programme; no new licences; the target stack is confirmed with you in phase 1
- **€92,000 fixed** in 3 phases with go/no-go gates; you can stop after phase 1

## 3. Margin figures stay with the people entitled to them: access is closed by default and tested
- **Deny by default:** a new report or app shows nothing until a role grants it. Margin and purchase-price columns are classed as sensitive and hidden unless the role allows them.
- Access rules live in code, and an automated test runs on every release: "store supervisor cannot see department margin" fails the release if broken.
[Sources: ERP (under development), Legacy functional apps, Store & logistics data FI / SE / DK] → [Integration layer: Stable data contracts per ERP object, ERP changes absorbed here, not in reports, Daily reconciliation] → [Data platform (public cloud): Conformed model: store, department, country, Sensitive-column tagging (margin, cost), Version-controlled, in Tokmanni's tenant] → [BI & apps: Row-level security: store / region / dept, Column-level security on margins, Access tests in CI + quarterly review]
(Access maps to your BI tool's native roles; without column-level security, margins are masked in the data layer · apps replaced one at a time, tested rollback)

_Deliverables: D1 inventory (keep / migrate / retire) · D2 role matrix signed by business, security tests in CI · D3 governed data layer, ERP interfaces via data contracts · D4 priority reports FI/SE/DK · D5 functional apps only where they remove cost · D6 Finnish runbooks and training._

## 4. Three gated phases fit around retail seasons
| Phase | Timing | Content | Gate |
| --- | --- | --- | --- |
| 1. Discovery & access model | Nov–Dec 2026 (6 wks) | Inventory, role matrix, ledger-cost baseline per tool, data-access probe on 3 priority tools, go/no-go risk report | You approve the list and access model |
| 2. Build wave 1 | Jan–Feb 2027 | Data layer, priority reports, access tests, parallel run | Supervisor pilot in agreed stores; access tests pass; retirement targets set against each tool's baseline |
| 3. Build wave 2 & retire | Mar–Apr 2027 | Functional apps, remaining reports, switch-off, handover | Legacy tools switched off, ledger lines removed |

_No go-lives during Christmas season or major campaign weeks; freeze calendar agreed with store operations in phase 1._

## 5. A proposed team with certificates you can verify before signing
- Replacement at your request: equal seniority within 10 working days, 2-week overlap at our cost
- You may recruit our consultants after 12 months, with no fee
- Written update every second week and a monthly steering; decisions logged, no extra status meetings
| Name | Role | Allocation | Certifications |
| --- | --- | --- | --- |
| Panu Alaluusua | Engagement lead, Mäntsälä on site | 40% | Microsoft Certified: Azure Data Engineer Associate |
| Aino Virtanen | Lead data engineer | 100% | Databricks Data Engineer Professional, Azure Data Engineer Associate |
| Sara Lindholm | BI & security developer (Swedish too) | 80% | Microsoft PL-300 Power BI Data Analyst, SC-900 |

_All certificates verifiable via Microsoft/Databricks credential links, provided with the contract. Planned availability from 16 November 2026, confirmed in writing at signature. References (contact persons on request): (1) Finnish retail chain, store reporting modernisation with role-based margin security, 40 legacy reports retired; (2) Finnish wholesale & logistics company, legacy Access/Excel tools replaced by cloud apps, running costs cut by €60k/year._

## 6. Price €92,000 fixed, no licence costs, paid at milestones
- Technical unknowns, each confirmed in phase 1: BI tool column-security support, ERP interface maturity, number of legacy tools and access to their code. Scope is re-confirmed at the gate.
| Phase | Price | Payment |
| --- | --- | --- |
| 1. Discovery & access model | €18,000 | At phase 1 sign-off |
| 2. Build wave 1 | €40,000 | At wave 1 acceptance |
| 3. Build wave 2 & retire | €34,000 | At final acceptance |
| **Total** | **€92,000** fixed, excl. VAT | Net 30 days; 10% of each milestone held until acceptance |
| Licence costs | €0 from Recordly | Uses your existing BI and cloud licences; cloud usage estimate given in phase 1 |

_Risks and assumptions: ERP schedule changes may move phase 3 interfaces (handled by change request, no surprise invoices); access to current data setup and a business owner per area about half a day per week; Sweden/Denmark specific reports included where data is in the current setup. Your standard contract terms accepted._
