import sys
import pandas as pd
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QCheckBox,
    QVBoxLayout, QHBoxLayout, QFormLayout, QMessageBox
)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
from studentGUI import EditStudentWindow
import csv
# Constants
ICON_PATH = "image/icon.png"
DATA_FILE_PATH = "data/student.csv"
GRADE_FILE_PATH = "data/grades.csv"
ECA_PATH = "data/eca.csv"


class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_window()
        self.init_ui()

    def setup_window(self):
        self.setWindowTitle("Login Page")
        self.setGeometry(500, 200, 400, 300)
        self.setWindowIcon(QIcon(ICON_PATH))
        self.setFixedSize(400, 300)

    def init_ui(self):
        title = QLabel("🔐 Secure Login")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username")

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Enter your password")

        self.remember_me = QCheckBox("Remember Me")

        login_button = QPushButton("Login")
        login_button.setStyleSheet("background-color: #4CAF50; color: white;")
        login_button.clicked.connect(self.handle_login)

        cancel_button = QPushButton("Cancel")
        cancel_button.setStyleSheet("background-color: #f44336; color: white;")
        cancel_button.clicked.connect(self.close)

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
        username = self.username_input.text()
        password = self.password_input.text()

        if not username or not password:
            QMessageBox.warning(self, "Input Error", "Both fields are required.")
            return

        try:
            user_data = pd.read_csv(DATA_FILE_PATH, dtype={'ID': str})
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", "Password file not found.")
            return

        user_row = user_data[
            (user_data['Username'] == username) & (user_data['Password'] == password)
        ]

        if user_row.empty:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")
            return

        user_role = user_row.iloc[0]["Role"]
        if user_role == "Student":
            QMessageBox.information(self, "Login Success", "Welcome, Student!")
            self.dashboard = StudentProfile(username, password)
            self.dashboard.show()
        else:
            QMessageBox.warning(self, "Login Failed", "User role not recognized.")


