from schemas import IngestionPayload
from pydantic import ValidationError

# 1. TEST VALID PAYLOAD (Hinglish WhatsApp Complaint)
valid_data = {
    "ticket_id": "GOV_2026_09412",
    "source_channel": "WHATSAPP",
    "timestamp": "2026-10-09T10:30:00Z",
    "raw_input": {
        "text": "Sadak pe gadda hai aur sewage paani beh raha h ward 4 main",
        "image_urls": ["https://storage.gov.in/photos/img_9412.jpg"]
    },
    "location": {
        "ward_number": 4,
        "landmark": "Near Govt School"
    }
}

try:
    payload = IngestionPayload(**valid_data)
    print("✅ Validation Successful! Payload passed to AI pipeline.")
except ValidationError as e:
    print("❌ Validation Failed:", e)

# 2. TEST INVALID PAYLOAD (Missing raw text, bad ticket format)
invalid_data = {
    "ticket_id": "INVALID_ID_123",
    "source_channel": "TIKTOK",  # Not a supported channel
    "timestamp": "not-a-date",
    "raw_input": {}  # Missing mandatory text
}

try:
    payload = IngestionPayload(**invalid_data)
except ValidationError as e:
    print("\n✅ Error Handling Works! Caught invalid input before AI pipeline:")
    print(e.json())