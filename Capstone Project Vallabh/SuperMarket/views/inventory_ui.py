# views/inventory_ui.py

import tkinter as tk
from tkinter import ttk, messagebox
from models import product
import os

ICON_PATH = os.path.join("assets", "app_icon.ico")


class InventoryUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Inventory Management")

        self.tree = ttk.Treeview(master, columns=('ID', 'Name', 'Category', 'Qty', 'Price'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Name', text='Product Name')
        self.tree.heading('Category', text='Category')
        self.tree.heading('Qty', text='Quantity')
        self.tree.heading('Price', text='Price')
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.refresh_tree()

        form = tk.Frame(master)
        form.pack(pady=10)

        self.name_var = tk.StringVar()
        self.cat_var = tk.StringVar()
        self.qty_var = tk.IntVar()
        self.price_var = tk.DoubleVar()

        tk.Label(form, text="Name").grid(row=0, column=0)
        tk.Entry(form, textvariable=self.name_var).grid(row=0, column=1)

        tk.Label(form, text="Category").grid(row=1, column=0)
        tk.Entry(form, textvariable=self.cat_var).grid(row=1, column=1)

        tk.Label(form, text="Quantity").grid(row=2, column=0)
        tk.Entry(form, textvariable=self.qty_var).grid(row=2, column=1)

        tk.Label(form, text="Price").grid(row=3, column=0)
        tk.Entry(form, textvariable=self.price_var).grid(row=3, column=1)

        btn_frame = tk.Frame(master)
        btn_frame.pack()

        tk.Button(btn_frame, text="Add Product", command=self.add_product).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Update Product", command=self.update_selected).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Delete Product", command=self.delete_selected).pack(side=tk.LEFT, padx=5)

        self.tree.bind("<Double-1>", self.load_selected)

    def refresh_tree(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in product.get_all_products():
            self.tree.insert('', tk.END, values=row)

    def add_product(self):
        try:
            product.add_product(
                self.name_var.get(), self.cat_var.get(),
                self.qty_var.get(), self.price_var.get()
            )
            self.refresh_tree()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def load_selected(self, event):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0])['values']
            self.selected_id = values[0]
            self.name_var.set(values[1])
            self.cat_var.set(values[2])
            self.qty_var.set(values[3])
            self.price_var.set(values[4])

    def update_selected(self):
        if not hasattr(self, 'selected_id'):
            messagebox.showwarning("Select a row", "No row selected.")
            return
        product.update_product(
            self.selected_id,
            self.name_var.get(), self.cat_var.get(),
            self.qty_var.get(), self.price_var.get()
        )
        self.refresh_tree()

    def delete_selected(self):
        selected = self.tree.selection()
        if selected:
            item = self.tree.item(selected[0])['values']
            product.delete_product(item[0])
            self.refresh_tree()
