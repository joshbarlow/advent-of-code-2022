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
    
    for x in nodeList:
        if(x.id == 0):
            x.pathCost = 0
            x.active = True
    
    count = 0
    lock = True
    FinalCost = 0

    while lock:

        lowestActiveNode = -1
        lowestActiveRisk = 100000

        for x in nodeList:
            if(x.active == True):
                if(x.pathCost < lowestActiveRisk):
                    lowestActiveNode = x.id
                    lowestActiveRisk = x.pathCost
                # print(f"{x.id} - {x.neighbours}")
        
        for nNode in nodeList[lowestActiveNode].neighbours:
            neighbourCurrentCost = nodeList[nNode].pathCost
            neighbourNodeRisk = nodeList[nNode].risk
            activePathCost = nodeList[lowestActiveNode].pathCost
            if(neighbourCurrentCost > activePathCost + neighbourNodeRisk):
                nodeList[nNode].pathCost = activePathCost + neighbourNodeRisk
                nodeList[nNode].previousNode = lowestActiveNode
                nodeList[nNode].active = True
            
            if(nodeList[nNode].id == (len(nodeList) - 1)):
                # print('Found Path')
                # print(f"Cost is {nodeList[nNode].pathCost}")
                FinalCost = nodeList[nNode].pathCost
                lock = False
        
        # print(f"LowestActive = {lowestActiveNode}")
        
        nodeList[lowestActiveNode].active = False

        count += 1
    
    return 0

class node:

    def __init__(self, height, x, y, lenX, lenY):
        
        self.x = x
        self.y = y
        self.start = False
        self.end = False
        self.height = ord(height) - 96
        if(height == 'S'):
            self.start = True
        elif(height == 'E'):
            self.end = True

        self.pathCost = 100000000
        self.previousNode = -1
        self.active = False

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