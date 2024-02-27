from domain.protocols.order.placeOrder import PlaceOrderInterface, PlaceOrderInput, PlaceOrderOutput
from domain.entity.order import Order
from application.protocols.beerRepo import BeerRepoInterface
from application.protocols.orderRepo import OrderRepoInterface

class PlaceOrderUseCase(PlaceOrderInterface):
    def __init__(self, beer_repo: BeerRepoInterface, order_repo: OrderRepoInterface):
        self.order_repo = order_repo
        self.beer_repo = beer_repo

    def execute(self, input: PlaceOrderInput) -> PlaceOrderOutput:
        beer = self.beer_repo.find(input["beer_id"])
        if beer is None:
            raise ValueError("Beer not found")
        order = Order(input["customer_name"], beer)
        self.order_repo.create(order)
        return order.id