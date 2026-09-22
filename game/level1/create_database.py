import sqlite3
from pathlib import Path

database_dir = Path("database")
database_dir.mkdir(exist_ok=True)

database_path = database_dir / "target.db"

connection = sqlite3.connect(database_path)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    role TEXT NOT NULL,
    access_level INTEGER NOT NULL
)
""")

cursor.execute("""
INSERT INTO users (username, role, access_level)
VALUES
    ('admin', 'administrator', 10),
    ('analyst', 'security analyst', 5),
    ('guest', 'guest', 1)
""")

connection.commit()
connection.close()

print(f"Database created: {database_path}")