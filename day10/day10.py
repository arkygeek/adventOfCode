import glob
import os
import requests  # this is needed to grab the puzzle text from the website
import time

from collections import deque
from typing import List
from PyQt5.QtGui import (
        QFont,
        QTextCharFormat,
        QTextCursor,
        QColor
)
from PyQt5.QtWidgets import (
        QApplication,
        QCheckBox,
        QDialog,
        QLabel,
        QMainWindow,
        QComboBox,
        QPushButton,
        QTextEdit,
        QVBoxLayout,
        QWidget,
)

class PuzzleOne:

    def __init__(self, theData: str, theOutputTextWidget: QTextEdit):
        self.sData = theData
        self.sOutputText = theOutputTextWidget
        self.sPipeMap = {
            '|': ['N', 'S'],
            '-': ['E', 'W'],
            'L': ['N', 'E'],
            'J': ['N', 'W'],
            '7': ['S', 'W'],
            'F': ['S', 'E'],
            'S': ['N', 'S', 'E', 'W']  # Assuming 'S' can connect in any direction
        }

    def find_start(self):
        for eaRow, eaLine in enumerate(self.sData): # remember that the enumerate object
            # yields pairs containing a count (from start, which defaults to 0) and a value
            # yielded by the iterable argument.
            # Enumerate is useful for obtaining an indexed list:
            #     (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
            for evCol, evChar in enumerate(eaLine):
                if evChar == 'S':
                    return (eaRow, evCol, self.sPipeMap[evChar])
        return None

    def process_data(self, theDebugFlag: bool = False) -> None:
        self.sData = [list(eaLine) for eaLine in self.sData.split('\n') if eaLine.strip()]
        if theDebugFlag:
            for eaLine in self.sData:
                self.sOutputText.setFont(QFont("Courier", 10))
                self.sOutputText.append(str(eaLine))

    def breadth_first_search(self, myRow, myCol, theDebugFlag: bool = False):
        # BFS explores all the neighbors at the present depth before moving on to nodes at
        # the next depth level. This approach can be more suitable for this problem as it
        # naturally handles cases where the shortest path to a node isn't the first one found.

        # Initialize the queue with the start position and distance
        myQueue = deque([(myRow, myCol, 0)])
        """ myQueue = deque([(myRow, myCol, 0)])

        This line is initializing a double-ended queue (deque) with a tuple containing
        the starting row (myRow), the starting column (myCol), and the initial distance (0).

        A deque (pronounced "deck") is a thread-safe double-ended queue that allows
        us to append and pop elements from both ends efficiently (O(1) complexity).

        In the context of this code, the deque is used to implement a breadth-first
        search (BFS) algorithm. The tuples in the queue represent cells in a grid,
        where myRow and myCol are the coordinates of the cell and the third element
        of the tuple is the distance from the start cell.

        The BFS algorithm starts by visiting an initial cell (in this case, the
        cell at (myRow, myCol)) and then iteratively visits all the unvisited
        neighbors of the already visited cells. The deque is used to keep track
        of which cells to visit next.
        """

        # Initialize visited as a set
        myVisitedNodes = set()
        myMaxSteps = 0

        while myQueue:
            myRow, myCol, mySteps = myQueue.popleft()
            # Get the character at the current cell
            char = self.sData[myRow][myCol]
            # If the cell has been visited, skip
            if (myRow, myCol) in myVisitedNodes:
                continue
            # Mark the cell as visited
            myVisitedNodes.add((myRow, myCol))
            # Update the maximum distance
            myMaxSteps = max(myMaxSteps, mySteps)
            # Get the directions that the character can connect to
            myDirections = self.sPipeMap[char]
            for eaDirection in myDirections:
                myNewRow, myNewCol = myRow, myCol
                if eaDirection == 'N':
                    myNewRow -= 1
                elif eaDirection == 'S':
                    myNewRow += 1
                elif eaDirection == 'E':
                    myNewCol += 1
                elif eaDirection == 'W':
                    myNewCol -= 1
                # Only move in the direction if the new cell's character allows it
                if 0 <= myNewRow < len(self.sData) and 0 <= myNewCol < len(self.sData[0]):
                    myNewChar = self.sData[myNewRow][myNewCol]
                    myOppositeDirection = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}[eaDirection]
                    if myNewChar != '.' and myOppositeDirection in self.sPipeMap[myNewChar]:
                        myQueue.append((myNewRow, myNewCol, mySteps + 1))
                        if theDebugFlag:
                            self.sOutputText.setFont(QFont("Courier", 10))
                            self.sOutputText.append(f"Moving from ({myRow}, {myCol}) with symbol '{char}'")
                            self.sOutputText.append(f"To ({myNewRow}, {myNewCol}) with symbol '{myNewChar}'")
                            self.sOutputText.append(f"Because '{char}' can connect to '{myNewChar}' in the '{eaDirection}' direction")
                            self.sOutputText.append("")

        return myMaxSteps

    def calculate_answer(self, theDebugFlag: bool = False) -> int:
        myStart = self.find_start()
        if myStart is not None:
            myRow, myCol, _ = myStart
            myFurthestDistance = self.breadth_first_search(myRow, myCol, theDebugFlag)
            return myFurthestDistance
        else:
            # Handle the case where 'S' is not found in the data
            return -1


