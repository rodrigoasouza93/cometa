class PlaceOrderInput:
    def __init__(self, customer_name: str, beer_id: str):
        self.customer_name = customer_name
        self.beer = beer_id

class PlaceOrderOutput:
    def __init__(self, id):
        self.id = id

class PlaceOrderInterface:
    def execute(self, input: PlaceOrderInput) -> PlaceOrderOutput:
        pass