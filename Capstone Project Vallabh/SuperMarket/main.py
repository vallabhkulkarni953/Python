# main.py

import tkinter as tk
from views.login_window import LoginWindow
from models.db import initialize_database
from views.inventory_ui import InventoryUI
from views.billing_ui import BillingUI
from views.reports_ui import ReportsUI
from views.user_mgmt_ui import UserManagementUI
import os

ICON_PATH = os.path.join("assets", "app_icon.ico")

def launch_dashboard(user):
    dashboard = tk.Tk()
    dashboard.title("Supermarket Dashboard")

    # root.iconbitmap(ICON_PATH)      # In login window
    # dashboard.iconbitmap(ICON_PATH) # In dashboard window


    tk.Label(dashboard, text=f"Welcome, {user[1]} ({user[3]})").pack(pady=10)

    tk.Button(dashboard, text="Manage Inventory", command=lambda: InventoryUI(tk.Toplevel(dashboard))).pack(pady=10)
    tk.Button(dashboard, text="Billing System", command=lambda: BillingUI(tk.Toplevel(dashboard))).pack(pady=10)
    tk.Button(dashboard, text="Sales Reports", command=lambda: ReportsUI(tk.Toplevel(dashboard))).pack(pady=10)

    if user[3] == "admin":
        tk.Button(dashboard, text="User Management", command=lambda: UserManagementUI(tk.Toplevel(dashboard))).pack(pady=10)

    dashboard.mainloop()

if __name__ == "__main__":
    initialize_database()
    
    root = tk.Tk()
    app = LoginWindow(root, launch_dashboard)
    root.mainloop()
