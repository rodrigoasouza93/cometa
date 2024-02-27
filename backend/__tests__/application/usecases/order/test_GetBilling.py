from unittest import TestCase
from unittest.mock import create_autospec
from application.protocols.orderRepo import OrderRepoInterface
from application.usecases.order.getBilling import GetBillingUseCase
from domain.entity.beer import Beer
from domain.entity.order import Order

class TestGetBilling(TestCase):
    orderRepo: OrderRepoInterface


    def setUp(self):
        super().setUp()
        self.orderRepo = create_autospec(OrderRepoInterface)
        self.getBillingUseCase = GetBillingUseCase(self.orderRepo)

    def test_should_call_order_repo_listUnpaid(self):
        self.orderRepo.listUnpaid.return_value = []
        self.getBillingUseCase.execute()
        self.orderRepo.listUnpaid.assert_called_once_with()

    def test_should_return_totalBilling(self):
        beer = Beer("Heineken", "Pilsner", 2, 10)
        order = Order("John Doe", beer)
        self.orderRepo.listUnpaid.return_value = [order]
        self.assertEqual(self.getBillingUseCase.execute()["totalBilling"], 10)

    def test_should_return_billingByCustomer(self):
        beer = Beer("Heineken", "Pilsner", 2, 10)
        order = Order("John Doe", beer)
        order2 = Order("Jane Doe", beer)
        self.orderRepo.listUnpaid.return_value = [order, order2]
        self.assertEqual(self.getBillingUseCase.execute()["billingByCustomer"], {"John Doe": 10, "Jane Doe": 10})

    def test_should_return_customers(self):
        beer = Beer("Heineken", "Pilsner", 2, 10)
        order = Order("John Doe", beer)
        order2 = Order("Jane Doe", beer)
        self.orderRepo.listUnpaid.return_value = [order, order2]
        self.assertEqual(self.getBillingUseCase.execute()["customers"], 2)

    def test_should_return_totalDividedBetweenCustomers(self):
        beer = Beer("Heineken", "Pilsner", 2, 10)
        beer2 = Beer("Any", "Pilsner", 2, 5)
        order = Order("John Doe", beer)
        order2 = Order("Jane Doe", beer2)
        self.orderRepo.listUnpaid.return_value = [order, order2]
        self.assertEqual(self.getBillingUseCase.execute()["totalDividedBetweenCustomers"], 7.5)
    

    