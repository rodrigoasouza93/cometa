from unittest import TestCase
from unittest.mock import create_autospec, patch
from application.protocols.beerRepo import BeerRepoInterface
from application.protocols.orderRepo import OrderRepoInterface
from application.usecases.order.placeOrder import PlaceOrderUseCase

class TestPlaceOrder(TestCase):
    beerRepo: BeerRepoInterface
    orderRepo: OrderRepoInterface


    def setUp(self):
        super().setUp()
        self.beerRepo = create_autospec(BeerRepoInterface)
        self.orderRepo = create_autospec(OrderRepoInterface)
        self.placeOrderUseCase = PlaceOrderUseCase(self.beerRepo, self.orderRepo)

    def test_should_call_beer_repo_find(self):
        with patch("application.usecases.order.placeOrder.Order") as order:
            self.beerRepo.find.return_value = {"name": "Heineken", "price": 2.5, "stock": 10, "id": "1", "style": "Pilsner"}
            self.placeOrderUseCase.execute({"customer_name": "1", "beer_id": "1"})
            self.beerRepo.find.assert_called_once_with("1")
    
    def test_should_raise_error_if_beer_not_found(self):
        self.beerRepo.find.return_value = None
        with self.assertRaises(ValueError) as context:
            self.placeOrderUseCase.execute({"customer_name": "1", "beer_id": "1"})
        self.assertEqual(str(context.exception), "Beer not found")

    def test_should_call_order_repo_create(self):
        with patch("application.usecases.order.placeOrder.Order") as order:
            self.beerRepo.find.return_value = {"name": "Heineken", "price": 2.5, "stock": 10, "id": "1", "style": "Pilsner"}
            self.placeOrderUseCase.execute({"customer_name": "1", "beer_id": "1"})
            self.orderRepo.create.assert_called_once_with(order("1", {"name": "Heineken", "price": 2.5, "stock": 10, "id": "1", "style": "Pilsner"}))