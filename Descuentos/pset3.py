from abc import ABC, abstractmethod

class Discount:
    @abstractmethod
    def getDiscount(self, amount):
        pass

class StanderDiscount(Discount):

    def getDiscount(self, amount):
        return amount * 0.9

class VIPDiscount(Discount):
    def getDiscount(self, amount):
        return amount * 0.8

