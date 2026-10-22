from model.base import Base


class Category(Base):
    def __init__(self, id, name):
        super().__init__(id)
        self.name = name

    def __str__(self):
        return f"ID: {self.id}, Category: {self.name}"