# ambitious approach with PyQt5

"""
Summary:
We need to analyze a series of numerical sequences (referred to as "histories")
and predict the next value in each sequence.

Each sequence represents a history of a single value. To predict the next value,
we need to create a new sequence from the differences between each pair of
consecutive values in the original sequence.

If the new sequence is not all zeroes, we repeat the process with the new sequence.

Once we have a sequence of ALL ZEROES, we can extrapolate the next value in the
original sequence by adding a zero to the end of the zero sequence and then
filling in placeholders from the bottom up.

The new value in each sequence is the result of increasing the value to its left
by the value below it.

The goal of the puzzle is to find the sum of the extrapolated values for all the
histories in your report.

(1) Import necessary PyQt5 modules.
(2) Create a class for the main window that inherits from QMainWindow.
(3) In the constructor of the main window class, set up the GUI:
    (a) Create a QLabel for the file selection.
    (b) Create a QComboBox for the file selection, add the options "sample9.txt" and "input9.txt".
    (c) Create a QPushButton for solving part one of the puzzle, connect its clicked signal to a slot method.
    (d) Create a QPushButton for solving part two of the puzzle, connect its clicked signal to a slot method.
    (e) Create a QLabel for displaying the solution.
    (f) Create a QTextEdit for displaying the logged output.
    (g) Arrange all the widgets using a layout.
(4) Implement the slot methods for solving parts one and two of the puzzle:
    (a) Read the selected file.
    (b) Create an instance of the PuzzleOne or PuzzleTwo class, pass the file data to it.
    (c) Call the process_data and calculate_answer methods.
    (d) Display the solution in the QLabel.
    (e) Display the logged output in the QTextEdit.
(5) Create a QApplication and an instance of the main window class and show the main window.

NOTES:
The code will need to be able to deal with negative values
There is a shortcut I think we can use that I noticed when looking at the output
example:
10  13  16  21  30  45  68
   3   3   5   9  15  23
     0   2   4   6   8
       2   2   2   2
         0   0   0

rewritten:
10  13  16  21  30  45  68
 3   3   5   9  15  23
 0   2   4   6   8
 2   2   2   2
 0   0   0

so for part one we don't need to go past the first check because we are only
worried about the one value! I bet that part 2 we need to add them all up haha









"""

import requests
from PyQt5.QtGui import QTextOption
from PyQt5.QtWidgets import (
    QApplication,
    QComboBox,
    QDialog,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class PuzzleOne:
    def __init__(self, theData):
        self.sData = theData

    def process_data(self):
        self.sData = [list(map(int, eaLine.split())) for eaLine in self.sData.split('\n') if eaLine.strip()]
        # print(f"self.sData = {self.sData}")

    def calculate_answer(self) -> int:
        myTotal = 0
        for eaHistory in self.sData:
            mySequences = [eaHistory]
            # Generate sequences until the last element is equal to the second-to-last element
            while mySequences[-1][1:] != mySequences[-1][:-1]:
                mySequences.append([j-i for i, j in zip(mySequences[-1][:-1], mySequences[-1][1:])])
            myExtrapolated = mySequences[-1][-1]
            # Extrapolate the missing elements in the sequence
            for eaSeq in reversed(mySequences[:-1]):
                myExtrapolated += eaSeq[-1]
            myTotal += myExtrapolated
        return myTotal

class PuzzleTwo:
    def __init__(self, theData):
        self.sData = theData

    def process_data(self):
        # TODO: Implement logic for processing the data
        pass

    def calculate_answer(self):
        # TODO: Implement logic for calculating the answer
        return 2

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # definition
        self.sFileLabel = QLabel("Select file:")
        self.sFileCombo = QComboBox()
        self.sFileCombo.addItems(["day9/sample9.txt", "day9/input9.txt"])
        self.sShowPuzzleButton = QPushButton("Show Puzzle")
        self.sShowPuzzleButton.clicked.connect(self.show_puzzle)
        self.sShowDataButton = QPushButton("Show Data")
        self.sShowDataButton.clicked.connect(self.show_data)
        self.sSolvePuzzle1Button = QPushButton("Solve Part 1")
        self.sSolvePuzzle1Button.clicked.connect(self.solve1)
        self.sSolvePuzzle2Button = QPushButton("Solve Part 2")
        self.sSolvePuzzle2Button.clicked.connect(self.solve2)
        self.sSolutionLabel = QLabel()
        self.sOutputText = QTextEdit()
        self.sClearButton = QPushButton("Clear Output")
        self.sClearButton.clicked.connect(self.clear_output)

        myLayout = QVBoxLayout()
        myLayout.addWidget(self.sFileLabel)
        myLayout.addWidget(self.sFileCombo)
        myLayout.addWidget(self.sShowPuzzleButton)
        myLayout.addWidget(self.sShowDataButton)
        myLayout.addWidget(self.sSolvePuzzle1Button)
        myLayout.addWidget(self.sSolvePuzzle2Button)
        myLayout.addWidget(self.sSolutionLabel)
        myLayout.addWidget(self.sOutputText)
        myLayout.addWidget(self.sClearButton)

        myWidget = QWidget()
        myWidget.setLayout(myLayout)
        self.setCentralWidget(myWidget)

    def show_data(self):
        myFilename = self.sFileCombo.currentText()
        with open(myFilename) as myRawFile:
            myData = myRawFile.read()
        self.sOutputText.setText(myData)

    def show_puzzle(self):
        myUrl = "https://adventofcode.com/2023/day/9"
        myResponse = requests.get(myUrl)
        myResponse.raise_for_status()  # Raise exception if the request fails

        # Extract the puzzle text
        myStartMarker = "--- Day 9: Mirage Maintenance ---"
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
        myFilename = self.sFileCombo.currentText()
        with open(myFilename) as myRawFile:
            myData = myRawFile.read()
        myPuzzle1 = PuzzleOne(myData)
        myPuzzle1.process_data()
        mySolution1 = myPuzzle1.calculate_answer()
        self.sSolutionLabel.setText(f"Solution Part 1: {mySolution1}")
        self.sOutputText.append(f"Solution Part 1: {mySolution1}")

    def solve2(self):
        myFilename = self.sFileCombo.currentText()
        with open(myFilename) as myRawFile:
            myData = myRawFile.read()
        myPuzzle2 = PuzzleTwo(myData)
        myPuzzle2.process_data()
        mySolution2 = myPuzzle2.calculate_answer()
        self.sSolutionLabel.setText(f"Solution Part 2: {mySolution2}")
        self.sOutputText.setText("Logged output for Part 2...")

ourApp = QApplication([])
ourWindow = MainWindow()
ourWindow.show()
ourApp.exec_()
