from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def processPayment(self):
        pass

class Discount(ABC):
    @abstractmethod
    def calculate(self, price):
        pass

class VIPDiscount(Discount):
    def calculate(self, price):
        return price * 0.50

class NoDiscount(Discount):
    def calculate(self, price):
        return price

def main():
    print()
    price = float(input("Introduce el precio del producto: "))
    print()
    
    vip_discount = VIPDiscount()
    no_discount = NoDiscount()
    
    vip_price = vip_discount.calculate(price)
    no_discount_price = no_discount.calculate(price)
    
    print(f"Precio original: {price}")
    print()
    print(f"Descuento VIP: Tu precio final es de {vip_price} mi bro")
    print()
    print(f"Sin Descuento: Tu precio es de {no_discount_price} no hay descuento para ti mi bro <3")
    print()

if __name__ == "__main__":
    main()