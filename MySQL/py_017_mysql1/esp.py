import sys

from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QListWidget

class P(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500,500)





app = QApplication([])
win = P()
win.show()
sys.exit(app.exec_())