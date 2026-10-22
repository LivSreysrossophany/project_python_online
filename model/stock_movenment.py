from model.base import Base


class StockMovement(Base):
    def __init__(self, id, product_id, movement_type, quantity):
        super().__init__(id)
        self.product_id = product_id
        self.movement_type = movement_type
        self.quantity = quantity

    def __str__(self):
        return (
            f"Movement ID: {self.id}, "
            f"Product ID: {self.product_id}, "
            f"Type: {self.movement_type}, "
            f"Quantity: {self.quantity}"
        )