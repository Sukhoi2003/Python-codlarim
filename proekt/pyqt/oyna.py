import sys

from kirish import Register
from fayl import savol
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kirish")
        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()
        self.h1_box = QHBoxLayout()

        self.login = QLabel("Login")
        self.loginga = QLineEdit()
        self.h1_box.addWidget(self.login)
        self.h1_box.addWidget(self.loginga)
        self.v_box.addLayout(self.h1_box)

        self.parol = QLabel("Parol")
        self.parolga = QLineEdit()
        self.h_box.addWidget(self.parol)
        self.h_box.addWidget(self.parolga)
        self.v_box.addLayout(self.h_box)


        self.kirish_btn = QPushButton("Kirish")
        self.v_box.addWidget(self.kirish_btn)

        self.kirish_btn.clicked.connect(self.kirish1)

        self.ruy_btn = QPushButton("Ro'yhatdan o'tish")
        self.v_box.addWidget(self.ruy_btn)

        self.ruy_btn.clicked.connect(self.Ruyhat)

        self.v_box.addWidget(self.parolga)




        self.setLayout(self.v_box)


    def Ruyhat(self):
        self.reg = Register()
        self.reg.show()
        self.hide()

    def kirish1(self):
        self.savol = savol()
        self.savol.show()
        self.hide()







app =QApplication([])
win = Window()
win.show()
sys.exit(app.exec_())