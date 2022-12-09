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

    scenicScores = []

    for y in range(mapHeight):
        for x in range(mapWidth):
            scenicScores.append(caclulateScore(x,y,mapWidth,mapHeight,mapArray))

    scenicScores.sort(reverse=True)

    return scenicScores[0]

def caclulateScore(treeX, treeY, mapWidth, mapHeight, mapArray):

    if ( (treeX == 0) or (treeY == 0) or (treeX == mapWidth-1) or (treeY == mapHeight -1) ):
        return 0
    
    treeHeight = mapArray[treeY][treeX]
    print('Tree at: ' + str(treeX) + 'x' + str(treeY) + ' - height: ' + str(treeHeight))

    leftHidden = False
    rightHidden = False
    upHidden = False
    downHidden = False

    # x visibility
    row = mapArray[treeY]
    col = []
    for y in range(mapHeight):
        col.append(mapArray[y][treeX])

    #arrays
    leftArray = row[:treeX]
    rightArray = row[treeX+1:]
    upArray = col[:treeY]
    downArray = col[treeY+1:]

    leftDist = len(leftArray)
    rightDist = len(rightArray)
    upDist = len(upArray)
    downDist = len(downArray)

    # left
    print('Left: ' + str(leftArray))
    for value in range(len(leftArray)):
        if (leftArray[value] >= treeHeight):
            leftHidden = True
            dist = (treeX - value)
            print('treex: ' + str(treeX) + ' - hitX: ' + str(value))
            if (dist < leftDist):
                leftDist = dist
    # right
    for value in range(len(rightArray)):
        if (rightArray[value] >= treeHeight):
            rightHidden = True
            dist = (value+1)
            if (dist < rightDist):
                rightDist = dist

    # up
    for value in range(len(upArray)):
        if (upArray[value] >= treeHeight):
            upHidden = True
            dist = (treeY - value)
            if (dist < upDist):
                upDist = dist

    # down
    for value in range(len(downArray)):
        if (downArray[value] >= treeHeight):
            downHidden = True
            dist = (value+1)
            if (dist < downDist):
                downDist = dist

    scenicScore = leftDist * rightDist * upDist *downDist

    return scenicScore

if __name__ == '__main__':
    print(calcSize(importData()))