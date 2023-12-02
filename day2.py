"""
    let's break down the problem into smaller steps:
    Parse the input data in each 'game' to
        (a) extract the game ID and
        (b) the sets of cubes revealed
    For each game:
        (1) check if any set of cubes revealed exceeds the given number of
            cubes of that color (12 red, 13 green, 14 blue).
            * If it does, the game is not possible.
        (2) If all sets of cubes revealed in a game are possible,
            add the game ID to the sum.
"""

import re
# Define the maximum number of cubes of each color
myMaxCubes = {'red': 12, 'green': 13, 'blue': 14}

# Initialize the sum of the IDs of the possible games
mySumOfIds = 0

# Open and read the input file
with open('input2.txt', 'r') as theFile:
    """ Extract the game ID and the sets of cubes revealed

        I will use a regular expression to extract the game ID and the sets of cubes revealed from the line.
        'Game (\d+): (.*)' matches the pattern 'Game ',
        followed by one or more digits (the game ID),
            followed by ': ',
                followed by any characters (the sets of cubes which were revealed)
        The match object's groups() method returns:
        (1) a tuple of the game ID
        (2) and the sets of cubes revealed,

    These are then unpacked into the variables myGameId and myCubeSets.
    """
    for myLine in theFile:
        myGameId, myCubeSets = re.match(r'Game (\d+): (.*)', myLine).groups() # this line
        myGameId = int(myGameId)
        myCubeSets = myCubeSets.split('; ')

        # Check if the game is possible
        foundPossible = True  # assume it is possible until we learn otherwise
        for theCubeSet in myCubeSets:
            myCubes = re.findall(r'(\d+) (\w+)', theCubeSet)
            for theCount, theColor in myCubes:
                if int(theCount) > myMaxCubes[theColor]:
                    foundPossible = False
                    break
            if not foundPossible:
                # exit the loop as soon as a game that's not possible is found,
                # because if that's the case there's no need to check the rest of the games.
                break

        # If the game is possible, add the game ID to the sum
        if foundPossible:
            mySumOfIds += myGameId

print(f"Sum of the IDs of the possible games: {mySumOfIds}")