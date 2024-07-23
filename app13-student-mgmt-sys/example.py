import sys
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton


class AgeCalculator(QWidget):

    def __init__(self):
        # The super().__init__() line is calling the __init__() method of the parent class (QWidget) to initialize the widget.
        super().__init__()
        self.setWindowTitle("Age Calculator")
        grid = QGridLayout()
        grid1 = QVBoxLayout()

        # Create the widgets
        name_label = QLabel("Name: ")
        self.name_line_edit = QLineEdit()

        date_label = QLabel("Date of Birth: (mm/dd/yyyy)")
        self.date_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate Age")
        calculate_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel("")

        # Add the widgets to the layout
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(date_label, 1, 0)
        grid.addWidget(self.date_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2) 
        grid.addWidget(self.output_label, 3, 0, 1, 2) 

        # Set the layout
        self.setLayout(grid)
    
    def calculate_age(self):
        current_date = datetime.now()
        date_of_birth = self.date_line_edit.text()
        year_of_birth = datetime.strptime(date_of_birth, "%m/%d/%Y").date().year
        age = current_date.year - year_of_birth
         
        self.output_label.setText(f"{self.name_line_edit.text()} is {age}")


app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())

