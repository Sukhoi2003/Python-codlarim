import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QLineEdit, QLabel, QListWidget

class Display(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ro'yhat")
        self.setFixedSize(400, 400)
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()

        self.mal =  QLabel("Malumotlar")
        self.mall = QListWidget()

        self.vbox.addWidget(self.mal)
        self.vbox.addWidget(self.mall)

        self.hbox.addLayout(self.vbox)

        self.setLayout(self.hbox)





# app = QApplication([])
# win = Display()
# win.show()
# sys.exit(app.exec_())