# views/reports_ui.py

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from models import report
import csv
from datetime import datetime
import os

ICON_PATH = os.path.join("assets", "app_icon.ico")

class ReportsUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sales Reports")

        self.tree = ttk.Treeview(master, columns=("ID", "Name", "Qty", "Price", "Total", "Timestamp"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

        self.load_all_sales()

        filter_frame = tk.Frame(master)
        filter_frame.pack(pady=5)

        self.start_var = tk.StringVar()
        self.end_var = tk.StringVar()

        tk.Label(filter_frame, text="Start Date (YYYY-MM-DD)").grid(row=0, column=0)
        tk.Entry(filter_frame, textvariable=self.start_var).grid(row=0, column=1)

        tk.Label(filter_frame, text="End Date (YYYY-MM-DD)").grid(row=0, column=2)
        tk.Entry(filter_frame, textvariable=self.end_var).grid(row=0, column=3)

        tk.Button(filter_frame, text="Filter", command=self.filter_sales).grid(row=0, column=4, padx=10)

        btn_frame = tk.Frame(master)
        btn_frame.pack()

        tk.Button(btn_frame, text="Export CSV", command=self.export_csv).pack(pady=5)

    def load_all_sales(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in report.get_all_sales():
            self.tree.insert('', tk.END, values=row)

    def filter_sales(self):
        start = self.start_var.get()
        end = self.end_var.get()
        try:
            datetime.strptime(start, '%Y-%m-%d')
            datetime.strptime(end, '%Y-%m-%d')
        except ValueError:
            messagebox.showerror("Invalid Date", "Use format YYYY-MM-DD")
            return

        rows = report.get_sales_by_date(start, end)
        self.tree.delete(*self.tree.get_children())
        for row in rows:
            self.tree.insert('', tk.END, values=row)

    def export_csv(self):
        file = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV File", "*.csv")])
        if not file:
            return

        with open(file, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Product", "Quantity", "Price", "Total", "Timestamp"])
            for row_id in self.tree.get_children():
                writer.writerow(self.tree.item(row_id)["values"])
        messagebox.showinfo("Exported", f"Sales report saved to {file}")
