# 🏛️ CivicTriage AI: Governance Grievance Engine (Case 07)

> **AI Synergy Hackathon 2026 — Round 1 Submission**  
> **Theme:** 07: Governance (*One Complaint, Five Departments*)  
> **Core Focus:** Multi-Channel Semantic Intake, Cross-Departmental Triage, and Auditable Escalation Engine

---

## 📌 Problem Overview & Strategic Focus

Municipal grievance systems receive complaints via web portals, phone calls, social media, and walk-in desks. Ingesting noisy, code-mixed (Hindi, English, Hinglish) complaints often leads to severe inter-departmental misrouting[cite: 10]. 

Case evidence indicates that **23% of complaints are reassigned at least once**[cite: 10], causing long delays while citizens receive generic status labels like "in process"[cite: 10].

Instead of building a superficial conversational chatbot (Framing A)[cite: 10], **CivicTriage AI** targets the administrative bottleneck (Framing B)[cite: 10]. The platform converts raw multi-channel inputs into semantically deduplicated, multi-tagged, confidence-scored tickets with human-in-the-loop verification and an immutable audit log[cite: 10].

---

## 🚀 Key Features & Architectural Boundaries

1. **Multi-Channel & Multilingual Normalization (`schemas.py`):** Ingests raw text, voice transcripts, and photo assets, validating inputs against a strict JSON Schema[cite: 10].
2. **Multi-Label Departmental Routing (`router_poc.py`):** Evaluates multi-department overlap (e.g., PWD vs. Water Board) and assigns primary lead responsibility[cite: 10].
3. **Public Safety Urgency Scoring (`router_poc.py`):** Automatically detects safety hazards (e.g., exposed live wires, deep potholes, gas leaks) to prioritize high-risk tickets[cite: 10].
4. **Parent-Child Spatial Deduplication (`dedup_poc.py`):** Clusters duplicate neighborhood reports under a single Parent Issue ID without auto-closing secondary tickets[cite: 10].
5. **Strict Boundary Enforcement:** Enforces the mandatory boundary rule—AI never closes or rejects tickets autonomously[cite: 10]. Predictions with confidence `< 0.60` route to a manual human triage queue[cite: 10].

---

## 📂 Repository Structure

```text
gov-ai-triage/
├── docs/                             # Person B: Strategic Briefs & Synergy Logs
│   ├── 01_Problem_Justification.md   # Framing A vs. Framing B comparative analysis
│   ├── 02_Evidence_Matrix.md         # Tagged Case, External, Assumption, and Unknown data
│   ├── 03_Synergy_Decision_Trail.md # Index of human overrides on AI advice
│   ├── 04_AI_Log_Links.md            # Accessible links to raw AI interaction sessions
│   └── 05_SRS_Core.md                # Acceptance tests, safeguards, and V1 exclusions
│
├── schemas.py                        # Person A: Pydantic ingestion data validators
├── router_poc.py                     # Person A: Multi-label classification & urgency engine
├── dedup_poc.py                      # Person A: Semantic vector similarity clustering
├── test_schema.py                    # Schema validation test suite
├── ingestion_schema.json             # Formal JSON Schema standard draft
├── mock_data.json                    # Multi-channel Hinglish test dataset
├── requirements.txt                  # Python dependencies
└── README.md                         # Main submission documentation
