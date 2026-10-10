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
    """Returns the count of recent reports for a given location."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # For the hackathon prototype, we just count all reports for the location
    cursor.execute('SELECT COUNT(*) FROM citizen_reports WHERE location = ?', (location,))
    count = cursor.fetchone()[0]
    conn.close()
    return count

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")
