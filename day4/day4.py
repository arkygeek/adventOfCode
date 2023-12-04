"""
    The plan:

    1 - Define a function calculatePoints that takes a list of cards as input.
    2 - For each card, split the card into two lists: myWinningNumbers and myNumbers.
    3 - Convert these lists into sets for faster lookup. see -> https://stackoverflow.com/questions/25294897/why-is-converting-a-list-to-a-set-faster-than-using-just-list-to-compute-a-list
    4 - Find the intersection of these two sets to get the matching numbers.
    5 - If there are no matching numbers, the card is worth 0 points.
    6 - If there are matching numbers, calculate the points for the card.
        a) The first match is worth 1 point, and
        b) ** EACH SUBSEQUENT MATCH DOUBLES THE POINTS **
    7 - Add the points for the card to a total sum.
    8 - After all of the cards have been processed, return the total.
"""



def CalculatePoints(myCards):
    """ Calculates the total points for a list of cards.
    Args:
        myCards (list): A list of cards.
    Returns:
        int: The total points for all the cards.
    """
    myTotalPoints = 0
    for aCard in myCards:
        aCard = aCard.split(': ')[1]  # Remove the leading text i.e. 'Card X: '
        myWinningNumbers, myNumbers = aCard.split('|')

        """ myWinningNumbers = set(map(int, myWinningNumbers.split()))
        This line of code is doing a few things, but generally, it converts
        a space-separated string of numbers into a set of integers.
        For example, if myWinningNumbers is: "41 48 83 86 17"
        this line of code would produce the set {41, 48, 83, 86, 17}
        This is how it works
            myWinningNumbers.split()
                This splits the string myWinningNumbers into a list of substrings.
                * By default, split() divides a string into parts wherever it finds a space.
            map(int, ...)
                This applies the int function to each substring in the list.
                The int function converts a string to an integer.
                (this just turns a list of numeric strings into a list of integers)
                @TODO implement a data validation step here in case there is weirdness in the input file
            set(...): This converts the list of integers into a set.
                        A set is an unordered collection of unique elements.
                        This is a nice efficient way of eliminating duplicates, checking membership, etc.
        """
        myWinningNumbers = set(map(int, myWinningNumbers.split()))
        myNumbers = set(map(int, myNumbers.split()))
        print(f'Winning numbers: {myWinningNumbers}')  # Debug
        print(f'My numbers: {myNumbers}')  # Debug
        myMatches = myWinningNumbers & myNumbers
        print(f'Matches: {myMatches}')  # Debug
        myPoints = 0 if len(myMatches) == 0 else 2**(len(myMatches) - 1)
        print(f'Points for this card: {myPoints}')  # Debug
        myTotalPoints += myPoints
    return myTotalPoints

with open('day4/input4.txt', 'r') as file: # I have my environment :P
    myCards = file.read().splitlines()

print(CalculatePoints(myCards))