import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QFormLayout, QCheckBox, QLineEdit
)
from PyQt5.QtCore import Qt


class StudentProfile(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Student Profile")
        self.setGeometry(0, 0, 1000, 1000)

        self.is_editing = False
        self.create_ui()

    def create_ui(self):
        self.main_layout = QVBoxLayout()

        # Title and Edit Button
        title_layout = QHBoxLayout()
        title = QLabel("Student Profile")
        self.edit_button = QPushButton("Edit")
        self.edit_button.clicked.connect(self.toggle_edit_mode)

        title_layout.addWidget(title)
        title_layout.addStretch()
        title_layout.addWidget(self.edit_button)
        self.main_layout.addLayout(title_layout)

        # Profile Picture and Name
        profile_pic = QLabel()
        profile_pic.setFixedSize(100, 100)
        profile_pic.setStyleSheet("background-color: gray; border-radius: 50px;")
        profile_pic.setAlignment(Qt.AlignCenter)

        self.name_label = QLabel("Student Name")
        self.name_label.setAlignment(Qt.AlignCenter)

        self.main_layout.addWidget(profile_pic)
        self.main_layout.addWidget(self.name_label)

        # Personal Info Section (editable)
        self.name_edit = QLineEdit("John Doe")
        self.dob_edit = QLineEdit("2000-01-01")
        self.address_edit = QLineEdit("123 Street, City")
        self.contact_edit = QLineEdit("9876543210")
        self.class_edit = QLineEdit("10")
        self.section_edit = QLineEdit("A")

        self.personal_info = QFormLayout()
        self.personal_info.addRow("Name:", self.name_edit)
        self.personal_info.addRow("DOB:", self.dob_edit)
        self.personal_info.addRow("Address:", self.address_edit)
        self.personal_info.addRow("Contact:", self.contact_edit)
        self.personal_info.addRow("Class:", self.class_edit)
        self.personal_info.addRow("Section:", self.section_edit)
        self.main_layout.addLayout(self.personal_info)

        # Academic Grades (editable)
        self.main_layout.addWidget(QLabel("Academic Grade:"))
        self.grades = {
            "Math": 60,
            "Science": 34,
            "Computer": 64,
            "Social": 32,
            "Nepali": 23
        }
        self.grade_edits = {}
        for subject, mark in self.grades.items():
            grade_input = QLineEdit(str(mark))
            grade_input.setReadOnly(True)
            self.grade_edits[subject] = grade_input
            self.main_layout.addLayout(self._form_row(subject, grade_input))

        # Extracurricular Activities
        self.main_layout.addWidget(QLabel("Extracurricular Activities (ECA):"))

        self.main_layout.addWidget(QLabel("Arts & Culture"))
        self.music_cb = QCheckBox("Music")
        self.dance_cb = QCheckBox("Dance")
        self.main_layout.addWidget(self.music_cb)
        self.main_layout.addWidget(self.dance_cb)

        self.main_layout.addWidget(QLabel("Sports"))
        self.football_cb = QCheckBox("Football")
        self.basketball_cb = QCheckBox("Basketball")
        self.main_layout.addWidget(self.football_cb)
        self.main_layout.addWidget(self.basketball_cb)

        self.main_layout.addWidget(QLabel("Academic & Intellectual"))
        self.coding_cb = QCheckBox("Coding Club")
        self.main_layout.addWidget(self.coding_cb)

        # Submit Button
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.submit_form)
        self.main_layout.addWidget(submit_button)

        self.set_editable(False)
        self.setLayout(self.main_layout)

    def _form_row(self, label, widget):
        layout = QHBoxLayout()
        layout.addWidget(QLabel(label + ":"))
        layout.addWidget(widget)
        return layout

    def toggle_edit_mode(self):
        self.is_editing = not self.is_editing
        self.set_editable(self.is_editing)
        self.edit_button.setText("Save" if self.is_editing else "Edit")

        if not self.is_editing:
            # Update the top name label
            self.name_label.setText(self.name_edit.text())

    def set_editable(self, editable):
        # Personal Info
        for widget in [
            self.name_edit, self.dob_edit, self.address_edit,
            self.contact_edit, self.class_edit, self.section_edit
        ]:
            widget.setReadOnly(not editable)

        # Grades
        for grade_input in self.grade_edits.values():
            grade_input.setReadOnly(not editable)

    def submit_form(self):
        print("Form submitted!")
        print("Name:", self.name_edit.text())
        print("DOB:", self.dob_edit.text())
        print("Address:", self.address_edit.text())
        print("Contact:", self.contact_edit.text())
        print("Class:", self.class_edit.text())
        print("Section:", self.section_edit.text())

        grades = {}
        for subject, grade_input in self.grade_edits.items():
            try:
                grades[subject] = int(grade_input.text())
            except ValueError:
                grades[subject] = "Invalid"
        print("Grades:", grades)

        print("ECA:", {
            "Music": self.music_cb.isChecked(),
            "Dance": self.dance_cb.isChecked(),
            "Football": self.football_cb.isChecked(),
            "Basketball": self.basketball_cb.isChecked(),
            "Coding Club": self.coding_cb.isChecked()
        })


# Run the application

def main():
    app = QApplication(sys.argv)
    window = StudentProfile()
    window.show()
    sys.exit(app.exec_())


if __name__=="__main__":
    main()
    