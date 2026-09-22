from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import sqlite3

DB = "database/target.db"


class GameServer(BaseHTTPRequestHandler):

    def send_json(self, data, status=200):
        body = json.dumps(data).encode()

        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.end_headers()

        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_json({"status": "ok"})

    def do_GET(self):
        if self.path == "/level1":
            self.send_json({
                "level": 1,
                "target": "Secure Database",
                "status": "PROTECTED",
                "mission": "Gain access to the target database."
            })
        else:
            self.send_json({"error": "Not found"}, 404)

    def do_POST(self):
        if self.path != "/level1/access":
            self.send_json({"error": "Not found"}, 404)
            return

        length = int(self.headers.get("Content-Length", 0))
        data = json.loads(self.rfile.read(length))

        username = data.get("username", "")

        connection = sqlite3.connect(DB)
        cursor = connection.cursor()

        cursor.execute(
            "SELECT username, role, access_level FROM users WHERE username = ?",
            (username,)
        )

        user = cursor.fetchone()
        connection.close()

        if user:
            self.send_json({
                "access": "GRANTED",
                "username": user[0],
                "role": user[1],
                "access_level": user[2],
                "message": "LEVEL 1 COMPLETE"
            })
        else:
            self.send_json({
                "access": "DENIED",
                "message": "ACCESS DENIED"
            })


server = HTTPServer(("0.0.0.0", 8080), GameServer)

print("====================================")
print("   UNIVERSAL CYBER RANGE SERVER")
print("====================================")
print("Level 1 server running")
print("http://localhost:8080")
print("Press CTRL+C to stop")

server.serve_forever()