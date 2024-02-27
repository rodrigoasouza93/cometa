from application.usecases.order.processPayment import ProcessPaymentUseCase
from infra.order.memoryOrderRepo import MemoryOrderRepo
from presentation.controllers.order.processPayment import ProcessPaymentController

def makePlaceOrderUseCase():
    orderRepo = MemoryOrderRepo.instance()
    return ProcessPaymentUseCase(orderRepo)

def makeProcessPaymentController():
    return ProcessPaymentController(makePlaceOrderUseCase())