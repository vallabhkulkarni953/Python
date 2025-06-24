# views/billing_ui.py

import tkinter as tk
from tkinter import ttk, messagebox
from models import product, billing
from utils.pdf_generator import generate_invoice
import webbrowser
import os


ICON_PATH = os.path.join("assets", "app_icon.ico")

class BillingUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Billing System")

        self.cart = []
        self.total_amount = 0

        form = tk.Frame(master)
        form.pack(pady=10)

        self.name_var = tk.StringVar()
        self.qty_var = tk.IntVar(value=1)

        tk.Label(form, text="Product Name").grid(row=0, column=0)
        tk.Entry(form, textvariable=self.name_var).grid(row=0, column=1)

        tk.Label(form, text="Quantity").grid(row=1, column=0)
        tk.Entry(form, textvariable=self.qty_var).grid(row=1, column=1)

        tk.Button(form, text="Add to Cart", command=self.add_to_cart).grid(row=2, column=0, columnspan=2, pady=5)

        self.tree = ttk.Treeview(master, columns=('Name', 'Qty', 'Unit Price', 'Total'), show='headings')
        for col in self.tree['columns']:
            self.tree.heading(col, text=col)
        self.tree.pack(pady=10)

        self.total_label = tk.Label(master, text="Total: ₹0.00", font=('Arial', 14))
        self.total_label.pack()

        tk.Button(master, text="Checkout", command=self.checkout).pack(pady=10)

    def add_to_cart(self):
        name = self.name_var.get()
        qty = self.qty_var.get()

        products = product.get_all_products()
        matched = [p for p in products if p[1].lower() == name.lower()]

        if not matched:
            messagebox.showerror("Error", "Product not found.")
            return

        prod = matched[0]
        if qty > prod[3]:
            messagebox.showerror("Error", "Not enough stock.")
            return

        total = qty * prod[4]
        self.cart.append((prod[1], qty, prod[4], total))

        self.refresh_cart()
        self.total_amount += total
        self.total_label.config(text=f"Total: ₹{self.total_amount:.2f}")

        # Optionally reduce stock here
        product.update_product(prod[0], prod[1], prod[2], prod[3] - qty, prod[4])

    def refresh_cart(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for item in self.cart:
            self.tree.insert('', tk.END, values=item)

    def checkout(self):
        for item in self.cart:
            billing.save_sale(*item[:3])
        
        invoice_path = generate_invoice(self.cart, self.total_amount)
        webbrowser.open_new(invoice_path)

        messagebox.showinfo("Success", f"Sale recorded!\nInvoice saved to:\n{invoice_path}")
        
        self.cart.clear()
        self.total_amount = 0
        self.refresh_cart()
        self.total_label.config(text="Total: ₹0.00")
