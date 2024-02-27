from unittest import TestCase
from unittest.mock import create_autospec, patch
from application.protocols.orderRepo import OrderRepoInterface
from application.usecases.order.processPayment import ProcessPaymentUseCase
from domain.entity.beer import Beer
from domain.entity.order import Order

class TestPlaceOrder(TestCase):
    orderRepo: OrderRepoInterface


    def setUp(self):
        super().setUp()
        self.orderRepo = create_autospec(OrderRepoInterface)
        self.processPaymentUseCase = ProcessPaymentUseCase(self.orderRepo)

    def test_should_call_order_repo_listUnpaid(self):
        self.orderRepo.listUnpaid.return_value = []
        with self.assertRaises(ValueError) as context:
            self.processPaymentUseCase.execute({"customer_name": "1", "payment_type": "MY_ORDERS", "value": 1})
        self.assertEqual(str(context.exception), "No unpaid orders found")

    def test_should_raise_error_if_value_is_less_than_value_to_pay(self):
        beer = Beer("Heineken", "Pilsner", 10, 5)
        order = Order("1", beer)
        self.orderRepo.listUnpaid.return_value = [order]
        with self.assertRaises(ValueError) as context:
            self.processPaymentUseCase.execute({"customer_name": "1", "payment_type": "MY_ORDERS", "value": 1})
        self.assertEqual(str(context.exception), "The value is less than the value to pay")

    def test_should_raise_error_if_value_is_greater_than_value_to_pay(self):
        beer = Beer("Heineken", "Pilsner", 10, 5)
        order = Order("1", beer)
        self.orderRepo.listUnpaid.return_value = [order]
        with self.assertRaises(ValueError) as context:
            self.processPaymentUseCase.execute({"customer_name": "1", "payment_type": "MY_ORDERS", "value": 6})
        self.assertEqual(str(context.exception), "The value is greater than the value to pay")

    def test_should_call_order_repo_update(self):
        beer = Beer("Heineken", "Pilsner", 10, 5)
        order = Order("1", beer)
        self.orderRepo.listUnpaid.return_value = [order]
        self.processPaymentUseCase.execute({"customer_name": "1", "payment_type": "MY_ORDERS", "value": 5})
        self.orderRepo.update.assert_called_once()
