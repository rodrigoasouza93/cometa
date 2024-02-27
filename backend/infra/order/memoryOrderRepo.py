from application.protocols.orderRepo import OrderRepoInterface
from domain.entity.order import Order

class MemoryOrderRepo(OrderRepoInterface):
    _instance = None
    def __init__(self):
        self.orders = []

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def create(self, order: Order):
        self.orders.append(order)
        return order.id
    
    def listUnpaid(self):
        return [order for order in self.orders if order.status == "PENDING"]
    
    def update(self, order: Order):
        for i in range(len(self.orders)):
            if self.orders[i].id == order.id:
                self.orders[i] = order
                break
        return order.id