import atexit
from datetime import datetime
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

_get_products = None
_started = False


def set_products_source(func):
    """main.py gives us a function that returns the current product list."""
    global _get_products
    _get_products = func


def create_inventory_pdf(products, filename):
    c = canvas.Canvas(str(filename), pagesize=A4)
    width, height = A4
    y = height - 60
    now = datetime.now()

    # Header
    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, y, "INVENTORY REPORT")
    y -= 30
    c.setFont("Helvetica", 11)
    c.drawString(50, y, f"Report No: INV-{now:%Y%m%d-%H%M%S}")
    y -= 18
    c.drawString(50, y, f"Date: {now:%Y-%m-%d %H:%M}")
    y -= 18
    c.drawString(50, y, f"Total Products: {len(products)}")
    y -= 35

    def table_header(y):
        c.setFont("Helvetica-Bold", 11)
        c.drawString(50, y, "Item")
        c.drawString(280, y, "Qty")
        c.drawString(350, y, "Price")
        c.drawString(440, y, "Total")
        y -= 8
        c.line(50, y, 540, y)
        return y - 20

    y = table_header(y)

    # Items
    c.setFont("Helvetica", 11)
    grand_total = 0
    for p in products:
        if y < 80:
            c.showPage()
            y = height - 60
            y = table_header(y)
            c.setFont("Helvetica", 11)

        qty = p.get_quantity
        price = p.get_price
        line_total = qty * price
        grand_total += line_total

        name = str(p.get_name).encode("latin-1", "replace").decode("latin-1")
        c.drawString(50, y, name[:40])
        c.drawString(280, y, str(qty))
        c.drawString(350, y, f"${price:,.2f}")
        c.drawString(440, y, f"${line_total:,.2f}")
        y -= 20

    # Grand total
    y -= 5
    c.line(50, y, 540, y)
    y -= 25
    c.setFont("Helvetica-Bold", 13)
    c.drawString(350, y, "TOTAL:")
    c.drawString(440, y, f"${grand_total:,.2f}")

    c.save()


def _save_on_exit():
    products = list(_get_products()) if _get_products else []
    if not products:
        print("\nNo products, so no PDF was created.")
        return

    logs_dir = Path(__file__).resolve().parent.parent / "logs"
    logs_dir.mkdir(exist_ok=True)
    path = logs_dir / f"report_{datetime.now():%Y-%m-%d_%H-%M-%S}.pdf"
    create_inventory_pdf(products, path)
    print(f"\nPDF saved to {path}")


def start_pdf_capture():
    global _started
    if not _started:
        _started = True
        atexit.register(_save_on_exit)