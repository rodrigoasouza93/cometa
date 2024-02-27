from fastapi.responses import JSONResponse

class PlaceOrderController:
    def __init__(self, place_order_usecase):
        self.place_order_usecase = place_order_usecase

    def handle(self, request):
        try:
            order_id = self.place_order_usecase.execute(request.dict())
            return JSONResponse(status_code=201, content={"order_id": order_id.__str__()})
        except Exception as e:
            if str(e) == "Beer not found":
                return JSONResponse(status_code=400, content={"message": str(e)})
            return JSONResponse(status_code=500, content={"message": str(e)})