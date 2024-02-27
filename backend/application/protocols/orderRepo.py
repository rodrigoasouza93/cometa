from typing import List

from domain.entity.order import Order

class OrderRepoInterface:
    def create(self, order: Order) -> str:
        pass
    def listUnpaid(self) -> List[Order]:
        pass
    def update(self, order: Order):
        pass