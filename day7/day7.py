from typing import List, Tuple, Generator

class PuzzleOne:
    def __init__(self):
        self.OrderedTypes = [
                       [5],  # Five of a kind
                    [4, 1],  # Four of a kind
                    [3, 2],  # Full house
                 [3, 1, 1],  # Three of a kind
                 [2, 2, 1],  # Two pairs
              [2, 1, 1, 1],  # One pair
            [1, 1, 1, 1, 1]  # High card
        ]
        self.OrderedLabels = 'AKQJT98765432'
        self.InputData = open('day7/input7.txt').read().splitlines()
        self.Hands = []

    def get_hand_type(self, theHand: str) -> int:
        myLabelCounts = [theHand.count(card) for card in set(theHand)]
        myLabelCounts.sort(reverse=True)
        return self.OrderedTypes.index(myLabelCounts)

    def make_cards_integers(self, theHand: str) -> Generator[int, None, None]:
        return (self.OrderedLabels.index(eaCard) for eaCard in theHand)

    def process_data(self):
        for eaLine in self.InputData:
            myHand, myBid = eaLine.split(' ')
            myEncodedHand = (
                self.get_hand_type(myHand),
                *self.make_cards_integers(myHand),
                int(myBid)
            )
            self.Hands.append(myEncodedHand)

        self.Hands.sort(reverse=True)

    def calculate_winnings(self) -> int:
        return sum(eaRank * eaHand[-1] for eaRank, eaHand in enumerate(self.Hands, start=1))



# Puzzle One
myPuzzle1 = PuzzleOne()
myPuzzle1.process_data()
myPuzzleOneAnswer = myPuzzle1.calculate_winnings()
print(myPuzzleOneAnswer)



# Part 2

from typing import List, Tuple, Generator

from typing import Generator, List, Tuple

