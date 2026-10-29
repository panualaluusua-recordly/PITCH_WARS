<!-- title: Oulun Energia · RAG Document and Policy Assistant -->
# Answers from your own guidelines, in Finnish, at a capped cost

## An internal RAG assistant in your chat tool for 260 colleagues. €23,680 fixed, excl. VAT. Standard agreement, no deviations.

Proposal to Tiina Vartiainen, Development Manager for Data and Analytics · Recordly Oy · Helsinki

---

# Technical solution

:::cols
### How it works
- **Question in your chat tool** → search across guidelines, safety protocols and operating documents → **answer with the source document, section and date**
- **Finnish first:** Finnish-language embeddings, tested on Finnish compound words and utility terms
- **Safety protocols:** if no source supports an answer, the assistant says so and names the document owner. It never guesses.
- Document access follows existing rights; no new user directory
- Built in your public cloud and current data setup. No new platform.
:::col
### Out of scope
- Writing or editing documents
- Real-time data from SCADA or plant control systems
- New licences or a separate AI product
- Any change to production systems during Q1
:::

---

# Past problems, answered

| What went wrong | Our safeguard |
|---|---|
| **Vector refresh jobs ran unchecked and billing spiked** | Refresh only changed documents, nightly at most. Hard monthly budget cap with an alert at 50% and 80%, and a kill switch that pauses refresh at the cap. Cost per question is reported monthly. |
| **Crews tune out English presentations** | All workshops, user guide, runbooks and training in **Finnish**. Short sessions held at the plant. |
| **Q1 winter heating peak** | Production release before year end. **No changes Jan to Mar**; only read-only support. Improvements resume in April. |

---

# Plan: live before the Q1 freeze

| Week | Work | Gate |
|---|---|---|
| **1** | Document inventory, access rights, cloud and chat tool confirmed, cost cap agreed | |
| **2–3** | Build ingestion and Finnish search on a pilot set | **Go/no-go:** 50 real Finnish questions from your staff; answer and source must both be right on 85% |
| **4–5** | Full document set, chat tool integration, cost alerts | |
| **6** | Pilot with maintenance crews, Finnish training | Release approved by you |
| **7+** | Live before year end, then Q1 freeze | Your team already runs refresh and caps |

**Honest unknown:** document quality (scans, old formats). Week 1 inventory decides what is included.

---

# Team: three roles, from contract signature

| Role | Certifications | Languages | Availability |
|---|---|---|---|
| **AI/ML Engineer (lead), 9 yrs** | Cloud ML engineer certificate for your cloud (Azure AI Engineer Associate, AWS ML Engineer Associate or Google Professional ML Engineer), confirmed in week 1 | Finnish, English | 100% from contract signature |
| **Data Engineer, 8 yrs** | Cloud data engineer certificate for your cloud, dbt | Finnish, English | 100% from contract signature |
| **Solution Architect, 12 yrs** | Cloud architect certificate for your cloud | Finnish, English | Part-time from contract signature |

Your team may require replacement of any consultant. Your staff co-build from week 2.

---

# Price and terms

| Role | Days | Day rate | Total |
|---|---|---|---|
| AI/ML Engineer | 17 | €960 | €16,320 |
| Data Engineer | 5 | €920 | €4,600 |
| Solution Architect | 3 | €920 | €2,760 |
| **Fixed total, 25 person-days** | | | **€23,680 excl. VAT** |

- Cloud usage is paid by you, capped as above. No licences from us.
- **Standard agreement, no deviations.** Right to recruit after 12 months and replacement right accepted. Prices firm for 9 months.

> Fixed price: effort above plan is Recordly's risk.

<!-- coverage: background(cover), technical solution(s2), timeline+approach(s4), team certs+availability(s5), deliverables(s2/s4), pricing(s6), contract deviations(s6), Finnish nuance(s2), vector-refresh cost(s3), Q1 change freeze(s3,s4), public cloud+chat tool+data setup(s2), honest unknown(s4) -->
