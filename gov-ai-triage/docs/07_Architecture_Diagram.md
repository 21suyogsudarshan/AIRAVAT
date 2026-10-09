# 🏗️ CivicTriage AI: System Architecture Diagram

```mermaid
graph TD
    %% Ingestion Layer
    subgraph INGESTION ["1. Multi-Channel Ingestion Layer"]
        A1[Web Portal] --> B
        A2[Phone Calls / Voice] --> B
        A3[WhatsApp / Social] --> B
        A4[Walk-in Desk] --> B
    end

    %% Validation & Processing
    subgraph PIPELINE ["2. Parsing & Validation Pipeline"]
        B[JSON Schema Validation<br/>`schemas.py`] --> C[Code-Mixed Hinglish<br/>Normalization]
        C --> D[Spatial Vector Clustering<br/>`dedup_poc.py`]
    end

    %% AI Logic Layer
    subgraph AI_ENGINE ["3. AI Triage & Urgency Engine"]
        D --> E1[Multi-Label Dept Classifier<br/>`router_poc.py`]
        D --> E2[Public Safety Urgency Scoring<br/>`router_poc.py`]
    end

    %% Boundary & Human Review
    subgraph BOUNDARY ["4. Human-in-the-Loop Safeguard Layer"]
        E1 --> F{Confidence >= 0.60?}
        F -- Yes --> G[Municipal Officer Dashboard<br/>`app.py`]
        F -- No --> H[General Manual Review Queue]
        E2 --> G
    end

    %% Action & Audit
    subgraph AUDIT ["5. Resolution & Audit Layer"]
        G -- Officer Confirm / Override --> I[(Immutable Audit Log)]
        I --> J[Plain-Language Citizen Update Feed]