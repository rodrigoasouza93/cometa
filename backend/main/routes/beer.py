from main.factories.beer.listBeersController import makeListBeersController

from fastapi import APIRouter

BeerRouter = APIRouter(
    prefix="/beers",
    tags=["beers"]
)

@BeerRouter.get("/")
def index():
    controller = makeListBeersController()
    return controller.handle()