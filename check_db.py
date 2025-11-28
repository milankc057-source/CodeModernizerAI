
import sqlite3

# Connect to your database
conn = sqlite3.connect("app.db")
cursor = conn.cursor()

# List all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in database:", tables)

# Optionally, see first 5 rows in the 'projects' table
if ('projects',) in tables:
    cursor.execute("SELECT * FROM projects LIMIT 5;")
    rows = cursor.fetchall()
    print("Sample rows from 'projects':", rows)
else:
    print("No 'projects' table found.")

conn.close()
