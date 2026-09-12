from app.models import SecurityEvent


event = SecurityEvent(
    timestamp="2026-09-12 22:00:00",
    source_ip="10.10.1.5",
    username="Hamid",
    event_type="login",
    status="failed",
    device_type="windows",
    vendor="Microsoft",
    event_id="4625",
    severity="banana",
    destination_ip="10.10.1.20",
    hostname="WIN-SERVER-01",
    action="login"
)

print(event)