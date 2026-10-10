import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "sentinel.db")

def init_db():
    """Initializes the SQLite database with the required tables."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create the citizen_reports table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS citizen_reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            location TEXT,
            issue_type TEXT,
            severity TEXT,
            description TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def insert_report(name, location, issue_type, severity, description):
    """Inserts a new citizen report into the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO citizen_reports (name, location, issue_type, severity, description)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, location, issue_type, severity, description))
    conn.commit()
    conn.close()

def get_reports_by_location(location):
    """Retrieves all reports for a specific location."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM citizen_reports WHERE location = ?', (location,))
    reports = cursor.fetchall()
    conn.close()
    return reports

def get_recent_reports_count(location):
    """Returns the count of recent reports for a given location in the last 24h, and the daily average over the past 7 days."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Last 24 hours
    cursor.execute('''
        SELECT COUNT(*) FROM citizen_reports 
        WHERE location = ? AND timestamp >= datetime('now', '-1 day')
    ''', (location,))
    last_24h_count = cursor.fetchone()[0]
    
    # Previous 7 days baseline (days 1-8 before now)
    cursor.execute('''
        SELECT COUNT(*) FROM citizen_reports 
        WHERE location = ? AND timestamp >= datetime('now', '-8 days') AND timestamp < datetime('now', '-1 day')
    ''', (location,))
    prev_7_days_count = cursor.fetchone()[0]
    
    conn.close()
    
    baseline_daily_avg = prev_7_days_count / 7.0
    return last_24h_count, baseline_daily_avg

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")
