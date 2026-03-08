import sqlite3

conn = sqlite3.connect("database.db")

cur = conn.cursor()

cur.execute("""
CREATE TABLE enquiries(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
phone TEXT,
email TEXT,
course TEXT,
message TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully")