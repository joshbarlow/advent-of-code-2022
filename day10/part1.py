import re

def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    cleanInputDataArray = []
    for line in inputDataArray:
        cleanInputDataArray.append(line.replace("\n", ""))
    return cleanInputDataArray

def calcString(inputDataArray):

    register = 1

    buffer = [0,0]

    timeArray = []
    signalStrenghArray = []

    step = 1

    inputDataArray.append('noop ')
    inputDataArray.append('noop ')
    inputDataArray.append('noop ')
    inputDataArray.append('noop ')

    for line in range(len(inputDataArray)):

        # print('===== Step:' + str(line+1) + ' =====')
        
        # print(buffer)

        print(buffer)

        print(register)

        # this is the value for the step

        value = inputDataArray[line][5:]

        if (inputDataArray[line][:4] == 'addx'):
            print('===== Step:' + str(step) + ' register:' + str(register) + ' signal:' + str(register * step) + ' =====')

            timeArray.append(register)
            signalStrenghArray.append(register * step )

            step += 1

            print('===== Step:' + str(step) + ' register:' + str(register) + ' signal:' + str(register * step) + ' =====')

            timeArray.append(register)
            signalStrenghArray.append(register * step )

            step += 1

            register += int(value)
        
        if (inputDataArray[line][:4] == 'noop'):

            print('===== Step:' + str(step) + ' register:' + str(register) + ' signal:' + str(register * step) + ' =====')

            timeArray.append(register)
            signalStrenghArray.append(register * step)

            step += 1
    
    # 20 60 100 140 180 220 .. hardcoded haha

    print(timeArray)
    print(signalStrenghArray[19])
    print(signalStrenghArray[59])
    print(signalStrenghArray[99])

    total = signalStrenghArray[19] + signalStrenghArray[59] + signalStrenghArray[99] + signalStrenghArray[139] + signalStrenghArray[179] + signalStrenghArray[219]
    # total = 0
    return total

if __name__ == '__main__':
    print(calcString(importData()))