class PuzzleTwo:
    def __init__(self):
        self.CardValues: dict[str, int] = {'A': 13, 'K': 12, 'Q': 11, 'T': 10, '9': 9, '8': 8, '7': 7,
                                           '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1}
        self.OrderedLabels: str = 'AKQT98765432J'
        self.InputData: List[str] = open('day7/input7.txt').read().splitlines()
        self.Hands: List[Tuple[str, Tuple[int, ...]]] = []

    def get_hand_type(self, theHand: str) -> int:
        myEditedHandWithNoJs = set(theHand.replace('J', ''))

        myCardCounts = [theHand.count(eaCard) for eaCard in myEditedHandWithNoJs]
        myJs = theHand.count('J')
        mySu = myCardCounts.count(1)
        myPr = myCardCounts.count(2)
        myK3 = myCardCounts.count(3)
        myK4 = myCardCounts.count(4)
        myK5 = myCardCounts.count(5)

        # uncomment to see what is happening to each hand
        # print(f'\ntheHand: {theHand}')
        # print(f'myJs = {myJs}')
        # print(f"mySu: {mySu}")
        # print(f"myPr: {myPr}")
        # print(f"myK3: {myK3}")
        # print(f"myK4: {myK4}")
        # print(f"myK5: {myK5}")


        # var assignment corresponds as follows:
        #(J,su,3k,2k,su)
        match (myJs, mySu, myPr, myK3, myK4, myK5):
            # 5 of a kind cases
            case (5, _, _, _, _, _):  # ( 5Js, _, _, _, _, _)
                print(f"{theHand} is a 5 of a kind")
                return 10             # JJJJJ returned as 5 of a kind handtype 10 (k5)
            case (4, 1, _, _, _, _):  # ( 4Js, 1su, _, _, _, _)
                print(f"{theHand} is a 5 of a kind")
                return 10             # aJJJJ as 5 of a kind handtype 10 (k5)
            case (3, _, 1, _, _, _):  # ( 3Js, _, 2pr, _, _, _)
                print(f"{theHand} is a 5 of a kind")
                return 10             # aaJJJ as 5 of a kind handtype 10 (k5)
            case (2, _, _, 1, _, _):  # ( 2Js, _, _, 1k3, _, _)
                print(f"{theHand} is a 5 of a kind")
                return 10             # aaaJJ as 5 of a kind handtype 10 (k5)
            case (1, _, _, _, 1, _):  # ( 1Js, _, _, _, 1k4, _)
                print(f"{theHand} is a 5 of a kind")
                return 10             # aaaaJ as 5 of a kind handtype 10 (k5)
            case (_, _, _, _, _, 1):  # ( _, _, _, _, _, 1k5)
                print(f"{theHand} is a 5 of a kind")
                return 10             # aaaaa as 5 of a kind handtype 10 (k5)
            # 4 of a kind cases
            case (3, 2, _, _, _, _):  #( 3Js, 2su, _, _, _, _)
                print(f"{theHand} is a 4 of a kind")
                return 9              # aJJJb as 5 of a kind handtype 9 (k4)
            case (2, _, 1, _, _, _):  # ( 2Js, _, 1pr, _, _, _)
                print(f"{theHand} is a 4 of a kind")
                return 9              # aaaJJ as 5 of a kind handtype 9 (k4)
            case (1, _, _, 1, _, _):  # ( 1Js, _, _, 1k3, _, _)
                print(f"{theHand} is a 4 of a kind")
                return 9             # aaaJb as 5 of a kind handtype 9 (k4)
            case (_, _, _, _, 1, _):  # ( _, _, _, _, 1k4, _,)
                print(f"{theHand} is a 4 of a kind")
                return 9  # aaaaa as 5 of a kind handtype 10 (k5)
            # Full House
            case (1, _, 2, _, _, _):
                print(f"{theHand} is a Full House")
                return 8   # Jaabb Full House
            case (_, _, 1, 1, _, _):
                print(f"{theHand} is a Full House")
                return 8   # aaabb Full House
            # 3 of a kind cases
            case (2, 3, _, _, _, _):
                print(f"{theHand} is a 3 of a kind")
                return 7  # aJJbc 3 of a kind
            case (1, 2, 1, _, _, _):
                print(f"{theHand} is a 3 of a kind")
                return 7  # aaJbc 3 of a kind
            case (_, _, _, 1, _, _):
                print(f"{theHand} is a 3 of a kind")
                return 7  # 3kind
            # 2 pairs
            case (0, _, 2, _, _, _):
                print(f"{theHand} is a 2 pairs")
                return 6  # Two pairs
            # 1 pair
            case (1, 4, _, _, _, _):
                print(f"{theHand} is a One pair")
                return 5  # aJbcd One pair
            case (0, 3, 1, _, _, _):
                print(f"{theHand} is a One pair")
                return 5  # One pair
            # high card
            case (0, 5, _, _, _, _):
                print(f"{theHand} is a High Card")
                return 4  # High card
            case _:
                print(f'This should never happen. The hand:\n{theHand}\n')
                return 0  # default value for invalid hand

    def make_cards_integers(self, theHand: str) -> Generator[int, None, None]:
        return (self.CardValues[eaCard] for eaCard in theHand)

    def process_data(self) -> None:
        for eaLine in self.InputData:
            myHand, myBid = eaLine.split(' ')
            myEncodedHand = (
                self.get_hand_type(myHand),
                *self.make_cards_integers(myHand),
                int(myBid)
            )
            self.Hands.append((myHand, myEncodedHand))
        # Sort hands by custom key
        self.Hands.sort(key=self.sort_hand, reverse=False)

    def sort_hand(self, theHandData: Tuple[str, Tuple[int, ...]]) -> Tuple[int, List[int]]:
        myOriginalHand, myEncodedHand = theHandData
        myHandType = myEncodedHand[0]
        myCardValues = [self.CardValues[card] for card in myOriginalHand]
        return tuple((myHandType, myCardValues))

    # Modify the calculate_winnings method to remove sorting by bid
    def calculate_winnings(self) -> int:
        myRanks = list(range(1, len(self.Hands) + 1))
        myTotalWinnings = 0  # Use a different variable to store the total winnings
        myHandTypes = ['High card', 'One pair', 'Two pairs', 'Three of a kind', 'Full house', 'Four of a kind', 'Five of a kind']

        for eaRank, (myOriginalHand, myEncodedHand) in zip(myRanks, self.Hands):
            myHandType = myHandTypes[myEncodedHand[0] - 4]
            myBid = myEncodedHand[-1]
            myWinnings = eaRank * myBid
            print(f"Rank:{eaRank} Hand: {myOriginalHand} is {myHandType}, Bid: {myBid}, Winnings: {eaRank}*{myBid}={myWinnings}")
            myTotalWinnings += myWinnings  # Accumulate winnings

        return myTotalWinnings


# Puzzle Two
myPuzzle2 = PuzzleTwo()
myPuzzle2.process_data()
myPuzzleTwoAnswer = myPuzzle2.calculate_winnings()
print(myPuzzleTwoAnswer)
