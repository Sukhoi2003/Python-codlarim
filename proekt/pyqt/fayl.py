import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout

class savol(QWidget):
    def __init__(self):
        super().__init__()
        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()

        self.ass = QPushButton("AssA")
        self.h_box.addWidget(self.ass)

        self.v_box.addLayout(self.h_box)

        self.setLayout(self.v_box)



