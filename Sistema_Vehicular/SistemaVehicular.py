class Vehicle:
    def transportar(self):
        print("Transporta...")
    def numeroRuedas(self):
        print("Por lo menos 1")

class Car(Vehicle):
    def transportar(self):
        print("BRUMMMM.... BRUUUUURMMM...")
    def numeroRuedas(self):
        print("4")

class Bicyle(Vehicle):
    def transportar(self):
        print("Voy a cruzar en rojo si me atropellan es culpa de ustedes")
    def numeroRuedas(self):
        print("2")

class TransportSystem:
    def __init__(self, vehiculo:Vehicle):
        self.vehiculo = vehiculo

    def usarVehiculo(self):
        self.vehiculo.transportar()

    def contarLlantas(self):
        self.vehiculo.numeroRuedas()

vehiculo = Car()
JuanTrucks = TransportSystem(vehiculo)
JuanTrucks.usarVehiculo()
JuanTrucks.contarLlantas()