class StudentProfile(QWidget):
    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password
        self.df = pd.read_csv(DATA_FILE_PATH)
        self.df_grade = pd.read_csv(GRADE_FILE_PATH)

        self.setWindowTitle("Student Profile")
        self.setGeometry(0, 0, 600, 1000)
        self.create_ui()
        self.load_personal_info()
        self.load_academic_record()
        self.load_eca_record()

    def create_ui(self):
        self.main_layout = QVBoxLayout()

        title_layout = QHBoxLayout()
        title = QLabel("Student Profile")
        title.setStyleSheet("font-size: 40px;")
        self.edit_button = QPushButton("Edit")
        self.edit_button.clicked.connect(self.toggle_edit_mode)

        title_layout.addWidget(title)
        title_layout.addStretch()
        title_layout.addWidget(self.edit_button)

        self.main_layout.addLayout(title_layout)

        profile_pic = QLabel()
        profile_pic.setFixedSize(100, 100)
        profile_pic.setStyleSheet("background-color: gray; border-radius: 50px;")
        profile_pic.setAlignment(Qt.AlignCenter)

        self.name_label = QLabel(self.username)
        self.name_label.setAlignment(Qt.AlignCenter)

        self.main_layout.addWidget(profile_pic)
        self.main_layout.addWidget(self.name_label)

    def load_personal_info(self):
        self.name_edit = QLineEdit()
        self.dob_edit = QLineEdit()
        self.address_edit = QLineEdit()
        self.contact_edit = QLineEdit()
        self.class_edit = QLineEdit()
        self.section_edit = QLineEdit()

        user_row = self.df[
            (self.df["Username"] == self.username) & (self.df["Password"] == self.password)
        ]

        if not user_row.empty:
            data = user_row.iloc[0]
            self.name_edit.setText(str(data.get("Name", "")))
            self.dob_edit.setText(str(data.get("DOB", "")))
            self.address_edit.setText(str(data.get("Address", "")))
            self.contact_edit.setText(str(data.get("Contact", "")))
            self.class_edit.setText(str(data.get("Class", "")))
            self.section_edit.setText(str(data.get("Section", "")))
        else:
            QMessageBox.warning(self, "Error", "User data not found.")

        self.main_layout.addWidget(QLabel("Personal Information:"))
        for label, widget in {
            "Name": self.name_edit, "DOB": self.dob_edit,
            "Address": self.address_edit, "Contact": self.contact_edit,
            "Class": self.class_edit, "Section": self.section_edit
        }.items():
            self.main_layout.addLayout(self._form_row(label, widget))

    def load_academic_record(self):
        self.main_layout.addWidget(QLabel("Academic Grade:"))
        user_row = self.df_grade[self.df_grade['Username'] == self.username]

        if user_row.empty:
            return

        self.grade_edits = {}
        subjects = ["Math", "Science", "Computer", "Social", "Nepali"]

        for subject in subjects:
            grade = user_row[subject].iloc[0]
            grade_input = QLineEdit(str(grade))
            grade_input.setReadOnly(True)
            self.grade_edits[subject] = grade_input
            self.main_layout.addLayout(self._form_row(subject, grade_input))

    def load_eca_record(self):
        self.main_layout.addWidget(QLabel("Extracurricular Activities (ECA):"))

        self.music_cb = QCheckBox("Music")
        self.dance_cb = QCheckBox("Dance")
        self.football_cb = QCheckBox("Football")
        self.basketball_cb = QCheckBox("Basketball")
        self.coding_cb = QCheckBox("Coding Club")

        # Add the checkboxes to the layout
        for section, widgets in {
            "Arts & Culture": [self.music_cb, self.dance_cb],
            "Sports": [self.football_cb, self.basketball_cb],
            "Academic & Intellectual": [self.coding_cb],
        }.items():
            self.main_layout.addWidget(QLabel(section))
            for w in widgets:
                self.main_layout.addWidget(w)

        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.save_eca_record)
        self.main_layout.addWidget(submit_button)

        # Pre-select checkboxes based on saved ECA data
        self.load_eca_data()

        self.setLayout(self.main_layout)

    def load_eca_data(self):
        try:
            eca_df = pd.read_csv(ECA_PATH)

            # Find the row for the logged-in user
            user_eca = eca_df[eca_df['Username'] == self.name_edit.text()]

            if not user_eca.empty:
                # Check each activity column and set the corresponding checkbox
                self.music_cb.setChecked(user_eca.iloc[0]['Music'] == 'Yes')
                self.dance_cb.setChecked(user_eca.iloc[0]['Dance'] == 'Yes')
                self.football_cb.setChecked(user_eca.iloc[0]['Football'] == 'Yes')
                self.basketball_cb.setChecked(user_eca.iloc[0]['Basketball'] == 'Yes')
                self.coding_cb.setChecked(user_eca.iloc[0]['Coding Club'] == 'Yes')
        except Exception as e:
            print(f"Error loading ECA data: {e}")

    def save_eca_record(self):
        selected_activities = {
            "Music": self.music_cb.isChecked(),
            "Dance": self.dance_cb.isChecked(),
            "Football": self.football_cb.isChecked(),
            "Basketball": self.basketball_cb.isChecked(),
            "Coding Club": self.coding_cb.isChecked()
        }

        # Convert checked activities to 'Yes' and unchecked to 'No'
        eca_data = {'Username': self.name_edit.text()}
        for activity, checked in selected_activities.items():
            eca_data[activity] = 'Yes' if checked else 'No'

        try:
            eca_df = pd.read_csv(ECA_PATH)

            # Check if the student already exists in the CSV, and update or append accordingly
            if self.name_edit.text() in eca_df['Username'].values:
                eca_df.loc[eca_df['Username'] == self.name_edit.text(), selected_activities.keys()] = list(eca_data.values())[1:]
            else:
                # Using concat() to append the new data
                new_row = pd.DataFrame([eca_data])
                eca_df = pd.concat([eca_df, new_row], ignore_index=True)

            # Save the updated DataFrame to the CSV
            eca_df.to_csv(ECA_PATH, index=False)

            QMessageBox.information(self, "Success", "Extracurricular activities saved successfully.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save activities: {e}")

    def toggle_edit_mode(self):
        user_data = {
            "Name": self.name_edit.text(),
            "DOB": self.dob_edit.text(),
            "Address": self.address_edit.text(),
            "Contact": self.contact_edit.text(),
            "Class": self.class_edit.text(),
            "Section": self.section_edit.text(),
        }
        self.editor_window = EditStudentWindow(user_data)
        self.editor_window.data_updated.connect(self.update_profile_data)
        self.editor_window.show()

    def update_profile_data(self, updated_data):
        for field, widget in {
            "Name": self.name_edit,
            "DOB": self.dob_edit,
            "Address": self.address_edit,
            "Contact": self.contact_edit,
            "Class": self.class_edit,
            "Section": self.section_edit,
        }.items():
            widget.setText(updated_data[field])

        self.name_label.setText(updated_data["Name"])

        try:
            df = pd.read_csv(DATA_FILE_PATH, dtype=str)
            user_index = df[
                (df["Username"] == self.username) & (df["Password"] == self.password)
            ].index

            if not user_index.empty:
                idx = user_index[0]
                for field in updated_data:
                    df.at[idx, field] = updated_data[field]

                df.to_csv(DATA_FILE_PATH, index=False)
                self.df = df
                QMessageBox.information(self, "Updated", "Profile updated successfully.")
            else:
                QMessageBox.warning(self, "Error", "User not found in data file.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to update CSV: {e}")

    def _form_row(self, label, widget):
        layout = QHBoxLayout()
        layout.addWidget(QLabel(label + ":"))
        layout.addWidget(widget)
        return layout


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_page = LoginPage()
    login_page.show()
    sys.exit(app.exec_())
