"""
    Let's break down the problem into smaller steps:

    Parse the input data to extract
        (a) the game ID and
        (b) the sets of cubes revealed in each game.

    For each game, find the maximum number of cubes of each colour revealed in any set.
        * This is the minimum number of cubes of that colour that must have been in the bag.

    Calculate the power of the minimum set of cubes for each game
    and add it to the running total for a final sum.
"""

import re
from collections import defaultdict

# Initialize the sum of the powers of the minimum sets of cubes
mySumOfPowers: int = 0

# Open and read the input file
with open('input2.txt', 'r') as file:
    for line in file:
        # print(line)  # Add this line to print the lines being read
        match = re.match(r'Game (\d+): (.*)', line)
        # print(match)  # Add this line to print the match object

        if match is None:
            continue

        myGameId, myCubeSets = match.groups()
        myCubeSets = myCubeSets.split('; ')

        # Find the minimum number of cubes of each colour that must have been in the bag
        myMinCubes = defaultdict(int)
        for theCubeSet in myCubeSets:
            myCubes = re.findall(r'(\d+) (\w+)', theCubeSet)
            for myCount, myColour in myCubes:
                myMinCubes[myColour] = max(myMinCubes[myColour], int(myCount))

        # Calculate the power of the minimum set of cubes and add it to the sum
        myPower = myMinCubes['red'] * myMinCubes['green'] * myMinCubes['blue']
        # print(myMinCubes)  # print the minCubes dictionary
        # print(myPower)  # print the power variable
        mySumOfPowers += myPower

print(f"Sum of the powers of the minimum sets of cubes: {mySumOfPowers}")