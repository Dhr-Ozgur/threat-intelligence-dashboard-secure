import sqlite3
import pandas as pd
import os

DB_PATH = "data/results.db"
os.makedirs("data", exist_ok=True)

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT,
            key_value TEXT,
            data TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

def save_result(results: dict):
    with sqlite3.connect(DB_PATH) as conn:
        for src, df in results.items():
            if isinstance(df, pd.DataFrame):
                for _, row in df.iterrows():
                    conn.execute("INSERT INTO reports (source, key_value, data) VALUES (?, ?, ?)",
                                 (src, str(row.get('ip') or row.get('domain') or row.get('email')), row.to_json()))
    conn.commit()

def get_all_results(as_df=False):
    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql_query("SELECT * FROM reports", conn)
    return df if as_df else df.to_dict(orient="records")

init_db()
