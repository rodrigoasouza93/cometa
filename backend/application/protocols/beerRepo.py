from typing import List

from domain.entity.beer import Beer

class ListBeersOutput:
    def __init__(self, beers: List[Beer]):
        self.beers = beers

class BeerRepoInterface:
    def list(self) -> ListBeersOutput:
        pass
    def find(self, id: str) -> Beer:
        pass