import re

def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    cleanInputDataArray = []
    for line in inputDataArray:
        cleanInputDataArray.append(line.replace("\n", ""))
    return cleanInputDataArray

def calcStreamStart(inputDataArray):

    stream = inputDataArray[0]

    buffer = []
    streamStart = 1

    for char in stream:
        # print(char)
        if (len(buffer) == 4):
            buffer.pop(0)
            buffer.append(char)

            bufferSet = set(buffer)

            if (len(bufferSet) == len(buffer)):
                break
        
        else:
            buffer.append(char)

        streamStart += 1
        print(buffer)
    
    return streamStart

if __name__ == '__main__':
    print(calcStreamStart(importData()))