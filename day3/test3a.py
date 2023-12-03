# Open the file for reading
with open('input3.txt', 'r') as theFile:
    myLines = [list(line.strip()) for line in theFile]

# Create the marked array
myMarked = [[False]*len(theLine) for theLine in myLines]

# Mark positions adjacent to a symbol
for i in range(len(myLines)):
    for j in range(len(myLines[i])):
        if myLines[i][j] in '#$%&@=+-/*':
            for myRowChange in range(-1, 2):
                for myColumnChange in range(-1, 2):
                    if 0 <= i+myRowChange < len(myLines) and 0 <= j+myColumnChange < len(myLines[i]):
                        myMarked[i+myRowChange][j+myColumnChange] = True

# Create a map of all the full numbers and their positions
num_map = {}
for i in range(len(myLines)):
    myLine = myLines[i]
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
            # Store the number in the map with all its positions
            for k in range(j-len(num)+1, j+1):
                num_map[(i, k)] = int(num)
        j += 1

# Initialize the total sum
total_sum = 0

# Iterate over each cell in the grid
for i in range(len(myLines)):
    for j in range(len(myLines[i])):
        # If the cell contains a '*', check its neighbors
        if myLines[i][j] == '*':
            neighbors = []
            # Check the up neighbor
            if i > 0 and (i-1, j) in num_map:
                neighbors.append(num_map[(i-1, j)])
            # Check the down neighbor
            if i < len(myLines)-1 and (i+1, j) in num_map:
                neighbors.append(num_map[(i+1, j)])
            # Check the left neighbor
            if j > 0 and (i, j-1) in num_map:
                neighbors.append(num_map[(i, j-1)])
            # Check the right neighbor
            if j < len(myLines[i])-1 and (i, j+1) in num_map:
                neighbors.append(num_map[(i, j+1)])
            # If exactly two neighbors are numbers, add their product to the total sum
            if len(neighbors) == 2:
                total_sum += neighbors[1]

# Print the total sum
print(f'Sum of gear ratios: {total_sum}')
