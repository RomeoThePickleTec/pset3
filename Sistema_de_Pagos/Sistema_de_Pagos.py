from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass

class PayPalPayment(Payment):
    def process_payment(self, amount: float):
        print(f"Pagando ${amount} con PayPal.")

class CreditCardPayment(Payment):
    def process_payment(self, amount: float):
        print(f"Pagando ${amount} con Tarjeta de Credito.")

class PaymentSystem:
    def __init__(self, payment: Payment):
        self.payment = payment

    def pay(self, amount: float):
        self.payment.process_payment(amount)

if __name__ == "__main__":
    paypal = PayPalPayment()
    credit_card = CreditCardPayment()

    payment_system = PaymentSystem(paypal)
    payment_system.pay(100.50)  

    payment_system = PaymentSystem(credit_card)
    payment_system.pay(250.75)  
