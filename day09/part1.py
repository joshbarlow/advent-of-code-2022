import re

def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    cleanInputDataArray = []
    for line in inputDataArray:
        cleanInputDataArray.append(line.replace("\n", ""))
    return cleanInputDataArray

def calcString(inputDataArray):

    head = [0,0]
    tail = [0,0]

    visitedArray = ['0-0']

    for line in inputDataArray:

        spliLine = line.split(' ')
        
        direction = [0,0]

        if(spliLine[0] == 'R'):
            direction = [1,0]
        if(spliLine[0] == 'L'):
            direction = [-1,0]
        if(spliLine[0] == 'U'):
            direction = [0,1]
        if(spliLine[0] == 'D'):
            direction = [0,-1]

        steps = int(spliLine[1])

        for step in range(steps):

            head[0] += direction[0]
            head[1] += direction[1]

            tail = SIM(head,tail)

            positionString = (str(tail[0]) + '-' + str(tail[1]))

            visitedArray.append(positionString)
        
    visitedCount = len(set(visitedArray))

    return visitedCount

def SIM(head,tail):

    xDist = abs(head[0] - tail[0])
    yDist = abs(head[1] - tail[1])

    newX = tail[0]
    newY = tail[1]

    # print('xdist: ' + str(xDist) + ' - ydist: ' + str(yDist))

    if ((xDist == 2) or (yDist == 2)):
        if(xDist == 0):
            newY += int((head[1] - tail[1])/2)
        elif(yDist == 0):
            newX += int((head[0] - tail[0])/2)
        
        elif((xDist == 1) and (yDist ==2)):
            newX += int(head[0] - tail[0])
            newY += int((head[1] - tail[1])/2)
        elif((xDist == 2) and (yDist == 1)):
            newY += int(head[1] - tail[1])
            newX += int((head[0] - tail[0])/2)
        elif((xDist == 2) and (yDist == 2)):
            newY += int((head[1] - tail[1])/2)
            newX += int((head[0] - tail[0])/2)
    
    # print(str(tail[0]) + ',' + str(tail[1]) + ' -> ' + str(newX) + ',' + str(newY) + ' (Head: ' + str(head[0]) + ',' + str(head[1]) + ')')

    return [newX,newY]

if __name__ == '__main__':
    print(calcString(importData()))