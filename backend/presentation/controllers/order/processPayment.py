from fastapi.responses import JSONResponse, Response
from fastapi import status

class ProcessPaymentController:
    def __init__(self, process_payment_usecase):
        self.process_payment_usecase = process_payment_usecase

    def handle(self, request):
        try:
            self.process_payment_usecase.execute(request.dict())
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            if str(e) == "No unpaid orders found":
                return JSONResponse(status_code=404, content={"message": str(e)})
            if str(e) == "The value is less than the value to pay":
                return JSONResponse(status_code=400, content={"message": str(e)})
            if str(e) == "The value is greater than the value to pay":
                return JSONResponse(status_code=400, content={"message": str(e)})
            return JSONResponse(status_code=500, content={"message": str(e)})