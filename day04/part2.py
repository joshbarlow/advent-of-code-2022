import string

def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    cleanInputDataArray = []
    for line in inputDataArray:
        cleanInputDataArray.append(line.replace("\n", ""))
    return cleanInputDataArray

def calculateOverlaps(inputDataArray):

    overlapCount = 0

    for line in inputDataArray:
        splitLine = line.split(',')
        elf1Array = listNums(splitLine[0])
        elf2Array = listNums(splitLine[1])

        # print('elf1: ', end ='')
        # print(elf1Array)
        # print('elf2: ', end = '')
        # print(elf2Array)

        overlap1 = False
        overlap2 = False

        for char in elf1Array:
            if char in elf2Array:
                overlap1 = True
        
        for char in elf2Array:
            if char in elf1Array:
                overlap2 = True
        
        if (overlap1 == True):
            # print('Overlap')
            overlapCount += 1

        elif (overlap2 == True):
            # print('Overlap')
            overlapCount += 1
        
        # print('==========')
    
    return overlapCount

def listNums(numText):

    splitText = numText.split('-')

    num1 = int(splitText[0])
    num2 = int(splitText[1])

    numsArray = [num1]
    counter = num1

    while(counter < num2):
        counter +=1 
        numsArray.append(counter)

    return numsArray

if __name__ == '__main__':
    print(calculateOverlaps(importData()))