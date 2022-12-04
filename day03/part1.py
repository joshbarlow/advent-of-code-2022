import string

def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    return inputDataArray

def rucksackCompare(inputDataArray):
    
    prioDict = buildPriotityDict()

    characterArray = []

    for line in inputDataArray:
        firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]

        doubleChar = ''

        for char in secondpart:
            if (char in firstpart):
                doubleChar = char
        
        characterArray.append(doubleChar)

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