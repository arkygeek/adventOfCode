from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QTextEdit, QPushButton, QLabel
import sys
import pickle

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create the layout
        layout = QVBoxLayout()

        # Create the dropdown menus
        self.day_dropdown = QComboBox()
        self.day_dropdown.addItems([str(i) for i in range(1, 26)])  # Days 1-25
        layout.addWidget(QLabel("Day:"))
        layout.addWidget(self.day_dropdown)

        self.puzzle_dropdown = QComboBox()
        self.puzzle_dropdown.addItems(['Puzzle 1', 'Puzzle 2'])  # The puzzles for each day
        layout.addWidget(QLabel("Puzzle:"))
        layout.addWidget(self.puzzle_dropdown)

        # Create the text fields
        self.puzzle_text = QTextEdit()
        layout.addWidget(QLabel("Puzzle Text:"))
        layout.addWidget(self.puzzle_text)

        self.input_data = QTextEdit()
        layout.addWidget(QLabel("Input Data:"))
        layout.addWidget(self.input_data)

        self.answer = QTextEdit()
        layout.addWidget(QLabel("Answer:"))
        layout.addWidget(self.answer)

        self.code = QTextEdit()
        layout.addWidget(QLabel("Code:"))
        layout.addWidget(self.code)

        # Create the buttons
        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_data)  # You need to implement the save_data method
        layout.addWidget(save_button)

        load_button = QPushButton("Load")
        load_button.clicked.connect(self.load_data)  # You need to implement the load_data method
        layout.addWidget(load_button)

        # Set the layout
        self.setLayout(layout)

    def save_data(self):
        # Get the current values from the GUI
        day = self.day_dropdown.currentText()
        puzzle = self.puzzle_dropdown.currentText()
        puzzle_text_data = self.puzzle_text.toPlainText()
        input_data_text = self.input_data.toPlainText()
        answer_text = self.answer.toPlainText()
        code_text = self.code.toPlainText()

        # Create a dictionary to store the data
        data = {
            'day': day,
            'puzzle': puzzle,
            'puzzle_text': puzzle_text_data,
            'input_data': input_data_text,
            'answer': answer_text,
            'code': code_text,
        }

        # Save the data to a file using pickle
        with open(f'day_{day}_puzzle_{puzzle}.pkl', 'wb') as file:
            pickle.dump(data, file)

    def load_data(self):
        pass  # Implement this method

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
