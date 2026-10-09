# Case 07 Evidence Classification Matrix

| Category | Evidence Point | Citation / Source | Solution Design Impact |
| :--- | :--- | :--- | :--- |
| **`[CASE EVIDENCE]`** | 23% of sampled grievances were reassigned at least once[cite: 10]. | Case File Page 10[cite: 10] | Requires multi-label department scoring in `router_poc.py`[cite: 10]. |
| **`[CASE EVIDENCE]`** | Complaints arrive via 4 channels in English, Hindi, and Hinglish[cite: 10]. | Case File Page 10[cite: 10] | Governs schema fields in `schemas.py` and `ingestion_schema.json`[cite: 10]. |
| **`[CASE EVIDENCE]`** | Generic "in process" status labels cause citizen frustration[cite: 10]. | Case File Page 10[cite: 10] | System generates specific milestone summaries when stage changes[cite: 10]. |
| **`[EXTERNAL EVIDENCE]`** | Central CPGRAMS guidelines mandate a 21-day disposal SLA benchmark. | DARPG Public Guidelines | Urgency engine prioritizes tickets approaching SLA limits. |
| **`[ASSUMPTION]`** | Officers will trust AI recommendations if keyword triggers are shown[cite: 3, 10]. | Team Hypothesis | Triage UI displays keyword feature attribution[cite: 10]. |
| **`[UNKNOWN]`** | Exact duplicate count across separate municipal databases[cite: 3, 10]. | Case File Page 10[cite: 10] | Requires global spatial deduplication in `dedup_poc.py`[cite: 10]. |