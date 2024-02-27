from fastapi.responses import JSONResponse

class GetBillingController:
    def __init__(self, get_billing_usecase):
        self.get_billing_usecase = get_billing_usecase

    def handle(self):
        try:
            billing = self.get_billing_usecase.execute()
            return JSONResponse(status_code=200, content={"billing": billing})
        except Exception as e:
            return JSONResponse(status_code=500, content={"message": str(e)})