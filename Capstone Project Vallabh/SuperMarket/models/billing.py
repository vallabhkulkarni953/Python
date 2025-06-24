# models/billing.py

import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join("data", "supermarket.db")

def save_sale(product_name, quantity, price):
    total = quantity * price
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sales (product_name, quantity, price, total) VALUES (?, ?, ?, ?)",
                   (product_name, quantity, price, total))
    conn.commit()
    conn.close()
