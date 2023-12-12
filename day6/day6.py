"""--- Day 6: Wait For It ---
The ferry quickly brings you across Island Island. After asking around, you discover
that there is indeed normally a large pile of sand somewhere near here, but you don't
see anything besides lots of water and the small island where the ferry has docked.

As you try to figure out what to do next, you notice a poster on a wall near the
ferry dock.

"Boat races! Open to the public! Grand prize is an all-expenses-paid trip to
Desert Island!"

That must be where the sand comes from! Best of all, the boat races are starting
in just a few minutes.

You manage to sign up as a competitor in the boat races just in time.
The organizer explains that it's not really a traditional race - instead, you will
get a fixed amount of time during which your boat has to travel as far as it can,
and you win if your boat goes the farthest.

As part of signing up, you get a sheet of paper (your puzzle input) that lists the
time allowed for each race and also the best distance ever recorded in that race.

To guarantee you win the grand prize, you need to make sure you go farther in
each race than the current record holder.

The organizer brings you over to the area where the boat races are held.
The boats are much smaller than you expected - they're actually toy boats, each
with a big button on top.

Holding down the button charges the boat, and releasing the button allows the
boat to move.

Boats move faster if their button was held longer, but time spent holding the
button counts against the total race time.

You can only hold the button at the start of the race, and boats don't move until
the button is released.

For example:

Time:      7  15   30
Distance:  9  40  200
This document describes three races:

The first race lasts 7 ms (milliseconds). The record distance in this race is 9 mm.
The second race lasts 15 ms. The record distance in this race is 40 mm.
The third race lasts 30 ms. The record distance in this race is 200 mm.

Your toy boat has a starting speed of zero mm per ms.

For each whole ms you spend at the beginning of the race holding down
the button, the boat's speed increases by one millimeter per ms.

So, because the first race lasts 7 ms, you only have a few options:

(1) Don't hold the button at all (that is, hold it for 0 ms) at the start of the race.
    The boat won't move;
    it will have traveled 0 mm by the end of the race.
(2) Hold the button for 1 ms at the start of the race.
    Then, the boat will travel at a speed of 1 millimeter per ms for
    6 ms, reaching a total distance traveled of 6 mm.
(3) Hold the button for 2 ms, giving the boat a speed of 2 mm per ms. It will
    then get 5 ms to move, reaching a total distance of 10 mm.
(4) Hold the button for 3 ms. After its remaining 4 ms of travel time, the boat
    will have gone 12 mm.
(5) Hold the button for 4 ms. After its remaining 3 ms of travel time, the boat
    will have gone 12 mm.
(6) Hold the button for 5 ms, causing the boat to travel a total of 10 mm.
(7) Hold the button for 6 ms, causing the boat to travel a total of 6 mm.
(8) Hold the button for 7 ms. That's the entire duration of the race.
    You never let go of the button.
    The boat can't move until you let go of the button.
    Please make sure you let go of the button so the boat gets to move.
    0 mm.

Since the current record for this race is 9 mm, there are actually 4 different ways you could win: you could hold the button for 2, 3, 4, or 5 ms at the start of the race.

In the second race, you could hold the button for at least 4ms and at most 11ms
and beat the record, a total of 8 different ways to win.

In the third race, you could hold the button for at least 11 ms and no more than
19ms and still beat the record, a total of 9 ways you could win.

To see how much margin of error you have, determine the number of ways you can
beat the record in each race; in this example, if you multiply these values
together, you get 288 (4 * 8 * 9).

Determine the number of ways you could beat the record in each race.

What do you get if you multiply these numbers together?

"""

"""Summary:

Boats are powered by holding and releasing a button;
    the longer the button is held, the faster the boat goes,
    but this time counts against the total race time.

    Note -->   The boats don't move until the button is released.

The goal is to beat the record distance for each race.
The document provides the time allowed for each race and the best distance ever
recorded in that race.

We need to determine the number of ways to beat the record in each race by
calculating how long to hold the button to achieve a distance greater than the record.

The final answer is obtained by multiplying these numbers together.


"""


# import logging
# logging.basicConfig(level=logging.DEBUG)


Sample_Data: str = """
    Time:      7  15   30
    Distance:  9  40  200
"""

def calculate_ways_to_win(theTotalTime, theRecordDistance):
    myWaysToWin = 0
    for eaButtonHoldTime in range(theTotalTime):
        myRemainingTime = theTotalTime - eaButtonHoldTime
        myDistance = eaButtonHoldTime * myRemainingTime
        if myDistance > theRecordDistance:
            myWaysToWin += 1
    return myWaysToWin

def preprocess_the_data(theInputData):
    myPreprocessedData = []
    # Split the lines into parts
    myTimes = theInputData[0].split()[1:]  # Skip first element (Time:)
    myDistances = theInputData[1].split()[1:]  # Skip the first element (Distance:)
    # Convert times and distances to integers and pair them together
    for eaTime, eaDistance in zip(myTimes, myDistances):  # NOTE: zip() explantion
        # The zip() function in Python:
        #   Takes in iterables as arguments and returns an iterator.
        #   This iterator generates a series of tuples containing elements
        #     from the input iterables.
        #   The ith tuple contains the ith element from each of the argument
        #     sequences or iterables.
        #
        #   zip() STOPS creating tuples when the SHORTEST input iterable is exhausted.
        #
        #   Note: If the input iterables are of different lengths, the resulting
        #         iterator will be as long as the shortest input iterable.
        myPreprocessedData.append((int(eaTime), int(eaDistance)))
    return myPreprocessedData

def get_solution_from(theData):
    if isinstance(theData, tuple):
        # If theData is a pair of integers, just calculate the ways to win
        return calculate_ways_to_win(*theData)
    else:
        # If theData is a list of pairs, calculate the ways to win for each pair and multiply them together
        myTotalWaysToWin = 1
        for eaTime, eaDistance in theData:
            myWaysToWin = calculate_ways_to_win(eaTime, eaDistance)
            myTotalWaysToWin *= myWaysToWin
        return myTotalWaysToWin

def puzzle2_preprocess(theData):
    myTimes = [str(eaTime) for eaTime, eaDistance in theData]
    myDistances = [str(eaDistance) for eaTime, eaDistance in theData]
    concatenatedTimes = int(''.join(myTimes))
    concatenatedDistances = int(''.join(myDistances))
    return concatenatedTimes, concatenatedDistances

myInputFile: str = 'day6/input6.txt'
with open(myInputFile, 'r') as myFile:
    myInputData = myFile.readlines()

# logging.debug(f"Input data: {myInputData}")
myPreProcessedData = preprocess_the_data(myInputData)

# logging.debug(f"Preprocessed data: {myPreProcessedData}")
# logging.debug(f"Puzzle 2: {puzzle2Solution}")
myPuzzleOneSolution = get_solution_from(myPreProcessedData)

# NOTE: we already have the stripped data, so lets just use that for part 2
myPuzzleTwoPreprocessedData = puzzle2_preprocess(myPreProcessedData)
puzzle2Solution = get_solution_from(myPuzzleTwoPreprocessedData) # and we can reuse a slightly modified puzzle_process too bad you can't overload in python

print(f"Puzzle 1: {myPuzzleOneSolution}")

print(f"Puzzle 2: {puzzle2Solution}")