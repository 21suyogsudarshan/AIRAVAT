# 📊 Presentation Deck Outline: CivicTriage AI (Case 07)

## Slide 1: Title & Team Introduction
- **Title:** CivicTriage AI: Cross-Departmental Grievance Intake & Auditable Escalation Engine[cite: 10]
- **Subtitle:** Resolving Inter-Departmental Misrouting in Municipal Governance[cite: 10]
- **Event:** AI Synergy Case Challenge 2026 — Round 1[cite: 1]
- **Team Structure:** 2-Person Engineering & Strategy Team[cite: 2]

---

## Slide 2: Case Investigation & Stakeholder Map
- **Situation:** Municipal ecosystem receiving high-volume multi-channel complaints (Web, Phone, WhatsApp, Walk-in) in Hindi, English, and Hinglish[cite: 10].
- **Key Signal:** 23% of complaints are reassigned at least once, causing long delays while citizens receive generic "in process" updates[cite: 10].
- **Stakeholder Pain Points:**
  - *Citizens:* Lack of plain-language progress visibility[cite: 10].
  - *Triage Staff:* Time wasted manually reading, translating, and forwarding misrouted tickets[cite: 10].
  - *Department Heads:* Blame-shifting and ping-pong reassignments between overlapping domains (e.g., PWD vs Water Board)[cite: 10].

---

## Slide 3: Divergent Problem Framings (Why Framing B Won)
- **Framing A (Rejected): Citizen Conversational Chatbot & Status Portal**[cite: 10]
  - *Why Rejected:* Addresses a superficial symptom (vague status labels) without fixing backend inter-departmental routing delays[cite: 10].
- **Framing B (Selected): Semantic Intake, Auditable Triage, and Urgency Engine**[cite: 10]
  - *Why Selected:* Targets root-cause administrative churn[cite: 10]. Converts raw multi-channel inputs into semantically deduplicated, multi-tagged, confidence-scored tickets with human-in-the-loop sign-off[cite: 10].

---

## Slide 4: Evidence Tagging Matrix
- **`[CASE EVIDENCE]`:** 23% reassignment rate[cite: 10]; 4 intake channels[cite: 10]; generic "in process" status labels[cite: 10].
- **`[EXTERNAL EVIDENCE]`:** CPGRAMS central public grievance guidelines setting 21-day disposal benchmarks.
- **`[ASSUMPTION]`:** Municipal officers will accept AI suggestions if keyword triggers and confidence scores are transparently displayed[cite: 3, 10].
- **`[UNKNOWN]`:** Exact duplicate count across separate municipal databases[cite: 3, 10].

---

## Slide 5: System Architecture & Workflow
- **Pipeline:** `Multi-Channel Intake` $\rightarrow$ `Pydantic Schema Validation` $\rightarrow$ `Multilingual Parsing` $\rightarrow$ `Spatial Deduplication Clustering` $\rightarrow$ `Multi-Label Scoring & Safety Urgency` $\rightarrow$ `Human Triage UI` $\rightarrow$ `Immutable Audit Log`[cite: 10].
- **Technical Proof:** Working Python prototype (`schemas.py`, `router_poc.py`, `dedup_poc.py`, `app.py`) committed on GitHub[cite: 2].

---

## Slide 6: Human-AI Responsibility & Boundary Enforcement
- **AI Responsibilities:** Translates Hinglish text, clusters duplicate reports under Parent Issue IDs, calculates multi-department confidence scores, and flags public safety risks[cite: 10].
- **Human Responsibilities:** Confirms or overrides suggested routing, validates parent-child ticket groupings, and signs off on resolution stages[cite: 10].
- **Strict Boundary Rule:** AI **never** closes or rejects complaints autonomously[cite: 10]. Confidence scores `<0.60` trigger an automatic route to a manual human review queue[cite: 10].

---

## Slide 7: Quantifiable Acceptance Metrics & V1 Scope Exclusions
- **Acceptance Targets:**
  - Routing Accuracy: $\ge 85\%$ correct primary department recommendations on benchmark datasets[cite: 10].
  - Deduplication Precision: $\ge 80\%$ precision in clustering ward-level duplicates[cite: 10].
  - Audit Log Latency: $<500\text{ ms}$ for recording human officer overrides[cite: 10].
- **Explicit V1 Non-Goals:** No autonomous complaint rejections[cite: 10, 11]; no field worker dispatch automation[cite: 11]; no social media scraping[cite: 4, 11].

---

## Slide 8: Human-AI Synergy Decision Trail
- **Decision 1 (Duplicate Closing):** REJECTED AI advice to auto-close secondary tickets; implemented Parent-Child clustering with mandatory officer sign-off[cite: 10].
- **Decision 2 (Language Pipeline):** MODIFIED AI advice to translate Hinglish to English first; adopted direct code-mixed keyword parsing to preserve local context[cite: 10].
- **Decision 3 (Urgency Scoring):** REJECTED AI sentiment analysis proposal; implemented a safety hazard keyword matrix to prevent emotional complaints from burying real physical hazards[cite: 10].
