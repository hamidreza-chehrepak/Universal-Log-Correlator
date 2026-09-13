from parsers.auth_log_parser import parse_auth_log
from app.correlator import correlate_events
from detections.brute_force import detect_brute_force


events = []

with open("data/auth.log", "r") as file:
    for line in file:
        line = line.strip()

        if line:
            event = parse_auth_log(line)
            events.append(event)


groups = correlate_events(events)

for group_key, correlated_events in groups.items():
    alerts = detect_brute_force(correlated_events)

    for alert in alerts:
        print("\n🚨 SECURITY ALERT")
        print(f"Type: {alert['type']}")
        print(f"Source IP: {alert['source_ip']}")
        print(f"Username: {alert['username']}")
        print(f"Failed Attempts: {alert['failed_attempts']}")
        print(f"Severity: {alert['severity']}")