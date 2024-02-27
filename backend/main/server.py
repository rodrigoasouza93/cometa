from main.routes.beer import BeerRouter
from main.routes.order import OrderRouter

from fastapi import FastAPI

app = FastAPI()

app.include_router(BeerRouter)
app.include_router(OrderRouter)
