from main.factories.order.placeOrderController import makePlaceOrderController
from main.factories.order.getBillingController import makeGetBillingController
from main.factories.order.processPaymentController import makeProcessPaymentController

from fastapi import APIRouter
from pydantic import BaseModel
from enum import Enum

class PlaceOrderInput(BaseModel):
    beer_id: str
    customer_name: str

class PaymentType(str, Enum):
    MY_ORDERS = "MY_ORDERS"
    DIVIDED = "DIVIDED"

class ProcessPaymentInput(BaseModel):
    customer_name: str
    payment_type: PaymentType
    value: float

OrderRouter = APIRouter(
    prefix="/orders",
    tags=["orders"]
)

@OrderRouter.post("/")
def index(request: PlaceOrderInput):
    controller = makePlaceOrderController()
    httpResponse = controller.handle(request)
    return httpResponse

@OrderRouter.get("/billing")
def billing():
    controller = makeGetBillingController()
    httpResponse = controller.handle()
    return httpResponse

@OrderRouter.post("/payment")
def payment(request: ProcessPaymentInput):
    controller = makeProcessPaymentController()
    httpResponse = controller.handle(request)
    return httpResponse