# 🏗️ CivicTriage AI: System Architecture Diagram

```mermaid
graph TD
    %% Ingestion Layer
    subgraph INGESTION [1. Multi-Channel Ingestion Layer]
        A1[Web Portal] --> B
        A2[Phone Calls or Voice] --> B
        A3[WhatsApp or Social] --> B
        A4[Walk-in Desk] --> B
    end

    %% Validation & Processing
    subgraph PIPELINE [2. Parsing and Validation Pipeline]
        B[JSON Schema Validation - schemas.py] --> C[Code-Mixed Hinglish Normalization]
        C --> D[Spatial Vector Clustering - dedup_poc.py]
    end

    %% AI Logic Layer
    subgraph AI_ENGINE [3. AI Triage and Urgency Engine]
        D --> E1[Multi-Label Dept Classifier - router_poc.py]
        D --> E2[Public Safety Urgency Scoring - router_poc.py]
    end

    %% Boundary & Human Review
    subgraph BOUNDARY [4. Human-in-the-Loop Safeguard Layer]
        E1 --> F{Confidence Above 0.60?}
        F -- Yes --> G[Municipal Officer Dashboard - app.py]
        F -- No --> H[General Manual Review Queue]
        E2 --> G
    end

    %% Action & Audit
    subgraph AUDIT [5. Resolution and Audit Layer]
        G -- Officer Confirm or Override --> I[(Immutable Audit Log)]
        I --> J[Plain-Language Citizen Update Feed]
    end