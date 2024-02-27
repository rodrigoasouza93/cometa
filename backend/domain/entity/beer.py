import uuid

class Beer:
    def __init__(self, name: str, style: str, stock: int, price: float):
        self.name = name
        self.style = style
        self.stock = stock
        self.price = price
        self.id = uuid.uuid4()
        if self.validate() is not None:
            raise ValueError(self.validate())

    def validate(self):
        if self.name == "":
            return "Name is required"
        if self.style == "":
            return "Style is required"
        if self.stock < 0:
            return "Stock must be greater than or equal to 0"
        if self.price < 0:
            return "Price must be greater than or equal to 0"
        return None
