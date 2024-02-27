from unittest import TestCase
from domain.entity.order import Order

from domain.entity.beer import Beer

class TestOrder(TestCase):
    def test_should_create_an_order(self):
        order = Order("1", Beer("Heineken", "Pilsner", 10, 2.5))
        self.assertEqual(order.customer_name, "1")
        self.assertEqual(order.beer.name, "Heineken")
        self.assertEqual(order.beer.style, "Pilsner")
        self.assertEqual(order.beer.stock, 10)
        self.assertEqual(order.beer.price, 2.5)
        self.assertIsNotNone(order.id)
        self.assertEqual(order.total, 2.5)

    def test_should_not_create_an_order_without_customer_name(self):
        with self.assertRaises(ValueError) as context:
            Order("", Beer("Heineken", "Pilsner", 10, 2.5))
        self.assertEqual(str(context.exception), "Customer Name is required")

    def test_should_not_create_an_order_without_beer(self):
        with self.assertRaises(ValueError) as context:
            Order("1", None)
        self.assertEqual(str(context.exception), "Beer is required")

    def test_should_mark_order_as_paid(self):
        order = Order("1", Beer("Heineken", "Pilsner", 10, 2.5))
        order.paid()
        self.assertEqual(order.status, "PAID")