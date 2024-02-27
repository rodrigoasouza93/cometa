class ProcessPaymentInput:
    def __init__(self, customer_name: str, payment_type: str, value: float):
        self.customer_name = customer_name
        self.payment_type = payment_type
        self.value = value

class ProcessPaymentInterface:
    def execute(self, input: ProcessPaymentInput):
        pass