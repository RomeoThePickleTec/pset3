# Bien : Agregar descuentos sin modificar la clase original
# Ahora podemos agregar más descuentos creando nuevas clases
class Discount_Good:
    def calculate(self, amount):
        return amount

class StanderDiscount(Discount):

    def calculate(self, amount):
        return amount * 0.9

class VIPDiscount(Discount):
    def calculate(self, amount):
        return amount * 0.8

