import sqlite3
import json
from datetime import datetime
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'database', 'weather.db')

def init_db():
    print("🛠️ Initializing DB at:", DB_PATH)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather_queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location TEXT,
            query_type TEXT,
            timestamp TEXT,
            response_json TEXT
        )
    ''')
    conn.commit()
    conn.close()


def save_query(location, query_type, response_data):
    print("📦 Saving:", location, query_type)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO weather_queries (location, query_type, timestamp, response_json)
        VALUES (?, ?, ?, ?)
    ''', (
        location,
        query_type,
        datetime.now().isoformat(),
        json.dumps(response_data)
    ))
    conn.commit()
    conn.close()

def get_all_queries():
    try:
        print("📂 Fetching all queries from DB...")
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute('SELECT location, query_type, timestamp, response_json FROM weather_queries ORDER BY timestamp DESC')
        rows = cursor.fetchall()
        conn.close()

        print(f"📄 Rows fetched: {len(rows)}")

        history = []
        for row in rows:
            location, query_type, timestamp, response_json = row
            try:
                parsed = json.loads(response_json)
            except json.JSONDecodeError:
                print("❗ Failed to decode JSON for one row")
                parsed = {"error": "Invalid JSON"}

            history.append({
                "location": location,
                "type": query_type,
                "timestamp": timestamp,
                "data": parsed
            })

        return history

    except Exception as e:
        print("❌ Error in get_all_queries():", e)
        return []

def clear_all_queries():
    print("🗑️ Clearing all weather query history...")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM weather_queries')
    conn.commit()
    conn.close()
    print("✅ History cleared.")
