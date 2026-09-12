from pydantic import BaseModel
from typing import Literal

class SecurityEvent(BaseModel):
    timestamp: str
    source_ip: str
    username: str
    event_type: str
    status: str
    device_type: str
    vendor: str
    event_id: str
    severity: Literal["low", "medium", "high", "critical"]
    destination_ip: str
    hostname: str
    action: str