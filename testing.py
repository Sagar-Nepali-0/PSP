import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Redirect Buttons")

        layout = QVBoxLayout()

        self.button1 = QPushButton("Go to Page 1")
        self.button2 = QPushButton("Go to Page 2")

        self.button1.clicked.connect(self.run_page1)
        self.button2.clicked.connect(self.run_page2)

        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

        self.setLayout(layout)

    def run_page1(self):
        subprocess.Popen(["python", "admin/admin.py"])

    def run_page2(self):
        subprocess.Popen(["python", "student/student.py"])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
