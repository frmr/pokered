import os
import sys

minLevel = 51
maxLevel = 63

def throwLineTypeError(lineType):
    sys.exit("Unknown line type: " + lineType)

def getFileLines(filename):
    return open(filename, "r").readlines()

def writeLinesToFile(lines, filename):
    open(filename, "w").writelines(lines)

def scaleLevel(level):
    return minLevel + int(float(level) / 100.0 * float(maxLevel - minLevel))

def deduceLineType(line):
    splitLine = line.split(" ")
    if splitLine[0].strip() == "db":
        args = splitLine[1].split(",")
        if args[0] == "EV_LEVEL":
            return "LineType_EvolutionLevel"
        elif args[0] == "EV_ITEM":
            return "LineType_EvolutionItem"
        elif args[0] == "$FF":
            return "LineType_PartyList"
        else:
            if len(args) == 2:
                return "LineType_LevelDeclaration"
    elif splitLine[0].strip() == "IF":
        return "LineType_If"
    elif splitLine[0].strip() == "ENDC":
        return "LineType_End"

    return "LineType_Other"

def getScaledLineEvolutionLevel(line):
    splitLine = line.split(" ")
    lineStart = splitLine[0]
    args = splitLine[1].split(",")
    return lineStart + " EV_LEVEL," + str(scaleLevel(int(args[1])) + 1) + "," + args[2]

def getScaledLineLevelDeclaration(line):
    splitLine = line.split(" ")
    lineStart = splitLine[0]
    args = splitLine[1].split(",")
    return lineStart + " " + str(scaleLevel(int(args[0]))) + "," + args[1]

def getScaledLine(line):
    lineType = deduceLineType(line)
    if lineType == "LineType_EvolutionLevel":
        return getScaledLineEvolutionLevel(line)
    elif lineType == "LineType_EvolutionItem":
        return line
    elif lineType == "LineType_PartyList":
        return line
    elif lineType == "LineType_LevelDeclaration":
        return getScaledLineLevelDeclaration(line)
    elif lineType == "LineType_If":
        return line
    elif lineType == "LineType_End":
        return line
    elif lineType == "LineType_Other":
        return line
    else:
        throwLineTypeError(lineType)

def scaleEvolutionsAndMoves():
    filename = "data/evos_moves.asm"
    linesOut = [getScaledLine(line) for line in getFileLines(filename)]
    writeLinesToFile(linesOut, filename)


def generateWildPokemonDeclarations(version):
    

def countWildPokemon(lines, version):
    countMap = {}
    for

def scaleWildPokemonFile(filename):
    lines = getFileLines(filename)
    #copy first two lines verbatim

    wildCount = countWildPokemon(lines, "_RED")


    #copy last line verbatim
    for pokemon, count in countMap.iteritems():

def scaleWildPokemon():
    directory = "data/wildPokemon/"
    filenames = [directory + name for name in os.listdir(directory)]

    for filename in filenames:
        linesOut = generateWildPokemonDeclarations(filename);
        writeLinesToFile(linesOut, filename)

scaleEvolutionsAndMoves()
scaleWildPokemon()
