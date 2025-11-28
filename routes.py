from fastapi import FastAPI
import sqlite3

app = FastAPI()

DB_FILE = "app.db"

@app.get("/projects")
def get_all_projects():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Fetch all projects
    cursor.execute("SELECT * FROM projects")
    rows = cursor.fetchall()
    
    conn.close()
    
    # Return as list of dicts
    projects = [{"id": row[0], "name": row[1], "modernization_level": row[2]} for row in rows]
    return {"projects": projects}

