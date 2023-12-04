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
    myTotalPoints = 0
    for aCard in myCards:
        aCard = aCard.split(': ')[1]  # Remove 'Card X: '
        myWinningNumbers, myNumbers = aCard.split('|')
        myWinningNumbers = [s for s in myWinningNumbers.split() if s.isdigit()]
        myNumbers = [s for s in myNumbers.split() if s.isdigit()]
        myWinningNumbers = set(map(int, myWinningNumbers))
        """
        This bit of code is doing a few things, but generally, it converts
        a space-separated string of numbers into a set of integers.
        For example, if myWinningNumbers is: "41 48 83 86 17"
        this line of code would produce the set {41, 48, 83, 86, 17}
        This is how it works
        myWinningNumbers.split()
            This splits the string myWinningNumbers into a list of substrings.
            (by default it will split() a string wherever it finds a SPACE)
        map(int, ...)
            This applies int (the function) to every substring in the list.
            (this just turns a list of numeric strings into a list of integers)
            @DONE implement a data validation step here in case there is weirdness in the input file
                the list comprehensions (the following two indented lines) create new lists
                that will only include the strings that can be converted to integers.
                    [s for s in myWinningNumbers.split() if s.isdigit()]
                    [s for s in myNumbers.split() if s.isdigit()]
                The isdigit method checks if a string consists only of digits, which means it can be converted to an integer.
        set(...)
            This converts the list of integers into a set.
            A Set is an UNORDERED collection of UNIQUE elements.
            This is a nice efficient way of eliminating duplicates, checking membership, etc.
        """
        myNumbers = set(map(int, myNumbers))
        print(f'Winning numbers: {myWinningNumbers}')  # Debug print
        print(f'My numbers: {myNumbers}')  # Debug print
        myMatches = myWinningNumbers & myNumbers
        print(f'Matches: {myMatches}')  # Debug print
        myPoints = 0 if len(myMatches) == 0 else 2**(len(myMatches) - 1) # B-)
        print(f'Points for this card: {myPoints}')  # Debug print
        myTotalPoints += myPoints
    return myTotalPoints

with open('day4/input4.txt', 'r') as file: # I have my environment :P
    myCards = file.read().splitlines()

print(CalculatePoints(myCards))