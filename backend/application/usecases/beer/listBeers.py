from application.protocols.beerRepo import BeerRepoInterface
from domain.protocols.beer.listBeers import ListBeers, ListBeersOutput

class ListBeersUseCase(ListBeers):
    def __init__(self, beerRepository: BeerRepoInterface):
        self.beerRepository = beerRepository

    def execute(self) -> ListBeersOutput:
        beers = self.beerRepository.list()
        beersWithStock = self.filterBeersWithStock(beers)
        return beersWithStock
    
    def filterBeersWithStock(self, beers):
        return list(filter(lambda beer: beer.stock > 0, beers))