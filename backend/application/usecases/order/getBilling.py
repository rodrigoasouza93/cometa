from domain.protocols.order.getBilling import GetBillingInterface

class GetBillingUseCase(GetBillingInterface):
    def __init__(self, order_repository):
        self.order_repository = order_repository

    def execute(self):
        orders = self.order_repository.listUnpaid()
        totalBilling = 0
        billingByCustomer = {}
        customers = 0
        for order in orders:
            totalBilling += order.beer.price
            if order.customer_name not in billingByCustomer:
                billingByCustomer[order.customer_name] = 0
            billingByCustomer[order.customer_name] += order.beer.price
        customers = billingByCustomer.keys().__len__()
        totalDividedBetweenCustomers = totalBilling / customers if customers > 0 else 0
        
        return {"totalBilling": totalBilling, "billingByCustomer": billingByCustomer, "customers": customers, "totalDividedBetweenCustomers": totalDividedBetweenCustomers}
