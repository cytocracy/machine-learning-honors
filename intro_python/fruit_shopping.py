
def totalFruitCost(fruitBasket, fruitCosts):
    cost = 0
    for fruit in fruitBasket:
        if fruit in fruitCosts:
            cost += fruitCosts[fruit]

    return cost


if __name__=="__main__":
    fruits = []
    fruits.append("banana")
    fruits.append("apple")
    fruits.append("apple")
    fruits.append("mango")

    applePrice = 2
    pearPrice = 5
    bananaPrice = 1
    fruitCost = {
        "apple": 2,
        "pear": 5,
        "banana": 1
    }
    fruitCost["mango"] = 7

    print(totalFruitCost(fruits, fruitCost))