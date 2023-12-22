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



ourSampleData: str = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

class PuzzleOne:
    def init(self):
         pass

    def process_data(self):
        pass


class PuzzleTwo:
    def init(self):
        pass


myPuzzle1 = PuzzleTwo()
myPuzzle1.process_data()
myPuzzleTwoAnswer = myPuzzle1.calculate_winnings()
print(myPuzzleTwoAnswer)