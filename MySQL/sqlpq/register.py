import sys

from PyQt5.QtWidgets import QPushButton, QListWidget, QLineEdit, QLabel
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QApplication

class Reg(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ro'yhatdan o'tiish")
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.hbox5 = QHBoxLayout()

        self.ism = QLabel("Ism")
        self.familya = QLabel("Familya")

        self.loginbtn = QLabel("Login")
        self.parolbtn = QLabel("Parol")

        self.ismga = QLineEdit()
        self.ismga.setPlaceholderText("Ismingizni kiriting")

        self.familyaga = QLineEdit()
        self.familyaga.setPlaceholderText("Familyangizni kiriting")

        self.login = QLineEdit()
        self.login.setPlaceholderText("Loginingizni kiriting")

        self.parol = QLineEdit()
        self.parol.setPlaceholderText("Parolingizni kiriting")

        self.saqlabtn = QPushButton("Saqlash")
        self.exit = QPushButton("Chiqish")

        self.hbox.addWidget(self.ism)
        self.hbox.addWidget(self.ismga)

        self.hbox2.addWidget(self.familya)
        self.hbox2.addWidget(self.familyaga)

        self.hbox3.addWidget(self.loginbtn)
        self.hbox3.addWidget(self.login)

        self.hbox4.addWidget(self.parolbtn)
        self.hbox4.addWidget(self.parol)

        self.hbox5.addWidget(self.saqlabtn)
        self.hbox5.addWidget(self.exit)

        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        self.vbox.addLayout(self.hbox5)

        self.setLayout(self.vbox)

        self.saqlabtn.clicked.connect(self.save)
        self.exit.clicked.connect(self.exit1)


    def exit1(self):
        self.close()

    def save(self):
        with open("databasas.txt", "w") as f:
            f.write(self.ismga.text() + " ")
            f.write(self.familyaga.text() + " ")
            f.write(self.loginbtn.text() + " ")
            f.write(self.parolbtn.text() + "\n")
            self.hide()





#
# app = QApplication([])
# win = Reg()
# win.show()
# sys.exit(app.exec_())
