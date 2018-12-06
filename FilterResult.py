from sys import argv

def getLinesFromPath(path):
    file = open(path,"r")
    return file.read().splitlines()

outputFilePath = argv[1]
inputFilePath = argv[2]
probesToCheck = eval(argv[3])

inputLines = getLinesFromPath(inputFilePath)
csvSeperator = inputLines[0][4:]
print('Start filtering', inputFilePath)

def seenInSequences(line):
    values = line.split(csvSeperator)
    return len(values) > max(probesToCheck) and list(map(lambda x: int(values[x]) > 0, probesToCheck)).count(True) == len(probesToCheck)

outputLines = list(filter(seenInSequences, inputLines[2:]))
print('Filter result:(', len(outputLines), '/', len(inputLines) ,')')


print('Writing output to', outputFilePath)
outputFile = open(outputFilePath, 'w')
outputFile.write(inputLines[0] + '\n')
outputFile.write(inputLines[1] + '\n')
for line in outputLines:
    outputFile.write(line + '\n')
outputFile.close()

print('Finished writing output')