import re

def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    cleanInputDataArray = []
    for line in inputDataArray:
        cleanInputDataArray.append(line.replace("\n", ""))
    return cleanInputDataArray

def calculateStacks(inputDataArray):

    numStacks = int((len(inputDataArray[0])+1)/4)

    stackArray = []

    for x in range(numStacks):
        print(x)
        stackArray.append([])
    
    instructionsList = []
    
    for line in inputDataArray:
        if('[' not in line):
            instructionsList.append(line)
        
        else:
            for stack in range(numStacks):
                stackValue = line[(stack*4)+1]

                if(stackValue != ' '):
                    stackArray[stack].append(stackValue)

            print(line)

    print(stackArray)
    instructionsList.pop(0)
    instructionsList.pop(0)

    for line in instructionsList:
        splitInstructions = re.split('move | from | to ',line)
        print('split =')
        print(line)
        print(splitInstructions)
        ammount = int(splitInstructions[1])
        fromStack = int(splitInstructions[2]) - 1
        toStack = int(splitInstructions[3]) - 1

        for x in range(ammount):
            moveValue = stackArray[fromStack][0]
            stackArray[toStack].insert(x,moveValue)
            stackArray[fromStack].pop(0)
    
    print('======')
    print(stackArray)

    finalString = ''

    for stack in stackArray:
        finalString += stack[0]
        
    return finalString

if __name__ == '__main__':
    print(calculateStacks(importData()))