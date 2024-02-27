from presentation.controllers.beer.listBeers import ListBeersController
from application.usecases.beer.listBeers import ListBeersUseCase
from infra.beer.memoryBeerRepo import MemoryBeerRepo

def makeListBeersUseCase():
    beerRepo = MemoryBeerRepo.instance()
    return ListBeersUseCase(beerRepo)

def makeListBeersController():
    return ListBeersController(makeListBeersUseCase())