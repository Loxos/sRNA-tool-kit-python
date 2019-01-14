# sRNA-tool-kit-python
## Frequency Analyzer

Takes an arbitrary number of input files and analyzes there word frequencies.

### Getting Started

Run 
```
py FrequencyAnalyzer.py outputFile.path input1.file input2.file inputN.file
```
in console.

For Example:
```
py FrequencyAnalyzer.py output.csv sel1-1_S2.input sel1-1_S9.input
```


### Prerequisites

Input files need to have one word per line. lines with bad content or having lengths other than specified in the Settings are ignored.

## Result Filter

Filters words that were not seen in all specified result files

### Getting Started

Run 
```
py FilterResult.py filteredOutput.csv inputFile.csv [1,2,..,N]
```
in console.

For Example:
```
py FilterResult.py filteredOutput.csv inputFile.csv [1,2,7]
```


### Prerequisites

Input file needs to specify a sperator within first line.


## Authors

* **Daniel Graf Hoyos** - *Initial work* - [Loxos](https://github.com/Loxos)

