from parsers.auth_log_parser import parse_auth_log


log = "2026-09-13 10:20:10 SUCCESS_LOGIN user=hamid ip=10.0.0.25"

event = parse_auth_log(log)

print(event)