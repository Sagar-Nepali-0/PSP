import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QCheckBox,
    QVBoxLayout, QHBoxLayout, QFormLayout, QMessageBox
)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Page")
        self.setGeometry(500, 200, 400, 300)
        self.setFixedSize(400, 300)
        self.init_ui()

    def init_ui(self):
        # Main title
        title = QLabel("🔐 Secure Login")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)

        # Username and Password
        username = QLabel("Username:")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username")

        password = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Enter your password")

        # Remember Me
        self.remember_me = QCheckBox("Remember Me")

        # Buttons
        login_button = QPushButton("Login")
        login_button.setStyleSheet("background-color: #4CAF50; color: white; padding: 6px;")
        cancel_button = QPushButton("Cancel")
        cancel_button.setStyleSheet("background-color: #f44336; color: white; padding: 6px;")

        login_button.clicked.connect(self.login)
        cancel_button.clicked.connect(self.close)

        # Form layout
        form_layout = QFormLayout()
        form_layout.addRow(username, self.username_input)
        form_layout.addRow(password, self.password_input)
        form_layout.addRow("", self.remember_me)

        # Button layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(login_button)
        button_layout.addWidget(cancel_button)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(title)
        main_layout.addSpacing(10)
        main_layout.addLayout(form_layout)
        main_layout.addSpacing(10)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def login(self):
        user = self.username_input.text()
        pwd = self.password_input.text()

        if user == "admin" and pwd == "admin":
            QMessageBox.information(self, "Login Success", f"Welcome, {user}!")
        else:
            QMessageBox.critical(self, "Login Failed", "Incorrect username or password.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginPage()
    window.show()
    sys.exit(app.exec_())
