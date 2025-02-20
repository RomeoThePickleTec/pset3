from abc import ABC, abstractmethod

class Discount:
    @abstractmethod
    def getDiscount(self, amount):
        pass

class StandardDiscount(Discount):

    def getDiscount(self, amount):
        return amount * 0.9

class VIPDiscount(Discount):
    def getDiscount(self, amount):
        return amount * 0.8


def main():
    standardClient = StandardDiscount()
    vipClient = VIPDiscount()
    amount = 100

    print(f"Original amount: {amount}")
    print("Standard client discount: ", standardClient.getDiscount(amount))
    print("VIP client discount: ", vipClient.getDiscount(amount))

if __name__ == "__main__":
    main()