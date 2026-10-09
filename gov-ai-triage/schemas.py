from enum import Enum
from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, Field, HttpUrl

class SourceChannel(str, Enum):
    PORTAL = "PORTAL"
    PHONE_TRANSCRIPT = "PHONE_TRANSCRIPT"
    WHATSAPP = "WHATSAPP"
    IN_PERSON = "IN_PERSON"

class RawInput(BaseModel):
    text: str = Field(..., min_length=5, description="Raw Hinglish/Hindi/English complaint text")
    audio_url: Optional[str] = None
    image_urls: List[str] = []

class LocationDetails(BaseModel):
    ward_number: Optional[int] = None
    landmark: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class IngestionPayload(BaseModel):
    ticket_id: str = Field(..., pattern=r"^GOV_[0-9]{4}_[0-9]{5}$")
    source_channel: SourceChannel
    timestamp: datetime
    raw_input: RawInput
    location: Optional[LocationDetails] = None