import json
import subprocess

result = subprocess.run(
    ["./c_engine/event_generator.exe"],
    capture_output=True,
    text=True
)

event = json.loads(result.stdout)

print("=== BLUE TEAM ===")
print(f"Event received: {event['event_type']}")
print(f"Status: {event['status']}")
print(f"Severity: {event['severity']}")

if event["status"] == "SIMULATED":
    print("ALERT: Simulated security event detected!")