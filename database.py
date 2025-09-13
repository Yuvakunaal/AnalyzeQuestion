import sqlite3
from datetime import datetime

conn = sqlite3.connect("problem.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS problems (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    problem_text TEXT,
    patterns TEXT,
    difficulty TEXT,
    approach TEXT,
    created_at TEXT
)
""")
conn.commit()

def save_problem(problem_text, patterns, difficulty, approach):
    cursor.execute(
        "INSERT INTO problems (problem_text, patterns, difficulty, approach, created_at) VALUES (?, ?, ?, ?, ?)",
        (problem_text, ",".join(patterns), difficulty, ",".join(approach), datetime.now().isoformat())
    )
    conn.commit()

def fetch_similar_problems(query_text, limit=3):
    cursor.execute(
        "SELECT problem_text, patterns, difficulty, approach FROM problems WHERE problem_text LIKE ? LIMIT ?",
        ('%' + query_text[:50] + '%', limit)
    )
    return cursor.fetchall()
