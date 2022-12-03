def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    return inputDataArray

def calculateScore(inputDataArray):
    scoreDict = {
        'A X': 4,
        'A Y': 8,
        'A Z': 3,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 7,
        'C Y': 2,
        'C Z': 6
    }

    totalScore = 0

    for x in inputDataArray:
        totalScore += scoreDict[x.replace("\n", "")]
    
    return totalScore

if __name__ == '__main__':
    print(calculateScore(importData()))