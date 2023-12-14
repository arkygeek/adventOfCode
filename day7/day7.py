""" Overview:
Read hands and bids from file, encode the hands into sortable tuples, sort the
tuples, and then calculate total winnings based on the rank and bid of each hand
"""

from typing import List, Tuple, Generator  # this is just so type hinting works properly

# Function to determine the type of a poker hand
def get_hand_type(theHand: str) -> int:
    # Define the types of camel poker hands in DESCENDING order of rank
    myOrderedTypes: List[List[int]] = [
                    [5], # Five of a kind
                 [4, 1], # Four of a kind
                 [3, 2], # Full house
              [3, 1, 1], # Three of a kind
              [2, 2, 1], # Two pairs
           [2, 1, 1, 1], # One pair
        [1, 1, 1, 1, 1]  # High card
    ]
    # Count the occurrences of each card in the hand
    myLabelCounts: List[int] = [theHand.count(eaCard) for eaCard in set(theHand)]
    # Sort the counts in descending order
    myLabelCounts.sort(reverse=True)
    # Return the index of the counts in the list of hand types
    return myOrderedTypes.index(myLabelCounts)

# Function to convert the cards in a hand to integers
def make_cards_integers(theHand: str) -> Generator[int, None, None]:
    # Define the order of the cards from highest to lowest
    myOrderedLabels: str = 'AKQJT98765432'
    # Return a generator that yields the index of each card in the order
    return (myOrderedLabels.index(eaCard) for eaCard in theHand) # I think this is nice and readable

# Read the input data from a file
myInputData: List[str] = open('day7/input7.txt').read().splitlines()

# Initialize a list to store the hand tuples (the hands)
myHands: List[Tuple[int, int, int, int, int, int]] = []  # (sortable) tuples of type, card values and bid

# For each line in the input data
for eaLine in myInputData:
    # Split each line into a hand and a bid
    myHand, myBid = eaLine.split(' ')
    # Encode the hand into a tuple (hand type, the integer representations of the cards, and the bid)
    myEncodedHand: Tuple[int, int, int, int, int, int] = (
        get_hand_type(myHand),
        *make_cards_integers(myHand),  # unpack the elements with the 'splat' operator (*)
        int(myBid)
    )
    # Add the encoded hand to the list of hands
    myHands.append(myEncodedHand)

# Sort the hands in DESCENDING order
myHands.sort(reverse=True)

# Calculate the winnings by adding the product of the rank and bid for each hand
myWinnings: int = sum(eaRank * eaHand[-1]  # rank * bid
               for eaRank, eaHand in enumerate(myHands, start=1))

""" ENUMERATE function in Python
class enumerate(
    iterable: Iterable[Tuple[int, int, int, int, int, int]],
    start: int = ...
)
Return an enumerate object.
  iterable
    an object supporting iteration

The enumerate object yields pairs containing a count (from start, which defaults
    to zero) and a value yielded by the iterable argument.

ENUMERATE is useful for obtaining an indexed list:
The enumerate function takes an iterable and returns an iterator
    that produces tuples of the form (index, element)
In this case, myHands is the iterable, which is a list of poker
    hand tuples.
'enumerate' is going through this list and for each hand, it is
    producing a tuple where the 1st element is the rank of the
    hand (the position in the sorted list) and the 2nd element
    is the hand itself.
The 'start=1' argument to 'enumerate' specifies that counting of
    the index should start at 1. By default, `enumerate` starts
    counting from 0 but in this case we want the first hand (the
    highest-ranking one) to have a rank of 1.
'eaRank' is the rank of the current hand in the SORTED LIST, and
'eaHand' is the current hand.
"""

# Print the total winnings
print(myWinnings)