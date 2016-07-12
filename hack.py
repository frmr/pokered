import os

minLevel = 51
maxLevel = 63

def scaleLevel(original):
    return minLevel + int(float(original) / 100.0 * float(maxLevel - minLevel))

directory = "data/wildPokemon/"

fileList = ["data/evos_moves.asm"]

wildFileList = os.listdir(directory);

for wildFile in wildFileList:
    fileList.append(directory + wildFile)

for file in fileList:
    linesOut = []
    fileIn = open(directory + file, "r")
    for lineIn in fileIn:
        splitLine = lineIn.split(" ")
        lineStart = splitLine[0]
        if lineStart == "\tdb" or lineStart == "\t\tdb":
            data = splitLine[1]
            splitData = data.split(",")
            if len(splitData) == 2:
                linesOut.append(lineStart + " " + str(scaleLevel(int(splitData[0]))) + "," + splitData[1])
                continue
            elif len(splitData) == 3:
                linesOut.append(lineStart + " " + EV_LEVEL, "," + str(scaleLevel(int(splitData[1]))) + "," + splitData[2])
                continue

        linesOut.append(lineIn)

    fileIn.close()

    fileOut = open(directory + file, "w")

    for lineOut in linesOut:
        fileOut.write(lineOut)

    fileOut.close()
