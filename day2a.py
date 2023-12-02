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
sumOfPowers: int = 0

# Open and read the input file
with open('input2.txt', 'r') as file:
    for line in file:
        print(line)  # Add this line to print the lines being read
        match = re.match(r'Game (\d+): (.*)', line)
        print(match)  # Add this line to print the match object
        if match is None:
            continue
        gameId, cubeSets = match.groups()
        # rest of the code
        cubeSets = cubeSets.split('; ')

        # Find the minimum number of cubes of each colour that must have been in the bag
        minCubes = defaultdict(int)
        for cubeSet in cubeSets:
            cubes = re.findall(r'(\d+) (\w+)', cubeSet)
            for count, colour in cubes:
                minCubes[colour] = max(minCubes[colour], int(count))

        # Calculate the power of the minimum set of cubes and add it to the sum
        power = minCubes['red'] * minCubes['green'] * minCubes['blue']
        print(minCubes)  # Add this line to print the minCubes dictionary
        print(power)  # Add this line to print the power variable
        sumOfPowers += power

print(f"Sum of the powers of the minimum sets of cubes: {sumOfPowers}")