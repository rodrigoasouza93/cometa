from application.usecases.order.placeOrder import PlaceOrderUseCase
from infra.order.memoryOrderRepo import MemoryOrderRepo
from infra.beer.memoryBeerRepo import MemoryBeerRepo
from presentation.controllers.order.placeOrder import PlaceOrderController

def makePlaceOrderUseCase():
    beerRepo = MemoryBeerRepo.instance()
    orderRepo = MemoryOrderRepo.instance()
    return PlaceOrderUseCase(beerRepo, orderRepo)

def makePlaceOrderController():
    return PlaceOrderController(makePlaceOrderUseCase())