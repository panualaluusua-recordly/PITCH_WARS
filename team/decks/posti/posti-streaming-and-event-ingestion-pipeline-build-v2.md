<!-- title: Posti Group · Real-Time Event Ingestion Pipeline -->
# Event ingestion that starts in one hub and stays with you through peak season

## AWS and Azure into Databricks Lakehouse and Lakebase, rolled out hub by hub, with Recordly on the bridge through your first peak. €43,240 fixed excl. VAT. Standard terms.

Proposal to Sanni Vainio, Head of Data Platforms · Recordly Oy · Helsinki

---

# Solution: contained rollout, no tracking message lost

:::cols
### Architecture
- **Brokers on AWS and Azure into Databricks Lakehouse** (Structured Streaming), current state to **Lakebase** for operational lookups. No extra external tools.
- **No message into the void:** idempotent writes, replay from offsets, dead-letter queue, lag and gap alerts per hub
- **SAP S/4HANA integration readiness:** event contracts and keys agreed; build of SAP interfaces excluded
- BI-ready tracking tables for your BI tool
:::col
### Out of scope
- No big-bang across all hubs
- No new platforms or licences
- No AI/ML features
- Real-time is for tracking events only. Where finance or reporting needs batch truth, batch stays.
:::

---

# Blast radius: one hub first, rollback at every step

| Step | Scope | Gate before widening |
|---|---|---|
| **Shadow** | One pilot hub, new pipeline runs **beside** the current one; nothing depends on it | Event counts match 100% for 2 weeks |
| **Pilot** | Pilot hub live, kill switch back to current flow | Chaos test passed |
| **Wave 2** | 2–3 hubs | Lag and loss alerts quiet for 2 weeks |
| **Wave 3** | Remaining hubs, in groups of your choosing | Your approval per group |

**Kept from our earlier outline:** chaos tests and simulated broker dropouts in every gate (cross-cloud network failure, broker restart, duplicate storms). Honest unknown: real hub event volumes. Pilot-hub profiling in week 2 sets sizing before anything is built.

---

# Plan and peak-season support: we do not leave at handover

| Phase | Weeks | What |
|---|---|---|
| Design and sizing | 1–2 | Architecture, volume profiling, event contracts |
| Build, pilot hub | 3–7 | Pipeline, replay, alerting, chaos tests, shadow run |
| Waves 2–3 | 8–12 | Hub-by-hub rollout, Finnish runbooks |
| **Peak-season support** | First peak after go-live | **8 reserved days:** stand-by and war-room with your platform team, tuning, incident reviews |

Your platform engineers pair with us from week 1, so that at peak they run it and we stand shoulder to shoulder with them. Peak dates are fixed at gate 2. Honest limit: not a 24/7 operations desk.

---

# Team and references

| | Senior Data Architect (lead) | Senior Data Engineer |
|---|---|---|
| **Certifications** | Databricks Data Engineer Professional · AWS Certified Data Engineer Associate | Azure Data Engineer Associate · Databricks Data Engineer Associate |
| **Experience** | 12 years; streaming and event pipelines | 9 years; Spark streaming, CI/CD, monitoring |
| **Languages, availability** | Finnish, English · from contract signature | Finnish, English · from contract signature |

| Reference (last 3 years, anonymised) | Relevance |
|---|---|
| Nordic logistics operator, 2025 | Event streaming into Databricks |
| Nordic retailer, 2025 | Cross-cloud ingestion, replay and monitoring |
| Finnish industrial company, 2024 | Real-time data to lakehouse, SAP source |

Contact persons provided to Posti on request and to shortlisted bidders.

---

# Price and terms

| Role | Person-days | Day rate | Amount |
|---|---|---|---|
| Senior Data Architect | 9 | €920 | €8,280 |
| Senior Data Engineer, build | 30 | €920 | €27,600 |
| Senior Data Engineer, peak-season support | 8 | €920 | €7,360 |
| **Fixed total, excl. VAT** | **47** | | **€43,240** |

- Invoiced per phase; support days invoiced after the peak window. Effort above plan is Recordly's risk.
- Included: travel, documentation in Finnish. No licences.
- **No contractual deviations.** Your standard terms accepted as written.

<!-- coverage: RFP: architecture (s2), delivery plan (s4), team certs+availability (s5), pricing (s6), 3 references (s5 anonymised, contacts to shortlisted), AWS+Azure->Databricks Lakehouse+Lakebase (s2), SAP readiness (s2), BI (s2). Feedback: all-hubs fear -> s3; peak-season hypercare -> s4,s6; chaos testing kept -> s3; Finnish crew. Earlier price complaint on teammate v1 -> price 43k. No VDE (Databricks). -->
