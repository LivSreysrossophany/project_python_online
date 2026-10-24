from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

def ask_text(prompt, default=None):
    """Ask for text; use default if the user just presses Enter."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        if default is not None:
            return default
        print("  Please enter a value.")


def ask_int(prompt):
    while True:
        try:
            value = int(input(prompt).strip())
            if value > 0:
                return value
            print("  Quantity must be greater than 0.")
        except ValueError:
            print("  Please enter a whole number.")


def ask_float(prompt):
    while True:
        try:
            value = float(input(prompt).strip())
            if value >= 0:
                return value
            print("  Price cannot be negative.")
        except ValueError:
            print("  Please enter a number (e.g. 2.50).")


def get_receipt_data():
    print("=== Receipt Generator ===\n")
    receipt_no = ask_text("Receipt No (Enter for R-0001): ", default="R-0001")
    customer = ask_text("Customer name: ")

    items = []
    print("\nAdd items (leave item name empty to finish)")
    while True:
        name = input(f"\nItem #{len(items) + 1} name: ").strip()
        if not name:
            if items:
                break
            print("  Add at least one item.")
            continue
        qty = ask_int("  Quantity: ")
        price = ask_float("  Price per unit: ")
        items.append({"name": name, "qty": qty, "price": price})

    return {
        "receipt_no": receipt_no,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "customer": customer,
        "items": items,
    }


def create_receipt_pdf(data, filename="receipt.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    y = height - 60

    # Header
    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, y, "RECEIPT")
    y -= 30
    c.setFont("Helvetica", 11)
    c.drawString(50, y, f"Receipt No: {data['receipt_no']}")
    y -= 18
    c.drawString(50, y, f"Date: {data['date']}")
    y -= 18
    c.drawString(50, y, f"Customer: {data['customer']}")
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
    for item in data["items"]:
        # Start a new page if we run out of space
        if y < 80:
            c.showPage()
            y = height - 60
            y = table_header(y)
            c.setFont("Helvetica", 11)

        line_total = item["qty"] * item["price"]
        grand_total += line_total
        c.drawString(50, y, item["name"][:40])
        c.drawString(280, y, str(item["qty"]))
        c.drawString(350, y, f"${item['price']:,.2f}")
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
    print(f"\nSaved {filename}")


if __name__ == "__main__":
    receipt = get_receipt_data()
    filename = f"receipt_{receipt['receipt_no']}.pdf"
    create_receipt_pdf(receipt, filename)