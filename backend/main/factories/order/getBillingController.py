from application.usecases.order.getBilling import GetBillingUseCase
from infra.order.memoryOrderRepo import MemoryOrderRepo
from presentation.controllers.order.getBilling import GetBillingController

def makeGetBillingUseCase():
    orderRepo = MemoryOrderRepo.instance()
    return GetBillingUseCase(orderRepo)

def makeGetBillingController():
    return GetBillingController(makeGetBillingUseCase())