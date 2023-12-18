import itertools
import math
from itertools import cycle

ourInputData = open('day8/input8.txt').read().splitlines()
ourSampleData = open('day8/sample8a.txt').read().splitlines()
from typing import List, Dict, Tuple, Iterator

class PuzzleOne:
    """ Solution for Advent of Code - Day 8 part 1.
    Attributes:
        sInputData (List[str]): The input data for the puzzle.
        sInstructions (str): The instructions for the puzzle.
        sData (Dict[str, Tuple[str, str]]): The data dictionary.
    Methods:
        __init__(self, theInputData: List[str]) -> None: Initializes the PuzzleOne object.
        process_data(self) -> Dict[str, Tuple[str, str]]: Processes the input data and returns the data dictionary.
        calculate_answer(self) -> int: Calculates and returns the answer for the puzzle.
    """

    def __init__(self, theInputData: List[str]) -> None:
        self.sInputData: List[str] = theInputData
        self.process_data()

    def process_data(self) -> Dict[str, Tuple[str, str]]:
        """ Process the input data and store it in a dictionary.
        Returns:  A dictionary containing the processed data. """
        self.sInstructions: str = self.sInputData[0]
        myData: List[List[str]] = [eaLine.split(' = ') for eaLine in self.sInputData[1:] if eaLine]
        self.sData: Dict[str, Tuple[str, str]] = {eaItem: tuple(eaValue.strip('()').split(', ')) for eaItem, eaValue in myData}
        return self.sData

    def calculate_answer(self) -> int:
        """  Calculate the answer for the puzzle.
        Returns: The answer for the puzzle. """
        myStartingItem: str = 'AAA'
        mySteps: int = 0
        myStack: List[Tuple[str, int]] = [(myStartingItem, mySteps)]
        myInstructionCycle: Iterator[str] = itertools.cycle(self.sInstructions)
        while myStack:
            myCurrentItem, mySteps = myStack.pop()
            if myCurrentItem == 'ZZZ':
                return mySteps
            myNextInstruction: str = next(myInstructionCycle)
            if myNextInstruction == 'L':
                myNextItem: str = self.sData[myCurrentItem][0]
            else:  # instruction == 'R'
                myNextItem: str = self.sData[myCurrentItem][1]
            myStack.append((myNextItem, mySteps + 1))
        print('ZZZ is not reachable')
        return -1

class PuzzleTwo:
    """ Solution for Advent of Code - Day 8 part 2.
    Attributes:
        sInputData (List[str]): The input data for the puzzle.
        sInstructions (List[int]): The list of instructions.
        sData (Dict[str, Tuple[str, str]]): The data dictionary.
    Methods:
        __init__(self, theInputData: List[str]) -> None: Initializes the PuzzleTwo object.
        process_data(self) -> Dict[str, Tuple[str, str]]: Processes the input data and returns the data dictionary.
        calculate_answer(self) -> int: Calculates and returns the answer for the puzzle.
    """

    def __init__(self, theInputData: List[str]) -> None:
        """ Initializes the PuzzleTwo object.
        Args: theInputData (List[str]): The input data for the puzzle."""
        self.sInputData: List[str] = theInputData
        self.process_data()

    def process_data(self) -> Dict[str, Tuple[str, str]]:
        """ Processes the input data and returns the data dictionary.
        Returns:  Dict[str, Tuple[str, str]]: The data dictionary. """
        self.sInstructions: List[int] = [0 if eaDirIndex == 'L' else 1 for eaDirIndex in self.sInputData[0]]
        myData: List[List[str]] = [eaLine.split(' = ') for eaLine in self.sInputData[1:] if eaLine]
        self.sData: Dict[str, Tuple[str, str]] = {eaItem: tuple(eaValues.strip('()').split(', ')) for eaItem, eaValues in myData}
        return self.sData

    def calculate_answer(self) -> int:
        """ Calculates and returns the answer for the puzzle.
        Returns: int: The answer for the puzzle."""
        myStartingNodes: List[str] = [eaNode for eaNode in self.sData if eaNode[2] == 'A']
        myCycles: List[int] = []
        for eaNode in myStartingNodes:
            for eaStep, eaDirIndex in enumerate(cycle(self.sInstructions), start=1):
                eaNode = self.sData[eaNode][eaDirIndex]
                if eaNode[2] == 'Z':
                    myCycles.append(eaStep)
                    break
        return math.lcm(*myCycles)

# Puzzle 1
myPuzzleOne: PuzzleOne = PuzzleOne(ourInputData)
myPuzzleOne.process_data()
print(myPuzzleOne.calculate_answer())

# Puzzle 2
myPuzzleTwo: PuzzleTwo = PuzzleTwo(ourInputData)
myPuzzleTwo.process_data()
print(myPuzzleTwo.calculate_answer())
