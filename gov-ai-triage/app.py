import json
from schemas import IngestionPayload
from router_poc import analyze_complaint
from dedup_poc import cluster_duplicates

def run_triage_dashboard():
    print("==================================================================")
    print(" 🏛️  CIVICTRIAGE AI: MUNICIPAL ADMINISTRATIVE DASHBOARD (CASE 07) ")
    print("==================================================================\n")
    
    # 1. Load Mock Ingestion Data
    with open("mock_data.json", "r") as f:
        raw_complaints = json.load(f)
        
    print(f"📥 [INGESTION] Loaded {len(raw_complaints)} incoming complaints across WhatsApp, Portal, and Phone.\n")
    
    # 2. Run Spatial Deduplication
    clusters = cluster_duplicates(raw_complaints)
    print(f"🔍 [DEDUPLICATION] Grouped into {len(clusters)} unique Ward Clusters.\n")
    
    # 3. Process Triage Queue
    print("------------------------------------------------------------------")
    print("               OFFICER TRIAGE & ROUTING QUEUE                    ")
    print("------------------------------------------------------------------\n")
    
    for idx, item in enumerate(raw_complaints, 1):
        # Validate Schema
        try:
            payload = IngestionPayload(**item)
            text = payload.raw_input.text
            channel = payload.source_channel.value
            ticket_id = payload.ticket_id
        except Exception as e:
            print(f"❌ Ticket #{idx} failed schema validation: {e}")
            continue

        # Run AI Multi-Label & Urgency Engine
        result = analyze_complaint(text)
        
        print(f"🎫 TICKET ID       : {ticket_id} (via {channel})")
        print(f"📝 RAW COMPLAINT   : \"{text}\"")
        print(f"🏷️  DEPARTMENT SCORES: {result['department_confidence']}")
        print(f"🎯 RECOMMENDED DEPT: {result['primary_suggested_dept']}")
        print(f"🚨 SAFETY URGENCY  : {result['urgency_score']} / 1.00")
        
        # Display Boundary Safeguard Flag
        if result['requires_human_triage']:
            print("⚠️  STATUS          : Low confidence (<0.60) -> ROUTED TO HUMAN REVIEW QUEUE")
        else:
            print("✅ STATUS          : High confidence -> PENDING OFFICER 1-CLICK CONFIRMATION")
            
        print("------------------------------------------------------------------\n")

if __name__ == "__main__":
    run_triage_dashboard()
    