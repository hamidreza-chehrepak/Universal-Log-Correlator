import re

from app.models import SecurityEvent


def parse_auth_log(line: str) -> SecurityEvent:
    pattern = (
        r"(?P<timestamp>\S+\s+\S+)\s+"
        r"(?P<event_type>FAILED_LOGIN|SUCCESS_LOGIN)\s+"
        r"user=(?P<username>\S+)\s+"
        r"ip=(?P<source_ip>\S+)"
    )

    match = re.match(pattern, line)

    if not match:
        raise ValueError("Invalid log format")

    data = match.groupdict()

    if data["event_type"] == "FAILED_LOGIN":
        data["status"] = "failed"
        data["severity"] = "medium"
        data["action"] = "login_attempt"
    else:
        data["status"] = "success"
        data["severity"] = "low"
        data["action"] = "login"

    data["device_type"] = "unknown"
    data["vendor"] = "unknown"
    data["event_id"] = "auth-001"
    data["destination_ip"] = "unknown"
    data["hostname"] = "unknown"

    return SecurityEvent(**data)