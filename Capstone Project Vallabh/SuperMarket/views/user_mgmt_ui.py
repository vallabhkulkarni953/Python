# views/user_mgmt_ui.py

import tkinter as tk
from tkinter import ttk, messagebox
from models import user
import os

ICON_PATH = os.path.join("assets", "app_icon.ico")

class UserManagementUI:
    def __init__(self, master):
        self.master = master
        self.master.title("User Management")

        form = tk.Frame(master)
        form.pack(pady=10)

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.role_var = tk.StringVar(value="cashier")

        tk.Label(form, text="Username").grid(row=0, column=0)
        tk.Entry(form, textvariable=self.username_var).grid(row=0, column=1)

        tk.Label(form, text="Password").grid(row=1, column=0)
        tk.Entry(form, textvariable=self.password_var, show="*").grid(row=1, column=1)

        tk.Label(form, text="Role").grid(row=2, column=0)
        ttk.Combobox(form, textvariable=self.role_var, values=["admin", "cashier"]).grid(row=2, column=1)

        tk.Button(form, text="Add User", command=self.add_user).grid(row=3, column=0, columnspan=2, pady=5)

        self.tree = ttk.Treeview(master, columns=("ID", "Username", "Role"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

        tk.Button(master, text="Delete Selected", command=self.delete_user).pack(pady=5)

        self.load_users()

    def add_user(self):
        uname = self.username_var.get()
        pwd = self.password_var.get()
        role = self.role_var.get()

        if not (uname and pwd):
            messagebox.showerror("Input Error", "All fields are required!")
            return

        success = user.add_user(uname, pwd, role)
        if success:
            messagebox.showinfo("Success", f"{role.title()} added successfully.")
            self.username_var.set("")
            self.password_var.set("")
            self.load_users()
        else:
            messagebox.showerror("Error", "Username already exists!")

    def load_users(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for u in user.get_all_users():
            self.tree.insert("", tk.END, values=u)

    def delete_user(self):
        selected = self.tree.selection()
        if not selected:
            return
        user_id = self.tree.item(selected[0])["values"][0]
        if messagebox.askyesno("Confirm", "Delete this user?"):
            user.delete_user(user_id)
            self.load_users()
