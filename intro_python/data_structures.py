newList = []
newList.append(5)
newList.append(70)
newList.append(12)
print(newList)

newList.remove(70)
print(newList)

#remove by index
newList.pop() #removes last thing

#dictionary
flowers = ["tulip", "tulip", "dandelion", "tulip", "rose", "rose"]
numFlowers = {}

for flower in flowers:
    if flower in numFlowers:
        numFlowers[flower] += 1
    else:
        numFlowers[flower] = 1
print(numFlowers)

flowerLocations = {}
for i in range(len(flowers)):
    flower = flowers[i]
    if flower in flowerLocations:
        flowerLocations[flower].append(i)
    else:
        flowerLocations[flower] = [i]


# tuples
coordinate = (2,4)
print(coordinate[0])

new2DList = []
for r in range(7):
    newRow = []
    for c in range(10):
        newRow.append(r*c)
    new2DList.append(newRow)
print(new2DList)

numEvens = 0
for r in range(len(new2DList)):
    for c in range(len(new2DList[0])):
        if new2DList[r][c]%2 == 0:
            numEvens += 1
print(numEvens)