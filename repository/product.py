class ProductRepository:

    def __init__(self):
        self.products = []
        self.categories = []
        self.suppliers = []
        self.stock_history = []

    def get_stock_history(self):
        return self.stock_history

    def add_stock_history(self, history):
         self.stock_history.append(history)
    def stock_entry(self, id, quantity):

            for product in self.products:

                if product.get_id == id:

                    product.set_quantity = product.get_quantity + quantity

                    self.stock_history.append(
                        f"Product {id}: +{quantity} stock entry"
                    )

                    return True

            return False
    def sales_order(self, id, quantity):

        for product in self.products:

            if product.get_id == id:

                if product.get_quantity < quantity:
                    return False

                product.set_quantity = product.get_quantity - quantity

                self.stock_history.append(
                    f"Product {id}: -{quantity} sales"
                )

                return True

        return False
    # Products
    def get_products(self):
        return self.products

    def add_product(self, product):
        self.products.append(product)

    # Categories
    def get_categories(self):
        return self.categories

    def add_category(self, category):
        self.categories.append(category)
    def stock_entry(self, id, quantity):
        for product in self.products:
            if product.get_id == id:
                product.set_quantity = product.get_quantity + quantity

                self.stock_history.append(
                    f"{product.get_name}: +{quantity} Stock Entry"
                )

                return True

        return False
    def stock_adjustment(self, id, quantity):

        for product in self.products:

            if product.get_id == id:
                product.set_quantity = quantity
                return True

        return False
    def purchase_order(self, id, quantity):
        for product in self.products:
            if product.get_id == id:
                product.set_quantity = product.get_quantity + quantity

                self.stock_history.append(
                    f"{product.get_name}: +{quantity} Purchase Order"
                )

                return True

        return False
    def sales_order(self, id, quantity):
        for product in self.products:
            if product.get_id == id:

                if product.get_quantity < quantity:
                    return False

                product.set_quantity = product.get_quantity - quantity

                self.stock_history.append(
                    f"{product.get_name}: -{quantity} Sales Order"
                )

                return True

        return False
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
        for product in self.products:
            if product.get_id == id:
                product.set_name = name
                product.set_price = price
                product.set_category = category
                product.set_quantity = quantity
                product.set_supplier = supplier
                product.set_description = description
                return True

        return False
    def remove_product(self, id):
        for product in self.products:

            if product.get_id == id:
                self.products.remove(product)
                return True

        return False
    # Search Product
    def search_product(self, keyword):
        results = []

        for product in self.products:
            if str(product.get_id) == str(keyword):
                results.append(product)
            elif keyword.lower() in product.get_name.lower():
                results.append(product)

        return results
    # Suppliers
    def get_suppliers(self):
        return self.suppliers

    def add_supplier(self, supplier):
        self.suppliers.append(supplier)