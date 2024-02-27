from unittest import TestCase
from unittest.mock import create_autospec, patch
from application.protocols.beerRepo import BeerRepoInterface
from application.usecases.beer.listBeers import ListBeersUseCase
from domain.entity.beer import Beer

class TestListBeers(TestCase):
    beerRepo: BeerRepoInterface

    def setUp(self):
        super().setUp()
        self.beerRepo = create_autospec(BeerRepoInterface)
        self.ListBeersUseCase = ListBeersUseCase(self.beerRepo)

    def test_should_return_a_list_of_available_beers(self):
        self.beerRepo.list.return_value = [
            Beer("Heineken", "Pilsner", 10, 10),
            Beer("Guinness", "Stout", 5, 3.5),
            Beer("Corona", "Pilsner", 15, 2.0),
            Beer("Spaten", "Pilsner", 0, 3.0),
        ]
        beers = self.ListBeersUseCase.execute()
        self.assertEqual(len(beers), 3)
        self.assertEqual(beers[0].name, "Heineken")
        self.assertEqual(beers[0].style, "Pilsner")
        self.assertEqual(beers[0].stock, 10)
        self.assertEqual(beers[0].price, 10)
        self.assertEqual(beers[1].name, "Guinness")
        self.assertEqual(beers[1].style, "Stout")
        self.assertEqual(beers[1].stock, 5)
        self.assertEqual(beers[1].price, 3.5)

    def test_should_return_an_empty_list_of_available_beers(self):
        self.beerRepo.list.return_value = [
            Beer("Spaten", "Pilsner", 0, 3.0),
        ]
        beers = self.ListBeersUseCase.execute()
        self.assertEqual(len(beers), 0)
        self.assertEqual(beers, [])