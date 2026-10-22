from model.product import Product
from colorama import Fore, Style, init
init(autoreset=True)
class ProductService:
    def __init__(self, repository):
        self.repository = repository
    # View Products
    def get_products(self):
        products = self.repository.get_products()
        if len(products) == 0:
            print(Fore.RED +"No Product Available")
            return
        for product in products:
            product.display()
    # Add Product
    def add_product(
        self,
        id,
        name,
        price,
        category,
        quantity,
        supplier,
        description
    ):
        product = Product(
            id,
            name,
            price,
            category,
            quantity,
            supplier,
            description
        )
        self.repository.add_product(product)
        print(Fore.YELLOW+"Product added successfully")
    # Update Product
    def update_product(
        self,
        id,
        name,
        price,
        category,
        quantity,
        supplier,
        description
    ):
        result = self.repository.update_product(
            id,
            name,
            price,
            category,
            quantity,
            supplier,
            description
        )
        if result:
            print(Fore.YELLOW +"Product updated successfully")
        else:
            print(Fore.RED +"Product not found")
    # Remove Product
    def remove_product(self, id):
        result = self.repository.remove_product(id)
        if result:
            print(Fore.YELLOW +"Product deleted successfully")
        else:
            print(Fore.RED +"Product not found")
    # Search Product
    def search_product(self, keyword):
        products = self.repository.search_product(keyword)
        if len(products) == 0:
            print(Fore.RED +"Product not found")
            return
        print(Fore.CYAN+"===========================================")
        print(Fore.CYAN+"|             Search Results              |")
        print(Fore.CYAN+"===========================================")
        for product in products:
            product.display()
    # Manage Categories
    def get_categories(self):
        categories = self.repository.get_categories()
        if len(categories) == 0:
            print(Fore.RED +"No Category Available")
            return
        print(Fore.CYAN+"===========================================")
        print(Fore.CYAN+"|               Categories                |")
        print(Fore.CYAN+"===========================================")
        for category in categories:
            print(f" {category}")
    def add_category(self, category):
        self.repository.add_category(category)
        print(Fore.YELLOW +"Category added successfully")
    # Manage Suppliers
    def get_suppliers(self):
        suppliers = self.repository.get_suppliers()
        if len(suppliers) == 0:
            print(Fore.RED +"No Supplier Available")
            return
        print(Fore.CYAN+"===========================================")
        print(Fore.CYAN+"|                 Suppliers               |")
        print(Fore.CYAN+"===========================================")
        for supplier in suppliers:
            print(f" {supplier}")
    def add_supplier(self, supplier):
        self.repository.add_supplier(supplier)
        print(Fore.YELLOW +"Supplier added successfully")
    # Stock Entry
    def stock_entry(self, id, quantity):
        result = self.repository.stock_entry(id, quantity)
        if result:
            print(Fore.YELLOW +"Stock entry successful")
        else:
            print(Fore.RED +"Product not found")
    # Stock Adjustment
    def stock_adjustment(self, id, quantity):
        result = self.repository.stock_adjustment(id, quantity)
        if result:
            print(Fore.YELLOW +"Stock adjusted successfully")
        else:
            print(Fore.RED +"Product not found")
    # Purchase Order
    def purchase_order(self, id, quantity):
        result = self.repository.purchase_order(id, quantity)
        if result:
            print(Fore.YELLOW +"Purchase order completed")
        else:
            print(Fore.RED +"Product not found")
    # Sales Order
    def sales_order(self, id, quantity):
        result = self.repository.sales_order(id, quantity)
        if result:
            print(Fore.YELLOW +"Sales order completed")
        else:
            print(Fore.RED +"Product not found or insufficient stock")
    # Low Stock Alert
    def low_stock_alert(self):
        products = self.repository.get_products()
        print(Fore.CYAN+"===========================================")
        print(Fore.CYAN+"|             Low Stock Alert             |")
        print(Fore.CYAN+"===========================================")
        found = False
        for product in products:
            if product.get_quantity <= 5:
                print(f"ID       : {product.get_id}")
                print(f"Name     : {product.get_name}")
                print(f"Quantity : {product.get_quantity}")
                print(Fore.CYAN+"====================================")
                found = True
        if not found:
            print(Fore.RED +"No low stock products")
    # Stock History
    def stock_history(self):
        history = self.repository.get_stock_history()
        if len(history) == 0:
            print("No Stock History")
            return
        print(Fore.CYAN+"=========================================")
        print(Fore.CYAN+"|             Stock History             |")
        print(Fore.CYAN+"=========================================")
        for item in history:
            print(item)
    # Reports
    def get_report(self):
        products = self.repository.get_products()
        if len(products) == 0:
            print(Fore.RED +"No Product Available")
            return
        total_products = len(products)
        total_quantity = 0
        total_value = 0
        print(Fore.CYAN+"========================================")
        print(Fore.CYAN+"|          INVENTORY REPORT            |")
        print(Fore.CYAN+"========================================")
        for product in products:
            total_quantity += product.get_quantity
            total_value += product.get_price * product.get_quantity
        print(f"Total Products       : {total_products}")
        print(f"Total Quantity       : {total_quantity}")
        print(f"Total Inventory Value: ${total_value:.2f}")
        print(Fore.CYAN+"===========================================")
        print(Fore.CYAN+"|          Product Details                |")
        print(Fore.CYAN+"===========================================")
        for product in products:
            value = product.get_price * product.get_quantity
            print(f"ID          : {product.get_id}")
            print(f"Name        : {product.get_name}")
            print(f"Category    : {product.get_category}")
            print(f"Price       : ${product.get_price:.2f}")
            print(f"Quantity    : {product.get_quantity}")
            print(f"Stock Value : ${value:.2f}")
            print(f"Supplier    : {product.get_supplier}")
            print(Fore.CYAN+"===========================================")