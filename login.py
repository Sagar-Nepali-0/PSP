import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Software Management')
        self.setWindowIcon(QIcon('icon.png'))  # Optional: set an icon
        self.setGeometry(100, 100, 300, 200)  # Initial window size and position

        self.layout = QVBoxLayout()

        # Create buttons for different files
        self.button1 = QPushButton('Admin')
        self.button2 = QPushButton('Student')

        # Connect buttons to respective functions
        self.button1.clicked.connect(self.open_admin)
        self.button2.clicked.connect(self.open_student)

        # Add buttons to layout
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)

        self.setLayout(self.layout)

        # Center window on the screen
        self.center_window()

    def center_window(self):
        screen_geometry = QApplication.desktop().availableGeometry()
        window_geometry = self.frameGeometry()
        center_point = screen_geometry.center()
        window_geometry.moveCenter(center_point)
        self.move(window_geometry.topLeft())

    def open_admin(self):
        self.close()
        subprocess.run([sys.executable, 'admin/admin.py'])

    def open_student(self):
        self.close()
        subprocess.run([sys.executable, 'student/students.py'])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
