import json
from typing import Dict, List

# Define department keyword features for multi-label scoring
DEPARTMENT_KEYWORDS = {
    "PWD_Roads": ["sadak", "gadda", "road", "pothole", "tar", "footpath"],
    "Sanitation": ["sewage", "badboo", "kachra", "garbage", "drain", "naali"],
    "Water_Board": ["paani", "water", "pipeline", "burst", "leakage", "supply"],
    "Electricity": ["wires", "khamba", "light", "transformer", "spark", "current"],
    "Public_Health": ["dengue", "mosquito", "smell", "infection", "hazard"]
}

SAFETY_HAZARD_KEYWORDS = ["wires", "open latak", "spark", "current", "burst", "hazard", "deep pothole"]

def analyze_complaint(text: str) -> Dict:
    text_lower = text.lower()
    scores = {}
    
    # Calculate confidence scores per department
    for dept, keywords in DEPARTMENT_KEYWORDS.items():
        matches = sum(1 for kw in keywords if kw in text_lower)
        scores[dept] = round(min(matches * 0.4, 0.95), 2)
    
    # Calculate Urgency Score based on public safety markers
    safety_matches = sum(1 for kw in SAFETY_HAZARD_KEYWORDS if kw in text_lower)
    urgency_score = round(min(0.3 + (safety_matches * 0.35), 0.99), 2)
    
    # Sort scores to get top departments
    sorted_depts = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top_dept, top_score = sorted_depts[0]
    
    # Boundary Fallback Flag: Low confidence triggers human review queue
    requires_human_triage = top_score < 0.60
    
    return {
        "department_confidence": scores,
        "primary_suggested_dept": top_dept if not requires_human_triage else "GENERAL_HUMAN_TRIAGE_QUEUE",
        "urgency_score": urgency_score,
        "requires_human_triage": requires_human_triage
    }

# Run PoC on Mock Data
if __name__ == "__main__":
    with open("mock_data.json", "r") as f:
        complaints = json.load(f)
        
    print("=== MUNICIPAL TRIAGE & ROUTING ENGINE POC OUTPUT ===\n")
    for item in complaints:
        text = item["raw_input"]["text"]
        result = analyze_complaint(text)
        print(f"Ticket ID: {item['ticket_id']}")
        print(f"Raw Input: '{text}'")
        print(f"Suggested Primary Dept: {result['primary_suggested_dept']}")
        print(f"Urgency Score: {result['urgency_score']}")
        print(f"Dept Scores: {result['department_confidence']}")
        print(f"Flagged for Manual Triage: {result['requires_human_triage']}")
        print("-" * 65)