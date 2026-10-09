# Software Requirements Specification (SRS) Core

## 1. Quantifiable Acceptance Tests
1. **Routing Accuracy Test:** System achieves $\ge 85\%$ correct primary department recommendations across a benchmark set of 200 mixed Hinglish complaints[cite: 10].
2. **Deduplication Precision Test:** System clusters duplicate complaints within the same ward with $\ge 80\%$ precision without false-positive grouping[cite: 10].
3. **Audit Latency Test:** Human officer overrides update the immutable audit log in $<500\text{ ms}$[cite: 10].

## 2. System Failure Modes & Safeguards
- **Low Confidence Scores (<0.60):** Automatically routes complaint to `GENERAL_HUMAN_TRIAGE_QUEUE`[cite: 10].
- **Sarcasm / Unclear Text:** Flags complaint for human review rather than misrouting[cite: 10].
- **Multi-Department Overlap:** Assigns a primary department lead and secondary co-assigned tags to prevent ping-pong reassignments[cite: 10].

## 3. Explicit V1 Scope Exclusions (What V1 will NOT do)
- Will **NOT** perform autonomous ticket closing or rejection[cite: 10, 11].
- Will **NOT** automate physical field worker dispatching[cite: 11].
- Will **NOT** scrape unconsented private citizen social media profiles[cite: 4, 11].