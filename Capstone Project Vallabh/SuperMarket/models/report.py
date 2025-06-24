# models/report.py

import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join("data", "supermarket.db")

def get_all_sales():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sales ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_sales_by_date(start, end):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM sales
        WHERE date(timestamp) BETWEEN ? AND ?
        ORDER BY timestamp DESC
    """, (start, end))
    rows = cursor.fetchall()
    conn.close()
    return rows
