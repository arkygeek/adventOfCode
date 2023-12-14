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
        """ The zip() function in Python:
        Takes in iterables as arguments and returns an iterator.
        This iterator generates a series of tuples containing elements from the input iterables.
        The i-th tuple contains the ith element from each of the argument sequences or iterables.

        class zip(
            __iter1: Iterable[_T1@__new__],
            __iter2: Iterable[_T2@__new__],
            /
        )

        zip(*iterables) --> zip objects yield tuples until AN input is exhausted

        EXAMPLE:
        list(zip('abcdefg', range(3), range(4)))
        [('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]

        The zip object yields n-length tuples, where n is the number of iterables
            passed as positional arguments to zip()
        The i-th element in every tuple comes from the i-th iterable argument to zip()
        This continues until the shortest argument is exhausted

        zip() STOPS creating tuples when the SHORTEST input iterable is exhausted.

        Note: If the input iterables are of different lengths, the resulting
              iterator will be as long as the shortest input iterable."""
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