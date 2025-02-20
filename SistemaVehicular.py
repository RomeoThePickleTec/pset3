class Vehicle:
    def transportar(self):
        print("Transporta...")

class Car(Vehicle):
    def transportar(self):
        print("BRUMMMM.... BRUUUUURMMM...")


class Bicyle(Vehicle):
    def transportar(self):
        print("Voy a cruzar en rojo si me atropellan es culpa de ustedes")

class TransportSystem:
    def __init__(self, vehiculo:Vehicle):
        self.vehiculo = vehiculo

    def usarVehiculo(self):
        self.vehiculo.transportar()