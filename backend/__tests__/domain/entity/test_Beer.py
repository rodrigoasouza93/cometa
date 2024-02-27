from unittest import TestCase

from domain.entity.beer import Beer

class TestBeer(TestCase):
    def test_should_create_a_beer(self):
        beer = Beer("Heineken", "Pilsner", 10, 2.5)
        self.assertEqual(beer.name, "Heineken")
        self.assertEqual(beer.style, "Pilsner")
        self.assertEqual(beer.stock, 10)
        self.assertEqual(beer.price, 2.5)
    
    def test_should_raise_an_error_when_name_is_empty(self):
        with self.assertRaises(ValueError) as context:
            Beer("", "Pilsner", 10, 2.5)
        self.assertEqual(str(context.exception), "Name is required")

    def test_should_raise_an_error_when_style_is_empty(self):
        with self.assertRaises(ValueError) as context:
            Beer("Heineken", "", 10, 2.5)
        self.assertEqual(str(context.exception), "Style is required")
    
    def test_should_raise_an_error_when_stock_is_negative(self):
        with self.assertRaises(ValueError) as context:
            Beer("Heineken", "Pilsner", -10, 2.5)
        self.assertEqual(str(context.exception), "Stock must be greater than or equal to 0")
    
    def test_should_raise_an_error_when_price_is_negative(self):
        with self.assertRaises(ValueError) as context:
            Beer("Heineken", "Pilsner", 10, -2.5)
        self.assertEqual(str(context.exception), "Price must be greater than or equal to 0")
    