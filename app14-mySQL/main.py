from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, \
    QPushButton, \
    QTableWidget, QTableWidgetItem, QDialog, QComboBox, QToolBar, QStatusBar, QMessageBox
from PyQt6.QtGui import QAction, QIcon
import sys
import mysql.connector


class DatabaseConnection:
    def __init__(self, host="localhost", user="root", password="password", database="students"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        connection = mysql.connector.connect(
            host=self.host, user=self.user, 
            password=self.password, database=self.database)
        return connection


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")
        self.setGeometry(100, 100, 800, 600)

        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")
        edit_menu_item = self.menuBar().addMenu("&Edit")

        add_student = QAction(QIcon("icons/add.png"), "Add Student", self)
        add_student.triggered.connect(self.insert)
        file_menu_item.addAction(add_student)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)
        # The line below will make the About menu item display on Mac
        about_action.setMenuRole(QAction.MenuRole.NoRole)
        about_action.triggered.connect(self.about)

        search_action = QAction(QIcon("icons/search.png"), "Search", self)
        edit_menu_item.addAction(search_action)
        search_action.triggered.connect(self.search)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("ID", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

        # Add a toolbar
        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        # Add actions to the toolbar
        toolbar.addAction(add_student)
        toolbar.addAction(search_action)

        # Create status bar
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)

        # Detect a cell click
        self.table.cellClicked.connect(self.cell_clicked)

    def cell_clicked(self):
        edit_button = QPushButton("Edit Record")
        edit_button.clicked.connect(self.edit)

        delete_button = QPushButton("Delete Record")
        delete_button.clicked.connect(self.delete)

        children = self.findChildren(QPushButton)
        if children:
            for child in children:
                self.statusbar.removeWidget(child)

        # Add the button to the status bar
        self.statusBar().addWidget(edit_button)
        self.statusBar().addWidget(delete_button)

    def load_data(self):
        connection = DatabaseConnection().connect()
        # MYSQL requires a cursor to execute queries instead of sqlite3 which doesn't require a cursor to fetch data
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")
        result = cursor.fetchall()
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()

    def search(self):
        dialog = SearchDialog()
        dialog.exec()

    def edit(self):
        dialog = EditDialog()
        dialog.exec()

    def delete(self):
        dialog = DeleteDialog()
        dialog.exec()

    def about(self):
        dialog = AboutDialog()
        dialog.exec()


class AboutDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        self.setText("This is a simple student management system")


class EditDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edit Student Data")
        self.setFixedWidth(300)
        self.setFixedHeight(200)

        layout = QVBoxLayout()

        # Select the student name from the table
        index = main_window.table.currentRow()
        student_name = main_window.table.item(index, 1).text()

        # Get ID from selected row
        self.student_id = main_window.table.item(index, 0).text()

        # Add student name widget
        self.student_name = QLineEdit(student_name)
        self.student_name.setPlaceholderText("Student Name")
        layout.addWidget(self.student_name)

        # Add student course widget
        course_name = main_window.table.item(index, 2).text()
        self.student_course = QComboBox()
        courses = ["Biology", "Math", "Astronomy", "Physics", "Deshtak", "FC24"]
        self.student_course.addItems(courses)
        self.student_course.setCurrentText(course_name)
        layout.addWidget(self.student_course)

        # Add student mobile widget
        student_mobile = main_window.table.item(index, 3).text()
        self.student_mobile = QLineEdit(student_mobile)
        self.student_mobile.setPlaceholderText("Student Mobile")
        layout.addWidget(self.student_mobile)

        # Add a submit button
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.update_student)
        layout.addWidget(submit_button)
        self.setLayout(layout)

    def update_student(self):
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("UPDATE students SET name = %s, course = %s, mobile = %s WHERE id = %s", (
            self.student_name.text(),
            self.student_course.currentText(),
            self.student_mobile.text(),
            self.student_id
        ))
        connection.commit()
        cursor.close()
        connection.close()
        main_window.load_data()

        # Close the dialog
        self.close()


class DeleteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete Student Data")

        layout = QGridLayout()
        confirmation = QLabel("Are you sure you want to delete this record?")
        yes = QPushButton("Yes")
        no = QPushButton("No")

        layout.addWidget(confirmation, 0, 0, 1, 2)
        layout.addWidget(yes, 1, 0)
        layout.addWidget(no, 1, 1)
        self.setLayout(layout)

        yes.clicked.connect(self.delete_student)
        no.clicked.connect(self.close)


    def delete_student(self):
        # Get selected row index and student id
        index = main_window.table.currentRow()
        student_id = main_window.table.item(index, 0).text()

        # Connect to the database and delete the record
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))

        # Commit the transaction
        connection.commit()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Refresh the data in the table
        main_window.load_data()

        # Close the dialog
        self.close()

        confirmation_widget = QMessageBox()
        confirmation_widget.setWindowTitle("Success")
        confirmation_widget.setText("Record deleted successfully")

        confirmation_widget.exec()


class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Student Data")
        self.setFixedWidth(300)
        self.setFixedHeight(200)

        layout = QVBoxLayout()

        # Add student name widget
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Student Name")
        layout.addWidget(self.student_name)

        # Add student course widget
        self.student_course = QComboBox()
        courses = ["Biology", "Math", "Astronomy", "Physics", "Deshtak", "FC24"]
        self.student_course.addItems(courses)
        layout.addWidget(self.student_course)

        # Add student mobile widget
        self.student_mobile = QLineEdit()
        self.student_mobile.setPlaceholderText("Student Mobile")
        layout.addWidget(self.student_mobile)

        # Add a submit button
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.add_student)
        layout.addWidget(submit_button)
        self.setLayout(layout)

    def add_student(self):
        student_name = self.student_name.text()
        student_course = self.student_course.itemText(self.student_course.currentIndex())
        student_mobile = self.student_mobile.text()

        connection = DatabaseConnection().connect()

        # Cursor is only needed when you're inserting data, not for reading data
        cursor = connection.cursor()

        # Don't forget to use the table names you created in the database, then use the variables you created above

        cursor.execute("INSERT INTO students (name, course, mobile) VALUES (%s, %s, %s)",
                       (student_name, student_course, student_mobile))
        # Commit the transaction
        connection.commit()
        cursor.close()
        connection.close()

        # Clear the input fields
        self.student_name.setText("")
        self.student_mobile.setText("")
        self.student_course.setCurrentIndex(0)

        # Refresh the data in the table
        main_window.load_data()


class SearchDialog(QDialog):
    def __init__(self):
        super().__init__()
        # Set window title and size
        self.setWindowTitle("Search Student")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        # Create layout and input widget
        layout = QVBoxLayout()
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        # Create button
        button = QPushButton("Search")
        button.clicked.connect(self.search)
        layout.addWidget(button)

        self.setLayout(layout)

    def search(self):
        name = self.student_name.text()
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students WHERE name = %s", (name,))
        result = cursor.fetchall()
        row = list(result)
        print(row)

        # from PyQt6.QtCore import Qt

        items = main_window.table.findItems(name, Qt.MatchFlag.MatchFixedString)
        for item in items:
            print(item)
            main_window.table.item(item.row(), 1).setSelected(True)

        cursor.close()
        connection.close()


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
main_window.load_data()
sys.exit(app.exec())
