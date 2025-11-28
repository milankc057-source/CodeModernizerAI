import sqlite3

DB_FILE = "app.db"  # This file will be created automatically

def get_connection():
    return sqlite3.connect(DB_FILE)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Create projects table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        modernization_level TEXT,
        content TEXT
    );
    """)
    
    conn.commit()
    conn.close()
    print("Database initialized.")
