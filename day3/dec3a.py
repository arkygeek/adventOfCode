'''
    This Python script calculates gear ratios from a given input file.
    The input file contains a map of gears and numbers, represented as a grid of characters.

    The script consists of several functions:

        mark_adjacent_positions(marked, i, j): Marks the positions adjacent to a given position in a 2D list.
        print_map(map): Prints a 2D list in a grid format.
        calculate_gear_ratios(input_lines, potential_labels, ratio_map, value_map): Calculates the sum of the gear ratios. A gear ratio is calculated by multiplying two numbers adjacent to a gear. A gear is represented by '*' and numbers are represented by 'F' in the ratio map.
        parse_input(input_lines): Parses the input lines to generate several maps and a list of potential labels. The maps include a gear map (marking the positions of gears), a ratio map (marking the positions of numbers), and a value map (marking the positions of numbers with their values).

    Steps:
        read the input file
        parse the input lines to generate the maps and potential labels
        calculate the sum of the gear ratios
        prints the result

        I also left lines in that will print the gear map and ratio map for visual inspection.
            * This was very useful for debugging using the small smaple data first,
            then the first three lines of the actual data
'''

def calculate_gear_ratios(theInputLines, thePotentialLabels, theRatioMap, theValueMap):
    myTotalGearRatioSum = 0
    for myRowIndex, myLine in enumerate(theInputLines):
        for myColumnIndex, myCharacter in enumerate(myLine):
            if myCharacter == '*':
                print(f'Gear found at position ({myRowIndex}, {myColumnIndex})')
                myAdjacentNumbers = set()
                for myRowOffset in [-1, 0, 1]:
                    for myColumnOffset in [-1, 0, 1]:
                        if myRowOffset == 0 and myColumnOffset == 0:
                            """
                            'continue' in Python is used to skip the rest of the code
                            inside the innermost loop and move to the next iteration.

                            In this context, myRowOffset == 0 and myColumnOffset == 0
                            checks if both offsets are zero. This would mean that the
                            current position is the center of the 3x3 grid (the position
                            of the gear itself)...

                            Since the goal is to check the cells adjacent to the gear,
                            not the gear itself, the continue statement is used to skip
                            the current iteration of the loop when the offsets are both
                            zero, effectively ignoring the gear's own position and only
                            processing adjacent cells.
                            """
                            continue

                        myAdjacentRow, myAdjacentColumn = myRowIndex + myRowOffset, myColumnIndex + myColumnOffset
                        # Check if the adjacent row is within the bounds of the input lines
                        myRowIsInBounds = 0 <= myAdjacentRow < len(theInputLines)
                        # Check if the adjacent column is within the bounds of the input lines
                        myCoulmnIsInBounds = 0 <= myAdjacentColumn < len(theInputLines[0])
                        # Check if the position in the ratio map is marked as 'F'
                        myMarkedPosition = theRatioMap[myAdjacentRow][myAdjacentColumn] == 'F'
                        # If all conditions are met, execute the code inside the if statement
                        if myRowIsInBounds and myCoulmnIsInBounds and myMarkedPosition:
                            myAdjacentNumbers.add(theValueMap[myAdjacentRow][myAdjacentColumn])

                if len(myAdjacentNumbers) == 2:
                    print(f'Adjacent numbers: {myAdjacentNumbers}')
                    myTotalGearRatioSum += myAdjacentNumbers.pop() * myAdjacentNumbers.pop()
    return myTotalGearRatioSum


def print_map(theMap):
    for myRow in theMap:
        print(''.join(str(myCell) for myCell in myRow))


def calculate_gear_ratios(theInputLines, thePotentialLabels, theRatioMap, theValueMap):
    myTotalSum = 0
    for myRowIndex, myLine in enumerate(theInputLines):
        for myColumnIndex, myCharacter in enumerate(myLine):
            if myCharacter == '*':
                # print(f'Gear found at position ({myRowIndex}, {myColumnIndex})')
                myAdjacentNumbers = set()
                for myRowOffset in [-1, 0, 1]:
                    for myColumnOffset in [-1, 0, 1]:
                        if myRowOffset == 0 and myColumnOffset == 0:
                            continue
                        myAdjacentRow, myAdjacentColumn = myRowIndex + myRowOffset, myColumnIndex + myColumnOffset
                        if 0 <= myAdjacentRow < len(theInputLines) and 0 <= myAdjacentColumn < len(theInputLines[0]) and theRatioMap[myAdjacentRow][myAdjacentColumn] == 'F':
                            myAdjacentNumbers.add(theValueMap[myAdjacentRow][myAdjacentColumn])
                if len(myAdjacentNumbers) == 2:
                    # print(f'Adjacent numbers: {myAdjacentNumbers}')
                    myTotalSum += myAdjacentNumbers.pop() * myAdjacentNumbers.pop()
    return myTotalSum


def parse_input(theInputLines):
    myPotentialLabels = []
    myGearMap = [['.' for _ in line] for line in theInputLines]
    myRatioMap = [['.' for _ in line] for line in theInputLines]
    myValueMap = [['.' for _ in line] for line in theInputLines]
    for myRowIndex, myLine in enumerate(theInputLines):
        myColumnIndex = 0
        while myColumnIndex < len(myLine):
            if myLine[myColumnIndex] == '*':
                myGearMap[myRowIndex][myColumnIndex] = '*'
            if myLine[myColumnIndex].isdigit():
                myStart = myColumnIndex
                myNum = myLine[myColumnIndex]

                # the following line of code (part of this while loop) checks if the next character in myLine is a digit:
                while myColumnIndex + 1 < len(myLine) and myLine[myColumnIndex + 1].isdigit():
                    """
                    Breaking down what this does:
                        myColumnIndex + 1 < len(myLine):
                            This checks if the next index is within the bounds of myLine.
                            If myColumnIndex + 1 is equal to or greater than (>=) len(myLine),
                            it means we've reached the end of myLine and there's no next character to check.
                        myLine[myColumnIndex + 1].isdigit():
                            This checks if the next character in myLine is a digit.
                            The isdigit method returns True if the string is a digit and False otherwise.

                        The while loop continues as long as the next character exists and is a digit.
                        For example, if myLine is '1234', this loop would treat '1234' as a single number,
                        rather than four separate numbers.
                    """
                    myColumnIndex += 1
                    myNum += myLine[myColumnIndex]
                myPotentialLabels.append({
                    'value': int(myNum),
                    'row': myRowIndex,
                    'start': myStart,
                    'end': myColumnIndex})
                for myRangeIndex in range(myStart, myColumnIndex+1):
                    myRatioMap[myRowIndex][myRangeIndex] = 'F'
                    myValueMap[myRowIndex][myRangeIndex] = int(myNum)
            myColumnIndex += 1
    return myPotentialLabels, myGearMap, myRatioMap, myValueMap

with open('input3.txt', 'r') as file:
    myInputLines = [line.strip() for line in file]

# print("Initial input data:")
# print_map(myInputLines)
myPotentialLabels, myGearMap, myRatioMap, myValueMap = parse_input(myInputLines)
myTotalSum = calculate_gear_ratios(myInputLines, myPotentialLabels, myRatioMap, myValueMap)
# print(myTotalSum)
# print("Map of all found gear symbols:")
# print_map(myGearMap)
# print("Map of all potential ratio objects:")
# print_map(myRatioMap)
myTotalSum = calculate_gear_ratios(myInputLines, myPotentialLabels, myRatioMap, myValueMap)
print(f'Total sum of gear ratios: {myTotalSum}')