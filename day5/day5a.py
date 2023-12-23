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

In the above example, the lowest location number can be obtained from
seed number 82              (read: which corresponds to ...)
    ↳ soil 84
        ↳ fertilizer 84
            ↳ water 84
                ↳ light 77
                    ↳ temperature 45
                        ↳ humidity 46
                            ↳ location 46  <-- <-- <-- <-- OUR TARGET

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


""" Some notes:

Each seed number is transformed through a series of maps:
(soil, fertilizer, water, light, temperature, humidity)
to determine its corresponding location number.

Each transformation is dependent on the result of the previous one (hence the term "cascading")




To begin, lets look at the actual input data:


First line of actual input data:
seeds: 4088478806 114805397 289354458 164506173 1415635989 166087295 1652880954 340945548 3561206012 483360452 35205517 252097746 1117825174 279314434 3227452369 145640027 2160384960 149488635 2637152665 236791935

seed data now comes in pairs (StartingSeedNumber, Range)
lets look at the first pair: 4088478806 114805397
this means that there are 114,805,397 seeds to examine from the first seed pair alone!
what about second third and fourth pairs

START NUM          HOW MANY?
4088478806        114,805,397
289354458         164,506,173
1415635989        166,087,295
1652880954        340,945,548
3561206012        483,360,452
35205517          252,097,746
1117825174        279,314,434
3227452369        145,640,027
2160384960        149,488,635
2637152665        236,791,935
              + -------------
  Total Seeds:  2,333,037,642

-+-+-+ THIS IS GOING TO BE A HUGE DATASET +-+-+-

(if we try to brute force it, it's going to take too long I think)

P2=[]
pairs=list(zip(seed[::2], seed[1::2]))
for aStart, aSize in pairs:
  # inclusive on the left, exclusive on the right
  # e.g. [1,3) = [1,2]
  # length of [a,b) = b-a
  # [a,b) + [b,c) = [a,c)
  R=[(aStart, aStart+aSize)]

The notation [a, b) is a common mathematical notation used to denote an interval.

In this context:

[a, b) means the interval that includes a and all numbers up to but not including b. This is why the comment says "inclusive on the left, exclusive on the right".
[1,3) is equivalent to [1,2] because it includes 1 and 2, but not 3.

The length of [a,b) is b-a because it includes all numbers from a to b, but not b itself.
[a,b) + [b,c) equals [a,c) because the two intervals are adjacent and their union forms a single interval from a to c.

This notation is used to describe the ranges in the seed data.

The square bracket [ means that the boundary is included in the interval, and
the round bracket ) means that the boundary is not included.

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

+-----------------------------+
|  What went down in the end  |
+-----------------------------+------------------------------------------------+
|                                                                              |
| I think that having both solutions in the same script like this is a great   |
| approach. I plan to implement this approach from day 6 onwards (if possible) |
|                                                                              |
+------------------------------------------------------------------------------+

Read unsplit puzzle input from file and use that input to solve both parts

+-----------------------+
|  solve_first_puzzle   |
+-----------------------+
This takes the puzzle input, splits it into chunks, and finds every seed value.
We then iterate over each seed value and each chunk, finding all conversions
(triplets of numbers) in each chunk.

For each conversion, we check if the seed value is in the range defined by the
start and delta of the conversion. If it is, we adjust the seed value by the
difference between the destination and the start of the conversion.

We keep track of the minimum seed value encountered and return this as the
solution to the first part of the puzzle.

+-----------------------+
|  solve_second_puzzle  |
+-----------------------+
Here, we take the puzzle input and split it into chunks again, just like before.

We then create a list of intervals from the seed values.

Now, we iterate over each INTERVAL, checking its level...
If the level is 8 we update the minimum location with the START of the interval.
    OTHERWISE, we find all conversions in the chunk corresponding to the level of the interval.

For each conversion, it checks if there's an overlap with the interval.

If there is an overlap with the interval, we can split the interval at the start
and end of the overlap, and adjust the interval by the difference between the
destination and the start of the conversion.

Now we can add the ADJUSTED interval to the list of intervals at the NEXT level.

This gives the minimum location, the solution to the second part of the puzzle.
"""

import re  # Support for regular expressions

