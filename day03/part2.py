import string

def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    return inputDataArray

def rucksackCompare(inputDataArray):

    prioDict = buildPriotityDict()
    characterArray = []

    for x in range(int(len(inputDataArray)/3.0)):
        pack1 = inputDataArray[x*3].replace("\n", "")
        pack2 = inputDataArray[(x*3) + 1].replace("\n", "")
        pack3 = inputDataArray[(x*3) + 2].replace("\n", "")

        doublesArray = []
        sharedChar = ''

        for char in pack1:
            if (char in pack2):
                doublesArray.append(char)

        for char in doublesArray:
            if (char in pack3):
                sharedChar = char
        
        characterArray.append(sharedChar)

    PriorityTotal = 0
    
    for char in characterArray:
        PriorityTotal += prioDict[char]

    return PriorityTotal

def buildPriotityDict():

    fullString = string.ascii_lowercase + string.ascii_uppercase
    counter = 1
    priorityDict = {}

    for character in fullString:
        priorityDict[character] = counter
        counter += 1
    
    return priorityDict


if __name__ == '__main__':
    print(rucksackCompare(importData()))