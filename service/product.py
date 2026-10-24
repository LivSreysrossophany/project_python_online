from model.product import Product
from utils.color import success, error, warning, info, title


class ProductService:
    def __init__(self, repository):
        self.repository = repository

    # View Products
    def get_products(self):
        products = self.repository.get_products()
        if len(products) == 0:
            warning("No Product Available")
            return
        for product in products:
            product.display()

    def add_product(self, id, name, price, category, quantity, supplier, description):
        product = Product(id, name, price, category, quantity, supplier, description)
        if self.repository.add_product(product):
            success("Product added successfully")
        else:
            error("Product ID already exists")

    # Update Product
    def update_product(self, id, name, price, category, quantity, supplier, description):
        result = self.repository.update_product(
            id, name, price, category, quantity, supplier, description
        )
        if result:
            success("Product updated successfully")
        else:
            error("Product not found")

    # Remove Product
    def remove_product(self, id):
        result = self.repository.remove_product(id)
        if result:
            success("Product deleted successfully")
        else:
            error("Product not found")

    # Search Product
    def search_product(self, keyword):
        products = self.repository.search_product(keyword)
        if len(products) == 0:
            error("Product not found")
            return
        title("===========================================")
        title("|             Search Results              |")
        title("===========================================")
        for product in products:
            product.display()

    # Manage Categories
    def get_categories(self):
        categories = self.repository.get_categories()
        if len(categories) == 0:
            warning("No Category Available")
            return
        title("===========================================")
        title("|               Categories                |")
        title("===========================================")
        for category in categories:
            info(f" {category}")

    def add_category(self, category):
        self.repository.add_category(category)
        success("Category added successfully")

    # Manage Suppliers
    def get_suppliers(self):
        suppliers = self.repository.get_suppliers()
        if len(suppliers) == 0:
            warning("No Supplier Available")
            return
        title("===========================================")
        title("|                 Suppliers               |")
        title("===========================================")
        for supplier in suppliers:
            info(f" {supplier}")

    def add_supplier(self, supplier):
        self.repository.add_supplier(supplier)
        success("Supplier added successfully")

    # Stock Entry
    def stock_entry(self, id, quantity):
        result = self.repository.stock_entry(id, quantity)
        if result:
            success("Stock entry successful")
        else:
            error("Product not found")

    # Stock Adjustment
    def stock_adjustment(self, id, quantity):
        result = self.repository.stock_adjustment(id, quantity)
        if result:
            success("Stock adjusted successfully")
        else:
            error("Product not found")

    # Purchase Order
    def purchase_order(self, id, quantity):
        result = self.repository.purchase_order(id, quantity)
        if result:
            success("Purchase order completed")
        else:
            error("Product not found")

    # Sales Order
    def sales_order(self, id, quantity):
        result = self.repository.sales_order(id, quantity)
        if result:
            success("Sales order completed")
        else:
            error("Product not found or insufficient stock")

    # Low Stock Alert
    def low_stock_alert(self):
        products = self.repository.get_products()
        title("===========================================")
        title("|             Low Stock Alert             |")
        title("===========================================")
        found = False
        for product in products:
            if product.get_quantity <= 5:
                warning(f"Low stock: {product.get_name}")
                info(f"ID       : {product.get_id}")
                info(f"Name     : {product.get_name}")
                info(f"Quantity : {product.get_quantity}")
                title("====================================")
                found = True
        if not found:
            success("No low stock products")

    # Stock History
    def stock_history(self):
        history = self.repository.get_stock_history()
        if len(history) == 0:
            warning("No Stock History")
            return
        title("=========================================")
        title("|             Stock History             |")
        title("=========================================")
        for item in history:
            info(str(item))

    # Reports
    def get_report(self):
        products = self.repository.get_products()
        if len(products) == 0:
            warning("No Product Available")
            return
        total_products = len(products)
        total_quantity = 0
        total_value = 0
        title("========================================")
        title("|          INVENTORY REPORT            |")
        title("========================================")
        for product in products:
            total_quantity += product.get_quantity
            total_value += product.get_price * product.get_quantity
        info(f"Total Products       : {total_products}")
        info(f"Total Quantity       : {total_quantity}")
        info(f"Total Inventory Value: ${total_value:.2f}")
        title("===========================================")
        title("|          Product Details                |")
        title("===========================================")
        for product in products:
            value = product.get_price * product.get_quantity
            info(f"ID          : {product.get_id}")
            info(f"Name        : {product.get_name}")
            info(f"Category    : {product.get_category}")
            info(f"Price       : ${product.get_price:.2f}")
            info(f"Quantity    : {product.get_quantity}")
            info(f"Stock Value : ${value:.2f}")
            info(f"Supplier    : {product.get_supplier}")
            title("===========================================")