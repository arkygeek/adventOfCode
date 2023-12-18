import itertools

ourInputData = open('day8/input8.txt').read().splitlines()

import itertools

class PuzzleOne:
    def __init__(self, theInputData):
        self.sInputData = theInputData
        self.process_data()

    # Get the data into a form we can use
    def process_data(self):
        # Split the instructions from the data
        self.sInstructions = self.sInputData[0]
        myData = [eaLine.split(' = ') for eaLine in self.sInputData[1:] if eaLine]
            # self.InputData[1:]
            # This slices the list starting from the second element (index 1),
            # skipping the first element (index 0)
        self.sData = {eaItem: tuple(eaValue.strip('()').split(', ')) for eaItem, eaValue in myData}
        return self.sData

    def calculate_answer(self):
        # Initialize the current item, the number of steps, and a stack for DFS
        myStartingItem = 'AAA'
        mySteps = 0
        myStack = [(myStartingItem, mySteps)]

        # Create an iterator that produces the instructions indefinitely
        myInstructionCycle = itertools.cycle(self.sInstructions)

        while myStack:
            myCurrentItem, mySteps = myStack.pop()

            # If we've reached 'ZZZ', return the number of steps
            if myCurrentItem == 'ZZZ':
                return mySteps

            # Get the next instruction
            myNextInstruction = next(myInstructionCycle)

            # Follow the instruction and push the next item to the stack
            if myNextInstruction == 'L':
                myNextItem = self.sData[myCurrentItem][0]
            else:  # instruction == 'R'
                myNextItem = self.sData[myCurrentItem][1]

            myStack.append((myNextItem, mySteps + 1))

        # If 'ZZZ' is not reachable, return -1
        print('ZZZ is not reachable')
        return -1

# build in test cases
# myPuzzle1_dfs1 = PuzzleOne(['LLR', '', 'AAA = (BBB, BBB)', 'BBB = (AAA, ZZZ)', 'ZZZ = (ZZZ, ZZZ)'])
# print(myPuzzle1_dfs1.calculate_answer())  # Expected Output: 6

myPuzzle1_dfs = PuzzleOne(ourInputData)
myPuzzle1_dfs.process_data()

# Call calculate_answer
print(myPuzzle1_dfs.calculate_answer())
