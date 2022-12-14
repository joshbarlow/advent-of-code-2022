import re

def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    cleanInputDataArray = []
    for line in inputDataArray:
        cleanInputDataArray.append(line.replace("\n", ""))
    return cleanInputDataArray

def calcSize(inputDataArray):

    # testArray = [1,2,3,4,5]
    # print(testArray)
    # print(testArray[:3])
    # print(testArray[3:])

    mapWidth = len(inputDataArray[0])
    mapHeight = len(inputDataArray)

    mapArray = []

    for line in inputDataArray:
        rowArray = []
        for char in line:
            rowArray.append(int(char))
        mapArray.append(rowArray)

    print('Map is ' + str(mapWidth) + 'x' + str(mapHeight))
    print(mapArray)

    totalVisible = 0

    for y in range(mapHeight):
        for x in range(mapWidth):
            if (caclulateVisible(x,y,mapWidth,mapHeight,mapArray)):
                totalVisible += 1
    
    return totalVisible

def caclulateVisible(treeX, treeY, mapWidth, mapHeight, mapArray):

    if ( (treeX == 0) or (treeY == 0) or (treeX == mapWidth-1) or (treeY == mapHeight -1) ):
        return True
    
    treeHeight = mapArray[treeY][treeX]
    print('Tree at: ' + str(treeX) + 'x' + str(treeY) + ' - height: ' + str(treeHeight))

    leftHidden = False
    rightHidden = False
    upHidden = False
    downHidden = False

    # x visibility
    row = mapArray[treeY]

    # left
    leftArray = row[:treeX]
    print('Left: ' + str(leftArray))
    for value in leftArray:
        if (value >= treeHeight):
            leftHidden = True
    # right
    rightArray = row[treeX+1:]
    for value in rightArray:
        if (value >= treeHeight):
            rightHidden = True

    # y visibility
    col = []
    for y in range(mapHeight):
        col.append(mapArray[y][treeX])
    
    # up
    leftArray = col[:treeY]
    for value in leftArray:
        if (value >= treeHeight):
            upHidden = True
    # down
    rightArray = col[treeY+1:]
    for value in rightArray:
        if (value >= treeHeight):
            downHidden = True

    if (leftHidden and rightHidden and upHidden and downHidden):
        return False
    else:
        return True

if __name__ == '__main__':
    print(calcSize(importData()))