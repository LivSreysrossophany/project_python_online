from colorama import Fore, Style, init
class Product:
    def __init__(
        self,
        id,
        name,
        price,
        category,
        quantity,
        supplier,
        description
    ):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__category = category
        self.__quantity = quantity
        self.__supplier = supplier
        self.__description = description
    # ID
    @property
    def get_id(self):
        return self.__id
    # Name
    @property
    def get_name(self):
        return self.__name
    @get_name.setter
    def set_name(self, name):
        self.__name = name
    # Price
    @property
    def get_price(self):
        return self.__price
    @get_price.setter
    def set_price(self, price):
        self.__price = price
    # Category
    @property
    def get_category(self):
        return self.__category
    @get_category.setter
    def set_category(self, category):
        self.__category = category
    # Quantity
    @property
    def get_quantity(self):
        return self.__quantity
    @get_quantity.setter
    def set_quantity(self, quantity):
        self.__quantity = quantity
    # Supplier
    @property
    def get_supplier(self):
        return self.__supplier
    @get_supplier.setter
    def set_supplier(self, supplier):
        self.__supplier = supplier
    # Description
    @property
    def get_description(self):
        return self.__description
    @get_description.setter
    def set_description(self, description):
        self.__description = description
    # Display
    def display(self):
        print(f"ID: {self.get_id}")
        print(f"Name: {self.get_name}")
        print(f"Price: ${self.get_price}")
        print(f"Category: {self.get_category}")
        print(f"Quantity: {self.get_quantity}")
        print(f"Supplier: {self.get_supplier}")
        print(f"Description: {self.get_description}")
        print(Fore.CYAN+"---------------------------")