# Read the puzzle input from the file
with open('day5/input5.txt', 'r') as myFile:
    myPuzzleInput = myFile.read()

def solve_first_puzzle(thePuzzleInput):
    # Split the puzzle input into chunks using two consecutive newlines
    myPuzzleChunks = thePuzzleInput.split('\n\n')

    # Extract seed values as integers from the first chunk using regex
    mySeedValuesStr = re.findall(r'\d+', myPuzzleChunks[0])

    # Initialize minimum location to positive infinity
    myMinLocation = float('inf')

    # Iterate through each seed value
    for eaSeedValue in map(int, mySeedValuesStr):
        # Iterate through each conversion rule in subsequent chunks
        for eaChunk in myPuzzleChunks[1:]:
            # Extract all conversion rules from the chunk
            myAllConversions = re.findall(r'(\d+) (\d+) (\d+)', eaChunk)

            # Iterate through each conversion rule
            for eaConversion in myAllConversions:
                myDestination, myStart, myDelta = map(int, eaConversion)

                # Check if the seed value falls within the current conversion range
                if eaSeedValue in range(myStart, myStart + myDelta):
                    # Update the seed value based on the conversion rule
                    eaSeedValue += myDestination - myStart
                    break

        # Update the minimum location based on the modified seed value
        myMinLocation = min(eaSeedValue, myMinLocation)

    # Return the minimum location
    return myMinLocation

def solve_second_puzzle(thePuzzleInput):
    # Split the puzzle input into chunks using two consecutive newlines
    myPuzzleChunks = thePuzzleInput.split('\n\n')

    # Initialize an interval list with the initial seed values
    # Iterate over all matches of two numbers separated by a space in the first chunk of the puzzle input
        # Convert the matched values to integers and assign them to myStartValue and myDeltaValue
        # Calculate the end value of the interval by adding the delta to the start value
        # Append the interval (start value, end value, level) to myIntervalList
    myIntervalList = []
    for eaSeedValue in re.findall(r'(\d+) (\d+)', myPuzzleChunks[0]):
        myStartValue, myDeltaValue = map(int, eaSeedValue)
        myEndValue = myStartValue + myDeltaValue
        myIntervalList.append((myStartValue, myEndValue, 1))

    # Initialize the minimum location to positive infinity
    myMinLocation = float('inf')

    # Process intervals in the interval list
    while myIntervalList:
        # Pop an interval from the list
        myStartValue, myEndValue, myLevel = myIntervalList.pop()

        # If the current level is the target level (8), update the minimum location and continue
        if myLevel == 8:
            myMinLocation = min(myStartValue, myMinLocation)
            continue

        # Extract all conversion rules for the current level from the puzzle input
        myAllConversions = re.findall(r'(\d+) (\d+) (\d+)', myPuzzleChunks[myLevel])

        # Iterate through each conversion rule
        for eaConversion in myAllConversions:
            # Parse the destination, start, and delta values from the conversion rule
            myDestination, myStart, myDelta = map(int, eaConversion)
            # Calculate the end value and the difference for the conversion
            myEnd = myStart + myDelta
            myDifference = myDestination - myStart

            # If the conversion does not overlap with the current interval, skip it
            if myEndValue <= myStart or myEnd <= myStartValue:
                continue

            # If the conversion starts after the current interval, split the interval and update the start value
            if myStartValue < myStart:
                myIntervalList.append((myStartValue, myStart, myLevel))
                myStartValue = myStart

            # If the conversion ends before the current interval, split the interval and update the end value
            if myEnd < myEndValue:
                myIntervalList.append((myEnd, myEndValue, myLevel))
                myEndValue = myEnd

            # Apply the conversion to the current interval and add the new interval to the list
            myIntervalList.append((myStartValue + myDifference, myEndValue + myDifference, myLevel + 1))
            break  # Stop checking other conversions for this interval

        else:
            # If no conversion was applied, add the original interval back to the list with the level incremented
            myIntervalList.append((myStartValue, myEndValue, myLevel + 1))

    # Return the minimum location
    return myMinLocation

# Print the results for both parts of the puzzle
print('Part 1:', solve_first_puzzle(myPuzzleInput))
print('Part 2:', solve_second_puzzle(myPuzzleInput))
