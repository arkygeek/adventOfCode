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

# NOTE: to self - I've been able to reuse the two functions I guess so that's cool

from bisect import bisect_right

def ParseTheMap(theMapLines):
    myMapRanges = []
    for aLine in theMapLines:
        if aLine:  # Skip empty lines
            myDestStart, mySrcStart, myLength = map(int, aLine.split())
            myMapRanges.append((mySrcStart, mySrcStart + myLength, myDestStart))
    myMapRanges.sort()
    return myMapRanges

def find_location(seed, maps):
    while True:
        new_seed = seed
        for map_ranges in maps:
            i = bisect_right(map_ranges, (new_seed,)) - 1
            if i >= 0 and map_ranges[i][0] <= new_seed < map_ranges[i][1]:
                new_seed = map_ranges[i][2] + (new_seed - map_ranges[i][0])
        if new_seed == seed:
            break
        else:
            seed = new_seed
    return seed

def parse_seeds(seed_line):
    _, seed_numbers = seed_line.split('seeds:')
    seed_ranges = list(map(int, seed_numbers.strip().split()))
    seeds = []
    for i in range(0, len(seed_ranges), 2):
        start, length = seed_ranges[i], seed_ranges[i+1]
        seeds.extend(range(start, start + length))
    print(f"Seeds: {seeds}")  # Debug print
    return seeds

def parse_maps(lines):
    maps = []
    while lines:
        line = lines.pop(0).strip()
        if line:  # Skip empty lines
            map_lines = []
            while lines and ':' not in lines[0]:
                map_line = lines.pop(0).strip()
                if map_line:  # Skip empty lines
                    map_lines.append(map_line)
            maps.append(parse_map(map_lines))
    return maps

def parse_map(map_lines):
    map_ranges = []
    for line in map_lines:
        dest_start, src_start, length = map(int, line.split())
        map_ranges.append((src_start, src_start + length, dest_start))
    map_ranges.sort()
    return map_ranges

def find_location(seed, maps):
    print(f"Starting seed: {seed}")  # Debug print
    for map_ranges in maps:
        i = bisect_right(map_ranges, (seed,)) - 1
        if i >= 0 and map_ranges[i][0] <= seed < map_ranges[i][1]:
            seed = map_ranges[i][2] + (seed - map_ranges[i][0])
    print(f"Final location: {seed}")  # Debug print
    return seed

def find_min_location(seeds, maps):
    seed_locations = [(seed, find_location(seed, maps)) for seed in seeds]
    min_seed, min_location = min(seed_locations, key=lambda x: x[1])
    return min_seed, min_location

sample="""
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
56 93 4"""

# with open('day5/sample5.txt', 'r') as file:
#     lines = file.readlines()

lines = sample.strip().split('\n')

initial_seeds = parse_seeds(lines[0])
maps = parse_maps(lines[1:])
min_seed, min_location = find_min_location(initial_seeds, maps)

print(f"Lowest location number that corresponds to any of the initial seed numbers: {min_location}")

# def ParseTheMap(theMapLines):
#     myMapRanges = []
#     for aLine in theMapLines:
#         if aLine:  # Skip empty lines
#             myDestStart, mySrcStart, myLength = map(int, aLine.split())
#             myMapRanges.append((mySrcStart, mySrcStart + myLength, myDestStart))
#     myMapRanges.sort()
#     print(f"Map Ranges: {myMapRanges}")  # Debug print
#     return myMapRanges

# def FindLocation(theSeed, theMaps):
#     originalSeed = theSeed  # Store the original seed
#     print(f"Starting seed: {originalSeed}")  # Debug print
#     for mapRanges in theMaps:
#         i = bisect_right(mapRanges, (theSeed,)) - 1
#         if i >= 0 and mapRanges[i][0] <= theSeed < mapRanges[i][1]:
#             print(f"Seed {theSeed} is in range {mapRanges[i]}")  # Debug print
#             theSeed = mapRanges[i][2] + (theSeed - mapRanges[i][0])
#             print(f"New seed: {theSeed}")  # Debug print
#     print(f"Final Location for seed {originalSeed}: {theSeed}")  # Debug print
#     return theSeed

# # Read the input data from the file
# with open('day5/sample5.txt', 'r') as file:
#     myLines = file.readlines()

# def parse_maps(lines):
#     maps = []
#     while lines:
#         lines.pop(0)
#         map_lines = []
#         while lines and ':' not in lines[0]:
#             map_lines.append(lines.pop(0).strip())
#         maps.append(ParseTheMap(map_lines))
#     return maps

# def find_min_location(seeds, maps):
#     seed_locations = [(seed, FindLocation(seed, maps)) for seed in seeds]
#     min_seed, min_location = min(seed_locations, key=lambda x: x[1])
#     return min_seed, min_location

# def parse_seeds(seed_line):
#     _, seed_numbers = seed_line.split('seeds:')
#     seed_ranges = list(map(int, seed_numbers.strip().split()))
#     seeds = []
#     for i in range(0, len(seed_ranges), 2):
#         start, length = seed_ranges[i], seed_ranges[i+1]
#         seeds.extend(range(start, start + length))
#     return seeds

# # Main code
# with open('day5/sample5.txt', 'r') as file:
#     myLines = file.readlines()

# theMaps = parse_maps(myLines.copy())  # Create a copy of myLines
# mySeedsLine = myLines[0]  # Assuming the first line contains the seed ranges
# initial_seeds = parse_seeds(mySeedsLine)
# min_seed, min_location = find_min_location(initial_seeds, theMaps)

# print(f"Lowest location number that corresponds to any of the initial seed numbers: {min_location}")