import os
import sys

minLevel = 51
maxLevel = 63
wildLevel = 51

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

def getScaledEvosMovesLine(line):
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
    linesOut = [getScaledEvosMovesLine(line) for line in getFileLines(filename)]
    writeLinesToFile(linesOut, filename)

def getScaledTrainerLine(line):
    if line.split(" ")[0].strip() == "db":
        return "\tdb 55" + line[line.find(","):]
    else:
        return line

def setTrainerPartyLevels():
    filename = "data/trainer_parties.asm"
    fileLines = getFileLines(filename)

    linesOut = fileLines[:58]
    linesOut += [getScaledTrainerLine(line) for line in getFileLines(filename)[58:336]]
    linesOut += fileLines[336:352]
    linesOut += [getScaledTrainerLine(line) for line in getFileLines(filename)[352:366]]
    linesOut += fileLines[366:370]
    linesOut += [getScaledTrainerLine(line) for line in getFileLines(filename)[370:432]]
    linesOut += fileLines[432:448]
    linesOut += [getScaledTrainerLine(line) for line in getFileLines(filename)[448:454]]
    linesOut += fileLines[454:473]
    linesOut += [getScaledTrainerLine(line) for line in getFileLines(filename)[473:498]]
    linesOut += fileLines[498:]

    writeLinesToFile(linesOut, filename)

scaleEvolutionsAndMoves()
setTrainerPartyLevels()
