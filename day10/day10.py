import requests  # this is needed to grab the puzzle text from the website
import time
from typing import List
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

    def process_data(self, theDebugFlag: bool = False) -> None:
        self.sData = [list(map(int, eaLine.split())) for eaLine in self.sData.split('\n') if eaLine.strip()]
        if theDebugFlag:
                self.sOutputText.append(f"self.sData = {self.sData}")

    def calculate_answer(self, theDebugFlag: bool = False) -> int:
        myTotal = 0
        return myTotal


class PuzzleTwo:
    def __init__(self, theData: str, theOutputTextWidget: QTextEdit):
        self.sData = theData
        self.sOutputText = theOutputTextWidget

    def process_data(self, theDebugFlag: bool = False) -> None:
        self.sData = [list(map(int, eaLine.split())) for eaLine in self.sData.split('\n') if eaLine.strip()]
        if theDebugFlag:
            self.sOutputText.append(f"self.sData = {self.sData}")

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
        self.sFileCombo.addItems(["day10/sample10.txt", "day10/input10.txt"])
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
        myFilename = self.sFileCombo.currentText()
        with open(myFilename) as myRawFile:
            myData = myRawFile.read()
        self.sOutputText.setText(myData)

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

        myFilename = self.sFileCombo.currentText()
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
        myFilename = self.sFileCombo.currentText()
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
