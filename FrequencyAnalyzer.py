from sys import argv
from itertools import *
from decimal import *
from datetime import *

### SETTINGS ###
characters = 'GATC'
wordLength = 9
decimalSeperator = ','
csvSeperator = '| '

#decimalPrecision = 15
#getcontext().prec = decimalPrecision
startTime = datetime.now()
charactersSet = set(characters)
outputFilePath = argv[1]
inputFilePaths = argv[2:]
dictionary = list(map(lambda x: ''.join(x), list(product(characters, repeat=wordLength))))


def getLinesFromPath(path):
    file = open(path,"r")
    return file.read().splitlines()

def calculateFrequenciesForFile(path):
    start = datetime.now()
    print('\n##### Calculating Frequencies for ', path, ' #####')
    inputWords = getLinesFromPath(path)
    totalWords = 0
    uniqueWords = 0
    frequencyTable = {}
    for word in dictionary:
        frequencyTable[word] = 0
    for word in inputWords:
        if len(word) == wordLength and set(word).issubset(charactersSet):
            if frequencyTable[word] == 0:
                uniqueWords += 1
            frequencyTable[word] += 1
            totalWords += 1
            
    #print (frequencyTable)
    print(totalWords, 'valid lines analyzed in input file. (ignoring', len(inputWords) - totalWords, 'mismatches)')
    print(uniqueWords, 'unique words found')
    timeElapsed = datetime.now() - start
    print('File analyzed in', str(timeElapsed.seconds ) + 's')
    return {'frequencyTable': frequencyTable, 'totalWords': totalWords, 'uniqueWords': uniqueWords, 'filePath': path}

def analyzeAllFiles(paths):
    print('\n######## Calculating word frequencies in ', len(inputFilePaths), ' input files. ########')
    resultsets = []
    for path in inputFilePaths:
        resultsets.append(calculateFrequenciesForFile(path))
    print('\n######## Finished analyzing ', len(resultsets), ' files', ' ########')
    print ('-'*80)
    print('\nStart writing output to file ', outputFilePath)
    writeOutputFile(resultsets, outputFilePath)
    print('Finished writing output file.')
    timeElapsed = datetime.now() - startTime
    print ('-'*80)
    print('\n##### Valid answer found in ', str(timeElapsed.seconds ) + 's' + ': 42 #####\n\n\n')
    
def writeOutputFile(results, outputPath):
    start = datetime.now()
    outputFile = open(outputFilePath, 'w')
    outputFile.write('sep=' + csvSeperator + '\n#Word')
    for result in results:
        outputFile.write(csvSeperator + 'abs_' + result['filePath'])
    for result in results:
        outputFile.write(csvSeperator + 'rel_' + result['filePath'])
    outputFile.write('\n')
    for word in dictionary:
        outputFile.write(word)
        for result in results:
            outputFile.write(csvSeperator + str(result['frequencyTable'][word]))
        for result in results:
            outputFile.write(csvSeperator + str(result['frequencyTable'][word] / result['totalWords']).replace('.', decimalSeperator))
        outputFile.write('\n')

    outputFile.close()
    timeElapsed = datetime.now() - start
    print('File analyzed in', str(timeElapsed.seconds) + 's')



analyzeAllFiles(inputFilePaths)
