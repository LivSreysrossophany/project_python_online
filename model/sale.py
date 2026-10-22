from model.base import Base


class Sale(Base):
    def __init__(self, id, product_id, quantity):
        super().__init__(id)
        self.product_id = product_id
        self.quantity = quantity

    def __str__(self):
        return (
            f"Sale ID: {self.id}, "
            f"Product ID: {self.product_id}, "
            f"Quantity: {self.quantity}"
        )