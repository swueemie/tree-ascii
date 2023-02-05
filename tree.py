from random import *

sizeX = 10
sizeY = 50
numberOfTrees = 5
treeSize = 4

viewPort = [[" " for x in range(sizeY)] for y in range(sizeX)]
possibleLeaf= 'ç=éà@}=*§'

def printViewPort():
    for i in range(sizeX):
        for j in range(sizeY):
            print(viewPort[i][j], end=" ")
        print()

def printGround():
    i = sizeX - 1
    for j in range(sizeY):
        viewPort[i][j] = "_"

def createTree(floors):
    startingPointX = randint(0, sizeX - floors - 3)
    startingPointY = randint(floors - 1, sizeY - floors)
    leafType = choice(possibleLeaf)
    leafCounter = 1
    viewPort[startingPointX][startingPointY] = leafType
    for i in range(1, floors):
        leafCounter += 2
        for j in range(leafCounter):
            viewPort[startingPointX + i][startingPointY - j + i] = leafType
    
    for i in range(startingPointX + floors, sizeX):
        viewPort[i][startingPointY] = "|"


for i in range(numberOfTrees):
    createTree(randint(2,treeSize))

printGround()
printViewPort()