# utils/pdf_generator.py

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import os

def generate_invoice(cart, total_amount, output_dir="invoices"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"invoice_{timestamp}.pdf"
    path = os.path.join(output_dir, filename)

    c = canvas.Canvas(path, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 20)
    c.drawString(200, height - 50, "Supermarket Invoice")

    c.setFont("Helvetica", 12)
    y = height - 100
    c.drawString(50, y, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    y -= 40
    c.drawString(50, y, "Product")
    c.drawString(200, y, "Quantity")
    c.drawString(300, y, "Price")
    c.drawString(400, y, "Total")

    y -= 20
    for item in cart:
        name, qty, price, total = item
        c.drawString(50, y, str(name))
        c.drawString(200, y, str(qty))
        c.drawString(300, y, f"₹{price:.2f}")
        c.drawString(400, y, f"₹{total:.2f}")
        y -= 20

    y -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(300, y, "TOTAL:")
    c.drawString(400, y, f"₹{total_amount:.2f}")

    c.save()
    return path
