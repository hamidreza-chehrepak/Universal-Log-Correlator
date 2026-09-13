from app.models import SecurityEvent


def detect_brute_force(events: list[SecurityEvent]) -> list[dict]:
    alerts = []

    failed_events = [
        event for event in events
        if event.event_type == "FAILED_LOGIN"
    ]

    if len(failed_events) >= 4:
        first_event = failed_events[0]

        alerts.append({
            "type": "BRUTE_FORCE",
            "source_ip": first_event.source_ip,
            "username": first_event.username,
            "failed_attempts": len(failed_events),
            "severity": "HIGH",
        })

    return alerts