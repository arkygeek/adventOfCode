# ambitious approach with PyQt5

"""
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

"""
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QComboBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QTextEdit
)


class PuzzleOne:
    def __init__(self, theData):
        self.sData = theData

    def process_data(self):
        # TODO: Implement logic for processing the data
        pass

    def calculate_answer(self):
        # TODO: Implement logic for calculating the answer
        return 1


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

        self.sFileLabel = QLabel("Select file:")
        self.sFileCombo = QComboBox()
        self.sFileCombo.addItems(["day9/sample9.txt", "day9/input9.txt"])
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
        self.sOutputText.setText("Logged output for Part 1...")

    def solve2(self):
        myFilename = self.sFileCombo.currentText()
        with open(myFilename) as myRawFile:
            myData = myRawFile.read()
        myPuzzle2 = PuzzleTwo(myData)
        myPuzzle2.process_data()
        mySolution2 = myPuzzle2.calculate_answer()
        self.sSolutionLabel.setText(f"Solution Part 2: {mySolution2}")
        self.sOutputText.setText("Logged output for Part 2...")

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()



myPuzzle1 = PuzzleTwo()
myPuzzle1.process_data()
myPuzzleTwoAnswer = myPuzzle1.calculate_answer()
print(myPuzzleTwoAnswer)