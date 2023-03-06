import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QListWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QPushButton

from register import Reg
from display import Display

class Register(QWidget):


    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registratsiya   :  )")
        # self.setFixedSize(700, 500)
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()

        self.login = QLabel("Login")
        self.loginga = QLineEdit()
        self.loginga.setPlaceholderText("Loginnni yozing")

        self.parol = QLabel("Parol")
        self.parolga = QLineEdit()
        self.parolga.setPlaceholderText("Parolni yozing")

        self.kirishbtn = QPushButton("Kirish")
        self.ruyhbtn = QPushButton("Ro'yhatdan o'tish")
        self.exit = QPushButton("Chiqish")


        self.hbox.addWidget(self.login)
        self.hbox.addWidget(self.loginga)

        self.hbox2.addWidget(self.parol)
        self.hbox2.addWidget(self.parolga)

        self.hbox3.addWidget(self.kirishbtn)
        self.hbox3.addWidget(self.ruyhbtn)
        self.hbox3.addWidget(self.exit)

        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)

        self.setLayout(self.vbox)

        self.ruyhbtn.clicked.connect(self.ruyhat)
        self.exit.clicked.connect(self.exit1)
        self.kirishbtn.clicked.connect(self.kir)

    def ruyhat(self):
        self.reg = Reg()
        self.reg.show()
        self.hide()


    def exit1(self):
        self.close()


    def kir(self):
        self.kiir = Display()
        self.kiir.show()
        self.hide()




app = QApplication([])
win = Register()
win.show()
sys.exit(app.exec_())

