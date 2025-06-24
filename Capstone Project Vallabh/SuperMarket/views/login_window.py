# views/login_window.py

import tkinter as tk
from tkinter import messagebox
import sqlite3
import os

ICON_PATH = os.path.join("assets", "app_icon.ico")
DB_PATH = os.path.join("data", "supermarket.db")

class LoginWindow:
    def __init__(self, master, on_login_success):
        self.master = master
        self.master.title("Supermarket Management - Login")
        self.master.geometry("300x200")
        self.on_login_success = on_login_success

        # root.iconbitmap(ICON_PATH)      # In login window
        # dashboard.iconbitmap(ICON_PATH) # In dashboard window


        tk.Label(master, text="Username").pack(pady=5)
        self.username_entry = tk.Entry(master)
        self.username_entry.pack()

        tk.Label(master, text="Password").pack(pady=5)
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack()

        tk.Button(master, text="Login", command=self.validate_login).pack(pady=10)

    def validate_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            self.master.destroy()
            self.on_login_success(user)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
