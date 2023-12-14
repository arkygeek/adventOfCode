"""--- Day 5: If You Give A Seed A Fertilizer ---

You take the boat and find the gardener right where you were told he would be:
managing a giant "garden" that looks more to you like a farm.

"A water source? Island Island is the water source!" You point out that Snow
Island isn't receiving any water.

"Oh, we had to stop the water because we ran out of sand to filter it with!
Can't make snow with dirty water. Don't worry, I'm sure we'll get more sand
soon; we only turned off the water a few days... weeks... oh no." His face
sinks into a look of horrified realization.

"I've been so busy making sure everyone here has food that I completely forgot
to check why we stopped getting more sand! There's a ferry leaving soon that is
headed over in that direction - it's much faster than your boat. Could you
please go check it out?"

You barely have time to agree to this request when he brings up another. "While
you wait for the ferry, maybe you can help us with our food production problem.
The latest Island Island Almanac just arrived and we're having trouble making
sense of it."

The almanac (your puzzle input) lists all of the seeds that need to be planted.
It also lists what type of soil to use with each kind of seed, what type of
fertilizer to use with each kind of soil, what type of water to use with each
kind of fertilizer, and so on. Every type of seed, soil, fertilizer and so on
is identified with a number, but numbers are reused by each category - that is,
soil 123 and fertilizer 123 aren't necessarily related to each other.
For example:

seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
The almanac starts by listing which seeds need to be planted: seeds 79, 14, 55, and 13.

The rest of the almanac contains a list of maps which describe how to convert
numbers from a source category into numbers in a destination category.
That is, the section that starts with seed-to-soil map: describes how to convert
a seed number (the source) to a soil number (the destination).
This lets the gardener and his team know which soil to use with which seeds,
which water to use with which fertilizer, and so on.

Rather than list every source number and its corresponding destination number one
by one, the maps describe entire ranges of numbers that can be converted.
Each line within a map contains three numbers: the destination range start, the
source range start, and the range length.

Consider again the example seed-to-soil map:

50 98 2
52 50 48

The first line has a destination range start of 50, a source range start of 98,
and a range length of 2. This line means that the source range starts at 98 and
contains two values: 98 and 99. The destination range is the same length, but it
starts at 50, so its two values are 50 and 51. With this information, you know
that seed number 98 corresponds to soil number 50 and that seed number 99
corresponds to soil number 51.

The second line means that the source range starts at 50 and contains 48 values:
50, 51, ..., 96, 97. This corresponds to a destination range starting at 52 and
also containing 48 values: 52, 53, ..., 98, 99.

So, seed number 53 corresponds to soil number 55.

Any source numbers that aren't mapped correspond to the same destination number.
So, seed number 10 corresponds to soil number 10.

So, the entire list of seed numbers and their corresponding soil numbers looks like this:

seed  soil
0     0
1     1
...   ...
48    48
49    49
50    52
51    53
...   ...
96    98
97    99
98    50
99    51
With this map, we can look up the soil number required for each initial seed number:

Seed number 79 corresponds to soil number 81.
Seed number 14 corresponds to soil number 14.
Seed number 55 corresponds to soil number 57.
Seed number 13 corresponds to soil number 13.
The gardener and his team want to get started as soon as possible, so they'd like
to know the closest location that needs a seed. Using these maps, find the lowest
location number that corresponds to any of the initial seeds.

To do this, we'll need to convert each seed number through other categories until
we can find its corresponding location number.

In this example, the corresponding types are:

Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.
So, the lowest location number in this example is 35.

What is the lowest location number that corresponds to any of the initial seed numbers?
"""

""" Summary:
A gardener needs help with a food production problem.
The gardener has an almanac that lists all the seeds that need to be planted
The Almanac also has the corresponding _______ for each seed:
    soil
    fertilizer
    water
    light
    temperature
    humidity
    location

The almanac uses a complex mapping system where:
    - each category is identified with a number, and
    - numbers are reused by each category.

So I think that the goal is to:
 - find the lowest location number that:
    - corresponds to any of the initial seed numbers by:
        - converting each seed number through other categories:
            - until we can find its corresponding location number.

"""


""" Observations
- Each line within a map contains three numbers:
    No.1 - the destination range start
    No.2 - the source range start, and
    No.3 - the range length

"""

