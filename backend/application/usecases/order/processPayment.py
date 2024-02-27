from domain.protocols.order.processPayment import ProcessPaymentInterface, ProcessPaymentInput
from domain.entity.order import Order
from application.protocols.orderRepo import OrderRepoInterface

class ProcessPaymentUseCase(ProcessPaymentInterface):
    def __init__(self, order_repo: OrderRepoInterface):
        self.order_repo = order_repo

    def execute(self, input: ProcessPaymentInput):
        unpaidOrders = self.order_repo.listUnpaid()
        if len(unpaidOrders) == 0:
            raise ValueError("No unpaid orders found")
        totalBilling = 0
        billingByCustomer = {}
        customers = 0
        for order in unpaidOrders:
            totalBilling += order.beer.price
            if order.customer_name not in billingByCustomer:
                billingByCustomer[order.customer_name] = 0
            billingByCustomer[order.customer_name] += order.beer.price
        customers = billingByCustomer.keys().__len__()
        totalDividedBetweenCustomers = totalBilling / customers if customers > 0 else 0

        valueToPay = 0
        if input["payment_type"] == "MY_ORDERS":
            valueToPay = billingByCustomer[input["customer_name"]]
        elif input["payment_type"] == "DIVIDED":
            valueToPay = totalDividedBetweenCustomers

        if valueToPay > input["value"]:
            raise ValueError("The value is less than the value to pay")
        if valueToPay < input["value"]:
            raise ValueError("The value is greater than the value to pay")
        
        for order in unpaidOrders:
            if order.customer_name == input["customer_name"]:
                order.paid()
                self.order_repo.update(order)