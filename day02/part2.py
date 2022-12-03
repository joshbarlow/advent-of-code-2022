def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    return inputDataArray

def calculateScore(inputDataArray):
    scoreDict = {
        'A X': 3,
        'A Y': 4,
        'A Z': 8,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 2,
        'C Y': 6,
        'C Z': 7
    }

    # x1 y2 z3
    # l0 d3 w6
    # x lose y draw z win
    totalScore = 0

    for x in inputDataArray:
        totalScore += scoreDict[x.replace("\n", "")]
    
    return totalScore

if __name__ == '__main__':
    print(calculateScore(importData()))