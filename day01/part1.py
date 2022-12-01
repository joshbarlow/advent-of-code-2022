def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    return inputDataArray

def calculateHighestCalories(inputDataArray):
    calorieList = []
    currentCount = 0

    for x in inputDataArray:
        lineValue = 0
        try:
            lineValue = int(x)
            currentCount += lineValue
        except:
            calorieList.append(currentCount)
            currentCount = 0
    
    if(currentCount > 0):
        calorieList.append(currentCount)

    calorieList.sort(reverse=True)
    return calorieList[0]

if __name__ == '__main__':
    print(calculateHighestCalories(importData()))