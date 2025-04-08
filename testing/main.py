# Sample GUI based on PyQt5

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Attractive PyQt5 Dashboard")
        self.setGeometry(100, 100, 1000, 600)
        self.setStyleSheet("background-color: #1e1e2f; color: white;")
        
        self.initUI()
    
    def initUI(self):
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Sidebar
        sidebar = QFrame()
        sidebar.setFixedWidth(200)
        sidebar.setStyleSheet("background-color: #2c2c3e;")
        sidebar_layout = QVBoxLayout()
        sidebar.setLayout(sidebar_layout)

        btn_names = ["Dashboard", "Analytics", "Users", "Settings", "Logout"]
        for name in btn_names:
            btn = QPushButton(name)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #2c2c3e;
                    border: none;
                    padding: 15px;
                    text-align: left;
                    font-size: 14px;
                }
                QPushButton:hover {
                    background-color: #3c3c5e;
                }
            """)
            sidebar_layout.addWidget(btn)
        
        sidebar_layout.addStretch()

        # Main content area
        content = QFrame()
        content.setStyleSheet("background-color: #252535; border-radius: 10px;")
        content_layout = QVBoxLayout()
        content.setLayout(content_layout)

        title = QLabel("Welcome to Your Dashboard")
        title.setFont(QFont("Segoe UI", 20))
        title.setAlignment(Qt.AlignCenter)

        content_layout.addWidget(title)
        
        main_layout.addWidget(sidebar)
        main_layout.addWidget(content)

# Run the app
app = QApplication(sys.argv)
window = Dashboard()
window.show()
sys.exit(app.exec_())
