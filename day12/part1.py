def importData():
    with open('test_input.txt') as input_file:
        inputDataArray = input_file.readlines()
    cleanInputDataArray = []
    for line in inputDataArray:
        cleanInputDataArray.append(line.replace("\n", ""))
    return cleanInputDataArray

def calculateShortestPath(inputDataArray):

    nodeList = []

    for y in range(len(inputDataArray)):
        for x in range(len(inputDataArray[0])):
            nodeList.append(node(inputDataArray[y][x],x,y,len(inputDataArray[0]),len(inputDataArray)))
    
    

    return 0

class node:

    def __init__(self, height, x, y, lenX, lenY):
        
        self.x = x
        self.y = y
        self.height = ord(height) - 96

        self.pathCost = 100000000
        self.previousNode = -1
        self.active = False

        self.start = False
        self.end = False

        self.id = idGen(x,y,lenX)

        self.neighbours = []

        if(self.x > 0):
            self.neighbours.append(idGen(x-1,y,lenX))
        if(self.x < lenX-1):
            self.neighbours.append(idGen(x+1,y,lenX))
        if(self.y > 0):
            self.neighbours.append(idGen(x,y-1,lenX))
        if(self.y < lenY-1):
            self.neighbours.append(idGen(x,y+1,lenX))

def idGen(x,y,lenX):
    return x + (y*lenX)
               
if __name__ == '__main__':
    print(calculateShortestPath(importData()))