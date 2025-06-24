# models/product.py

import sqlite3
import os

DB_PATH = os.path.join("data", "supermarket.db")

def get_all_products():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    conn.close()
    return rows

def add_product(name, category, quantity, price):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, category, quantity, price) VALUES (?, ?, ?, ?)",
                   (name, category, quantity, price))
    conn.commit()
    conn.close()

def update_product(product_id, name, category, quantity, price):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET name=?, category=?, quantity=?, price=? WHERE id=?",
                   (name, category, quantity, price, product_id))
    conn.commit()
    conn.close()

def delete_product(product_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
    conn.commit()
    conn.close()
