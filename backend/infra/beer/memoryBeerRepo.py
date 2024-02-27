from typing import Any
from application.protocols.beerRepo import BeerRepoInterface
from domain.entity.beer import Beer

class MemoryBeerRepo(BeerRepoInterface):
    _instance = None

    def __init__(self):
        self.beers = [
            Beer("Skol", "Pilsner", 5, 2),
            Beer("Brahma", "Pilsner", 5, 1),
            Beer("Heineken", "Pilsner", 7, 5),
            Beer("Stella Artois", "Pilsner", 7, 4),
        ]

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def list(self):
        return self.beers
    
    def find(self, id: str):
        for beer in self.beers:
            if beer.id.__str__() == id:
                return beer
        return None