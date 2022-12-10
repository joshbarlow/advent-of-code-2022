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
    k1 = [0,0]
    k2 = [0,0]
    k3 = [0,0]
    k4 = [0,0]
    k5 = [0,0]
    k6 = [0,0]
    k7 = [0,0]
    k8 = [0,0]
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

            k1 = SIM(head,k1)
            k2 = SIM(k1,k2)
            k3 = SIM(k2,k3)
            k4 = SIM(k3,k4)
            k5 = SIM(k4,k5)
            k6 = SIM(k5,k6)
            k7 = SIM(k6,k7)
            k8 = SIM(k7,k8)
            tail = SIM(k8,tail)

            print(str(head[0]) + ',' + str(head[1]) + ' - ' + str(k1[0]) + ',' + str(k1[1]) + ' - ' + str(k2[0]) + ',' + str(k2[1]) + ' - ' + str(k3[0]) + ',' + str(k3[1]) + ' - ' + str(k4[0]) + ',' + str(k4[1]) + ' - ' + str(k5[0]) + ',' + str(k5[1]) + ' - ' + str(k6[0]) + ',' + str(k6[1]) + ' - ' + str(k7[0]) + ',' + str(k7[1]) + ' - ' + str(k8[0]) + ',' + str(k8[1]) + ' - ' + str(tail[0]) + ',' + str(tail[1]))

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