from model.base import Base


class Purchase(Base):
    def __init__(self, id, product_id, quantity, supplier_id):
        super().__init__(id)
        self.product_id = product_id
        self.quantity = quantity
        self.supplier_id = supplier_id

    def __str__(self):
        return (
            f"Purchase ID: {self.id}, "
            f"Product ID: {self.product_id}, "
            f"Quantity: {self.quantity}"
        )