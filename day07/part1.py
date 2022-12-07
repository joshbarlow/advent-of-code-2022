import re

def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    cleanInputDataArray = []
    for line in inputDataArray:
        cleanInputDataArray.append(line.replace("\n", ""))
    return cleanInputDataArray

def calcSize(inputDataArray):

    folderStructure = buildFolderStructure(inputDataArray)

    # printFolderStructure(folderStructure,0)

    total = calculateSizeTotals(folderStructure)

    return total

class directory:
    def __init__(self, name, parent):
        self.name = name
        self.children = []
        self.filetype = 'Directory'
        self.parent = parent

    def addChild(self, child):
        self.children.append(child)
    
    def child(self, name):
        targetChild = ''

        for x in self.children:
            if x.name == name:
                targetChild = x
        
        return targetChild


class file:
    def __init__(self, name, size):
        self.name = name
        self.extension = 'Unknown'

        if ('.' in self.name):
            splitfile = self.name.split('.')
            self.extension = splitfile[1]

        self.filetype = 'File'
        self.filesize = size

def printFolderStructure(folderStructure, level):
    preString = '-' * level

    if(folderStructure.filetype == 'Directory'):
        print(preString + folderStructure.name)
        for item in folderStructure.children:
            printFolderStructure(item, level + 1)
    else:
        print(preString + folderStructure.name + ' - ' + str(folderStructure.filesize))

def calculateSizeTotals(folderStructure):

    total = 0
    goalSize = 100000

    if(folderStructure.filetype == 'Directory'):
        print(folderStructure.name + ' - ' + str(getDirSize(folderStructure)))
        if (getDirSize(folderStructure) <= goalSize):
            print('Found!')
            total += getDirSize(folderStructure)
        for item in folderStructure.children:
            total += calculateSizeTotals(item)
    # else:
    #     print(preString + folderStructure.name + ' - ' + str(folderStructure.filesize))

    # for item in folderStructure.children:
    #     if (item.filetype == 'Directory'):

    #         print(item.name + ' size = ' + str(getDirSize(item)))
    
    return total

def getDirSize(Dir):
    totalSize = 0

    for item in Dir.children:
        if (item.filetype == 'File'):
            totalSize += int(item.filesize)
        else:
            totalSize += getDirSize(item)
    return int(totalSize)


def buildFolderStructure(inputDataArray):

    inputDataArray.pop(0)
    folderStructure = directory('/', '')

    currentFolder = folderStructure

    listing = False

    for line in inputDataArray:
        if (line[0] == '$'):

            listing = False

            print(line[2:4])

            if (line[2:4] == 'cd'):
                dirName = line.split(' cd ')[1]

                if (line == '$ cd ..'):
                    print('going back up to: ' + currentFolder.parent.name)
                    currentFolder = currentFolder.parent
                else:
                    print('going into ' + dirName)
                    currentFolder = currentFolder.child(dirName)
            
            if (line[2:4] == 'ls'):
                listing = True
        
        elif (listing == True):
            splitLine = line.split(' ')

            if (splitLine[0] == 'dir'):
                print('Build Dir: ' + splitLine[1])
                currentFolder.addChild(directory(splitLine[1], currentFolder))
            
            else:
                print('Build File: ' + splitLine[1])
                currentFolder.addChild(file(splitLine[1], splitLine[0]))

    return folderStructure


if __name__ == '__main__':
    print(calcSize(importData()))