""" The Plan
I think lists, sets, and maps (dictionaries in Python) will be a good approach...
Here's a rough plan:
- Lists: use lists to store the initial seed numbers and the corresponding location numbers

- Sets: Sets can be used to keep track of the seed numbers that have been processed.
        This can help to avoid processing the same seed number multiple times.

- Dictionaries: Dictionaries can be used to map each seed number to its corresponding location number.
                I can also use dictionaries to store the mappings from the almanac.

                **NOTE**
                In Python, a map is not a built-in data type,
                *** but ***
                there is a built-in function called map().

                The map() function applies a given function to each item of an iterable
                (such as a list or tuple) and returns a list of the results.

                Here's an example of how to use the map() function:
                    def square(n):
                    return n ** 2

                    numbers = [1, 2, 3, 4, 5]
                    squares = map(square, numbers)

                    # Convert the map object to a list to print the results
                    print(list(squares))  # Output: [1, 4, 9, 16, 25]

                In this example, the map() function applies the square function
                to each item in the numbers list.

                In Python, a dictionary is a built-in data type that stores key-value pairs.

                Here's an example of a dictionary:

                student = {
                    "name": "John Doe",
                    "age": 20,
                    "grade": "A"
                }

                print(student["name"])  # Output: John Doe

                In this example:

                 keys    :  Value
                -------     ----------
                "name"   :  "John Doe"
                "age"    :  20
                "grade"  :  "A"

                We can access the value of a key by using the key inside square brackets [].

"""

""" More detailed plan
1. Parse the input data:
    Read the almanac file and parse it into a suitable data structure.
    We can use a dictionary to store the mappings from each category to the next.
2. Initialize the data structures:
    Create a list to store the initial seed numbers and a set to keep track of
    the seed numbers that have been processed. Also, create a dictionary to map
    each SEED number to its corresponding LOCATION number.
3. Process the seed numbers:
    a) For each SEED number, use the mappings from the almanac to find the
        corresponding LOCATION number.
    b) Add the SEED number to the set of processed seed numbers and add the
        LOCATION number to the list of location numbers.
4. Repeat the process:
    Continue processing the seed numbers until all seed numbers have been processed.
    NOTE: If a seed number is already in the set of processed seed numbers, we can
    skip it to avoid processing the same seed number multiple times.
5. Find the lowest location number:
    Once all SEED numbers have been processed, find the lowest LOCATION number
    in the list of location numbers.

    This should be the solution to the puzzle...
"""

""" What I actually did
1.  Read data from a file, parsed it into a series of maps,
    and then found the minimum location for a set of seeds.
2.  ParseTheMap
    This function takes a list of map lines as input and then:
    a)  for each line, splits the line into three integers:
            1. the start of the destination range
            2. the start of the source range, and
            3. the length of the range.
    b)  we then append a tuple representing the source range and the
        corresponding destination start to a list of map ranges.
    c)  the list of map ranges is sorted and returned.
3.  FindLocation
    This function takes a seed and a list of maps as input.
    For each map:
    a) it finds the range that the seed falls into and
    b) map the seed to the corresponding destination.

    The final mapped seed is then returned.

The solution (minimum location) can now be printed.
"""

from typing import List, Tuple
from bisect import bisect_right

def ParseTheMap(theMapLines: List[str]) -> List[Tuple[int, int, int]]:
    myMapRanges = []
    for aLine in theMapLines:
        if aLine:  # Skip empty lines
            myDestStart, mySrcStart, myLength = map(int, aLine.split())
            myMapRanges.append((mySrcStart, mySrcStart + myLength, myDestStart))
    myMapRanges.sort()
    return myMapRanges

def FindLocation(theSeed: int, theMaps: List[List[Tuple[int, int, int]]]) -> int:
    for myMapRanges in theMaps:
        i = bisect_right(myMapRanges, (theSeed,)) - 1
        if i >= 0 and myMapRanges[i][0] <= theSeed < myMapRanges[i][1]:
            theSeed = myMapRanges[i][2] + (theSeed - myMapRanges[i][0])
    return theSeed

# Read the input data from the file
with open('day5/input5.txt', 'r') as myFile:
    myLines: List[str] = myFile.readlines()

# Parse the seeds
mySeedsLine = myLines.pop(0)
mySeeds: List[int] = list(map(int, mySeedsLine.split(':')[1].split()))

# Parse the maps
myMaps: List[List[Tuple[int, int, int]]] = []
while myLines:
    # Remove the map title line
    myLines.pop(0)
    # Get the map lines
    myMapLines: List[str] = []
    while myLines and ':' not in myLines[0]:
        myMapLines.append(myLines.pop(0).strip())
    # Parse the map and add it to the list of maps
    myMaps.append(ParseTheMap(myMapLines))

# Find the minimum location number
myMinLocation: int = min(FindLocation(aSeed, myMaps) for aSeed in mySeeds)

print(myMinLocation)
