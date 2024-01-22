myFile = open('mystery.txt')
# print(myFile)
stringFile = myFile.read()
words = stringFile.split()
sentences = stringFile.splitlines()

with open("mystery.txt") as f:
    lines = f.read().splitlines()