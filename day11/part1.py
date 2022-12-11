import re

def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    cleanInputDataArray = []
    for line in inputDataArray:
        cleanInputDataArray.append(line.replace("\n", ""))
    return cleanInputDataArray

def calcString(inputDataArray):

    monkeylists = []
    monkeyList = []

    for line in range(len(inputDataArray)):
        lineIndex = line % 7
        monkeyList.append(inputDataArray[line])
        if(lineIndex == 6):
            monkeylists.append(monkeyList)
            monkeyList = []
    
    monkeysArray = []

    # print(monkeylists)

    for monk in monkeylists:

        name = monk[0][:-1]
        startingList = []
        if(',' in monk[1]):
            startingList = monk[1][18:].split(',')
        else:
            startingList.append(monk[1][18:])

        operation = monk[2][19:]
        
        test = monk[3][21:]

        trueMonkey = monk[4][29:]
        FalseMonkey = monk[5][30:]

        monkeysArray.append(monkey(name,startingList,operation,test,trueMonkey,FalseMonkey))

    rounds = 20

    for round in range(rounds):
        for monk in monkeysArray:
            thrown = monk.inspectAndThrow()
            for item in thrown:
                splitThrow = item.split(',')
                itemValue = int(splitThrow[0])
                targetMonkey = int(splitThrow[1])
                monkeysArray[targetMonkey].Items.append(itemValue)
    
    totalInspections = []

    for monk in monkeysArray:
        totalInspections.append(monk.inspections)
    
    totalInspections.sort(reverse=True)

    print(totalInspections[0])

    return totalInspections[0] * totalInspections[1]

class monkey:

    def __init__(self, name, startingItems, operation, test, trueMonkey, falseMonkey):
        self.name = name
        self.Items = [] 
        for x in startingItems:
            self.Items.append(int(x))
        
        self.operationA = ''
        self.operationB = ''
        self.operationFunction = '+'

        if('+' in operation):
            splitOp = operation.split(' + ')
            self.operationA = splitOp[0]
            self.operationB = splitOp[1]
        elif('*' in operation):
            splitOp = operation.split(' * ')
            self.operationFunction = '*'
            self.operationA = splitOp[0]
            self.operationB = splitOp[1]
        
        self.testValue = int(test)

        self.trueMonkey = int(trueMonkey)
        self.falseMonkey = int(falseMonkey)

        self.inspections = 0
    
    def inspectAndThrow(self):

        throwList = []

        opA = 0
        opB = 0

        newWorry = 0

        for item in self.Items:
            
            if(self.operationA == 'old'):
                opA = int(item)
            else:
                opA = int(self.operationA)
            
            if(self.operationB == 'old'):
                opB = int(item)
            else:
                opB = int(self.operationB)
            
            # first operation
            
            if(self.operationFunction == '+'):
                newWorry = opA + opB
            else:
                newWorry = opA * opB
            
            # division operation
            newWorry = int(newWorry // 3.0)

            # test

            divisible = newWorry % self.testValue
            
            targetMonkey = 0

            if(divisible == 0):
                targetMonkey = self.trueMonkey
            else:
                targetMonkey = self.falseMonkey
            
            outputString = (str(newWorry) + ',' + str(targetMonkey))

            throwList.append(outputString)

            self.inspections += 1
        
        self.Items = []
        
        return throwList
            
            
if __name__ == '__main__':
    print(calcString(importData()))