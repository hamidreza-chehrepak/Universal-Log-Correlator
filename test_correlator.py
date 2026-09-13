from parsers.auth_log_parser import parse_auth_log
from app.correlator import correlate_events


events = []

with open("data/auth.log", "r") as file:
    for line in file:
        line = line.strip()

        if line:
            event = parse_auth_log(line)
            events.append(event)


groups = correlate_events(events)


for group_key, correlated_events in groups.items():
    print(f"\nCorrelation Group: {group_key}")

    for event in correlated_events:
        print(f"  {event.timestamp} - {event.event_type} - {event.username}")