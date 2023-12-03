'''
The plan...
Open file 'input3.txt' for reading.
Read file line by line and store the lines in a list.
Create a 2D boolean array (marked with the same dimensions as the input) initialized with False.
Iterate over the list of lines. For each line:
    Iterate over each character in the line.
    If the character is a symbol, mark all 8 positions around it in the marked array.
    Initialize variable theSum = 0.
Iterate over the list of lines again. For each line:
    Iterate over each character in the line.
    If the character is a digit and its position is marked, add it to theSum.
    If the character is a digit and the next character is also a digit, concatenate them to form a multi-digit number before adding to theSum.
    Check if the position of any digit in the number is marked.
'''

# Open the file for reading
with open('input3.txt', 'r') as theFile:
    myLines = [list(line.strip()) for line in theFile]

# Create the marked array
myMarked = [[False]*len(theLine) for theLine in myLines]

# Mark positions adjacent to a symbol
# Mark positions adjacent to a symbol
for i in range(len(myLines)):
    for j in range(len(myLines[i])):
        if myLines[i][j] in '#$%&@=+-/*':
            for myRowChange in range(-1, 2):
                for myColumnChange in range(-1, 2):
                    if 0 <= i+myRowChange < len(myLines) and 0 <= j+myColumnChange < len(myLines[i]):
                        myMarked[i+myRowChange][j+myColumnChange] = True

# Initialize the sum
theSum = 0

# Iterate over the lines
for i in range(len(myLines)):
    myLine = myLines[i]
    # Iterate over the characters in the line
    j = 0
    while j < len(myLine):
        char = myLine[j]
        # Check if the character is a digit
        if char.isdigit():
            # Check for multi-digit numbers
            num = char
            while j+1 < len(myLine) and myLine[j+1].isdigit():
                num += myLine[j+1]
                j += 1
            # Check if the position of any digit is marked
            if any(myMarked[i][j-len(num)+k+1] for k in range(len(num))):
                # Add the number to the sum
                theSum += int(num)
        j += 1

# Print the sum
print(f'Final sum: {theSum}')