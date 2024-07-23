import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
from backend import Chatbot
import threading


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.chatbot = Chatbot()

        # Set the window properties
        self.setWindowTitle("Chatbot")
        self.setGeometry(100, 100, 800, 600)

        # Add chat area widgets
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # Add the input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)
        self.input_field.returnPressed.connect(self.send_message)


        # Add the send button widget
        self.send_button = QPushButton("Send", self)
        self.send_button.setGeometry(500, 340, 100, 40)
        self.send_button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        self.input_field.clear()
        self.chat_area.append(f"<p style='color:#FFFF00'>User: {user_input}</p>")

        thread = threading.Thread(target=self.get_chatbot_response, args=(user_input,))
        thread.start()

    def get_chatbot_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"<p style='color:#333333; background-color: #E9E9E9'>Chatbot: {response}</p>")


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())