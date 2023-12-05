"""--- Part Two ---

Everyone will starve if you only plant such a small number of seeds. Re-reading
the almanac, it looks like the seeds: line actually describes ranges of seed numbers.

The values on the initial seeds: line come in pairs. Within each pair, the first
value is the start of the range and the second value is the length of the range.
So, in the first line of the example above:

seeds: 79 14 55 13

This line describes two ranges of seed numbers to be planted in the garden.
    The first range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92.
The second range starts with seed number 55 and contains 13 values: 55, 56, ..., 66, 67.

Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.

In the above example, the lowest location number can be obtained from seed number 82,
which corresponds to soil 84, fertilizer 84, water 84, light 77, temperature 45,
humidity 46, and location 46.

So, the lowest location number is 46.

Consider all of the initial seed numbers listed in the ranges on the first line of the almanac.

What is the lowest location number that corresponds to any of the initial seed numbers?

"""

""" Summary:
    Now seed numbers are given in RANGES.
    Each RANGE is defined by a pair of numbers: the start of the range and the length of the range.
    For example, "79 14" represents a RANGE starting at 79 and containing 14 VALUES.

    The task is to consider all seed numbers in these ranges and find the lowest
    location number that corresponds to any of these seed numbers.

    The location number is determined by a series of transformations represented
    by different maps (soil, fertilizer, water, light, temperature, humidity).

    The goal is:
        Find the LOWEST -FINAL- location number across -ALL- INITIAL seed numbers IN THE GIVEN RANGES.

"""

""" The Plan:
    1. Import the bisect_right function from the bisect module.
    2. Define a function ParseTheMap that takes a list of map lines, parses each line
        into a range of source and destination values, and returns a sorted list of these ranges.
    3. Define a function FindLocation that takes a seed and a list of maps, finds the
        final location of the seed by applying each map in order, and return the final location.
    4. Open the input file and read all lines into a list.
    5. Parse the first line of the file to get the initial seed values.
    6. Parse the seed ranges, generate all the seed numbers
    7. Parse the maps, and then find the minimum final location across all seeds.

    I think... ¯\_(ツ)_/¯  lol
"""

# NOTE: to self - at this point I've just pasted in the code from the first puzzle for reference
from bisect import bisect_right

def ParseTheMap(theMapLines):
    myMapRanges = []
    for aLine in theMapLines:
        if aLine:  # Skip empty lines
            myDestStart, mySrcStart, myLength = map(int, aLine.split())
            myMapRanges.append((mySrcStart, mySrcStart + myLength, myDestStart))
    myMapRanges.sort()
    return myMapRanges

def FindLocation(theSeed, theMaps):
    for mapRanges in theMaps:
        i = bisect_right(mapRanges, (theSeed,)) - 1
        if i >= 0 and mapRanges[i][0] <= theSeed < mapRanges[i][1]:
            theSeed = mapRanges[i][2] + (theSeed - mapRanges[i][0])
    return theSeed

# Read the input data from the file
with open('day5/input5.txt', 'r') as file:
    myLines = file.readlines()

# Parse the seeds
mySeedsLine = myLines.pop(0)
mySeeds: list = list(map(int, mySeedsLine.split(':')[1].split()))

# Parse the maps
myMaps = []
while myLines:
    # Remove the map title line
    myLines.pop(0)
    # Get the map lines
    myMapLines = []
    while myLines and ':' not in myLines[0]:
        myMapLines.append(myLines.pop(0).strip())
    # Parse the map and add it to the list of maps
    myMaps.append(ParseTheMap(myMapLines))

# Find the minimum location number
myMinLocation = min(FindLocation(aSeed, myMaps) for aSeed in mySeeds)

print(myMinLocation)