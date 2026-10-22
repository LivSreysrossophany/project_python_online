from model.base import Base


class Supplier(Base):
    def __init__(self, id, name, phone, email):
        super().__init__(id)
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return (
            f"ID: {self.id}, "
            f"Supplier: {self.name}, "
            f"Phone: {self.phone}, "
            f"Email: {self.email}"
        )