import unittest

import part1, part2

def importData():
    with open('test_input2.txt') as input_file:
        inputDataArray = input_file.readlines()
    cleanInputDataArray = []
    for line in inputDataArray:
        cleanInputDataArray.append(line.replace("\n", ""))
    return cleanInputDataArray

class Test_TestPart1(unittest.TestCase):
    def test_part1(self):

        self.assertEqual(part1.calcString(importData()), 88)

class Test_TestPart2(unittest.TestCase):
    def test_part2(self):

        self.assertEqual(part2.calcString(importData()), 36)

if __name__ == '__main__':
    unittest.main()
