import re

def importData():
    with open('test_input.txt') as input_file:
        inputDataArray = input_file.readlines()
    cleanInputDataArray = []
    for line in inputDataArray:
        cleanInputDataArray.append(line.replace("\n", ""))
    return cleanInputDataArray

def calcSize(inputDataArray):

    mapWidth = len(inputDataArray[0])
    mapHeight = len(inputDataArray)

    mapArray = []

    for line in inputDataArray:
        rowArray = []
        for char in line:
            rowArray.append(int(char))
        mapArray.append(rowArray)

    print('Map is ' + str(mapWidth) + 'x' + str(mapHeight))
    # print(mapArray)

    totalVisible = 0

    for y in range(mapHeight):
        for x in range(mapWidth):
            if (caclulateVisible(x,y,mapWidth,mapHeight,mapArray)):
                totalVisible += 1
    
    return totalVisible

def caclulateVisible(treeX, treeY, mapWidth, mapHeight, mapArray):

    if ( (treeX == 0) or (treeY == 0) or (treeX == mapWidth-1) or (treeY == mapHeight -1) ):
        return False
    
    # iterarate through each row/column and check
    # for any trees as high or higher than current.

    return True

if __name__ == '__main__':
    print(calcSize(importData()))