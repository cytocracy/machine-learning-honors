class FruitShop:
    def __init__(self, name, fruitPrices):
        self.fruitPrices = fruitPrices
        self.name = name

    def addFruit(self, newFruit, newPrice):
        self.fruitPrices[newFruit] = newPrice

    def getCostPerPound(self, fruit):
        if fruit in self.fruitPrices:
            return self.fruitPrices[fruit]
        else:
            print("Sorry, no", fruit, "in stock.")

    def getPriceOfOrder(self, orderList):
        pass
    
    def getName(self):
        return self.name