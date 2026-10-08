import json
from typing import List, Dict

# Simple keyword jaccard similarity for rapid baseline deduplication proof
def calculate_similarity(text1: str, text2: str) -> float:
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())
    intersection = words1.intersection(words2)
    union = words1.union(words2)
    return round(len(intersection) / len(union), 2) if union else 0.0

def cluster_duplicates(complaints: List[Dict], similarity_threshold: float = 0.25) -> List[Dict]:
    clusters = []
    
    for item in complaints:
        text = item["raw_input"]["text"]
        ward = item["location"]["ward_number"]
        ticket_id = item["ticket_id"]
        
        assigned_cluster = None
        
        # Check against existing clusters in the same ward
        for cluster in clusters:
            if cluster["ward_number"] == ward:
                # Compare with parent complaint in cluster
                sim_score = calculate_similarity(text, cluster["parent_text"])
                if sim_score >= similarity_threshold:
                    assigned_cluster = cluster["cluster_id"]
                    cluster["child_tickets"].append({
                        "ticket_id": ticket_id,
                        "similarity_score": sim_score,
                        "status": "LINKED_FOR_HUMAN_REVIEW" # BOUNDARY SAFEGUARD: Never auto-closed!
                    })
                    break
        
        # If no matching cluster in ward, create new Parent Cluster
        if not assigned_cluster:
            cluster_id = f"CLUSTER_WARD{ward}_{len(clusters)+1:03d}"
            clusters.append({
                "cluster_id": cluster_id,
                "ward_number": ward,
                "parent_ticket_id": ticket_id,
                "parent_text": text,
                "child_tickets": []
            })
            
    return clusters

if __name__ == "__main__":
    with open("mock_data.json", "r") as f:
        complaints = json.load(f)
        
    print("=== MUNICIPAL DEDUPLICATION CLUSTERING POC ===\n")
    clusters = cluster_duplicates(complaints)
    
    for c in clusters:
        print(f"Parent Cluster ID : {c['cluster_id']} (Ward {c['ward_number']})")
        print(f"Primary Ticket ID : {c['parent_ticket_id']}")
        print(f"Primary Text      : '{c['parent_text']}'")
        print(f"Linked Child Count: {len(c['child_tickets'])}")
        for child in c['child_tickets']:
            print(f"   └── Child Ticket: {child['ticket_id']} | Similarity: {child['similarity_score']} | Status: {child['status']}")
        print("-" * 65)