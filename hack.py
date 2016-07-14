import os

minLevel = 51
maxLevel = 63

def getFileLines(filename):
    return open(filename, "r").readlines()

def writeLinesToFile(lines, filename):
    open(filename, "w").writelines(lines)

def scaleLevel(original):
    return minLevel + int(float(original) / 100.0 * float(maxLevel - minLevel))

def getScaledLine(line, offset):
    splitLine = line.split(" ")
    lineStart = splitLine[0]
    if lineStart == "\tdb" or lineStart == "\t\tdb":
        data = splitLine[1]
        splitData = data.split(",")
        if len(splitData) == 2:
            return lineStart + " " + str(scaleLevel(int(splitData[0]))) + "," + splitData[1]
        elif len(splitData) == 3:
            return lineStart + " EV_LEVEL," + str(scaleLevel(int(splitData[1]))) + "," + splitData[2]

    return line

def scaleEvolutionsAndMoves():
    filename = "data/evos_moves.asm"
    linesOut = [getScaledLine(line, 1) for line in getFileLines(filename)]
    writeLinesToFile(linesOut, filename)

def scaleWildPokemon:
    directory = "data/wildPokemon/"
    fileList += [directory + name for name in os.listdir(directory)]
    for fileIn in fileList:
        linesOut = [getScaledLine(line,0) for line in getFileLines(fileIn)]
        writeLinesToFile(linesOut)


scaleEvolutionsAndMoves()
scaleWildPokemon()
