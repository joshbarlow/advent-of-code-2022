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

            timeArray.append([register,step])

            step += 1

            print('===== Step:' + str(step) + ' register:' + str(register) + ' signal:' + str(register * step) + ' =====')

            timeArray.append([register,step])

            step += 1

            register += int(value)
        
        if (inputDataArray[line][:4] == 'noop'):

            print('===== Step:' + str(step) + ' register:' + str(register) + ' signal:' + str(register * step) + ' =====')

            timeArray.append([register,step])

            step += 1
    
    offsets = [0,40,60,100,140,180,220]
    offset = 0
    pixel = 0

    for pixel in range(len(timeArray)):
        step = timeArray[pixel][1]
        register = timeArray[pixel][0]

        print(checkPixel(step,register), end='')
        if (checkOffset(step)):
            print(' ')

    return 0

def checkPixel(step,register):
    pixel = (step-1)%40

    sprite = []
    sprite.append(register-1)
    sprite.append(register)
    sprite.append(register+1)

    for x in sprite:
        if (pixel == x):
            return '#'

    return '.'

def checkOffset(step):

    offsets = [40,80,120,160,200]

    for val in offsets:
        if(step == val):
            # print('Step = ' + str(val))
            return True
    
    return False

if __name__ == '__main__':
    print(calcString(importData()))