# studentgui.py

from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QGridLayout
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSignal


class EditStudentWindow(QWidget):
    data_updated = pyqtSignal(dict)

    def __init__(self, data):
        super().__init__()
        self.setWindowTitle("Edit Student Info")
        self.setFixedSize(500, 450)
        self.data = data
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        title = QLabel("Edit Profile")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        main_layout.addWidget(title)

        grid_layout = QGridLayout()
        self.fields = {}

        labels = ["Name", "Address", "Class", "DOB", "Contact", "Section"]
        for i, label in enumerate(labels):
            row, col = divmod(i, 3)
            grid_layout.addWidget(QLabel(f"{label}:"), row, col * 2)
            edit = QLineEdit(self.data.get(label, ""))
            self.fields[label] = edit
            grid_layout.addWidget(edit, row, col * 2 + 1)

        main_layout.addLayout(grid_layout)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_data)
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(save_button)
        main_layout.addLayout(btn_layout)

        self.setLayout(main_layout)

    def save_data(self):
        updated_data = {label: field.text() for label, field in self.fields.items()}
        self.data_updated.emit(updated_data)
        self.close()
