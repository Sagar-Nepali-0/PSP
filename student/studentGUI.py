import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QFormLayout, QGroupBox, QGridLayout
)
from PyQt5.QtGui import QFont, QPixmap, QPainter, QColor, QBrush
from PyQt5.QtCore import Qt, QSize

class StudentProfile(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Profile")
        self.setGeometry(400, 150, 500, 450)
        self.setFixedSize(500, 450)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # Title
        title = QLabel("Student Profile")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setAlignment(Qt.AlignLeft)
        main_layout.addWidget(title)

        # Profile Picture
        profile_pic = QLabel()
        profile_pic.setFixedSize(100, 100)
        profile_pic.setStyleSheet("border-radius: 50px; background-color: #ccc;")
        profile_pic.setAlignment(Qt.AlignCenter)

        name_label = QLabel("Student Name")
        name_label.setAlignment(Qt.AlignCenter)

        pic_layout = QVBoxLayout()
        pic_layout.addWidget(profile_pic, alignment=Qt.AlignCenter)
        pic_layout.addWidget(name_label)

        main_layout.addLayout(pic_layout)
        main_layout.addSpacing(10)

        # Info Update Form
        form_label = QLabel("Update Personal Information:")
        form_label.setFont(QFont("Arial", 12, QFont.Bold))
        main_layout.addWidget(form_label)

        grid_layout = QGridLayout()

        # Left Column
        grid_layout.addWidget(QLabel("Name:"), 0, 0)
        grid_layout.addWidget(QLineEdit(), 0, 1)

        grid_layout.addWidget(QLabel("Address:"), 1, 0)
        grid_layout.addWidget(QLineEdit(), 1, 1)

        grid_layout.addWidget(QLabel("Class:"), 2, 0)
        grid_layout.addWidget(QLineEdit(), 2, 1)

        # Right Column
        grid_layout.addWidget(QLabel("DOB:"), 0, 2)
        grid_layout.addWidget(QLineEdit(), 0, 3)

        grid_layout.addWidget(QLabel("Contact:"), 1, 2)
        grid_layout.addWidget(QLineEdit(), 1, 3)

        grid_layout.addWidget(QLabel("Section:"), 2, 2)
        grid_layout.addWidget(QLineEdit(), 2, 3)

        main_layout.addLayout(grid_layout)

        # Save Button
        save_button = QPushButton("Save")
        save_button.setFixedWidth(80)
        save_button.setStyleSheet("background-color: #999; color: white; border-radius: 10px;")
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(save_button)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StudentProfile()
    window.show()
    sys.exit(app.exec_())
