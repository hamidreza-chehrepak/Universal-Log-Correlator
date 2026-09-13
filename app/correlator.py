from datetime import timedelta

from app.models import SecurityEvent


def correlate_events(
    events: list[SecurityEvent],
    window_minutes: int = 5
) -> dict[tuple[str, str], list[SecurityEvent]]:

    groups = {}

    for event in events:
        key = (event.source_ip, event.username)

        if key not in groups:
            groups[key] = []

        groups[key].append(event)

    correlated_groups = {}

    for key, event_list in groups.items():

        event_list.sort(key=lambda event: event.timestamp)

        current_group = []
        group_number = 1
        window = timedelta(minutes=window_minutes)

        for event in event_list:

            if not current_group:
                current_group.append(event)
                continue

            first_event_time = current_group[0].timestamp

            if event.timestamp - first_event_time <= window:
                current_group.append(event)

            else:
                correlated_groups[(key, group_number)] = current_group
                group_number += 1
                current_group = [event]

        if current_group:
            correlated_groups[(key, group_number)] = current_group

    return correlated_groups