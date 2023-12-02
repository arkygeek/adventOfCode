import re

theSum: int = 0
# Define a dictionary mapping spelled out numbers to their numerical equivalents
theNumberDict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
                 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
                 '1': '1', '2': '2', '3': '3', '4': '4', '5': '5',
                 '6': '6', '7': '7', '8': '8', '9': '9'}

# Define a regular expression pattern to match spelled-out numbers and digits
thePattern = re.compile(r'(?=(one|two|three|four|five|six|seven|eight|nine))')

with open('input.txt', 'r') as file:
    myLinesInFile = file.readlines()
    for myLine in myLinesInFile:
        myLine = myLine.lower()  # Convert to lowercase in case they are being dicks
        myMatchedNumbers = thePattern.findall(myLine)
        if myMatchedNumbers:
            myDigitList = [theNumberDict[number] for number in myMatchedNumbers]
            myConcatenatedNumber = int(myDigitList[0] + myDigitList[-1])
            theSum += myConcatenatedNumber

print(f"Final sum: {theSum}")