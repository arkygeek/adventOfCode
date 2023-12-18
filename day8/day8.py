# Day 8

import itertools

# ourInputData = open('day8/input8.txt').read().splitlines()
ourInputData = open('day8/input8.txt').read().splitlines()


class PuzzleOne:
    def __init__(self):
        # define the object properties
        self.InputData = ourInputData
        print(f'Input Data: {self.InputData}')

    def process_data(self):
        # Split the instructions from the data
        self.instructions = self.InputData[0]
        data = [line.split(' = ') for line in self.InputData[1:] if line]
        self.data = [(item, tuple(values.strip('()').split(', '))) for item, values in data]


    def find_steps_to_ZZZ(self, instructions, data):
        # Create a dictionary from the data
        myDataDict = {item: (left, right) for item, (left, right) in data}

        # Initialize the current item and the number of steps
        myCurrentItem = list(myDataDict.keys())[0]
        mySteps = 0

        # Create an iterator that produces the instructions indefinitely
        instructions_cycle = itertools.cycle(instructions)

        # Iterate over the instructions
        while myCurrentItem != 'ZZZ':
            # Get the next instruction
            instruction = next(instructions_cycle)

            # Follow the instruction
            if instruction == 'L':
                myCurrentItem = myDataDict[myCurrentItem][0]
            else:  # instruction == 'R'
                myCurrentItem = myDataDict[myCurrentItem][1]

            # Increment the number of steps
            mySteps += 1

        # Return the number of steps
        return mySteps


    def calculate_answer(self):
        # calculate the answer
        pass



# Puzzle One
myPuzzle1 = PuzzleOne()
myPuzzle1.process_data()
print(myPuzzle1.find_steps_to_ZZZ(myPuzzle1.instructions, myPuzzle1.data))

