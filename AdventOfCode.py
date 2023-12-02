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













"""
import tkinter as tk
from tkinter import ttk

import pickle

def load_data():
    # Get the current values from the dropdown menus
    day = day_var.get()
    puzzle = puzzle_var.get()

    # Load the data from the file using pickle
    with open(f'day_{day}_puzzle_{puzzle}.pkl', 'rb') as file:
        data = pickle.load(file)

    # Set the values in the GUI
    puzzle_text.delete("1.0", tk.END)
    puzzle_text.insert("1.0", data['puzzle_text'])

    input_data.delete("1.0", tk.END)
    input_data.insert("1.0", data['input_data'])

    answer.delete("1.0", tk.END)
    answer.insert("1.0", data['answer'])

    code.delete("1.0", tk.END)
    code.insert("1.0", data['code'])

def save_data():
    # Get the current values from the GUI
    day = day_var.get()
    puzzle = puzzle_var.get()
    puzzle_text_data = puzzle_text.get("1.0", tk.END)
    input_data_text = input_data.get("1.0", tk.END)
    answer_text = answer.get("1.0", tk.END)
    code_text = code.get("1.0", tk.END)

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




# Create the main window
root = tk.Tk()

# Create the dropdown menus
day_var = tk.StringVar()
day_dropdown = ttk.Combobox(root, textvariable=day_var)
day_dropdown['values'] = list(range(1, 26))  # Days 1-25
day_dropdown.grid(column=0, row=0)

puzzle_var = tk.StringVar()
puzzle_dropdown = ttk.Combobox(root, textvariable=puzzle_var)
puzzle_dropdown['values'] = ['Puzzle 1', 'Puzzle 2']  # The puzzles for each day
puzzle_dropdown.grid(column=1, row=0)

# Create labels for the text fields
puzzle_text_label = tk.Label(root, text="Puzzle Text:")
puzzle_text_label.grid(column=0, row=1, sticky='W')

input_data_label = tk.Label(root, text="Input Data:")
input_data_label.grid(column=0, row=2, sticky='W')

answer_label = tk.Label(root, text="Answer:")
answer_label.grid(column=0, row=3, sticky='W')

code_label = tk.Label(root, text="Code:")
code_label.grid(column=0, row=4, sticky='W')

# Create the text fields
puzzle_text = tk.Text(root)
puzzle_text.grid(column=0, row=1, columnspan=2)

input_data = tk.Text(root)
input_data.grid(column=0, row=2, columnspan=2)

answer = tk.Text(root)
answer.grid(column=0, row=3, columnspan=2)

code = tk.Text(root)
code.grid(column=0, row=4, columnspan=2)

# Create the buttons
save_button = tk.Button(root, text="Save", command=save_data)  # You need to implement the save_data function
save_button.grid(column=0, row=5)

load_button = tk.Button(root, text="Load", command=load_data)  # You need to implement the load_data function
load_button.grid(column=1, row=5)

# Start the main loop
root.mainloop()

"""