class PuzzleTwo:
    def __init__(self, theData: str, theOutputTextWidget: QTextEdit):
        self.sData = theData
        self.sOutputText = theOutputTextWidget

    def process_data(self, theDebugFlag: bool = False) -> None:
        self.sData = [list(eaLine) for eaLine in self.sData.split('\n') if eaLine.strip()]
        if theDebugFlag:
            for line in self.sData:
                self.sOutputText.setFont(QFont("Courier", 10))
                self.sOutputText.append(str(line))

    def calculate_answer(self, theDebugFlag: bool = False) -> int:
        myTotal = 0
        return myTotal


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window's size to be twice as wide
        self.resize(self.width() * 2, self.height())

        # definition
        self.sFileLabel = QLabel("Select file:")
        self.sFileCombo = QComboBox()
        self.sFileCombo.setFixedWidth(200)
        # populate sFileCombo with all .txt files in the day10 folder
        myCurrentWorkingDir = os.getcwd()
        # get a list of all the .txt files in the day10 directory
        myTextFiles = glob.glob(os.path.join(myCurrentWorkingDir, 'day10', '*.txt'))
        # show the filename only, retain the the full path
        for file in myTextFiles:
            self.sFileCombo.addItem(os.path.basename(file), file)

        self.sShowPuzzleButton = QPushButton("Show Puzzle")
        self.sShowPuzzleButton.clicked.connect(self.show_puzzle)
        self.sShowDataButton = QPushButton("Show Data")
        self.sShowDataButton.clicked.connect(self.show_data)
        self.sSolvePuzzle1Button = QPushButton("Solve Part 1")
        self.sSolvePuzzle1Button.clicked.connect(self.solve1)
        self.sSolvePuzzle2Button = QPushButton("Solve Part 2")
        self.sSolvePuzzle2Button.clicked.connect(self.solve2)
        self.sSolutionLabel = QLabel()
        self.sSolutionLabel.setStyleSheet("font-size: 18px; color: darkblue;")
        self.sOutputText = QTextEdit()
        self.sDebugCheckbox = QCheckBox("Debug", self)
        self.sClearButton = QPushButton("Clear Output")
        self.sClearButton.clicked.connect(self.clear_output)

        # Set a fixed width for the buttons
        myButtonWidth = 100
        self.sShowPuzzleButton.setFixedWidth(myButtonWidth)
        self.sShowDataButton.setFixedWidth(myButtonWidth)
        self.sSolvePuzzle1Button.setFixedWidth(myButtonWidth)
        self.sSolvePuzzle2Button.setFixedWidth(myButtonWidth)
        self.sClearButton.setFixedWidth(myButtonWidth)

        # Create a vertical box layout
        myLayout = QVBoxLayout()

        # Add widgets to the layout
        myLayout.addWidget(self.sFileLabel)  # Label for file selection
        myLayout.addWidget(self.sFileCombo)  # Dropdown for file selection
        myLayout.addWidget(self.sShowPuzzleButton)  # Button to get and show the puzzle
        myLayout.addWidget(self.sShowDataButton)  # Button to show the data
        myLayout.addWidget(self.sSolvePuzzle1Button)  # Button for part 1 of the puzzle
        myLayout.addWidget(self.sSolvePuzzle2Button)  # Button for part 2 of the puzzle
        myLayout.addWidget(self.sSolutionLabel)  # Label to display the solution
        myLayout.addWidget(self.sOutputText)  # Text edit for output
        myLayout.addWidget(self.sDebugCheckbox)  # Checkbox to enable/disable debug mode
        myLayout.addWidget(self.sClearButton)  # Button to clear the output

        # Create a widget to hold the layout
        myWidget = QWidget()
        myWidget.setLayout(myLayout)

        # Set the widget as the central widget of the main window
        self.setCentralWidget(myWidget)

    def show_data(self):
        myFilename = self.sFileCombo.currentData()  # Get the full path of the selected file
        with open(myFilename) as myRawFile:
            myData = myRawFile.read()

        self.sOutputText.setFont(QFont("Courier", 10))

        if self.sDebugCheckbox.isChecked():
            # Create a new QTextCharFormat and set its color
            myRedFormat = QTextCharFormat()
            myRedFormat.setForeground(QColor("red"))

            # Create a default QTextCharFormat
            myDefaultFormat = QTextCharFormat()

            # Create a QTextCursor on the QTextEdit's document
            myCursor = QTextCursor(self.sOutputText.document())

            # Insert the text character by character
            for eaChar in myData:
                if eaChar == 'S':
                    # If the character is 'S', use the red format
                    myCursor.insertText(eaChar, myRedFormat)
                else:
                    # Otherwise, insert the text normally
                    myCursor.insertText(eaChar, myDefaultFormat)
        else:
            self.sOutputText.setText(myData)
        self.sOutputText.update()

    def show_puzzle(self):
        myUrl = "https://adventofcode.com/2023/day/10"
        myResponse = requests.get(myUrl)
        myResponse.raise_for_status()  # Raise an exception if the request fails

        # Extract the puzzle text
        myStartMarker = "--- Day 10:"
        myEndMarker = "To play, please identify yourself via one of these services:"
        puzzle_text = myResponse.text.partition(myStartMarker)[2].partition(myEndMarker)[0]

        # Create a dialog box with a QTextEdit inside it
        myDialog = QDialog(self)
        myDialog.setWindowTitle("Puzzle Text")
        myDialog.resize(600, 400)  # Adjust size

        myTextEdit = QTextEdit()
        myTextEdit.setReadOnly(True)
        myTextEdit.setHtml(puzzle_text)

        myLayout = QVBoxLayout()
        myLayout.addWidget(myTextEdit)
        myDialog.setLayout(myLayout)

        myDialog.exec_()

    def clear_output(self):
        self.sOutputText.clear()

    def solve1(self):
        # Record the start time
        myStartTime = time.time()

        myFilename = self.sFileCombo.currentData()  # Get the full path of the selected file
        with open(myFilename) as myRawFile:
            myData = myRawFile.read()
        myPuzzle1 = PuzzleOne(myData, self.sOutputText)  # Pass the output text widget to PuzzleOne
        myDebugQCheckBoxStatus = self.sDebugCheckbox.isChecked()
        myPuzzle1.process_data(myDebugQCheckBoxStatus)
        mySolution1 = myPuzzle1.calculate_answer(myDebugQCheckBoxStatus)
        self.sSolutionLabel.setText(f"Solution Part 1: {mySolution1}")
        self.sOutputText.append(f"Solution Part 1: {mySolution1}")

        # Record the end time
        myEndTime = time.time()
        # Calculate and print the execution time
        myExecutionTime = myEndTime - myStartTime
        self.sOutputText.append(f"Execution time: {myExecutionTime} seconds")

    def solve2(self):
        # Record the start time to measure code speed
        myStartTime = time.time()
        myFilename = self.sFileCombo.currentData()  # Get the full path of the selected file
        with open(myFilename) as myRawFile:
            myData = myRawFile.read()
        myPuzzle2 = PuzzleTwo(myData, self.sOutputText)  # Pass the output text widget to PuzzleTwo
        myDebugQCheckBoxStatus = self.sDebugCheckbox.isChecked()
        myPuzzle2.process_data(myDebugQCheckBoxStatus)
        mySolution2 = myPuzzle2.calculate_answer(myDebugQCheckBoxStatus)
        self.sSolutionLabel.setText(f"Solution Part 2: {mySolution2}")
        self.sOutputText.append(f"Solution Part 2: {mySolution2}")
        # Record the end time
        myEndTime = time.time()

        # Calculate and print the execution time
        myExecutionTime = myEndTime - myStartTime
        self.sOutputText.append(f"Execution time: {myExecutionTime} seconds")


ourApp = QApplication([])
ourWindow = MainWindow()
ourWindow.show()
ourApp.exec_()
