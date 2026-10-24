import json
from datetime import datetime
from pathlib import Path

from model.product import Product

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def _load(filename):
    """Read a JSON list; return [] if the file is missing, empty or broken."""
    try:
        with (DATA_DIR / filename).open("r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def _save(filename, data):
    DATA_DIR.mkdir(exist_ok=True)
    with (DATA_DIR / filename).open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


class ProductRepository:
    def __init__(self):
        self.products = [
            Product(
                p["id"], p["name"], p["price"], p["category"],
                p["quantity"], p.get("supplier", ""), p.get("description", ""),
            )
            for p in _load("products.json")
        ]
        self.categories = [c["name"] for c in _load("categories.json")]

        suppliers = _load("suppliers.json")
        self.suppliers = [s["name"] for s in suppliers]
        self._supplier_info = {
            s["name"]: {"phone": s.get("phone", ""), "email": s.get("email", "")}
            for s in suppliers
        }

        self.history = _load("stock_history.json")

    # ---------- saving ----------
    def _save_products(self):
        _save("products.json", [
            {
                "id": p.get_id,
                "name": p.get_name,
                "price": p.get_price,
                "category": p.get_category,
                "quantity": p.get_quantity,
                "supplier": p.get_supplier,
                "description": p.get_description,
            }
            for p in self.products
        ])

    def _save_categories(self):
        _save("categories.json", [
            {"id": i, "name": name} for i, name in enumerate(self.categories, 1)
        ])

    def _save_suppliers(self):
        _save("suppliers.json", [
            {
                "id": i,
                "name": name,
                "phone": self._supplier_info.get(name, {}).get("phone", ""),
                "email": self._supplier_info.get(name, {}).get("email", ""),
            }
            for i, name in enumerate(self.suppliers, 1)
        ])

    def _log(self, product_id, move_type, quantity, note):
        next_id = max((h["id"] for h in self.history), default=0) + 1
        self.history.append({
            "id": next_id,
            "product_id": product_id,
            "type": move_type,
            "quantity": quantity,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "note": note,
        })
        _save("stock_history.json", self.history)

    def _find(self, id):
        return next((p for p in self.products if p.get_id == id), None)

    # ---------- products ----------
    def get_products(self):
        return self.products

    def add_product(self, product):
        if self._find(product.get_id):
            return False                      # duplicate ID
        self.products.append(product)
        self._save_products()
        return True

    def update_product(self, id, name, price, category, quantity, supplier, description):
        product = self._find(id)
        if not product:
            return False
        product.set_name = name
        product.set_price = price
        product.set_category = category
        product.set_quantity = quantity
        product.set_supplier = supplier
        product.set_description = description
        self._save_products()
        return True

    def remove_product(self, id):
        product = self._find(id)
        if not product:
            return False
        self.products.remove(product)
        self._save_products()
        return True

    def search_product(self, keyword):
        results = []
        for product in self.products:
            if str(product.get_id) == str(keyword):
                results.append(product)
            elif keyword.lower() in product.get_name.lower():
                results.append(product)
        return results

    # ---------- categories / suppliers ----------
    def get_categories(self):
        return self.categories

    def add_category(self, category):
        self.categories.append(category)
        self._save_categories()

    def get_suppliers(self):
        return self.suppliers

    def add_supplier(self, supplier):
        self.suppliers.append(supplier)
        self._save_suppliers()

    # ---------- stock ----------
    def stock_entry(self, id, quantity):
        product = self._find(id)
        if not product:
            return False
        product.set_quantity = product.get_quantity + quantity
        self._save_products()
        self._log(id, "STOCK_IN", quantity, "Stock entry")
        return True

    def purchase_order(self, id, quantity):
        product = self._find(id)
        if not product:
            return False
        product.set_quantity = product.get_quantity + quantity
        self._save_products()
        self._log(id, "PURCHASE", quantity, "Purchase order")
        return True

    def sales_order(self, id, quantity):
        product = self._find(id)
        if not product or product.get_quantity < quantity:
            return False
        product.set_quantity = product.get_quantity - quantity
        self._save_products()
        self._log(id, "SALE", quantity, "Sales order")
        return True

    def stock_adjustment(self, id, quantity):
        product = self._find(id)
        if not product:
            return False
        old = product.get_quantity
        product.set_quantity = quantity
        self._save_products()
        self._log(id, "ADJUSTMENT", quantity, f"Adjusted from {old} to {quantity}")
        return True

    # ---------- history ----------
    def get_stock_history(self):
        """Return readable lines for the Stock History screen."""
        lines = []
        for h in self.history:
            product = self._find(h["product_id"])
            name = product.get_name if product else f"Product {h['product_id']}"
            sign = {"SALE": "-", "ADJUSTMENT": "="}.get(h["type"], "+")
            lines.append(
                f"{h['date']} | {name} | {h['type']} {sign}{h['quantity']} | {h['note']}"
            )
        return lines