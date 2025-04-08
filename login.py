import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QCheckBox,
    QVBoxLayout, QHBoxLayout, QFormLayout, QMessageBox
)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
import pandas as pd
from admin.admin_panel import admin_panel

# Constants
ICON_PATH = "image/icon.png"
DATA_FILE_PATH = "data/passwords.csv"

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_window()
        self.init_ui()

    def setup_window(self):
        """Configure window properties."""
        self.setWindowTitle("Login Page")
        self.setGeometry(500, 200, 400, 300)
        self.setWindowIcon(QIcon(ICON_PATH))
        self.setFixedSize(400, 300)

    def init_ui(self):
        """Initialize the user interface."""
        # Title
        title = QLabel("🔐 Secure Login")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)

        # Form inputs
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username")

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Enter your password")

        # Remember Me
        self.remember_me = QCheckBox("Remember Me")

        # Buttons
        login_button = QPushButton("Login")
        login_button.setStyleSheet("background-color: #4CAF50; color: white; padding: 6px;")
        login_button.clicked.connect(self.handle_login)

        cancel_button = QPushButton("Cancel")
        cancel_button.setStyleSheet("background-color: #f44336; color: white; padding: 6px;")
        cancel_button.clicked.connect(self.close)

        # Layouts
        form_layout = QFormLayout()
        form_layout.addRow("Username:", self.username_input)
        form_layout.addRow("Password:", self.password_input)
        form_layout.addRow("", self.remember_me)

        button_layout = QHBoxLayout()
        button_layout.addWidget(login_button)
        button_layout.addWidget(cancel_button)

        main_layout = QVBoxLayout()
        main_layout.addWidget(title)
        main_layout.addLayout(form_layout)
        main_layout.addSpacing(10)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def handle_login(self):
        """Handle login logic."""
        username = self.username_input.text()
        password = self.password_input.text()

        # Validate inputs
        if not username or not password:
            QMessageBox.warning(self, "Input Error", "Both fields are required.")
            return

        try:
            # Read user data
            user_data = pd.read_csv(DATA_FILE_PATH, dtype={'ID': str})
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", "Password file not found.")
            return

        # Authenticate user
        user_row = user_data[
            ((user_data['Username'] == username) | (user_data['ID'] == username)) &
            (user_data['Password'] == password)
        ]

        if user_row.empty:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")
            return

        # Determine user role
        user_role = user_row.iloc[0]["Role"]

        if user_role == "Admin":
            QMessageBox.information(self, "Login Success", "Welcome, Admin!")
            self.close()
            admin_panel() 
            # just function soon GUI appear
        elif user_role == "Student":
            QMessageBox.information(self, "Login Success", "Welcome, Student!")
            print("STUDENT")  # Replace with appropriate student panel functionality
        else:
            QMessageBox.warning(self, "Login Failed", "User role not recognized.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_page = LoginPage()
    login_page.show()
    sys.exit(app.exec_())
