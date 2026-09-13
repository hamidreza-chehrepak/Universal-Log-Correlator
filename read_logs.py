from parsers.auth_log_parser import parse_auth_log


with open("data/auth.log", "r") as file:
    for line in file:
        line = line.strip()

        if not line:
            continue

        event = parse_auth_log(line)

        print(event)