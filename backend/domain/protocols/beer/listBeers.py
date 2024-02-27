from typing import List

from domain.entity.beer import Beer

class ListBeersOutput:
    def __init__(self, beers: List[Beer]):
        self.beers = beers

class ListBeers:
    def __init__(self, beer_repository):
        self.beer_repository = beer_repository

    def execute(self) -> ListBeersOutput:
        return self.beer_repository.list()