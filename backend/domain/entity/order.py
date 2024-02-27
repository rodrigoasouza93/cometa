import uuid

class Order:
    def __init__(self, customer_name, beer):
        self.customer_name = customer_name
        self.beer = beer
        if self.beer is not None:
            self.beer.price = beer.price
            self.total = beer.price
        self.id = uuid.uuid4()
        self.status = "PENDING"
        if self.validate() is not None:
            raise ValueError(self.validate())
        

    def validate(self):
        if self.customer_name == "":
            return "Customer Name is required"
        if self.beer is None:
            return "Beer is required"
        return None
    
    def paid(self):
        self.status = "PAID"